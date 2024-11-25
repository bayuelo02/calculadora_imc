import customtkinter as ctk

class IMCView(ctk.CTk):
    def __init__(self):
        """Inicializa la ventana de la calculadora de IMC."""
        super().__init__()
        self.title("Calculadora de IMC")
        self.geometry("400x400")
        self.resizable(False, False)
        self._configurar_estilo()
        self._crear_widgets()

    def _configurar_estilo(self):
        """Configura el estilo de la interfaz gráfica."""
        self.configure(bg="black")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def _crear_widgets(self):
        """Crea los elementos de la interfaz gráfica."""
        self.label_titulo = ctk.CTkLabel(self, text="Calculadora de IMC", font=("Arial", 20), text_color="white")
        self.label_titulo.pack(pady=20)
        
        self.frame = ctk.CTkFrame(self, fg_color="black")
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.label_peso = ctk.CTkLabel(self.frame, text="Peso (kg):", text_color="white")
        self.label_peso.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_peso = ctk.CTkEntry(self.frame, placeholder_text="Ej. 70", fg_color="gray", text_color="white")
        self.entry_peso.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_altura = ctk.CTkLabel(self.frame, text="Altura (m):", text_color="white")
        self.label_altura.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_altura = ctk.CTkEntry(self.frame, placeholder_text="Ej. 1.75", fg_color="gray", text_color="white")
        self.entry_altura.grid(row=1, column=1, padx=10, pady=10)
        
        self.boton_calcular = ctk.CTkButton(self, text="Calcular IMC", fg_color="darkblue", text_color="white")
        self.boton_calcular.pack(pady=20)
        
        self.label_resultado = ctk.CTkLabel(self, text="", font=("Arial", 16), text_color="white")
        self.label_resultado.pack(pady=10)

    def vincular_controlador(self, controlador):
        """Vincula el controlador al botón de cálculo de IMC."""
        self.boton_calcular.configure(command=controlador)

    def obtener_datos(self):
        """Obtiene el peso y la altura ingresados."""
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            return peso, altura
        except ValueError:
            raise ValueError("Por favor, introduce valores numéricos válidos.")

    def mostrar_resultado(self, mensaje, color="green"):
        """Muestra el resultado en la interfaz."""
        self.label_resultado.configure(text=mensaje, text_color=color)
