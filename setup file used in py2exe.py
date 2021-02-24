from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {}},
    zipfile = None,
    windows = [{
            'script': "E:\Computer-Resources\PortableApps\Launcher\Faeq's Portable Application Collection - final program that was converted to exe.py",
            "icon_resources": [(1, "E:\Computer-Resources\PortableApps\Launcher\Icon_for_windows.ico")],
            "dest_base":"Faeq's Portable Application Collection"
            }],
    name = "Faeq's Portable Application Collection",
    version = "0.1",
    author = "Faeq",
    author_email = "faeqfaisal@hotmail.co.uk",
    license = "Free for any use",

)
