all: schema.rst

readme.html: README.rst
	pandoc README.rst -o readme.html

schema.rst: .build/combined.md
	pandoc .build/combined.md -o schema.rst --list-tables

.build/combined.md: .build/out
	cat .build/out/README.md .build/out/schema.md .build/out/schema-*.md > .build/combined.md

.build/out: .build/schemas/schema.json
	npx jsonschema2md -o .build/out -d .build/schemas -e json

.build/schemas/schema.json: document_slammer/resources/schema.yaml .build/schemas
	python -c 'import yaml, json; from pathlib import Path; print(json.dumps(yaml.load(Path("document_slammer/resources/schema.yaml").read_text(), yaml.CSafeLoader)))' > .build/schemas/schema.json

.build/schemas:
	mkdir -p .build/schemas
