from swift_tools.package_tools import WrapPackage

class GyroscopePackage(WrapPackage):

    name = "Gyroscope"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        
    ]

package = GyroscopePackage 