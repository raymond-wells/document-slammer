import json
import os
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

from jinja2 import Template

from document_slammer.commands.sync import Sync

command_map = {
    "sync": Sync,
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
