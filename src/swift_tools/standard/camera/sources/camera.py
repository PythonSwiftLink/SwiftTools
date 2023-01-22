from swift_types import *

"import AVFoundation"

# with SwiftImports:
#     "AVFoundation"

@wrapper(py_init=False)
class CVPixelBuffer:

    def __buffer__(self):...


@wrapper
class CameraBase:


    class Callbacks:

        def new_texture(self, w: int, h: int): ...

        def on_frame(self, buffer: object): ...

    def start(self): ...

    def stop(self): ...