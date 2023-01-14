from swift_types import *

@wrapper
class Brightness:

    level = Property(float)
    
    def current_level(self) -> float: ...

    def set_level(self, level: float): ...

    
