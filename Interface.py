import customtkinter as ctk
import csv

# Función para mostrar explicación
def show_explanation():
    explanation_text = (
        "...Funcionamiento en Desarrollo..."
    )
    explanation_label.configure(text=explanation_text)

# Función para activar el programa
def Introduce_variables():

    # Lista de preguntas a mostrar en la ventana auxiliar
    preguntas = ["Paso I: Masa del BH y Posicion del Observador", "Paso II: Datos para la Simulacion", "Paso III: Datos para Representar la Imagen y Sonido"]
    
    Data_Description = [["M (Masa del agujero negro):", "t0 (Coordenada temporal del observador):", "r_0 (Coordenada radial del observador):",
                         "phi_0 (Coordenada angular acimutal del observador):", "theta_0 (Coordenada angular cenital del observador):"],
                        ["N_pix (Número de pixeles para crear una imagen cuadrada N_pix x N_pix)", "Factor_Screen (Zoom que se hace sobre la imagen)",
                         "r_limit (Coordenada Radial a partir de la que se considera que un fotón va a infinito)", "name (Nombre de la métrica: Kerr / Kerr_Newman)"],
                        ["Back_Im (Opción de Imagen Background o Colores: Image / Colours)", "image_name (Nombre del archivo imagen)", 
                         "sound (Nombre del archivo sonido al acabar el programa)", "axis (Opcion de Ejes o no al representar la imagen: Yes / No)"]
                         ]
    
    Placeholder_Text = [["1", "0", "8*M", "pi/2", "pi/2"],
                        ["100", "4", "10*M", "Kerr-Newman"],
                        ["Colours", "Colours.png", "Barra_Metal_Cayendo.mp3", "No"]]



    Saved_Data = {"M": "1", "t0": "0", "r0": "8*M", "phi0": "pi/2", "theta0": "pi/2",
                  "N_pix": "100", "Factor_Screen": "4", "r_limit": "10*M", "name": "Kerr-Newman",
                  "Back_Im": "Colours", "image_name": "Colours.png", "sound": "Barra_Metal_Cayendo", "axis": "No"}
    

    # Fuction with the first information needed
    def First_Page():

        # Clear the frame
        for widget in Input_window.winfo_children():
            widget.destroy()

        # Introduction of the Window
        Introduction = ctk.CTkLabel(Input_window, text=preguntas[0],
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)


        Entries=[]
        for i in range(len(Data_Description[0])): 
            ctk.CTkLabel(Input_window, text=Data_Description[0][i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text=Placeholder_Text[0][i]))
            Entries[i].pack(pady=5)

        
        # Botón para enviar los valores
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Second_Page(Entries)).pack(pady=10)

    # Function to change the window content
    def Second_Page(Entries:list):

        # Save the Data before Claring the frame and Widgets
        values = []
        for i in range(len(Entries)):
            values.append(Entries[i].get())

        # Clear the frame
        for widget in Input_window.winfo_children():
            widget.destroy()
        
        # Introduction of the Second Window
        Introduction = ctk.CTkLabel(Input_window, text=preguntas[1],
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)

        Entries=[]
        for i in range(len(Data_Description[1])): 
            ctk.CTkLabel(Input_window, text=Data_Description[1][i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text=Placeholder_Text[1][i]))
            Entries[i].pack(pady=5)

        # Botón para enviar los valores
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Third_Page(Entries, values)).pack(pady=10)

    # Function to change the window content
    def Third_Page(Entries:list, values:list):

        # Save the Data before Claring the frame and Widgets
        for i in range(len(Entries)):
            values.append(Entries[i].get())

        # Clear the frame
        for widget in Input_window.winfo_children():
            widget.destroy()
        
        # Introduction of the Second Window
        Introduction = ctk.CTkLabel(Input_window, text=preguntas[2],
                                    font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                    corner_radius=20)
        Introduction.pack(pady=20)

        Entries=[]
        for i in range(len(Data_Description[2])): 
            ctk.CTkLabel(Input_window, text=Data_Description[2][i]).pack(pady=5)
            Entries.append(ctk.CTkEntry(Input_window, placeholder_text=Placeholder_Text[2][i]))
            Entries[i].pack(pady=5)

        # Botón para enviar los valores
        ctk.CTkButton(Input_window, text="Enviar", command = lambda: Save_Data(Entries, values)).pack(pady=10)


    def Save_Data(Entries:list, values:list):

        for i in range(len(Entries)):
            values.append(Entries[i].get())

        # Assign values to dictionary keys
        for key, value in zip(Saved_Data.keys(), values):
            if value == "":
                Saved_Data[key] = Saved_Data[key] # If Nothing is introduced, write the placeholder value
            else:
                Saved_Data[key] = value

        print(Saved_Data)

        # Escribimos los datos en el fichero Input.csv para su uso en la simulacion
        with open("./Input/Input.csv", "w", newline="") as file_Input: 
            csv_Input = csv.writer(file_Input)

            for key, value in zip(Saved_Data.keys(), Saved_Data.values()):
                print(key, value)
                csv_Input.writerow([key, value])



    # Crear ventana secundaria para ingresar variables
    Input_window = ctk.CTkToplevel(root)
    Input_window.title("Variables del agujero negro")
    Input_window.geometry("600x500")

    # Etiqueta de saludo
    greeting_label = ctk.CTkLabel(Input_window, text="¿Que variables deseas modificar?",
                                font=("Arial", 21), fg_color="#a8fff2", text_color = "#240070",
                                corner_radius=20)
    greeting_label.pack(pady=20)


    buttons_label = ["Basic Variables for Shadow Simulation", "Basic Variables for unique Particle Trayectory", "Extra Constants of the Black Hole"]
    
    
    # Frame donde colocar las distintas opciones
    Variable_Options = ctk.CTkFrame(Input_window)
    Variable_Options.pack()


    # Botón para cargar las primeras variables
    activate_button = ctk.CTkButton(Variable_Options, text=buttons_label[0], command=First_Page)
    activate_button.pack(pady=10)

    # Botón para cargar las segundas variables
    activate_button = ctk.CTkButton(Variable_Options, text=buttons_label[1], command=print("WORK IN PROGRESS"))
    activate_button.pack(pady=10)

    # Botón para cargar las terceras variables
    activate_button = ctk.CTkButton(Variable_Options, text=buttons_label[2], command=print("WORK IN PROGRESS"))
    activate_button.pack(pady=10)

    






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

# Botón para mostrar explicación
explanation_button = ctk.CTkButton(Button_Frame, text="Explicación", fg_color="#deffa0", hover_color="#ffece3", text_color="Black", font=("Arial", 15),
                                   corner_radius=20, command = show_explanation)
explanation_button.pack(pady=25)

# Etiqueta para mostrar explicación
explanation_label = ctk.CTkLabel(root, text="", wraplength=450, justify="left")
explanation_label.pack(pady=20)


# Botón para activar programa
activate_button = ctk.CTkButton(Button_Frame, text="Introducir Variables", command=Introduce_variables)
activate_button.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()