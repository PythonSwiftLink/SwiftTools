from package_tools import WrapPackage



class CoreVideoPackage(WrapPackage):

    name = "CoreVideo"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = []

package = CoreVideoPackage