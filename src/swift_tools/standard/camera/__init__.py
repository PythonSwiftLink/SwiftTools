from swift_tools.package_tools import WrapPackage


from swift_tools.apple import CoreVideo



class CameraPackage(WrapPackage):

    name = "Camera"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        CoreVideo.package
    ]
    plist_keys = {"NSCameraUsageDescription": "$(PRODUCT_NAME) camera description."}

package = CameraPackage
