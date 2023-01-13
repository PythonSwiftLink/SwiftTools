from abc import ABC,abstractclassmethod, abstractproperty, abstractmethod, abstractstaticmethod
from typing import Optional
from json import dumps as jdumps



class SwiftPackage:
    name: str
    url: str
    min: Optional[str]
    max: Optional[str]
    branch: Optional[str]
    depends: list[object]

    def __init__(self,name: str, url: str, min: Optional[str] = None, max: Optional[str] = None, branch: Optional[str] = None, depends: list = [] ):
        self.name = name
        self.url = url
        self.min = min
        self.max = max
        self.branch = branch
        self.depends = depends



class Package(ABC):
    
    name: str
    depends: list[object] = []
    swift_packages: list[SwiftPackage] = []
    file = __file__
    
    @abstractclassmethod
    def dump(cls):
        return {
            "name": cls.name,
            "library": cls.__module__,
            "depends": [x.package.dump() for x in cls.depends],# type: ignore            
            "swift_packages": [x.__dict__ for x in cls.swift_packages],
            "file": cls.file
        }



class Dependency:
    name: str
    target: Package

    def __init__(self, target: list[str], library: str = "apple" ) -> None:
        ...



class WrapPackage(Package):

    depends: list[Dependency]
