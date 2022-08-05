from swift_types import *

UIAlertActionStyle = Enum(
    default = 0,
    cancel = 1,
    destructive = 2
)

@swift_object
class UIAlertView:

    def __init__(self, title: str, message: str):...

    def show(self): ...

    def add_action(self, style: UIAlertActionStyle, text: str, callback: object): ...
