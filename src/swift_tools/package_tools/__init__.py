from abc import ABC,abstractclassmethod, abstractproperty, abstractmethod, abstractstaticmethod
from typing import Optional
from json import dumps as jdumps



class SwiftPackage:
    name: str
    url: str
    min: Optional[str]
    max: Optional[str]
    branch: Optional[str]
    dependencies: list[object]

    def __init__(self,name: str, url: str, min: Optional[str] = None, max: Optional[str] = None, branch: Optional[str] = None, dependencies: list = [] ):
        self.name = name
        self.url = url
        self.min = min
        self.max = max
        self.branch = branch
        self.dependencies = dependencies


class Package(ABC):
    
    name: str = "Package"
    swift_packages: list[SwiftPackage] = []
    file: str = __file__
    library = __module__

    plist_keys: dict = {}

    pbxproj_flags: dict = {}

    deployment_target: str = "11.0"


class WrapPackage(Package):

    dependencies: list[Package] = []


class XCProject(ABC):

    name: str = "xc_project"
    dependencies: list[WrapPackage] = []
    swift_packages: list[SwiftPackage] = []
    python_source: str = ""
    linked_source: bool = False

class WorkDirectory(ABC):

    """
    class MyDirectory(WorkDirectory):
    
        projects = [
            MyProject,
            OtherProject
        ]

        kivy_recipes = [
            "pillow"
        ]

        pips = [
            "kivymd",
            "pygments"
        ]

    directory = MyDirectory
    """

    python: str = "python3.9"
    site_packages: str = "venv/lib/python3.9/site-packages"

    projects: list[XCProject] = []
    pips: list[str] = []
    kivy_recipes: list[str] = []

