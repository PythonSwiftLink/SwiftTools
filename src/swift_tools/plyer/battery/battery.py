from swift_types import *

@wrapper
class Battery:

    state = property(object, setter=False)
    
    def get_state(self) -> object: ...




@wrapper
class BatteryAdvanced:

    class Callbacks:
        def batteryLevelChanged(self, level: float): ...
        def batteryStateChanged(self, state: int): ...