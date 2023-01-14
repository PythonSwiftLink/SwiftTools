from package_tools import WrapPackage

class FileChooserPackage(WrapPackage):

    name = "FileChooser"
    file = __file__
    library = __module__
    version = "1.0.0"
    depends = [
        
    ]

package = FileChooserPackage