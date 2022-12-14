from swift_types import *



@wrapper
class WebViewer:

    

    def reload(self): ... 

    def reloadFromOrigin(self): ... 

    def forward(self): ...
    can_go_forward = property(bool, setter=False)

    def back(self): ...
    can_go_back = property(bool, setter=False)

    def load_data(self,data: data, mime: str, char_encoing: str, base_url: str): ...

    def load_url(self, url: str): ...

    def load_html_string(self, string: str, base_url: Optional[str]): ...

    def set_frame(self, x: float, y: float, w: float, h: float): ...

    def show(self): ...

    def present(self): ...

    def dismiss(self): ...

@wrapper
class JavaViewer:

    def load_html(self, html: str): ...

    def evaluate_javascript(self, js: str): ...


    def set_frame(self, x: float, y: float, w: float, h: float): ...

    def show(self): ...

    def present(self): ...

    def dismiss(self): ...