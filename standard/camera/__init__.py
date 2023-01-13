from package_tools import WrapPackage


from apple import CoreVideo



class CameraPackage(WrapPackage):

    name = "Camera"
    file = __file__
    depends = [
        CoreVideo
    ]

package = CameraPackage
