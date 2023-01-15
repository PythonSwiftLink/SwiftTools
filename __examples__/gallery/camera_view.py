
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty, AliasProperty, ColorProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import Screen

from camera import CameraBase




Builder.load_string("""
<CameraScreen>:
    cam_view: cam_view
    CameraView:
        id: cam_view

<CameraView>:
    app: app
    canvas:
        Rectangle:
            texture: self.tex
            pos: self.offset_pos
            size: self.norm_image_size
        Color:
            rgb: self.capture_outline_color[:3]
            a: self.capture_outline_alpha
        Line:
            width: 8
            rectangle: self.x, self.y - 8 , self.width - 8, self.height - 8
""")

class CameraScreen(Screen):
    cam_view = ObjectProperty(None)
    def __init__(self, **kw):
        super(CameraScreen,self).__init__(**kw)

    def on_pre_enter(self):
        self.cam_view.cam.start()

    def on_leave(self):
        self.cam_view.cam.stop()


class CameraView(RelativeLayout):
    app = ObjectProperty(None)
    tex = ObjectProperty(None)
    touch_pos = ListProperty([0,0])
    touched =  NumericProperty(0)

    capture_outline_color = ColorProperty()
    capture_outline_alpha = NumericProperty(0.0)

    preview_buffersize: int

    def get_image_ratio(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        print("get_image_ratio")
        tex = self.tex
        if tex:
            return tex.width / float(tex.height)
        return 1.

    image_ratio = AliasProperty(get_image_ratio, bind=('tex',), cache=True)

    def get_norm_image_size(self):
        tex = self.tex
        if not tex:
            return list(self.size)
        ratio = self.image_ratio
        w, h = self.size
        #tw, th = tex.size

        # ensure that the width is always maximized to the container width

        iw = w
        # calculate the appropriate height
        ih = iw / ratio
        # if the height is too higher, take the height of the container
        # and calculate appropriate width. no need to test further. :)
        if ih > h:
            ih = h
            iw = ih * ratio
        return [iw, ih]

    norm_image_size = AliasProperty(get_norm_image_size,
                                    bind=('tex', 'size',
                                        'image_ratio'),
                                    cache=True)


    def get_offset_pos(self):
        w, h = self.size
        tw, th = self.norm_image_size

        offset_x = (w - tw) / 2
        offset_y = (h - th) / 2

        return [self.x + offset_x, self.y + offset_y]

    offset_pos = AliasProperty(get_offset_pos,
                            bind=('norm_image_size','pos'),
                            cache=True
                            )

    def __init__(self, **kw):
        
        #self.bind(offset_pos=self.send_texture_pos)
        #self.bind(norm_image_size=self.send_texture_size)
        super(CameraView, self).__init__(**kw)

        self.update_cam = self.canvas.ask_update

        cam = CameraBase()
        cam.py_callback = self
        self.cam = cam
    
    
    def new_texture(self, w: int, h: int):
        print("new_texture", w, h)
        tex = Texture.create(size=(w,h),colorfmt='bgra')
        tex.flip_vertical()
        #tex.flip_horizontal()
        self.tex = tex

    def on_frame(self, buffer: object):
        self.tex.blit_buffer(buffer, colorfmt='bgra')
        self.update_cam()
    
