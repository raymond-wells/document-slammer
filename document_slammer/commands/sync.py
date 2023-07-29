__all__ = ["Sync"]

import json
import yaml
import os
import subprocess
from copy import deepcopy
from functools import cached_property
from pathlib import Path

from jinja2 import Template
from jsonschema import Draft7Validator


class Sync:
    """
    Generates all booklet building project files from the provided ``doc.json``
    configuration.
    """

    def __init__(self, definition_path: str):
        self._definition_path = Path(definition_path)
        self._output_file = "Booklet.pdf"
        self._templates = Path(__file__).parents[1].joinpath("templates")
        self._doc_root = Path(os.getcwd()).absolute()
        self._resource_path = Path(__file__).parents[1].joinpath("resources")
        self._filler_page = self._resource_path.joinpath("blank.pdf").absolute()

    def run(self):
        self._output_file = self._configuration.get("output", self._output_file)
        self._output_base = os.path.basename(self._output_file)[:-4]
        self._includes = deepcopy(self._configuration.get("includes", []))
        self._number_script = self._doc_root.joinpath(".slammer", "numbering.awk")
        self._blank_page = self._doc_root.joinpath(".slammer", "blank.pdf")
        self._doc_root.joinpath(".slammer").mkdir(exist_ok=True, parents=True)
        self._number_script.write_bytes(
            self._resource_path.joinpath("numbering.awk").read_bytes()
        )
        self._blank_page.write_bytes(
            self._resource_path.joinpath("blank.pdf").read_bytes()
        )
        self._number_script = self._number_script.relative_to(self._doc_root)
        self._blank_page = self._blank_page.relative_to(self._doc_root)
        self._start_page = 1

        current_page = self._start_page

        for include in self._includes:
            pdf_info = {
                components[0].strip(): components[1].strip()
                for components in map(
                    lambda _s: _s.split(":", 1),
                    subprocess.check_output(["pdfinfo", include["path"]])
                    .decode("utf-8")
                    .splitlines(),
                )
            }
            include.update({"pdf_info": pdf_info})
            include["start_page"] = current_page
            current_page += int(pdf_info["Pages"])

        self._filler_page_count = 4 - ((2 + current_page) % 4)

        template_context = {
            "config": self._configuration,
            "context": {
                k.lstrip("_"): v for k, v in self.__dict__.items() if k.startswith("_")
            },
        }

        with self._templates.joinpath("title-and-toc.tex.j2").open("r") as _template:
            with self._doc_root.joinpath("title-and-toc.tex").open("w") as _output:
                _output.write(Template(_template.read()).render(template_context))

        with self._templates.joinpath("Makefile.j2").open("r") as _template:
            with self._doc_root.joinpath("Makefile").open("w") as _output:
                _output.write(Template(_template.read()).render(template_context))

    @cached_property
    def _configuration(self):
        with self._definition_path.open("r") as _file:
            if any(map(self._definition_path.name.lower().endswith, ["yml", "yaml"])):
                definition = yaml.load(_file, yaml.CSafeLoader)
            else:
                definition = json.load(_file)

        with self._resource_path.joinpath("schema.yaml").open("r") as _file:
            schema = yaml.load(_file, yaml.CSafeLoader)
            Draft7Validator(schema).validate(definition)

        return definition
