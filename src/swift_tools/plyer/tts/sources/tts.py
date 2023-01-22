from swift_types import *

@wrapper
class TextToSpeech:
    
    def set_locale(self, locale: str): ...

    def speak(self, message: str): ...
