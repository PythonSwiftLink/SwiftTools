from package_tools import WrapPackage

class BrightnessPackage(WrapPackage):

    name = "Brightness"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        
    ]

package = BrightnessPackage