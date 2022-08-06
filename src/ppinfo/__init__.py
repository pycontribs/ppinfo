"""ppinfo package."""
import configparser
import os
from pathlib import Path
from typing import Union


# pylint: disable=too-few-public-methods
class Project:
    """Class representing a python project."""

    # 3.7 default value is used because at the time this library was
    # written, this was the oldest still supported version of Python
    min_python: str = "3.7"

    def __init__(self, path: Union[Path, str] = Path(".")) -> None:
        """Construct a python Project instance."""
        if isinstance(path, str):
            path = Path(path)
        self.path = path

        if (path / "setup.cfg").exists():
            config = configparser.ConfigParser()
            config.read(path / "setup.cfg")
            if "options" in config:
                value = config["options"].get("python_requires", None)
                if not (value and value.startswith(">=")):
                    raise NotImplementedError("Unable to parse python_requires")
                self.min_python = value[2:]
