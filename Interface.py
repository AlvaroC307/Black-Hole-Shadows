import customtkinter as ctk
from PIL import Image, ImageTk
import csv

# ------------------------------------------ VENTANA DE EXPLICACION Y TUTORIAL ------------------------------------------
def Explanation():
    
    def Tutorial_Physics(): # Funcion para explicar conceptos físicos detrás de la simulación
        print("WORK IN PROGRESS")


    def Tutorial_Programm(): # Función para explicar como usar el programa y detalles del mismo
        print("WORK IN PROGRESS")


    def Tutorial_Opening(): # Función para abrir la ventana inicial de explicación y tutorial

        # Saludo al usuario 
        greeting_label = ctk.CTkLabel(Explanation_window, text="Explicación de la Simulación",
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        greeting_label.pack(pady=20)


        # Distintas opciones para explicaciones a las que acceder
        Tutorial_Options_label = ["Física detrás de la Simulación", "Detalles del Programa"]
        
        
        # Frame donde colocar las distintas opciones
        Tutorial_frame = ctk.CTkFrame(Explanation_window)
        Tutorial_frame.pack()


        # Botón para camenzar la explicacion de los conceptos físicos
        tutorial_physics_button = ctk.CTkButton(Tutorial_frame, text=Tutorial_Options_label[0], command=Tutorial_Physics)
        tutorial_physics_button.pack(pady=10)

        # Botón para camenzar la explicacion y detalles del programa
        tutorial_programm_button = ctk.CTkButton(Tutorial_frame, text=Tutorial_Options_label[1], command=Tutorial_Programm)
        tutorial_programm_button.pack(pady=10)

        # Frame para colocar las imagenes de los Agujeros Negros reales
        img_frame = ctk.CTkFrame(Explanation_window)
        img_frame.pack(pady=100)


        # Frame para M87*
        m87_frame = ctk.CTkFrame(img_frame)
        m87_frame.pack(side="left", padx=10)
        
        m87_img = ctk.CTkImage(Image.open("./Tutorial_Image/M87_star.jpg"), size=(200, 200)) # Imagen de M87*
        m87_label = ctk.CTkLabel(m87_frame, image=m87_img, text="")
        m87_label.pack()
    
        m87_caption = ctk.CTkLabel(m87_frame, text="Messier 87*", width=200) # Caption de M87*
        m87_caption.pack(pady=5)


        # Frame para SagA*
        sagA_frame = ctk.CTkFrame(img_frame)
        sagA_frame.pack(side="right", padx=10)

        sagA_img = ctk.CTkImage(Image.open("./Tutorial_Image/Sag_A_star.jpg"), size=(200, 200)) # Imagen de SagA*
        sagA_label = ctk.CTkLabel(sagA_frame, image=sagA_img, text="")
        sagA_label.pack()

        sagA_caption = ctk.CTkLabel(sagA_frame, text="Saggitarius A*", width=200) # Capition de SagA*
        sagA_caption.pack(pady=5)


    # Crear ventana secundaria en la que escribir la explicación
    Explanation_window = ctk.CTkToplevel(root)
    Explanation_window.title("Explicación")
    Explanation_window.geometry("800x600")

    Tutorial_Opening() # Activar ventana inicial de explicación y tutorial


# ------------------------------------------ FIN DE VENTANA DE EXPLICACION Y TUTORIAL ------------------------------------------



# ------------------------------------------ VENTANA DE INTRODUCCIÓN DE VARIABLES ------------------------------------------
def Introduce_variables():


    #--------------------------------------- SIMULACIÓN DE LA SOMBRA ---------------------------------------

    # Lista de preguntas a mostrar en cada paso
    Shadow_preguntas = ["Paso I: Masa del BH y Posicion del Observador", "Paso II: Datos para la Simulacion", "Paso III: Datos para Representar la Imagen y Sonido"]
    
    # Descripciones de los datos necesarios a introducir
    Shadow_Data_Description = [["M (Masa del agujero negro):", "t0 (Coordenada temporal del observador):", "r_0 (Coordenada radial del observador):",
                         "phi_0 (Coordenada angular acimutal del observador):", "theta_0 (Coordenada angular cenital del observador):"],
                        ["N_pix (Número de pixeles para crear una imagen cuadrada N_pix x N_pix)", "Factor_Screen (Zoom que se hace sobre la imagen)",
                         "r_limit (Coordenada Radial a partir de la que se considera que un fotón va a infinito)", "name (Nombre de la métrica: Kerr / Kerr_Newman)"],
                        ["Back_Im (Opción de Imagen Background o Colores: Image / Colours)", "image_name (Nombre del archivo imagen)", 
                         "sound (Nombre del archivo sonido al acabar el programa)", "axis (Opcion de Ejes o no al representar la imagen: Yes / No)"]
                         ]
    
    # Valores Genéricos que se recomiendan introducir
    Shadow_Placeholder_Text = [["1", "0", "8*M", "pi/2", "pi/2"],
                        ["100", "4", "10*M", "Kerr-Newman"],
                        ["Colours", "Colours.png", "Barra_Metal_Cayendo.mp3", "No"]]

    # Diccionario donde guardar los valores obtenidos (y ya está inicializado con los valores genéricos)
    Shadow_Saved_Data = {"M": "1", "t0": "0", "r0": "8*M", "phi0": "pi/2", "theta0": "pi/2",
                  "N_pix": "100", "Factor_Screen": "4", "r_limit": "10*M", "name": "Kerr-Newman",
                  "Back_Im": "Colours", "image_name": "Colours.png", "sound": "Barra_Metal_Cayendo", "axis": "No"}


    # Primer paso para introducir las variables de la sombra
    def Shadow_First_Page():

        # Limpiamos la ventana
        for widget in Input_window.winfo_children():
            widget.destroy()

        # Saludo al usuario y nombre del paso
        Introduction = ctk.CTkLabel(Input_window, text = Shadow_preguntas[0],
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)

        # Creamos los Entry para introducir los valores del primer paso
        Entries=[]
        for i in range(len(Shadow_Data_Description[0])): 
            ctk.CTkLabel(Input_window, text = Shadow_Data_Description[0][i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text = Shadow_Placeholder_Text[0][i]))
            Entries[i].pack(pady=5)

        
        # Botón para finalizar el paso y pasar al siguiente
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Shadow_Second_Page(Entries)).pack(pady=10)

    # Primer paso para introducir las variables de la sombra
    def Shadow_Second_Page(Entries:list):

        # Guardamos los valores del primer paso antes de limpiar la ventana
        values = []
        for i in range(len(Entries)):
            values.append(Entries[i].get())

        # Limpiamos la ventana
        for widget in Input_window.winfo_children():
            widget.destroy()
        
        # Saludo al usuario y nombre del paso
        Introduction = ctk.CTkLabel(Input_window, text = Shadow_preguntas[1],
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)

        # Creamos los Entry para introducir los valores del segundo paso
        Entries=[]
        for i in range(len(Shadow_Data_Description[1])): 
            ctk.CTkLabel(Input_window, text = Shadow_Data_Description[1][i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text = Shadow_Placeholder_Text[1][i]))
            Entries[i].pack(pady=5)


        # Botón para finalizar el paso y pasar al siguiente
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Shadow_Third_Page(Entries, values)).pack(pady=10)

    # Primer paso para introducir las variables de la sombra
    def Shadow_Third_Page(Entries:list, values:list):

        # Guardamos los valores del primer y segundo paso antes de limpiar la ventana
        for i in range(len(Entries)):
            values.append(Entries[i].get())

        # Limpiamos la ventana
        for widget in Input_window.winfo_children():
            widget.destroy()
        
        # Saludo al usuario y nombre del paso
        Introduction = ctk.CTkLabel(Input_window, text = Shadow_preguntas[2],
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)

        # Creamos los Entry para introducir los valores del tercer paso
        Entries=[]
        for i in range(len(Shadow_Data_Description[2])): 
            ctk.CTkLabel(Input_window, text = Shadow_Data_Description[2][i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text = Shadow_Placeholder_Text[2][i]))
            Entries[i].pack(pady=5)

        # Botón para finalizar la introducción de variables y guardar los datos en el archivo Input/Input.csv
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Shadow_Save_Data(Entries, values)).pack(pady=10)

    # Funcion para escribir los datos en el archivo Input/Input.csv
    def Shadow_Save_Data(Entries:list, values:list):

        # Guardamos los valores introducidos en una lista
        for i in range(len(Entries)):
            values.append(Entries[i].get())

        # Asignamos cada valor a su clave correspondiente en el dict Shadow_Saved_Data
        for key, value in zip(Shadow_Saved_Data.keys(), values):
            if value == "": # Si no se introduce ningun valor se escribe el placeholder genérico
                Shadow_Saved_Data[key] = Shadow_Saved_Data[key] 
            else:
                Shadow_Saved_Data[key] = value

        print(Shadow_Saved_Data) # Inprimimos los valores guardados para comprobar que son correctos

        # Escribimos los valores en el archivo
        with open("./Input/Input.csv", "w", newline="") as file_Input: 
            csv_Input = csv.writer(file_Input)

            for key, value in zip(Shadow_Saved_Data.keys(), Shadow_Saved_Data.values()):
                print(key, value)
                csv_Input.writerow([key, value])


    #--------------------------------------- FIN DE SIMULACIÓN DE LA SOMBRA ---------------------------------------

    #--------------------------------------- VALORES EXTRA PARA LAS MÉTRICAS ESPECIALES ---------------------------------------

    # Pregunta a mostrar
    Extra_Cte_preguntas = "Constantes Extra para la Simualcion"

    # Descripciones de los datos necesarios a introducir
    Extra_Cte_Data_Description = ["a (Parametro de Kerr (Rotación) del agujero negro):", "Q_e(Carga del agujero negro)"]

    # Valores Genéricos que se recomiendan introducir
    Extra_Cte_Placeholder_Text = ["0.9", "0"]

    Extra_Cte_Saved_Data = {} #------------IN PROGRESS---------

    def Number_Extra_Constants(): #------------IN PROGRESS--------- (Pedir al usuario cuantos valores extra necesita su métrica)
        return 0 

    def Extra_Constants_Page(): #------------IN PROGRESS---------

        # Clear the frame
        for widget in Input_window.winfo_children():
            widget.destroy()

        # Introduction of the Window
        Introduction = ctk.CTkLabel(Input_window, text = Extra_Cte_preguntas,
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)


        Entries=[]
        for i in range(len(Extra_Cte_Data_Description)): 
            ctk.CTkLabel(Input_window, text = Extra_Cte_Data_Description[i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text = Extra_Cte_Placeholder_Text[i]))
            Entries[i].pack(pady=5)

        
        # Botón para enviar los valores
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Extra_Constants_Save_Data(Entries)).pack(pady=10)

    def Extra_Constants_Save_Data(Entries:list): #------------IN PROGRESS---------
        return 0

    #--------------------------------------- FIN DE VALORES EXTRA PARA LAS MÉTRICAS ESPECIALES ---------------------------------------




    #--------------------------------------- GEODÉSICA ESPECÍFICA ---------------------------------------
    #--------------------------------------- FIN DE GEODÉSICA ESPEFÍFICA ---------------------------------------





    #--------------------------------------- PREGUNTAR AL USUARIO QUE ARCHIVO QUIERE MODIFICAR ---------------------------------------


    # Crear ventana secundaria para ingresar variables
    Input_window = ctk.CTkToplevel(root)
    Input_window.title("Variables del agujero negro")
    Input_window.geometry("600x500")

    # Saludo al usuario
    greeting_label = ctk.CTkLabel(Input_window, text="¿Que variables deseas modificar?",
                                font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                corner_radius=20)
    greeting_label.pack(pady=20)


    # Opciones de las distintos tipos de variables que se pueden introducir
    buttons_label = ["Basic Variables for Shadow Simulation", "Basic Variables for unique Particle Trayectory", "Extra Constants of the Black Hole"]
    
    
    # Frame donde colocar las distintas opciones
    Variable_Options = ctk.CTkFrame(Input_window)
    Variable_Options.pack()


    # Botón para cargar las variables básicas para la simulación de la sombra
    variable_Input_button = ctk.CTkButton(Variable_Options, text=buttons_label[0], command=Shadow_First_Page)
    variable_Input_button.pack(pady=10)

    # Botón para cargar las variables básicas para calcular la trayectoria de una única partícula
    variable_Input_Geodesic_button = ctk.CTkButton(Variable_Options, text=buttons_label[1], command=print("WORK IN PROGRESS"))
    variable_Input_Geodesic_button.pack(pady=10)

    # Botón para cargar las variables extra necesarias para distintas métricas
    variable_extra_cte_button = ctk.CTkButton(Variable_Options, text=buttons_label[2], command=print("WORK IN PROGRESS"))
    variable_extra_cte_button.pack(pady=10)

    #--------------------------------------- FIN DE PREGUNTAR AL USUARIO QUE ARCHIVO QUIERE MODIFICAR ---------------------------------------

