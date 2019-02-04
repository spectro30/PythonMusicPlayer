from tkinter import *
from pygame import mixer


def playMusic():
    mixer.music.load("musicTitanic.mp3")
    mixer.music.play()


def stopMusic():
    mixer.music.stop()


def setVolume(val):
    volume = int(val)/100
    # set the volume (value must be inbetween 0.0 to 1.0)
    mixer.music.set_volume(volume)


# Initializing Everything
root = Tk()
mixer.init()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create a subMenu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project')
subMenu.add_command(label='Exit')

# Create a subMenu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='About Us')
subMenu.add_command(label='Contact')

# Top Bar & Window Size
root.geometry('600x400')
root.title("Furu's Music Player")
root.iconbitmap('fmp.ico')

# Play Button
playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=playMusic)
playBtn.pack()

# Stop Button
stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stopMusic)
stopBtn.pack()

# Volume Scale
initVolume = 10
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=setVolume)
scale.set(initVolume)
mixer.music.set_volume(initVolume/100)
scale.pack()


root.mainloop()
