
from __future__ import print_function

import os
import random
import shutil
import string

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def remove_docker_file():
    file_names = ["DockerFile"]
    for file_name in file_names:
        os.remove(file_name)

def main():
    # debug = "{{ cookiecutter.debug }}".lower() == "y"
    if "{{ cookiecutter.use_docker }}".lower() == "n":
        remove_docker_file()
    print(SUCCESS + "Project created successfully!" + TERMINATOR)


if __name__ == "__main__":
    main()