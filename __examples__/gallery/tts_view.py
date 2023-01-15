from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty, AliasProperty, ColorProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import Screen

from tts import TextToSpeech



Builder.load_string("""
<TextToSpeechScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Text2Speech"
            size_hint_y: 0.1
            
        TextInput:
            id: tts_input
        Button:
            text: "Speak"
            size_hint_y: 0.2
            on_press:
                root.tts.speak(tts_input.text)
""")

class TextToSpeechScreen(Screen):


    def __init__(self, **kw):
        super(TextToSpeechScreen, self).__init__(**kw)
        self.tts = TextToSpeech()
