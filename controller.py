from model import IMCModel
from view import IMCView

class IMCController:
    def __init__(self):
        """Inicializa el controlador con el modelo y la vista."""
        self.model = IMCModel()  # Instancia del modelo
        self.view = IMCView()  # Instancia de la vista
        self.view.vincular_controlador(self.calcular_imc)  # Vincula el controlador al botón en la vista

    def calcular_imc(self):
        """Controlador para manejar el evento del botón de cálculo de IMC."""
        try:
            peso, altura = self.view.obtener_datos()  # Obtiene los datos de la vista
            imc, estado = self.model.calcular_imc(peso, altura)  # Calcula el IMC utilizando el modelo
            self.view.mostrar_resultado(f"Tu IMC es: {imc:.2f}\nEstado: {estado}", color="green")  # Muestra el resultado en la vista
        except ValueError as e:
            self.view.mostrar_resultado(f"Error: {str(e)}", color="red")  # Muestra un mensaje de error si los datos no son válidos
        except Exception as e:
            self.view.mostrar_resultado("Ocurrió un error inesperado.", color="red")  # Muestra un mensaje de error para otros casos

    def run(self):
        """Ejecuta la aplicación y mantiene la interfaz en funcionamiento."""
        self.view.mainloop()  # Inicia el bucle principal de la vista
