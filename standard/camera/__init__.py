from package_tools import WrapPackage


from apple import CoreVideo



class CameraPackage(WrapPackage):

    name = "Camera"
    file = __file__
    library = __module__
    version = "1.0.0"
    depends = [
        CoreVideo
    ]

package = CameraPackage
