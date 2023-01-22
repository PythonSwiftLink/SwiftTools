from swift_types import *
"import CoreLocation"
@wrapper
class GPS:

      def configure(self, on_location: object, on_status: object): ...

      def start(self, minTime: int, minDistance: int):...  

      def stop(self):...



@wrapper(py_init=False)
class CLLocation:
    
    latitude = property(float, setter=False)
    longitude = property(float, setter=False)

    altitude = property(float, setter=False)
    #ellipsoidalAltitude = property(float, setter=False, available=iOS(15.0))
    horizontalAccuracy = property(float, setter=False)
    verticalAccuracy = property(float, setter=False)
    
    speed = property(float, setter=False)
    speedAccuracy = property(float, setter=False)
    course = property(float, setter=False)
    #courseAccuracy = property(float, setter=False, available=iOS(13.4))
    