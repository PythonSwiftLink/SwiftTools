from swift_types import *



@wrapper
class Gyroscope:

    def enable(self): ...
    def disable(self):...

    def get_orientation(self) -> object: ...
    
    def get_rotation_uncalib(self) -> object: ...

    

