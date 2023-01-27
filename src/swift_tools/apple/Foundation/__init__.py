from swift_tools.package_tools import WrapPackage

class FoundationPackage(WrapPackage):

    name = "Foundation"
    file = __file__
    library = __module__
    version = "1.0.0"
    depends = [
        
    ]

package = FoundationPackage