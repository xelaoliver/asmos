from tkinter import *
import math

window = Tk()
window.title("")
window.geometry("200x200")
window.geometry("+0+0")
window.resizable(0,0)
window.iconbitmap("blank.ico")

fps = 60

direction = ["+", "+"]
speed = 4
moveX = 0
moveY = 0

def main():
    if window.winfo_x() > window.winfo_screenwidth()-window.winfo_width():  
        direction[0] = "-"
    elif window.winfo_x() < 0:
        direction[0] = "+"
    if window.winfo_y() > window.winfo_screenheight()-(window.winfo_height()+((11*window.winfo_screenheight())/100.0)):
        direction[1] = "-"
    elif window.winfo_y() < 0:
        direction[1] = "+"


    if direction[0] == "+":
        moveX = speed
    else:
        moveX = -speed
    
    if direction[1] == "+":
        moveY = speed
    else:
        moveY = -speed
    
    window.geometry("+"+str(int(window.winfo_x())+moveX)+"+"+str(int(window.winfo_y())+moveY))
    window.after(math.floor(1000/fps), main)

window.after(math.floor(1000/fps), main)
window.mainloop()