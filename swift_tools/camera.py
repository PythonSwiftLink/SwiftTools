from kivy.uix.relativelayout import RelativeLayout
from kivy._event import EventDispatcher
from kivy.lang.builder import Builder
from kivy.properties import AliasProperty
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty
from swift_types import *

@swift_object
class CameraBase:

	@send_self
	def __init__(self): ...

	def start(self, ask_update: object): ...

	def stop(self): ...

@python
class CameraPreviewData(CameraBase, EventDispatcher):

    preview_texture = ObjectProperty(Texture.create(size=[128, 128]))

@python
class PreviewViewer(RelativeLayout):

    preview_texture = ObjectProperty(None)

    def get_image_ratio(self):
        tex = self.preview_texture
        if tex:
            return tex.width / float(tex.height)
        return 1.

    image_ratio = AliasProperty(get_image_ratio, bind=('preview_texture',), cache=True)

    def get_norm_image_size(self):
        tex = self.preview_texture
        if not tex:
            return list(self.size)
        ratio = self.image_ratio
        w, h = self.size
        # tw, th = tex.size

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
                                    bind=('preview_texture', 'size',
                                          'image_ratio'),
                                    cache=True)

    def get_offset_pos(self):
        w, h = self.size
        tw, th = self.norm_image_size

        offset_x = (w - tw) / 2
        offset_y = (h - th) / 2

        return [self.x + offset_x, self.y + offset_y]

    offset_pos = AliasProperty(get_offset_pos,
                               bind=('norm_image_size', 'pos'),
                               cache=True
                               )

    def __init__(self, **kw):
        super(PreviewViewer, self).__init__(**kw)

#     def ask_update(self):
#         #...
#         self.canvas.ask_update()


Builder.load_string("""
<PreviewViewer>:
    tex: app.camera_data.preview_texture
    canvas:
        Rectangle:
            texture: self.tex
            pos: self.offset_pos
            size: self.norm_image_size
""")
