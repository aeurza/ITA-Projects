# Importar las bibliotecas necesarias
import tkinter as gui
from tkinter import *
from tkinter import HORIZONTAL, messagebox
import time
import numpy as np
import serial

# Simulación de comunicación serial
class SerialSimulation:
    def __init__(self):
        self.buffer = ""

    def write(self, data):
        self.buffer += data

#!Simula la instancia de comunicación serial

# arduino = SerialSimulation()

# arduino = serial.Serial("COM6", 9600)
# time.sleep(2)

# Constantes para HOME de cada articulación
home_base = 90  # Detener el servo en su posición central
home_hombro = 130
home_codo = 180
home_pinza = 0

# Variables para el estado de los servos
base_speed = 0  # Velocidad de rotación de la base
base_position = home_base  # Posición actual de la base
hombro_position = home_hombro
codo_position = home_codo
pinza_position = home_pinza

# Función para actualizar la posición de la base
def update_base_position():
    global base_position
    base_position += base_speed
    if base_position > 180:
        base_position = 180
    elif base_position < 0:
        base_position = 0

    # Actualizar el valor de la escala y enviarlo al simulador (esto simularía la posición del servo)
    val_base.set(base_position)
    a = 's1' + str(base_position) + '\n'
    arduino.write(a.encode('utf-8'))

# Función para mover la base a la izquierda
def move_base_left():
    global base_speed
    base_speed += 1  # Aumentar velocidad hacia la izquierda

# Función para mover la base a la derecha
def move_base_right():
    global base_speed
    base_speed -= 1  # Aumentar velocidad hacia la derecha

# Función para detener la base
def stop_base():
    global base_speed
    base_speed = 0  # Detener el movimiento

# Función para guardar la posición actual de la base
def guarda_pos():
    # Guardar la posición actual en un vector
    pos_base.append(base_position)

# Función para enviar cada punto de la trayectoria de la base al robot
def trayectoria_base():
    for pos in pos_base:
        base_position = pos
        update_base_position()
        time.sleep(0.002)
        # Coloca el slider en la posición indicada
        val_base.set(base_position)

# Función para mover el hombro
def move_hombro(a):
    a = 's2' + str(val_hombro.get()) + '\n'
    arduino.write(a.encode('utf-8'))

# Función para mover el codo
def move_codo(a):
    a = 's3' + str(val_codo.get()) + '\n'
    arduino.write(a.encode('utf-8'))

# Función para mover la pinza
def move_pinza(a):
    a = 's4' + str(val_pinza.get()) + '\n'
    arduino.write(a.encode('utf-8'))

# Función para guardar la posición actual de los otros servos
def guarda_pos_hombro_codo_pinza():
    pos_hombro.append(hombro_position)
    pos_codo.append(codo_position)
    pos_pinza.append(pinza_position)

