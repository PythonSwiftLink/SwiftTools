from package_tools import WrapPackage


from apple import CoreVideo



class CameraPackage(WrapPackage):

    name = "camera"

    depends = [
        CoreVideo
    ]

package = CameraPackage