# ------------------------------------------ VENTANA DE INTRODUCCIÓN DE VARIABLES ------------------------------------------



#-------------------------------------------------------- VENTANA PRINCIPAL ----------------------------------------------------

# Configurar CustomTkinter
ctk.set_appearance_mode("Dark")  # Opciones: "System" (según el SO), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Tema de colores: "blue", "dark-blue", "green"

# Crear ventana principal
root = ctk.CTk()
root.title("Simulación de Sombra de un Agujero Negro")
root.geometry("700x400")

# Etiqueta de saludo
greeting_label = ctk.CTkLabel(root, text="Bienvenido al Programa de Simulación de Agujeros Negros",
                               font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                               corner_radius=20)
greeting_label.pack(pady=20)


# Frame donde colocar las distintas opciones
Button_Frame = ctk.CTkFrame(root)
Button_Frame.pack()

# Botón para redirigir a la ventana expliación/tutorial
explanation_button = ctk.CTkButton(Button_Frame, text="Explicación", fg_color="#deffa0", hover_color="#ffece3", text_color="Black", font=("Arial", 15),
                                   corner_radius=20, command = Explanation)
explanation_button.pack(pady=25)


# Botón para redirigir a la ventana introducción de variables
save_variable_button = ctk.CTkButton(Button_Frame, text="Introducir Variables", command=Introduce_variables)
save_variable_button.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()

#-------------------------------------------------------- VENTANA PRINCIPAL ----------------------------------------------------