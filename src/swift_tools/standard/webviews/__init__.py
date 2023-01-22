from swift_tools.package_tools import WrapPackage,SwiftPackage


from swift_tools.apple import Foundation



class WebViewsPackage(WrapPackage):

    name = "WebViews"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        Foundation.package
    ]
    swift_packages = [

        
    ]

package = WebViewsPackage

