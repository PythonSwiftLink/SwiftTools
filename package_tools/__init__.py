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

    # def dump(self):
    #     return {
    #         "name": self.name,
    #         "url": self.url,
    #         "min": self.min,
    #         "max": self.max,
    #         "branch": self.branch,
    #         "depends": [x for x in self.depends]
    #     }



class Package(ABC):
    
    name: str = "Package"
    depends: list[object] = []
    swift_packages: list[SwiftPackage] = []
    file: str = __file__
    
    plist_keys: dict = {}
    # @abstractclassmethod
    # def dump(cls):
    #     return {
    #         "_str": "abc",
    #         "_float": 4566.866788,
    #         "_int": 5775577,
    #         "_bool": True,
    #         "_uint8": 1,

    #         "name": cls.name,
    #         "library": cls.__module__,
    #         "depends": [x.package for x in cls.depends],# type: ignore            
    #         "swift_packages": [x for x in cls.swift_packages],
    #         "file": cls.file
    #     }



class Dependency:
    name: str
    target: Package

    def __init__(self, target: list[str], library: str = "apple" ) -> None:
        ...



class WrapPackage(Package):

    depends: list[Dependency] = []
