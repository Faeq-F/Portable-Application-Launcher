#--------------------------------------modules used---------------------------------------#
import time  # |
import os  # |
from math import *  # |
import tkinter as tk
from tkinter import *
from string import ascii_uppercase
import ctypes
import functools
from PIL import Image
from PIL import ImageTk
import PIL
from os import listdir
from PIL import Image, ImageFont, ImageDraw, ImageTk
import textwrap
import pickle
from elevate import elevate
import warnings
#does not show the warnings in the shell
warnings.filterwarnings("ignore")
import sys
import wx.adv
import wx
import os
import wmi
#to check where the last click was
lastClickX = 0
lastClickY = 0
#allows apps to open as their own processes instead of children processses to the program
import subprocess
from multiprocessing import Process
#allows program to run with administrative privelages
#elevate(show_console=False)
import threading



def checkNOW():
    while True:
        try:
            search = entry_field.get()
            print(search)
        except:
            time.sleep(0)


thread = threading.Thread(target=checkNOW)
thread.daemon = True
thread.start()


imagetouse = []
#--------------------------------------scrolling---------------------------------------#
def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
count = 0
#--------------------------------------directory and application listing---------------------------------------#
#gets working directory
directory = os.getcwd()
#redirects to directory with portable apps
directory = directory + "Computer Resources\\PortableApps\\"
#function to update executable list
with open(directory+"Launcher\\executableList.txt", 'rb') as fp:
    executables = pickle.load(fp)
#list of executable file names
names = []
#adds names to names list
for app in executables:
    name = app[1]
    names.append(name)
#--------------------------------------GUI---------------------------------------#

#executes apps using the directory and functools
def executeApps(appdir):
    from subprocess import Popen, PIPE
    # use this if you want to suppress output to stdout from the subprocess
    FNULL = open(os.devnull, 'w')
    args = appdir
    #opens process as its own parent process, not a child process
    proc = Popen(appdir, stdout=PIPE, stderr=PIPE,
                 encoding='utf8', errors='ignore')



root = tk.Tk()

root.wm_overrideredirect(True)
root.attributes("-topmost", True)

def update():
    #list with all apps
    AllAppsFolders = listdir(directory)
    #all executable files for apps (.exe files with name) - ([directory to executable file,name of file without file extention],{next item})
    executables = []
    #all files in portable apps directory
    files = []
    #adding items to above lists
    # r=root, d=directories, f = files
    for r, d, f in os.walk(directory):
        for file in f:
            #checks if the file is executable
            if file[-4:] == '.exe':
                #adds the directory to the file to the sublist
                file = os.path.join(r, file)
                #checking if the executable is within the root folder for the application data
                splitstring = file.split('\\')
                length = len(splitstring)
                #anything more than five is not in application root folder
                if int(length) > 5:
                    #skips
                    time.sleep(0)
                else:
                    #adds directory to sublist
                    filename = splitstring[len(splitstring) - 1]
                    #removes file extention and adds directory and file name to sublist
                    newlist = (file, filename[:-4])
                    #adds executable to list
                    executables.append(newlist)
            else:
                #skips if not an executable
                time.sleep(0)

    #writes the executable list to a file to speed up boot time
    with open(directory+'Launcher//executableList.txt', 'wb') as fp:
        pickle.dump(executables, fp)

    extract = [item[0] for item in executables]
    try:
        import shutil
        shutil.rmtree(directory + "Launcher\\icons")
    except:
        time.sleep(0)
    os.mkdir(directory+"Launcher\\icons")
    for i in extract:
        #gets the icons from every program executable needed
        command = directory+"Launcher\\BatchIconExtractor.exe  \""+i+"\""
        p12 = subprocess.Popen(command, shell=False)
        c = wmi.WMI()
        for p in c.Win32_Process(Name="BatchIconExtractor.exe"):
            os.system("taskkill /im BatchIconExtractor.exe")

    #closes window
    self.destroy()

    #creates new window
    mainWindow = tk.Tk()
    mainWindow.overrideredirect(True)

    #window's icon
    try:
        mainWindow.iconbitmap(
            directory+"Launcher\\Icon_for_windows.ico")
    except:
        time.sleep(0)

        #can't resize window
    mainWindow.resizable(width=False, height=False)

    #centers window on the screen

    mainWindow.geometry('1700x50')
    mainWindow['bg'] = '#FFFFFF'

    CustomFont_Label(mainWindow, text="Please relaunch program",
                        font_path=directory+"Launcher\\Phenomena-Regular.ttf", size=40, bg='#FFFFFF').grid(sticky='n')
    center(mainWindow)
    time.sleep(5)
    sys.exit(0)

    #runs window
    mainWindow.mainloop()




