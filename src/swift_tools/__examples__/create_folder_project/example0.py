
from package_tools import WorkDirectory, XCProject

from standard import camera, phpicker, webviews, notification, speech_recognizer
from plyer import brightness, tts, filechooser, audio


class MyProject(XCProject):

    name = "please_work"
    python_source = "/Volumes/WorkSSD/pyswifttests/pysrc"
    linked_source = True

    dependencies = [
        camera.package,
        phpicker.package,
        webviews.package,
        notification.package,
        filechooser.package,
        tts.package,
        brightness.package,
        audio.package,
        speech_recognizer.package
    ]
    

class MyDirectory(WorkDirectory):

    python = "python3.9" # or write full path to your python, default is python3.9
    # overwrite site-packages
    site_packages = "venv/lib/python3.9/site-packages" 

    projects = [
        MyProject,
    ]

    kivy_recipes = [
        "pillow"
    ]

    pips = [
        "kivymd",
        "pygments"
    ]
project = MyProject
#directory = MyDirectory
