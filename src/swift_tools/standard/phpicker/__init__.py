from swift_tools.package_tools import WrapPackage,SwiftPackage


from swift_tools.apple import Foundation



class PHPickerPackage(WrapPackage):

    name = "PHPicker"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        Foundation.package
    ]
    swift_packages = [
        # SwiftPackage(
        #     "SwiftyJson",
        #     "https://github.com/SwiftyJSON/SwiftyJSON",
        #     branch="main", 
        #     dependencies= [
        #         SwiftPackage("PathKit","https://github.com/kylef/PathKit.git", min = "1.0.0")
        #     ]
        # ),
        
    ]

package = PHPickerPackage