# Función para enviar cada punto de la trayectoria de los otros servos al robot
def trayectoria_hombro_codo_pinza():
    for i in range(len(pos_hombro)):
        a = 's2' + str(pos_hombro[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.002)
        a = 's3' + str(pos_codo[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.002)
        a = 's4' + str(pos_pinza[i]) + '\n'
        arduino.write(a.encode('utf-8'))
        time.sleep(0.002)
        # Coloca los sliders en las posiciones indicadas
        val_hombro.set(pos_hombro[i])
        val_codo.set(pos_codo[i])
        val_pinza.set(pos_pinza[i])

# Función para detener todos los servos
def stop_servos():
    global base_speed
    base_speed = 0

# Función para enviar todos los servos a la posición de HOME
def home_robot():
    global base_speed, base_position, hombro_position, codo_position, pinza_position
    base_speed = 0
    base_position = home_base
    hombro_position = home_hombro
    codo_position = home_codo
    pinza_position = home_pinza
    update_base_position()
    val_hombro.set(home_hombro)
    val_codo.set(home_codo)
    val_pinza.set(home_pinza)
    messagebox.showinfo('Atención', 'Robot en posición de HOME')



# !Instrucciones para la interfaz de usuario
control = gui.Tk()
control.title("Team Rocket")
#& control.configure(cursor="size 150x150")
control.geometry('1020x500')


image = PhotoImage(file="Robot1.PNG")
image = image.zoom(6)
image = image.subsample(15)

img = Label(control, image = image, width=200,height=500)

img.pack()




# Variables utilizadas para la posición de cada servo
val_base = gui.IntVar(value=home_base)
val_hombro = gui.IntVar(value=home_hombro)
val_codo = gui.IntVar(value=home_codo)
val_pinza = gui.IntVar(value=home_pinza)
pos_base = []
pos_hombro = []
pos_codo = []
pos_pinza = []

# Barras deslizantes para el control
base_s = gui.Scale(control, variable=val_base, to=180, orient=HORIZONTAL, length=400,
                   label='Base', font=("Great Vibes", 10))
hombro_s = gui.Scale(control, variable=val_hombro, to=18, orient=HORIZONTAL, length=400,
                    label='Hombro', font=("Great Vibes", 10))
codo_s = gui.Scale(control, variable=val_codo, to=180, orient=HORIZONTAL, length=400,
                   label='Codo', font=("Great Vibes", 10))
pinza_s = gui.Scale(control, variable=val_pinza, from_=10, to=90, orient=HORIZONTAL, length=400,
                   label='Pinza', font=("Great Vibes", 10))

# Botones para el control
btn_move_left = gui.Button(text="<===", command=move_base_left, pady=0, width=10, bg="#6f70fb", bd=1,
                           height=1, relief="raised", borderwidth=8, font=("Great Vibes", 15, "bold"), cursor="hand1", fg="#fafbfd")

btn_move_right = gui.Button(text="===>", command=move_base_right, pady=0, width=10, bg="#6f70fb", bd=5,
                            height=1, relief="raised", borderwidth=8, font=("Great Vibes", 15, "bold"), cursor="hand1", fg="#fafbfd" )

btn_stop = gui.Button(text="Detener", command=stop_base, pady=0, width=15, bg="#8ED1FC", bd=5,
                      height=3, relief="raised", borderwidth=5, font=("Great Vibes", 10,"bold"), cursor="hand1")

btn_stop_servos = gui.Button(text="Detener Todos", command=stop_servos, pady=0, width=15, bg="#8ED1FC", bd=5,
                            height=3, relief="raised", borderwidth=5, font=("Great Vibes", 10,"bold"), cursor="hand1")

btn_guardar_base = gui.Button(text="Guardar Pos. Base", command=guarda_pos, pady=1, width=15, bg="#fff500", bd=5, height=3, relief="raised", borderwidth=5, font=("Great Vibes", 10,"bold"), cursor="hand1")


btn_guardar_hombro_codo_pinza =  gui.Button(text="Guardar \n Pos.Hom/Cod/Pin", command=guarda_pos_hombro_codo_pinza,pady=1, width=15, bg="#fff500", bd=5, height=3, relief="raised", borderwidth=5, font=("Great Vibes", 10,"bold"), cursor="hand1")

btn_run_base = gui.Button(text="Ejecutar Base", command=trayectoria_base, pady=1, width=15, bg="#00ff75", bd=5,
                          height=3, relief="raised", borderwidth=5, font=("Great Vibes", 10,"bold"), cursor="exchange")

btn_run_hombro_codo_pinza = gui.Button(text="Ejecutar \n Hom/Cod/Pin", command=trayectoria_hombro_codo_pinza,
                                      pady=1, width=15, bg="#00ff75", bd=5, height=3, relief="raised", borderwidth=5,
                                      font=("Great Vibes", 10,"bold"), cursor="exchange")

btn_home = gui.Button(text="Ir a Home", command=home_robot, pady=0, width=25, bg="#ff5e5e", bd=5, height=1,
                      relief="raised", borderwidth=5, font=("Great Vibes", 15,"bold"), cursor="dotbox")


# # Distribución de cada elemento en la interfaz del robot
# pinza_s.grid(row=4, column=0, columnspan=2, sticky="")                  #
# codo_s.grid(row=3, column=0, columnspan=2, sticky="nsew")                   #
# hombro_s.grid(row=6, column=0, columnspan=2, sticky="nsew")                 #
# base_s.grid(row=7, column=0, columnspan=2, sticky="nsew")                   #?
# btn_move_right.grid(row=8, column=1, sticky="nsew")                         ##6f70fb
# btn_move_left.grid(row=8, column=0, sticky="nsew")                          ##6f70fb
# btn_stop.grid(row=3, column=4, sticky="nsew")                               ##8ED1FC
# btn_stop_servos.grid(row=3, column=5, sticky="nsew")                        ##8ED1FC
# btn_guardar_base.grid(row=4, column=4, sticky="e")                          ##fff500
# btn_guardar_hombro_codo_pinza.grid(row=4, column=5, sticky="nsew")          ##fff500
# btn_run_base.grid(row=5, column=4, sticky="e")                              ##00ff75
# btn_run_hombro_codo_pinza.grid(row=5, column=5, sticky="nsew")              ##00ff75
# btn_home.grid(row=7, column=4, columnspan=2, sticky="nsew")                 ##ff5e5e




# ? imagen
img.grid(row=0, column=10, rowspan=10)

#^ ESPACIOS
space00 = Label(control, text="  ", width=2)
space00.grid(row=0, column=0, rowspan=8)

space03 = Label(control, text="  ", width=5)
space03.grid(row=0, column=3, rowspan=8)

space05 = Label(control, text="  ", width=1)
space05.grid(row=0, column=5, rowspan=6)

space09 = Label(control, text="  ", width=1)
space09.grid(row=0, column=9, rowspan=8)


pinza_s.grid(row=2, column=1, columnspan=2)                  #
codo_s.grid(row=3, column=1, columnspan=2)                   #
hombro_s.grid(row=4, column=1, columnspan=2)                 #
base_s.grid(row=5, column=1, columnspan=2)                   #?
btn_move_right.grid(row=6, column=2)                         ##6f70fb
btn_move_left.grid(row=6, column=1)                          ##6f70fb
btn_stop.grid(row=2, column=4)                               ##8ED1FC
btn_stop_servos.grid(row=2, column=6)                        ##8ED1FC
btn_guardar_base.grid(row=3, column=4)                          ##fff500
btn_guardar_hombro_codo_pinza.grid(row=3, column=6)          ##fff500
btn_run_base.grid(row=4, column=4)                              ##00ff75
btn_run_hombro_codo_pinza.grid(row=4, column=6)              ##00ff75
btn_home.grid(row=6, column=4, columnspan=3)                 ##ff5e5e


control.mainloop()