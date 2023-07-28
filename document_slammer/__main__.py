import json
from jinja2 import Template
from pathlib import Path
from copy import deepcopy
import sys
import os
import subprocess


class SyncCommand:
    def __init__(self, definition_path: str):
        self._definition_path = Path(definition_path)
        self._output_file = "Booklet.pdf"
        self._templates = Path(__file__).parent.joinpath("templates")
        self._doc_root = Path(os.getcwd()).absolute()
        self._resource_path = Path(__file__).parent
        self._filler_page = self._resource_path.joinpath("blank.pdf").absolute()

    def run(self):
        with self._definition_path.open("r") as _config:
            self._configuration = json.load(_config)

        self._output_file = self._configuration.get("output", self._output_file)
        self._output_base = os.path.basename(self._output_file)[:-4]
        self._includes = deepcopy(self._configuration.get("includes", []))
        self._start_page = 3
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

        self._filler_page_count = 4 - (current_page % 4)

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


command_map = {
    "sync": SyncCommand,
}

try:
    command = command_map[sys.argv[1]](*sys.argv[2:])
except IndexError:
    print("No command specified. Bailing.", file=sys.stderr)
    sys.exit(1)
except KeyError:
    print("Unknown command: %s. Bailing." % sys.argv[1], file=sys.stderr)
    sys.exit(1)

command.run()
