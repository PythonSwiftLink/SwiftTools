print(globals())


from package_tools import WorkDirectory, XCProject

from standard import camera, phpicker, webviews
from plyer import brightness, tts


class MyProject(XCProject):

    name = "my_project"
    dependencies = [
        camera.package,
        phpicker.package,
        webviews.package,
        
        tts.package,
        brightness.package
    ]
    
class OtherProject(XCProject):

    name = "my_other_project"
    dependencies = [
        camera.package,
        phpicker.package,
        webviews.package,
        
        tts.package,
        brightness.package
    ]
    


class MyDirectory(WorkDirectory):

    python = "python3.9" # or write full path to your python

    projects = [
        MyProject,
        OtherProject
    ]

    kivy_recipes = [
        "pillow"
    ]

    pips = [
        "kivymd",
        "pygments"
    ]

directory = MyDirectory
