class Project:
    def __init__(self, project_name: str):
        self._project_name = project_name

    def create_project(self) -> None:
        pass

    def delete_project(self) -> None:
        pass

    def __str__(self):
        return f"Project name is {self._project_name}"
