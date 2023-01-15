
from filechooser import FileChooser, some_module_func

from brightness import Brightness


from notification import Notification

#from test_buffers import TestBuffer

from phpicker import PHPicker

from array import array


# import numpy as np

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from uuid import uuid4
from timeit import timeit

from kivy.graphics.texture import Texture


from camera_view import CameraScreen
from main_screen import MainScreen
from tts_view import TextToSpeechScreen
from webview_screen import JavaScreen, WebScreen


#Window.softinput_mode = "below_target"




class MainView(BoxLayout): ...

Builder.load_string("""
#:import uuid uuid.uuid4

<MainView>:
    orientation: "vertical"
    BoxLayout:
        size_hint_y: 0.05
        Button:
            text: "Main"
            on_press: sm.current = "main"
        Button:
            text: "Camera"
            on_press: sm.current = "camera"
        Button:
            text: "TextToSpeech"
            on_press: sm.current = "tts"
        Button:
            text: "WebView"
            on_press: sm.current = "web"
        Button:
            text: "JavaViews"
            on_press: sm.current = "java"
    ScreenManager:
        id: sm
        MainScreen:
            name: "main"
        CameraScreen:
            name: "camera"
        TextToSpeechScreen:
            name: "tts"
        WebScreen:
            name: "web"
        JavaScreen:
            name: "java"

<MainViewOld>:
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
                app.tts.speak(tts_input.text)
        Label:
            text: "Notifications"
            size_hint_y: 0.1
        TextInput:
            id: noti_title
            size_hint_y: 0.1
            hint_text: "title"
        TextInput:
            id: noti_msg
            hint_text: "message"
        Button:
            text: "Send Event"
            size_hint_y: 0.2
            on_press:
                app.notification.new_notification(noti_title.text, noti_msg.text, 10, uuid().hex, False)

    BoxLayout:
        orientation: "vertical"
        Button:
            text: "FileChooser open"
            on_press:
                app.filechooser.open()
        Button:
            text: "set badge count +1"
            on_press:
                app.notification.increase_badge_count(1)
    BoxLayout:
        orientation: "vertical"
        CameraView:
            id: cam_view
            app: app
        Slider:
            min: 0.0
            max: 1.0
            value: 1.0
            on_value:
                app.brightness.level = self.value
        Button:
            on_press: app.picker.open(5)
        
""")


class DocPickerApp(App):

    #preview_texture = ObjectProperty(None)
    cam_state: bool

    def __init__(self, **kwargs):
        super(DocPickerApp,self).__init__(**kwargs)
        #self.preview_texture = Texture.create(size=(1920, 1080), colorfmt='rgba', bufferfmt="ubyte")
        self.brightness = Brightness()
        self.notification = Notification()
        try:
            self.filechooser = FileChooser(callback_class=self)
        except:
            print("filechooser init failed")
        self.notification.reset_bagde_count()
        #self.test_buf = TestBuffer()

        self.cam_state = False

        self.picker = PHPicker()
        self.picker.py_callback = self
    

    def picker_didFinishPicking(self, results: object):

        def imgExtract(url,err):
            print(url, err)

        self.imgExtract = imgExtract # function must have strong ref
        self.picker.dismiss()
        for item in results:
            item.loadFileRepresentation("public.item",imgExtract)
    
    def trigger_cam(self):
        if not self.cam_state:
            self.cam_state = True
        

    def on_start(self,*args):
        print("on_start")

        # cam_view = self.main.ids.cam_view
        # self.cam_view = cam_view
        

    def build(self):
        print("on_build")
        self.main = MainView()
        return self.main




    def handleBuffer(self):
        print()
        print("handleBuffer:")

        # a = TestBuffer()
        
        # before = list(memoryview(a)[:8])
        # print("before: ",before)

        # nparr = np.asarray(a)

        # nparr[:8] = [1,1,1,1,1,1,1,1]

        # after = list(memoryview(a)[:8])
        # print("after: ",after)

        # print()

        # self.testBufferSpeed()




    # def testBufferSpeed(self):
    #     print()
    #     count = 1_000_000
    #     result = timeit("a = asarray(test_buf)", globals={"test_buf": self.test_buf, "handleBuffer": self.handleBuffer, "asarray":np.asarray}, number=count)
    #     print(f"time: {result}, count: {count}, time each: {(result/count)*1_000} ms")
    #     print()


if __name__ == "__main__":

    DocPickerApp().run()







