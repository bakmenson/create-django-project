from os import chdir
from subprocess import Popen, PIPE, call


class Project:
    def __init__(self, project_name: str):
        self._project_name = project_name.replace("-", "_")

    def create_project(self) -> None:
        call("mkdir " + self._project_name, shell=True)

    def delete_project(self) -> None:
        call("rm -rf " + self._project_name, shell=True)

    def is_exists(self) -> bool:
        ls = Popen(
            ["ls -1"], shell=True, stdout=PIPE, encoding='utf-8'
        ).communicate()[0]

        return True if self._project_name in ls.split() else False

    def __str__(self):
        return f"Project name is {self._project_name}"


class ProjectDir:
    def __init__(self):
        self._project_dir: str = ""

    @property
    def dir_name(self):
        return self._project_dir

    @dir_name.setter
    def dir_name(self, dir_name: str) -> None:
        self._project_dir = dir_name.replace("-", "_")

    def create_dir(self) -> None:
        call("mkdir " + self.dir_name, shell=True)

    def delete_dir(self) -> None:
        call("rm -rf " + self.dir_name, shell=True)

    @property
    def is_exists(self) -> bool:
        ls = Popen(
            ["ls -1"], shell=True, stdout=PIPE, encoding='utf-8'
        ).communicate()[0]

        return True if self.dir_name in ls.split() else False

    def __str__(self):
        return f"Project dir name is {self.dir_name}"
