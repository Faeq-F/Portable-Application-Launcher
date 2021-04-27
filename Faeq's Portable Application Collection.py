
import sys
import os
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
from threading import Thread
import tempfile
import base64
import zlib
from tkinter import *
#                                                                                               |

import tkinter as tk#                                                                       |
from tkinter import messagebox
import time

try:
    import pyglet
except:
    time.sleep(0)

def executeApps(appdir):
    try:
        #opens process as its own parent process, not a child process
        #import subprocess
        '''
        def str_to_raw(s):
            raw_map = {8: r'\b', 7: r'\a', 12: r'\f',
                10: r'\n', 13: r'\r', 9: r'\t', 11: r'\v'}
            return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)
            '''
        #appdir = str_to_raw(appdir)
        #subprocess.Popen(appdir)
        appposition = appdir[3:]
        appposition = str(os.getcwd())+appposition
        appposition = '\"' + appposition + '\"'
        batchcommand = r'Start "'+str(os.getcwd())+"Computer-Resources\\PortableApps\\Launcher\\runningExecutables.bat\" "+appposition
        os.system(batchcommand)
    except:
        messagebox.showwarning(
            "Could not open application", "Please update the list of applications\n(This should fix the problem)")

try:
    import warnings
    #does not show the warnings in the shell
    warnings.filterwarnings("ignore")
except:
    time.sleep(0)

try:
    import wx.adv
    import wx
except:
    time.sleep(0)


try:
    import wmi
except:
    time.sleep(0)

import pickle

#allows working path to be scanned
from os import listdir

#allows apps to open as their own processes instead of children processses to the program


#allows custom font to be used without installation
import textwrap

try:
    from PIL import Image, ImageFont, ImageDraw, ImageTk

    #previous PIL imports sometimes does not work - individual import does
    import PIL
    from PIL import ImageTk
    from PIL import Image
except:
    time.sleep(0)

#                                                                                                             |

