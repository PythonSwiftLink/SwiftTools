from package_tools import WrapPackage

class SpeechRecognizerPackage(WrapPackage):

    name = "SpeechRecognizer"
    file = __file__
    library = __module__
    version = "1.0.0"
    dependencies = [
        
    ]
    plist_keys = {"NSSpeechRecognitionUsageDescription" : "$\{PRODUCT_NAME\} SpeechRecognitionUsage"}

package = SpeechRecognizerPackage


