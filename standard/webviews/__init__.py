from package_tools import WrapPackage,SwiftPackage


from apple import Foundation



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

