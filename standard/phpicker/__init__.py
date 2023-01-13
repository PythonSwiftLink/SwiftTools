from package_tools import WrapPackage


from apple import Foundation



class PHPickerPackage(WrapPackage):

    name = "PHPicker"
    file = __file__
    library = __module__
    version = "1.0.0"
    depends = [
        Foundation
    ]

package = PHPickerPackage

