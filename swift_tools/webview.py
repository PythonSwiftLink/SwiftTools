from swift_types import *

@swift_func
def static_webview(cls: object): ...

@swift_func
def load_web_url(url: str): ...

@swift_func
def webview_forward(): ...

@swift_func
def webview_back(): ...

@swift_func
def java_webview(html: str, cls: object): ...

@swift_func
def inject_js(js: str): ...

