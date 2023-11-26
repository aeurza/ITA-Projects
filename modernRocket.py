import tkinter
import tkinter.messagebox
import customtkinter
import serial
import numpy as np
import time




#^Comunicacion con arduino
# arduino = serial.Serial("COM6", 9600)
# time.sleep(2)

control = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#& Dimesiones de la ventana


control.title("Team Rocket")
control.geometry("1020x532")
control.resizable(0,0)

control.grid_columnconfigure((1,2), weight=0, )
# control.grid_rowconfigure(15, weight=1)



#*Elementos
sliders_box1a = customtkinter.CTkFrame(control,
                               width=210,
                               height=450,
                               corner_radius=10,
                            #    fg_color="#C4F5CC"
                                ).grid(row=0,
                                column=1,
                                rowspan=500,
                                columnspan=2,
                                sticky="nsew",
                                padx=(10,0),
                                pady=(10, 10)
                                )

sliders_box1b = customtkinter.CTkFrame(control,
                               width=210,
                               height=450,
                               corner_radius=10,
                            #    fg_color="#C4F5CC"
                                ).grid(row=0,
                                column=2,
                                rowspan=500,
                                columnspan=2,
                                sticky="nsew",
                                padx=(0,10),
                                pady=(10, 10)
                                )

label_base = customtkinter.CTkLabel(control,
                                    text="..Base..",font=customtkinter.CTkFont(size=20, weight="bold"),
                                    width=210,
                                    ).grid(row=0,
                                    column=1,
                                    columnspan=2,
                                    sticky="nsew",
                                    # padx=(0,0),
                                    pady=(20,2),
                                    )


label_izqBase = customtkinter.CTkLabel(control,
                                    text="<-- Izquierda",font=customtkinter.CTkFont(size=15, weight="bold"),
                                    # width=210,
                                    ).grid(row=1,
                                                        column=1,
                                                        sticky="w",
                                                        padx=(10,0),
                                                        pady=(2,2),
                                                        )

label_derBase = customtkinter.CTkLabel(control,
                                    text="Derecha -->",font=customtkinter.CTkFont(size=15, weight="bold"),
                                    # width=210,
                                    ).grid(row=1,column=2,sticky="e",
                                    padx=(0,0),
                                    pady=(2,2)
                                    )

slider_base = customtkinter.CTkSlider(control,
                                      from_=100,
                                      to=80,
                                    #   width=350,
                                      ).grid(row=3,
                                             column=1,
                                             padx=(0,0),
                                             pady=(20,20),
                                             columnspan=2,
                                             )




control.mainloop()