# Importamos la libreria TKinter
from tkinter import *

# Usaremos POO
class Foro:
    def __init__(self, window):
        
        self.wind = window
        self.wind.title("Foro de Algoritmia de Programación del Software")
        self.wind.geometry("500x500")

        # Empezamos a construir la interfaz
        # Ejecutamos la funcion donde nos muuestra el planteamiento del problema
        self.problem()
        # Creamos boton para dar solucion al problema
        self.button1 = Button(self.wind, text = "Solución", command = self.solution).pack(pady = 10)

    def solution(self):
        self.wind_solution = Toplevel()
        self.wind_solution.title("Solución")
        self.wind_solution.geometry("500x500")

        Label(self.wind_solution, text = "SOLUCIÓN", font = "Arial").pack()

    def problem(self):
        self.txt = """Estimado estudiante.

        Responda las siguiente pregunta:

        Debido a la pandemia una empresa de transporte quiere resolver el
        inconveniente que, dado cuatro localidades a recorrer, debe hallar la ruta
        que le permita llegar todas las localidades una exclusiva vez, dando por
        seguro que la distancia que recorra sea mínima. El transporte no recorre la
        misma ruta todos los días por lo que la distancias entres los lugares varia.

        Por ejemplo, se tiene este conjunto de puntos a recorrer con sus
        respectivas distancias.

        Para Ud. ¿Cuál sería el algoritmo solución y código fuente en Python si los
        valores de las distancias varían?"""
        self.img = PhotoImage(file = "img.png")

        Label(self.wind, text = self.txt).pack()
        Label(self.wind, image = self.img).pack(pady = 10)

# Aqui empieza a correr el codigo
if __name__ == '__main__':
    window = Tk()
    app = Foro(window)
    window.mainloop()