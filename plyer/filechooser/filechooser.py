from swift_types import *

def some_module_func() -> object: ...

@wrapper
class FileChooser:

    #level = Property(float, setter=false)

    def __init__(self): ...

    class Callbacks:
        def didFinishPicking(self, results: list[str]): ...

    def open(self): ...


    # def __getitem__(self, key) -> object: ...

    # def __setitem__(self,key,value): ...

