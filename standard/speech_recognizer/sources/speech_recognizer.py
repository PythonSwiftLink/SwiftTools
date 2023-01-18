


@wrapper
class SpeechRecognizer:

    class Callbacks:

        def speak(self,message: str): ...


    def start(self): ...

    def stop(self): ...