##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#end of update function
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################




#--------------------------------------window items---------------------------------------#
from PIL import Image, ImageFont, ImageDraw, ImageTk
import textwrap

#--------------------------------------functions for using custom font without installation---------------------------------------#
def truetype_font(font_path, size):
    return ImageFont.truetype(font_path, size)

class CustomFont_Label(Label):
    def __init__(self, master, text, foreground="#0095B6", truetype_font=None, font_path=None, family=None, size=None, **kwargs):
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")

            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)

        width, height = truetype_font.getsize(text)

        image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        draw.text((0, 0), text, font=truetype_font, fill=foreground)

        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

class CustomFont_Message(Label):
    def __init__(self, master, text, width, foreground="#0095B6", truetype_font=None, font_path=None, family=None, size=None, **kwargs):
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")

            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)

        lines = textwrap.wrap(text, width=width)

        width = 0
        height = 0

        line_heights = []
        for line in lines:
            line_width, line_height = truetype_font.getsize(line)
            line_heights.append(line_height)

            width = max(width, line_width)
            height += line_height

        image = Image.new("RGBA", (width, height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        y_text = 0
        for i, line in enumerate(lines):
            draw.text((0, y_text), line,
                        font=truetype_font, fill=foreground)
            y_text += line_heights[i]

        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

    #--------------------------------------creation of bg and items---------------------------------------#

#creates a canvas to put the image on
PutImageForBackground = Canvas(root)

#displays canvas
PutImageForBackground.grid()

#puts image for background onto canvas
image1 = PhotoImage(
    file=directory+"Launcher\\blankbg.gif")

#keep a link to the image to stop the image being garbage collected
PutImageForBackground.img = image1

#resizes background image
displayimage = image1.subsample(1, 1)

#displays image in background
PutImageForBackground.create_image(400, 300, image=displayimage)

# create frame
frame1 = tk.Frame(PutImageForBackground, bg='#FFFFFF', padx=10)
frame1.grid(sticky=tk.W)

#--------------------------------------class for item list using scrollable frame---------------------------------------#
class ScrollbarFrame(tk.Frame):
    #Extends class tk.Frame to support a scrollable Frame - This class is independent from the widgets to be scrolled and can be used to replace a standard tk.Frame

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        # The Scrollbar, layout to the right
        vsb = tk.Scrollbar(self, orient="vertical")
        vsb.pack(side="right", fill="y")

        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = tk.Canvas(
            self, borderwidth=0, background="#ffffff", height=400, width=280)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.configure(command=self.canvas.yview)

        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = tk.Frame(
            self.canvas, background=self.canvas.cget('bg'))
        self.canvas.create_window(
            (4, 4), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        #Set the scroll region to encompass the scrolled frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

labelspace = tk.Label(frame1, text="", background='white', font=(
    "calibri", 12), justify=LEFT)
labelspace.grid(sticky="w")

# Use your font here: font_path
CustomFont_Label(frame1, text="Portable Apps Launcher",
                    font_path=directory+"Launcher\\Phenomena-Regular.ttf", size=20, bg='#FFFFFF').grid()

#original use for class (just incase it is needed)
#CustomFont_Message(inner_frame, text=lorem_ipsum, width=40,
#               font_path=directory+"Launcher\\Phenomena-Regular.ttf", size=40).pack(pady=(30, 0))

#creates empty space with varied heights
labelspace = tk.Label(frame1, text="", background='white', font=(
    "calibri", 12), justify=LEFT)
labelspace.grid(sticky="w")

#--------------------------------------creation of scrollable frame---------------------------------------#
sbf = ScrollbarFrame(frame1)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)
sbf.grid(row=0, column=0, sticky='nsew')
frame = sbf.scrolled_frame
#original creation just incase
# sbf.pack(side="top", fill="both", expand=True)

#--------------------------------------sorting list of apps and relaying execution commands to executeapps function---------------------------------------#
mylist = []
for name in names:
    name = name.replace('portable', '')
    name = name.replace('Portable', '')
    mylist.append(name)
mylist.sort(key=str.lower)

def func(name):
    extract = [item[0] for item in executables]
    # Driver code
    for i in extract:
        if name in i:
            appposition = i
            p1 = threading.Thread(
                name='child procs', target=executeApps(appposition))
            p1.start()
        else:
            continue

#--------------------------------------numerating rows and adding icons---------------------------------------#

icons = []

# Some data, layout into the sbf.scrolled_frame

for row in range(len(executables)):
    text = "%s" % row
    CustomFont_Label(frame, text=text, font_path=directory+"Launcher\\Phenomena-Regular.ttf",
                        size=20, bg='#FFFFFF', relief=FLAT, borderwidth="1").grid(row=row, column=0)

for item in mylist:
    for r, d, f in os.walk(directory + "Launcher\\icons\\"):
        for file in f:
            #checks if the file is executable
            if '.ico' in file:
                #adds executable to list
                icons.append(file)
            else:
                #skips if not an executable
                time.sleep(0)
    possibleimage = [s for s in icons if item.lower() in s.lower()]
    try:
        from PIL import Image, ImageTk
        if len(possibleimage) > 1:
            imagetouse = possibleimage[0]
        else:
            time.sleep(0)
        pilImage = Image.open(
            directory + "Launcher\\icons\\"+imagetouse)
        pilImage = pilImage.resize((32, 32), resample=1)
        image = ImageTk.PhotoImage(pilImage)
        #image = image.subsample(3, 3)
        button = Button(frame, image=image, relief=FLAT,
                        bg='#FFFFFF', fg='#6EA3DE', command=functools.partial(func, item))
        button.grid(column=1, sticky=W, row=mylist.index(item))
        button.image = image
    except:
        time.sleep(0)

#--------------------------------------making list scrollable using mouse wheel and adding items---------------------------------------#

frame.bind("<MouseWheel>", mouse_wheel)

for item in mylist:
    CustomFont_Label(frame, text=item, font_path=directory+"Launcher\\Phenomena-Regular.ttf",
                        size=20, bg='#FFFFFF').grid(column=2, row=mylist.index(item), sticky=W)

    #--------------------------------------rest of window---------------------------------------#

entry_field = tk.Entry(root, width=60, fg='#0000FF', cursor="target")
entry_field.grid(row=3, column=0)


#creates update button
updateimage = tk.PhotoImage(file=directory+"Launcher\\update.png")
#resizes background image
updateimagee = updateimage.subsample(3, 3)
updateButton = tk.Button(frame1, image=updateimagee, bg="#FFFFFF", fg='#FFFFFF', relief=FLAT, cursor= "target", command=update)
updateButton.grid(sticky=W, row=4, column=0)
updateButton.image = updateimagee

#exit button
Quitimage = tk.PhotoImage(file=directory+"Launcher\\5.gif")
#resizes background image
Quitimagee = Quitimage.subsample(3, 3)

QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF", fg='#FFFFFF', relief=FLAT, cursor= "target", command=root.destroy)

QuitButton.grid(sticky="w", row=5, column=0)
QuitButton.image = Quitimagee
root.mainloop()
