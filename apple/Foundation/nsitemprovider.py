from swift_types import *
from typing import Optional

@wrapper(pyinit=False)
class NSItemProvider:

    suggestedName = property(Optional[str])
    #suggestedName = property(str)
#     #preferredPresentationSize = property(list[float])

#     #def send(self, l: list[str]): ...
    registeredTypeIdentifiers = property(list[str], setter= False) 
    

    def loadFileRepresentation(self,forTypeIdentifier: str, completionHandler: callable[[Optional[URL],Optional[Error]]]): ...

    @args_rename(id="_ typeIdentifier")
    def hasItemConformingToTypeIdentifier(self, id: str) -> bool: ...

    def loadInPlaceFileRepresentation(self,forTypeIdentifier: str, completionHandler: callable[[Optional[URL],bool,Optional[Error]]]): ...

    def loadDataRepresentation(self,forTypeIdentifier: str, completionHandler: callable[[Optional[data],Optional[Error]]]): ...
