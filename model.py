class IMCModel:
    @staticmethod
    def calcular_imc(peso, altura):
        """Calcula el IMC dado un peso y altura."""
        if peso <= 0 or altura <= 0:
            raise ValueError("Peso y altura deben ser mayores que cero.")
        
        imc = peso / (altura ** 2)
        if imc < 18.5:
            estado = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            estado = "Peso normal"
        elif 25 <= imc < 29.9:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        return round(imc, 2), estado
