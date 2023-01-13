from abc import ABC,abstractclassmethod, abstractproperty, abstractmethod, abstractstaticmethod
from typing import Optional




class SwiftPackage:
    name: str
    url: str
    min: Optional[str]
    max: Optional[str]
    branch: Optional[str]
    depends: list[object]

    

class Package(ABC):
    
    name: str
    depends: list[object]
    swift_packages: list[object]

    @abstractclassmethod
    def dump(cls):
        return {
            "name": cls.name,
            "library": cls.__module__,
            "depends": [x.package.dump() for x in cls.depends],# type: ignore            
            "swift_packages": [x.__dict__ for x in cls.depends]
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
