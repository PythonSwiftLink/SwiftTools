from package_tools import WrapPackage

class NotificationPackage(WrapPackage):

    name = "Notification"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        
    ]

package = NotificationPackage