def center(win):  # |
    #                                                                                                         |
    #updates window to make it active#                                                                        |
    win.update_idletasks()  # |
    #                                                                                                         |
    #finds width of screen#                                                                                   |
    width = win.winfo_width()  # |
    #                                                                                                         |
    #finds height of screen#                                                                                  |
    height = win.winfo_height()  # |
    #                                                                                                         |
    #creates the x coordinate for the window by finding the center by dividing it by 2#                       |
    x = (win.winfo_screenwidth() // 2) - (width // 2)  # |
    #                                                                                                         |
    #creates the y coordinate for the window by finding the center by dividing it by 2#                       |
    y = (win.winfo_screenheight() // 2) - (height // 2)  # |
    #                                                                                                         |
    #creates the final coordinates#                                                                           |
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # |

#creates frame for window with a gradient (easier to see window with overideredirect on)
class GradientFrame(tk.Canvas):
    #A gradient frame which uses a canvas to draw the background
    def __init__(self, parent, borderwidth=-9, relief="flat"):
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


#allows me to use math to decompress and compress data                                                        |
from math import *    #                                                                                       |
import ctypes
from string import ascii_uppercase



#gets working directory
directory = os.getcwd()
#redirects to directory with portable apps
directory = directory + "Computer-Resources\\PortableApps\\"
try:
    pyglet.font.add_file(directory+"Launcher\\Phenomena-Regular.ttf")
except:
    time.sleep(0)
#function to update executable list

try:
    with open(directory+"Launcher\\executableList.txt", 'rb') as fp:
        executables = pickle.load(fp)
except:
    time.sleep(0)






#First create application class
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        #These variables will be used in the poll function so i
        #Set them at the start of the program to avoid errors.
        self.config(bg = '#FFFFFF')
        self.search_var = StringVar()
        self.switch = False
        self.search_mem = ''


        self.grid()
        self.create_widgets()


        def click(*args):
            self.lbox.focus_set()

        def OnEntryDown(*args):
            if self.selection < self.lbox.size()-1:
                self.lbox.select_clear(self.selection)
                self.selection += 1
                self.lbox.select_set(self.selection)

        def OnEntryUp(*args):
            if self.selection > 0:
                self.lbox.select_clear(self.selection)
                self.selection -= 1
                self.lbox.select_set(self.selection)

        def SelectZero(*args):
            self.selection = 0
            self.lbox.select_set(self.selection)
        self.selection = 0
        self.lbox.select_set(self.selection)
        #self.bind_all("<Enter>", SelectZero)
        self.bind_all("<Down>", click)
        self.bind_all("<Up>", click)
        self.lbox.bind("<Down>", OnEntryDown)
        self.lbox.bind("<Up>", OnEntryUp)

        def CurSelet(event):
            try:
                i = self.lbox.curselection()[0]
                text = self.lbox.get(i)
                text = text[2:]
                widget = event.widget
                for i in executables:
                    itemname = i[0]
                    path = i[1]
                    if text == itemname:
                        appposition = path
                        executeApps(appposition)


                    # Driver code
                    else:
                        time.sleep(0)
            except:
                messagebox.showwarning("Could not open application","Please update the list of applications\n(This should fix the problem)")

        self.lbox.bind("<Return>", CurSelet)






    #Create main GUI window
    def create_widgets(self):
        #Use the StringVar we set up in the __init__ function
        #as the variable for the entry box
        '''
        #text entry field                                                                                            |
        imag = tk.PhotoImage(file="entry.gif")#                                                                      |
        #                                                                                                            |
        # create a frame and pack it                                                                                 |
        self.frame2 = tk.Frame(self,bg='#FFFFFF',padx=15)#                                                              |
        self.frame2.grid()#                                                                                               |
        #                                                                                                            |
        #makes the image smaller (by subsampling)                                                                    |
        imagee = imag.subsample(3, 3)#                                                                               |
        self.s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')#                                           |
        #                                                                                                            |
        #places the image behind the entry field                                                                     |
        self.s.grid(column = 2, row = 20)#                                                                                |
        self.s.image = imagee#                                                                                            |
        #                                                                                                            |
        #creartes a entry field that only allows integers to be entered                                              |
        #(uses a class that I defined above)                                                                         |
        #                                                                                                            |


'''
        self.entry = Entry(self, textvariable=self.search_var, width=45, font=(
            'Phenomena', 15), relief=SUNKEN, bd=3, fg='DodgerBlue3')
        self.lbox = Listbox(self, width=55, height=25, font=('Phenomena',15), activestyle = 'none', cursor = 'target', selectbackground = '#4d4dff', selectmode = SINGLE, bg = '#FFFFFF', relief = GROOVE, bd = 3, fg = 'DodgerBlue3')
        global size
        size = 'There are ', str(self.lbox.size()), ' applications'
        self.label = Label(self, text = size, font=('Phenomena',15), fg = 'DodgerBlue3', bg = '#FFFFFF')

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
                            foldername = splitstring[len(splitstring) - 2]
                            item = foldername + ' (' + filename + ')'
                            #removes file extention and adds directory and file name to sublist
                            newlist = (item, file)
                            #adds executable to list
                            executables.append(newlist)
                    else:
                        #skips if not an executable
                        time.sleep(0)

            #writes the executable list to a file to speed up boot time
            with open(directory+'Launcher//executableList.txt', 'wb') as fp:
                pickle.dump(executables, fp)
            #code thaat used to extract the icons from the executables
            '''extract = [item[0] for item in executables]
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
'''


            #closes window
            root.destroy()

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

            mainWindow.geometry('1700x100')
            mainWindow['bg'] = '#FFFFFF'

            Label(mainWindow, text="Please relaunch program", font=('Phenomena',40), bg = '#FFFFFF').grid(sticky= 'n')
            center(mainWindow)
            #runs window
            mainWindow.update()
            time.sleep(5)
            sys.exit(0)




        #end of update function

        def close():
            root.destroy()

        self.update = Button(self, text='Update list of applications', font=('Phenomena',15), command = update, relief = GROOVE, cursor = 'target', bg = '#FFFFFF', fg = 'DodgerBlue3')
        self.exit = Button(self, text='Exit launcher', font=('Phenomena',15), command = close, relief = GROOVE, cursor = 'target', bg = '#FFFFFF', fg = 'DodgerBlue3')

        self.lbox.grid(row=0, column=0, padx=10, pady=3)
        self.entry.grid(row=1, column=0, padx=10, pady=3)
        #self.entry.grid(row=1, column=0, padx=10, pady=3)
        self.label.grid(row=2, column=0, padx=10, pady=3)
        self.update.grid(row=3, column=0, padx=10, pady=3)
        self.exit.grid(row=4, column=0, padx=10, pady=3)


        #Function for updating the list/doing the search.
        #It needs to be called here to populate the listbox.
        self.update_list()

        self.poll()

    #Runs every 50 milliseconds.
    def poll(self):
        #Get value of the entry box
        self.search = self.search_var.get()
        if self.search != self.search_mem: #self.search_mem = '' at start of program.

            self.update_list(is_contact_search=True)

            #set switch and search memory
            self.switch = True #self.switch = False at start of program.
            self.search_mem = self.search

        #if self.search returns to '' after preforming search
        #it needs to reset the contents of the list box. I use
        #a 'switch' to determine when it needs to be updated.
        if self.switch == True and self.search == '':
            self.update_list()
            self.switch = False
        self.after(50, self.poll)

    def update_list(self, **kwargs):
        try:
            is_contact_search = kwargs['is_contact_search']
        except:
            is_contact_search = False

        #Just a generic list to populate the listbox
        lbox_list = executables
        self.lbox.delete(0, END)





        PlaceItem = []
        def place(PlaceItem):
            self.lbox.insert(END, PlaceItem)


        if is_contact_search == True:
            try:
                #Searches contents of lbox_list and only inserts
                #the item to the list if it self.search is in
                #the current item.

                self.data = {}
                for item in executables:
                    itemname = item[0]
                    path = item[1]
                    if self.search.lower() in itemname.lower():
                        self.data.update({itemname: path})
                        PlaceItem = '  ' + itemname
                        place(PlaceItem)
                    else:
                        time.sleep(0)


            except:
                time.sleep(0)
            size = 'There are', str(self.lbox.size()), 'applications in your search'
            size = str(size)[1:-1]
            size = size.replace('\'', '')
            size = size.replace(',', '')
            self.label.config(text = size)
        else:
            try:

                self.data = {}
                for i in executables:
                    itemname = i[0]
                    path = i[1]
                    self.data.update({itemname: path})
                    PlaceItem = '  ' + itemname
                    place(PlaceItem)
            except:
                time.sleep(0)




            size = 'There are', str(self.lbox.size()), 'applications total'
            size = str(size)[1:-1]
            size = size.replace('\'', '')
            size = size.replace(',', '')
            self.label.config(text = size)


#running app


TRAY_TOOLTIP = 'Faeq\'s Portable Apps Collection'
IconDirectory = directory[:43]
TRAY_ICON = IconDirectory+'\Icon_for_windows.ico'


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
        #try:
        global root
        root = Tk()


        ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
                                                'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON)

        root.iconbitmap(default=ICON_PATH)
        gradient_frame = GradientFrame(root)
        gradient_frame.pack(side="top", fill="both", expand=True)
        inner_frame = tk.Frame(gradient_frame, bg='#FFFFFF')
        inner_frame['bg'] = '#FFFFFF'
        inner_frame.pack(side="top", fill="both",
                        expand=True, padx=8, pady=(16, 8))
        app = Application(master=inner_frame)

        x, y = 0, 0

        def mouse_motion(event):
            global x, y
            # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
            offset_x, offset_y = event.x - x, event.y - y
            new_x = root.winfo_x() + offset_x
            new_y = root.winfo_y() + offset_y
            new_geometry = f"+{new_x}+{new_y}"
            root.geometry(new_geometry)

        def mouse_press(event):
            global x, y
            count = time.time()
            x, y = event.x, event.y

        # Hold the left mouse button and drag events
        app.bind("<B1-Motion>", mouse_motion)

        # The left mouse button press event, long calculate by only once
        app.bind("<Button-1>", mouse_press)

        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root['bg'] = '#FFFFFF'

        center(root)
        root.mainloop()
        #except:
         #   pass



    def on_exit(self, event):
        sys.exit(0)

#--------------------------------------running program---------------------------------------#


if __name__ == "__main__":
    main()
