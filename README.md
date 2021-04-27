# Portable-Application-Launcher
A launcher for portable apps on your usb drive or computer

This launcher is a way of running your portable apps easily, without the need for shortcuts or looking through multiple folders or directories for the executable files.

## Requirements:
 - A computer running Windows 7 or higher
 - A folder hierarchy where the Launcher file is at the root of it and portable apps are at "\Computer-Resources\PortableApps\"
 - Any portable apps being used have their main executable file at the root of their respected folder (e.g. "\Computer-Resources\PortableApps\PortableApp1\PortableApp1.exe")
 - A Windows defender exclusion for the location of the launcher and it's Portable Apps (Add exclusions to any other anti-malware software that is installed on your computer; you do not want the software to mistake the apps for viruses or other malware.)

## Suggestions:
 - Keeping portable applications on a USB drive enables you to use an appication on any computer with ease
 - Setting up a task to run the launcher at startup in Task Scheduler helps ease of use as you won't need to start the program manually
 - The 'Phenomena' fontface was used to give a cleaner look to the program. The font does not need to be installed for use but if you are using it, the 'Phenomena-Regular.ttf' file just needs to be placed in the "\Computer-Resources\PortableApps\Launcher\" directory
 - If you wish to do so, you can use the 'shortcuts for ease of use.py' program to create shortcuts for all of your portable apps in a new directory so that you can combine other launchers with the program

## Instuctions for use:
1. Run the launcher and click on it's icon in the system tray.<br><br>
    You can search for the program you want in the search field
2. Select your program by either using the arrow keys or by clicking on it with your mouse pointer
3. Press enter to execute the app

    If you have added new programs, you can press the 'update list' button to rebuild the list; this will need a program restart <br>
    If you have executed your app, you can press 'exit launcher' to minimise it's window. To get back to it, just press on the launcher icon in the system tray again<br>
    If you wish to close the launcher, you can right-click the launcher icon in the system tray and press on 'exit'

## Screenshots:
![LanucherScreenshot1](https://user-images.githubusercontent.com/61658458/110971701-1acb7e00-8353-11eb-92e0-30561f996a04.png)
![LauncherScreenshot2](https://user-images.githubusercontent.com/61658458/110971703-1b641480-8353-11eb-9860-ca551d4d5b1c.png)
