from package_tools import WrapPackage,SwiftPackage


from apple import Foundation



class PHPickerPackage(WrapPackage):

    name = "PHPicker"
    file = __file__
    library = __module__
    version = "1.0.0"
    depends = [
        Foundation
    ]
    swift_packages = [
        SwiftPackage(
            "SwiftyJson",
            "https://github.com/SwiftyJSON/SwiftyJSON",
            branch="main", 
            depends= [
                SwiftPackage("PathKit","https://github.com/kylef/PathKit.git", min = "1.0.0")
            ]
        ),
        
    ]

package = PHPickerPackage

