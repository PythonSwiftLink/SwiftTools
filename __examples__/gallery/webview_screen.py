
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty, AliasProperty, ColorProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

from kivy.extras.highlight import KivyLexer
from pygments.lexers.javascript import JavascriptLexer

from web_views import JavaViewer, WebViewer
from json import dumps

py_string = """json_data = [
    {
        "x": ['giraffes', 'orangutans', 'monkeys'],
        "y": [20, 14, 23],
        "type": 'bar'
    }
]"""

# json_data = dumps(data)

js_script = """

Plotly.newPlot(gd, {json_data});

"""

html_code = """
<head>
    <script src="https://cdn.plot.ly/plotly-2.17.0.min.js"></script>
</head>
<div id="gd"></div>

"""


plot_scripts_dict = {
"contour": """
from math import *

size = 100
x = [0]*size
y = [0]*size
z = []

for i in range(size):
    x[i] = y[i] = -2 * pi + 4 * pi * i / size
    temp_z = []
    z.append(temp_z)
    for v in range(100):
        r2 = x[i]*x[i] + y[j]*y[j]
        temp_z.append(
            sin(x[i]) * cos(y[v]) * sin(r2) / log(r2+1)
        )
json_data = [ {
		"z": z,
		"x": x,
		"y": y,
		"type": 'contour'
	}
]
""",
"heatmap": """
json_data = [
  {
    "z": [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
    "type": 'heatmap'
  }
]
""",
"bar": """
json_data = [{
    "x": ['giraffes', 'orangutans', 'monkeys'],
    "y": [20, 14, 23],
    "type": 'bar'
}]
""",
"scatter": """
trace1 = {
    "x": [1, 2, 3, 4],
    "y": [10, 15, 13, 17],
    "type": 'scatter'
}

trace2 = {
    "x": [1, 2, 3, 4],
    "y": [16, 5, 11, 9],
    "type": 'scatter'
}

json_data = [trace1, trace2]
""",
"pie":"""
json_data = [{
    "values": [19, 26, 55],
    "labels": ['Residential', 'Non-Residential', 'Utility'],
    "type": 'pie'
}]

"""
}




class JavaScreen(Screen):

    html = StringProperty(html_code)
    js = StringProperty(js_script)
    py_script = StringProperty(py_string)
    json_data = StringProperty("[]")
    widget_view = ObjectProperty()
    java_viewer = ObjectProperty()

    option = StringProperty("bar")

    def __init__(self, **kw):
        self.java_viewer = JavaViewer()
        super(JavaScreen, self).__init__(**kw)

    def view_size_changed(self,wid,_):
        y = Window.size[1] - wid.top
        self.java_viewer.set_frame(wid.x,y,wid.width,wid.height)

    def on_pre_enter(self, *args):
        v = self.java_viewer
        v.load_html(html_code)

    def on_enter(self, *args):
        print("on_enter:")
        v = self.java_viewer
        wid = self.widget_view
        y = Window.size[1] - wid.top
        v.set_frame(wid.x,y,wid.width,wid.height)

        

        v.show()
        v.evaluate_javascript(self.gen_js(self.js.format(json_data=self.json_data)))
        return super().on_pre_enter(*args)

    def on_pre_leave(self, *args):
        self.java_viewer.dismiss()
        return super().on_leave(*args)

    def gen_js(self,js: str) -> str:
        return f"gd = document.getElementById('gd');\n{js}"
    
    def on_js(self,wid,js):
        self.java_viewer.evaluate_javascript(self.gen_js(js.format(json_data=self.json_data)))

    def on_json_data(self,_,data: str):
        string = self.gen_js(self.js.format(json_data=self.json_data))
        print(string)
        self.java_viewer.evaluate_javascript(string)

    def on_option(self, _, option):
        self.py_script = plot_scripts_dict[option]

    def on_py_script(self,_,string):
        locals = {}
        try:
            exec(string,globals(),locals)
        except:
            return
        self.json_data = dumps(locals["json_data"])
        

        

class JavaView(BoxLayout):
    ...


class WebScreen(Screen):

    def __init__(self, **kw):
        super(WebScreen, self).__init__(**kw)
        self.view = WebViewer()

    def on_size(self,*_):
        y = Window.size[1] - self.top
        self.view.set_frame(self.x,y,self.width,self.height)

    def on_pre_enter(self, *args):
        self.view.load_url("https://kivy.org")
        
    def on_enter(self, *args):
        v = self.view
        y = Window.size[1] - self.top
        v.set_frame(self.x,y,self.width,self.height)
        v.show()
        print(self.x,self.top,self.width,self.height)

    def on_pre_leave(self, *args):
        self.view.dismiss()
        return super().on_leave(*args)



class WebViews(Screen): ...


Builder.load_string("""

<JavaScreen>:
    widget_view: view_widget
    JavaView:
        id: js_view
        BoxLayout:
            orientation: "vertical"
            Button:
                text: "bar"
                on_press: root.option = self.text
            Button:
                text: "pie"
                on_press: root.option = self.text
            Button:
                text: "scatter"
                on_press: root.option = self.text
            Button:
                text: "contour"
                on_press: root.option = self.text
            Button:
                text: "heatmap"
                on_press: root.option = self.text
            
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                size_hint_y: 0.3
                CodeInput:
                    id: js_edit
                    text: root.py_script
                    on_focus: 
                        if not self.focus: root.py_script = self.text
                
            Widget:
                id: view_widget
                size_hint: 1,1
                on_pos: root.view_size_changed(self,0)
                on_size: root.view_size_changed(self,0)
        


            
""")