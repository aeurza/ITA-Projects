import serial
import tkinter as gui
from tkinter import HORIZONTAL, messagebox
import time
import numpy as np

arduino = serial.Serial("COM6", 9600)
time.sleep(2)


def mov_cuerpo(a):
    a = 's1' + str(val_cuerpo.get()) + '\n'
    arduino.write(a.encode('utf-8'))

home_cero = 90
val_cuerpo = gui.IntVar(value=home_cero)

pos_cuerpo = np.linspace(home_cero, home_cero, num=1)


control = gui.Tk()

cuerpo_s = gui.Scale(control, variable=val_cuerpo, command=mov_cuerpo, to=180, orient=HORIZONTAL, length=300, label='Cuerpo', font=("ProductSans", 14), cursor="hand1")


control.mainloop()