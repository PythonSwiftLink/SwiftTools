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

    

class Package(ABC):
    
    name: str
    depends: list[object] = []
    swift_packages: list[object] = []
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

    name: str
    depends: list[Dependency]
    swift_packages: list[object]
