import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pygame import mixer


def playMusic():
    try:
        paused  # if pause is initialized or not
    except NameError:
        try:
            mixer.music.load(fileName)
            mixer.music.play()
            statusBar['text'] = "now playing       " + \
                os.path.basename(fileName)
        except:
            tkinter.messagebox.showerror("Error", "No music is added")
    else:
        mixer.music.unpause()
        statusBar['text'] = "Music Resumed"


def pauseMusic():
    global paused
    paused = True
    mixer.music.pause()
    statusBar['text'] = "Music Paused"


def stopMusic():
    mixer.music.stop()
    statusBar['text'] = "Music Stopped"


def setVolume(val):
    volume = int(val)/100
    # set the volume (value must be inbetween 0.0 to 1.0)
    mixer.music.set_volume(volume)


def about_us():
    tkinter.messagebox.showinfo("About This Player", "Alif Biswas || #1502060")


def browse_file():
    global fileName
    fileName = filedialog.askopenfilename()


# Initializing Everything
root = Tk()
mixer.init()

# Top Bar & Window Size
root.geometry('600x400')
root.title("Furu's Music Player")
root.iconbitmap('fmp.ico')

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a subMenu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Open', command=browse_file)
subMenu.add_command(label='Exit', command=root.destroy)

# Create a subMenu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='About Us', command=about_us)
subMenu.add_command(label='Contact')


# Play Button
playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=playMusic)
playBtn.pack()

# Stop Button
stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stopMusic)
stopBtn.pack()

# Pause Button
pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pauseMusic)
pauseBtn.pack()

# Volume Scale
initVolume = 10
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=setVolume)
scale.set(initVolume)
mixer.music.set_volume(initVolume/100)
scale.pack()

# Create a status bar
statusBar = Label(root, text='Welcome to Music Player',
                  relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)


root.mainloop()
