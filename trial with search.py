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

icons=[]

def checkNOW():
    while True:
        try:
            search = entry_field.get()
            print(search)
            while search == "":
                #--------------------------------------numerating rows and adding icons---------------------------------------#
                # Some data, layout into the sbf.scrolled_frame
                for row in range(len(executables)):
                    text = "%s" % row
                    CustomFont_Label(frame, text=text, font_path=directory+"Launcher\\Phenomena-Regular.ttf",
                                     size=20, bg='#FFFFFF', relief=FLAT, borderwidth="1").grid(row=row, column=0)

                for item in mylist:
                    for r, d, f in os.walk(directory +"Launcher\\icons\\"):
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
                        pilImage = Image.open(directory + "Launcher\\icons\\"+imagetouse)
                        pilImage = pilImage.resize((32, 32), resample=1)
                        image = ImageTk.PhotoImage(pilImage)
                        #image = image.subsample(3, 3)
                        button = Button(frame, image=image, relief=FLAT,
                                        bg='#FFFFFF', fg='#6EA3DE', command=functools.partial(func, item))
                        button.grid(column=1, sticky=W, row=mylist.index(item))
                        button.image = image
                    except:
                        time.sleep(0)


                for item in mylist:
                    CustomFont_Label(frame, text=item, font_path=directory+"Launcher\\Phenomena-Regular.ttf",
                                     size=20, bg='#FFFFFF').grid(column=2, row=mylist.index(item), sticky=W)
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

def func(name):
    extract = [item[0] for item in executables]
    # Driver code
    for i in extract:
        if name in i:
            appposition = i
            p1 = threading.Thread(name='child procs', target=executeApps(appposition))
            p1.start()
        else:
            continue


with open(directory+"Launcher\\executableList.txt", 'rb') as fp:
    global executables
    executables = pickle.load(fp)

#list of executable file names
names=[]
#adds names to names list
for app in executables:
    name = app[1]
    names.append(name)

mylist = []
for name in names:
    name = name.replace('portable','')
    name = name.replace('Portable','')
    mylist.append(name)
mylist.sort(key=str.lower)




#--------------------------------------GUI---------------------------------------#

def center(win):#                                                                                             |
    #                                                                                                         |
    #updates window to make it active#                                                                        |
    win.update_idletasks()#                                                                                   |
    #                                                                                                         |
    #finds width of screen#                                                                                   |
    width = win.winfo_width()#                                                                                |
    #                                                                                                         |
    #finds height of screen#                                                                                  |
    height = win.winfo_height()#                                                                              |
    #                                                                                                         |
    #creates the x coordinate for the window by finding the center by dividing it by 2#                       |
    x = (win.winfo_screenwidth() // 2) - (width // 2)#                                                        |
    #                                                                                                         |
    #creates the y coordinate for the window by finding the center by dividing it by 2#                       |
    y = (win.winfo_screenheight() // 2) - (height // 2)#                                                      |
    #                                                                                                         |
    #creates the final coordinates#                                                                           |
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))#                                                  |


#--------------------------------------global functions and classes---------------------------------------#

#executes apps using the directory and functools
def executeApps(appdir):
    from subprocess import Popen, PIPE
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = appdir
    #opens process as its own parent process, not a child process
    proc = Popen(appdir, stdout=PIPE, stderr=PIPE,encoding='utf8', errors='ignore')

#creates frame for window with a gradient (easier to see window with overideredirect on)
class GradientFrame(tk.Canvas):
    #A gradient frame which uses a canvas to draw the background
    def __init__(self, parent, borderwidth=1, relief="sunken"):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        #left color
        self._color1 = "SteelBlue1"
        #right color
        self._color2 = "DodgerBlue3"
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        #Draw the gradient
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

