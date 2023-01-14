from package_tools import WrapPackage

class TextToSpeechPackage(WrapPackage):

    name = "TextToSpeech"
    file = __file__
    library = __module__
    version = "1.0.0"
    depends = [
        
    ]

package = TextToSpeechPackage