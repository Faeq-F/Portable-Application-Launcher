#add features
#ui
#search 'APP' folders in default app directoies
#dynamic drive letter changing

import pyglet
import warnings
#does not show the warnings in the shell
warnings.filterwarnings("ignore")
import wx.adv
import wx
import sys
import wmi
#to check where the last click was
lastClickX = 0
lastClickY = 0
#allows program to run with administrative privelages
from elevate import elevate
elevate(show_console=False)
import pickle
#allows lists to be written to text files to speed up boot
#allows apps to open as their own processes instead of children processses to the program
import subprocess
from multiprocessing import Process
#allows custom font to be used without installation
import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageTk
#allows working path to be scanned
from os import listdir
#previous PIL imports sometimes does not work - individual import does
import PIL
from PIL import ImageTk
from PIL import Image
#allows each item in application list to run through a function to execute the application
import functools
import time
import ctypes
from string import ascii_uppercase
import threading
from tkinter import *#                                                                      |
#makes sure that no matter what update you are on, the program will still try to work       |
import tkinter as tk#                                                                       |

#-----------------------------------------------------------------------------------------------#-------------#
#                                                                                                             |
#allows me to use math to decompress and compress data                                                        |
from math import *    #                                                                                       |
#                                                                                                             |
#                                                                                                             |
#                                                                                                             |
#                                                                                                             |
#allows me to manipulate os (mostly used for checking if things exist)                                        |
import os #                    
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


#gets working directory
directory = os.getcwd()
#redirects to directory with portable apps
directory = directory + "Computer Resources\\PortableApps\\"
pyglet.font.add_file(directory+"Launcher\\Phenomena-Regular.ttf")
#function to update executable list


with open(directory+"Launcher\\executableList.txt", 'rb') as fp:
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

#executes apps using the directory and functools
def executeApps(appdir):
    from subprocess import Popen, PIPE
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = appdir
    #opens process as its own parent process, not a child process
    proc = Popen(appdir, stdout=PIPE, stderr=PIPE,encoding='utf8')#, errors='ignore'

        
def CurSelet(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    extract = [item[0] for item in executables]
    # Driver code
    for i in extract:
        if picked in i:
            appposition = i
            print(i)
            p1 = threading.Thread(name='child procs', target=executeApps(appposition))
            p1.start()
        else:
            continue


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
    
#First create application class
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #These variables will be used in the poll function so i 
        #Set them at the start of the program to avoid errors.
        self.search_var = StringVar()
        self.switch = False
        self.search_mem = ''

        self.grid()
        self.create_widgets()

    #Create main GUI window
    def create_widgets(self):
        #Use the StringVar we set up in the __init__ function 
        #as the variable for the entry box
        #--------------------------------------creation of frames---------------------------------------#
        
#--------------------------------------window items---------------------------------------#
        from PIL import Image, ImageFont, ImageDraw, ImageTk
        import textwrap

        self.entry = Entry(self, textvariable=self.search_var, width=13)
        self.lbox = Listbox(self, width=45, height=15, font=('Phenomena',15))
                        
  

        self.lbox.bind('<<ListboxSelect>>',CurSelet)


        self.entry.grid(row=0, column=0, padx=10, pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3)
        
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
        lbox_list = mylist

        self.lbox.delete(0, END)

        for item in lbox_list:
            if is_contact_search == True:
                #Searches contents of lbox_list and only inserts
                #the item to the list if it self.search is in 
                #the current item.
                if self.search.lower() in item.lower():
                    self.lbox.insert(END, item)
            else:
                self.lbox.insert(END, item)

root = Tk()
center(root)
app = Application(master=root)
app.mainloop()