#actual application
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_overrideredirect(True)
        self.attributes("-topmost", True)

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
                shutil.rmtree(directory +"Launcher\\icons")
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
                mainWindow.iconbitmap(directory+"Launcher\\Icon_for_windows.ico")
            except:
                time.sleep(0)

                #can't resize window
            mainWindow.resizable(width=False, height=False)

            #centers window on the screen

            mainWindow.geometry('1700x50')
            mainWindow['bg'] = '#FFFFFF'

            CustomFont_Label(mainWindow, text="Please relaunch program",
                        font_path=directory+"Launcher\\Phenomena-Regular.ttf", size=40,bg = '#FFFFFF').grid(sticky= 'n')
            center(mainWindow)
            time.sleep(5)
            sys.exit(0)


            #runs window
            mainWindow.mainloop()

        #--------------------------------------creation of frames---------------------------------------#
        gradient_frame = GradientFrame(self)
        gradient_frame.pack(side="top", fill="both", expand=True)
        inner_frame = tk.Frame(gradient_frame)
        inner_frame.pack(side="top", fill="both", expand=True, padx=8, pady=(16,8))


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
                    draw.text((0, y_text), line, font=truetype_font, fill=foreground)
                    y_text += line_heights[i]

                self._photoimage = ImageTk.PhotoImage(image)
                Label.__init__(self, master, image=self._photoimage, **kwargs)

            #--------------------------------------creation of bg and items---------------------------------------#

        #creates a canvas to put the image on
        PutImageForBackground = Canvas(inner_frame)

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
        frame1 = tk.Frame(PutImageForBackground,bg='#FFFFFF',padx=10)
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
#        labelspace = tk.Label(frame1, text="", background='white', font=(
 #           "calibri", 12), justify=LEFT)
  #      labelspace.grid(sticky="w")


        #--------------------------------------creation of scrollable frame---------------------------------------#
        sbf = ScrollbarFrame(frame1)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        sbf.grid(row=0, column=0, sticky='nsew')
        global frame
        frame = sbf.scrolled_frame
        #original creation just incase
        # sbf.pack(side="top", fill="both", expand=True)

#--------------------------------------sorting list of apps and relaying execution commands to executeapps function---------------------------------------#

        
        #--------------------------------------making list scrollable using mouse wheel and adding items---------------------------------------#

        frame.bind("<MouseWheel>", mouse_wheel)

            #--------------------------------------rest of window---------------------------------------#
        global entry_field
        #text entry field                                                                                            |
        imag = tk.PhotoImage(file=directory+"Launcher\\entry.gif")#                                                                      |
        #makes the image smaller (by subsampling)                                                                    |
        imagee = imag.subsample(4, 4)#                                                                               |
        s = tk.Label(frame1, borderwidth=1, image=imagee, bg = '#FFFFFF')#                                           |
        #                                                                                                            |
        #places the image behind the entry field                                                                     |
        s.grid(row=3, column=0)
        s.image = imagee#                                                                                            |
        #                                                                                                            |
        #creartes a entry field that only allows integers to be entered                                              |
        #(uses a class that I defined above)                                                                         |
        #                                                                                                            |
        entry_field = Entry(frame1,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',12), fg = 'SteelBlue1')#     |
        entry_field.grid(row=3, column=0)

        #entry_field = tk.Entry(frame1, width=60, fg='#0000FF', cursor="target")

        #entry_field.grid(row=3, column=0)

        #creates update button
        updateimage = tk.PhotoImage(file=directory+"Launcher\\update.png")
        #resizes background image
        updateimagee = updateimage.subsample(2, 2)
        updateButton = tk.Button(frame1, image=updateimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=update)
        updateButton.grid(sticky=NSEW, row = 4, column = 0)
        updateButton.image = updateimagee


        #exit button
        Quitimage = tk.PhotoImage(file=directory+"Launcher\\5.gif")
        #resizes background image
        Quitimagee = Quitimage.subsample(3, 3)


        QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=self.destroy)

        QuitButton.grid(sticky=NSEW,row=5,column = 0)
        QuitButton.image = Quitimagee





TRAY_TOOLTIP = 'Faeq\'s Portable Apps Collection'
TRAY_ICON = directory+'//Launcher//Icon_for_windows.ico'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TrApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    TrayApp = TrApp(False)
    TrayApp.MainLoop()





class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        #--------------------------------------making window draggable---------------------------------------#

        def SaveLastClickPos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y

        def Dragging(event):
            x, y = event.x - lastClickX + app.winfo_x(), event.y - lastClickY + \
                app.winfo_y()
            app.geometry("+%s+%s" % (x, y))

        app = SampleApp()
        app.bind('<Button-1>', SaveLastClickPos)
        app.bind('<B1-Motion>', Dragging)
        app.mainloop()


    def on_exit(self, event):
        os._exit(1)

#--------------------------------------running program---------------------------------------#


if __name__ == "__main__":
    main()
