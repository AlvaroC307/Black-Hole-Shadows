import customtkinter as ctk
from math import pi

# Configurar CustomTkinter
ctk.set_appearance_mode("Dark")  # Opciones: "System" (según el SO), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Tema de colores: "blue", "dark-blue", "green"

# Función para mostrar explicación
def show_explanation():
    explanation_text = (
        "Este programa simula numéricamente la sombra de un agujero negro utilizando Backwards Ray-Tracing\n"
        "Una vez activar el programa se piden los datos de una serie de variables necesarias para el cálculo.\n"
    )
    explanation_label.configure(text=explanation_text)

# Función para activar el programa
def activate_program():
    def submit_variables():
        # Obtener los valores ingresados por el usuario
        M = float(mass_entry.get())
        a = float(rotation_entry.get())
        r_0 = eval(r0_entry.get())
        theta_0 = eval(theta0_entry.get())
        # Mostrar los valores en consola o realizar cálculos con ellos
        print(f"M: {M}, a: {a}, r_0: {r_0}, theta_0: {theta_0}")
        result_label.configure(
            text=f"Valores recibidos:\nM={M}, a={a}, r_0={r_0}, theta_0={theta_0}"
        )
        variable_window.destroy()

    # Crear ventana secundaria para ingresar variables
    variable_window = ctk.CTkToplevel(root)
    variable_window.title("Variables del agujero negro")
    variable_window.geometry("400x600")

    # Entradas de datos
    ctk.CTkLabel(variable_window, text="M (Masa del agujero negro):").pack(pady=5)
    mass_entry = ctk.CTkEntry(variable_window)
    mass_entry.pack(pady=5)

    ctk.CTkLabel(variable_window, text="a (Rotación del agujero negro):").pack(pady=5)
    rotation_entry = ctk.CTkEntry(variable_window)
    rotation_entry.pack(pady=5)

    ctk.CTkLabel(variable_window, text="r_0 (Posición radial del observador):").pack(pady=5)
    r0_entry = ctk.CTkEntry(variable_window)
    r0_entry.pack(pady=5)

    ctk.CTkLabel(variable_window, text="theta_0 (Posición angular del observador):").pack(pady=5)
    theta0_entry = ctk.CTkEntry(variable_window)
    theta0_entry.pack(pady=5)

    # Botón para enviar los valores
    ctk.CTkButton(variable_window, text="Enviar", command=submit_variables).pack(pady=10)

# Crear ventana principal
root = ctk.CTk()
root.title("Simulación de Sombra de un Agujero Negro")
root.geometry("700x400")

# Etiqueta de saludo
greeting_label = ctk.CTkLabel(root, text="Bienvenido a la Simulación de un Agujero Negro", font=("Arial", 18))
greeting_label.pack(pady=20)

# Botón para mostrar explicación
explanation_button = ctk.CTkButton(root, text="Explicación", command=show_explanation)
explanation_button.pack(pady=10)

# Botón para activar programa
activate_button = ctk.CTkButton(root, text="Activar programa", command=activate_program)
activate_button.pack(pady=10)

# Etiqueta para mostrar explicación
explanation_label = ctk.CTkLabel(root, text="", wraplength=450, justify="left")
explanation_label.pack(pady=20)

# Etiqueta para mostrar resultados
result_label = ctk.CTkLabel(root, text="", wraplength=450, justify="left")
result_label.pack(pady=20)

# Ejecutar la interfaz gráfica
root.mainloop()
