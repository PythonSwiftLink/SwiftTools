
from swift_tools.package_tools import WorkDirectory, XCProject

#atm only swift_tools plyer and standard supports this system, other wrappers must be added manually
from swift_tools.standard import camera, phpicker, webviews, notification, speech_recognizer
from swift_tools.plyer import brightness, tts, filechooser, audio


class MyProject(XCProject):

    name = "my_project"
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

    python = "python3.10" # or write full path to your python, default is python3.9
    # overwrite site-packages
    site_packages = "venv/lib/python3.10/site-packages" 

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


#project = MyProject
directory = MyDirectory


