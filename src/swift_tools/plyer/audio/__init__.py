from package_tools import WrapPackage

class AudioPackage(WrapPackage):

    name = "Audio"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        
    ]
    plist_keys = {"NSMicrophoneUsageDescription" : "$\{PRODUCT_NAME\} MicrophoneUsage"}

package = AudioPackage


