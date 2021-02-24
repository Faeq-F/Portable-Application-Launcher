import os, pickle, time, win32com.client
import sys
#allows working path to be scanned
from os import listdir

#gets working directory
directory = os.getcwd()
#redirects to directory with portable apps
directory = directory[:-8]


def update():
    #list with all apps
    AllAppsFolders = listdir(directory)
    #all executable files for apps (.exe files with name) - ([directory to executable file,name of file without file extention],{next item})
    executables = []
    #all files in portable apps directory
    files = []
    #adding items to above lists
    # r=root, d=list of directories, f = list of files
    for r, d, f in os.walk(directory):
        for file in f:
            #checks if the file is executable
            if file[-4:] == '.exe' or file[-4:] == '.jar' or file[-4:] == '.py' or file[-4:] == '.ps' or file[-4:] == '.bat':
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

update()

with open(directory+"Launcher//executableList.txt", 'rb') as fp:
    executables = pickle.load(fp)

paths=[]

for i in executables:
    j = i[1]
    text = j[3:]
    paths.append(text)

for i in paths:
    appposition = i
    drive = str(os.getcwd())
    drive = drive[:-40]
    appposition = drive+appposition
    ogappposition = appposition
    appposition = '\"' + appposition + '\"'
    print(appposition)
    location = "E:\\Computer-Resources\\Shortcuts to apps\\"
    splitstring = appposition.split('\\')
    name = splitstring[4]
    name = name[:-5]
    print(name)
    nameAndExtension = name+'.lnk'

    path = os.path.join(location, nameAndExtension)
    
    target = appposition
    icon = ogappposition+',0'

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()

