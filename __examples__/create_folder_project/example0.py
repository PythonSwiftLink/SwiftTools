print(globals())


from package_tools import WorkDirectory, XCProject

from standard import camera, phpicker, webviews
from plyer import brightness, tts


class MyProject(XCProject):

    name = "my_project"
    python_source = "/Volumes/WorkSSD/pyswifttests/pysrc"
    linked_source = True

    dependencies = [
        camera.package,
        # phpicker.package,
        # webviews.package,
        
        # tts.package,
        # brightness.package
    ]
    
# class OtherProject(XCProject):

#     name = "my_other_project"
#     dependencies = [
#         camera.package,
#         # phpicker.package,
#         # webviews.package,
        
#         # tts.package,
#         # brightness.package
#     ]
    


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

directory = MyDirectory
