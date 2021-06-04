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

        # Construcción de la interfaz
        Label(self.wind_solution, text = "SOLUCIÓN", font = "Arial").grid(row = 0, column = 2)
        Label(self.wind_solution, text = "INGRESA LA DISTANCIA ENTRE :").grid(row = 1, column = 1)
        
        Label(self.wind_solution, text = "F -> B").grid(row = 2, column = 1, pady = 5)
        self.dist_FB = Entry(self.wind_solution)
        self.dist_FB.grid(row = 2, column = 2)
        self.dist_FB.focus()
        Label(self.wind_solution, text = "F -> J").grid(row = 3, column = 1, pady = 5)
        self.dist_FJ = Entry(self.wind_solution)
        self.dist_FJ.grid(row = 3, column = 2)
        Label(self.wind_solution, text = "F -> A").grid(row = 4, column = 1, pady = 5)
        self.dist_FA = Entry(self.wind_solution)
        self.dist_FA.grid(row = 4, column = 2)
        Label(self.wind_solution, text = "B -> A").grid(row = 5, column = 1, pady = 5)
        self.dist_BA = Entry(self.wind_solution)
        self.dist_BA.grid(row = 5, column = 2)
        Label(self.wind_solution, text = "B -> J").grid(row = 6, column = 1, pady = 5)
        self.dist_BJ = Entry(self.wind_solution)
        self.dist_BJ.grid(row = 6, column = 2)
        Label(self.wind_solution, text = "A -> J").grid(row = 7, column = 1, pady = 5)
        self.dist_AJ = Entry(self.wind_solution)
        self.dist_AJ.grid(row = 7, column = 2)

        Label(self.wind_solution, text = "Indica el punto de partida :").grid(row = 8, column = 2)
        self.button_F = Button(self.wind_solution, text = "F", bg = "blue", fg = "white", font = "Arial", command = self.run_button_F)
        self.button_F.grid(row = 9, column = 1, pady = 5)
        self.button_B = Button(self.wind_solution, text = "B", bg = "red", fg = "white", font = "Arial", command = self.run_button_B)
        self.button_B.grid(row = 9, column = 2, pady = 5)
        self.button_J = Button(self.wind_solution, text = "J", bg = "red", fg = "white", font = "Arial", command = self.run_button_J)
        self.button_J.grid(row = 10, column = 1, pady = 5)
        self.button_A = Button(self.wind_solution, text = "A", bg = "blue", fg = "white", font = "Arial", command = self.run_button_A)
        self.button_A.grid(row = 10, column = 2, pady = 5)

        self.result = Label(self.wind_solution, text = "", font = "Arial", fg = "red")
        self.result.grid(row = 11, columnspan = 4, sticky = W)
        self.distance = Label(self.wind_solution, text = "", font = "Arial", fg = "blue")
        self.distance.grid(row = 12, columnspan = 4, sticky = W)

        Button(self.wind_solution, text = "Limpiar campos", command = self.delete).grid(row =13, column = 2)
    
    # Enunciado del problema
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

    # Funcion al presionar el boton F
    def run_button_F(self):
        self.sum = 0
        if self.button_F:
            if self.dist_FB.get() <= self.dist_FJ.get() and self.dist_FB.get() <= self.dist_FA.get() and self.dist_BA.get() <= self.dist_BJ.get():
                self.sum = int(self.dist_FB.get()) + int(self.dist_BA.get()) + int(self.dist_AJ.get()) + int(self.dist_FJ.get())
                self.result["text"] = "Ruta a seguir: F -> B -> A -> J -> F"
                #print("\nRuta a seguir: F -> B -> A -> J -> F")
        
            elif self.dist_FA.get() <= self.dist_FJ.get() and self.dist_FA.get() <= self.dist_FB.get() and self.dist_BA.get() <= self.dist_AJ.get():
                self.sum = int(self.dist_FA.get()) + int(self.dist_BA.get()) + int(self.dist_BJ.get()) + int(self.dist_FJ.get())
                self.result["text"] = "Ruta a seguir: F -> A -> B -> J -> F"
                #print("\nRuta a seguir: F -> A -> B -> J -> F")
        
            elif self.dist_FJ.get() <= self.dist_FB.get() and self.dist_FJ.get() <= self.dist_FA.get() and self.dist_BJ.get() <= self.dist_AJ.get():
                self.sum = int(self.dist_FJ.get()) + int(self.dist_BJ.get()) + int(self.dist_BA.get()) + int(self.dist_FA.get())
                self.result["text"] = "Ruta a seguir: F -> J -> B -> A -> F"
                #print("\nRuta a seguir: F -> J -> B -> A -> F")
        
            elif self.dist_FJ.get() <= self.dist_FB.get() and self.dist_FJ.get() <= self.dist_FA.get() and self.dist_AJ.get() <= self.dist_BJ.get():
                self.sum = int(self.dist_FJ.get()) + int(self.dist_AJ.get()) + int(self.dist_BA.get()) + int(self.dist_FB.get())
                self.result["text"] = "Ruta a seguir: F -> J -> A -> B -> F"
                #print("\nRuta a seguir: F -> J -> A -> B -> F")
        
            elif self.dist_FB.get() <= self.dist_FJ.get() and self.dist_FB.get() <= self.dist_FA.get() and self.dist_BJ.get() <= self.dist_BA.get():
                self.sum = int(self.dist_FB.get()) + int(self.dist_BJ.get()) + int(self.dist_AJ.get()) + int(self.dist_FA.get())
                self.result["text"] = "Ruta a seguir: F -> B -> J -> A -> F"
                #print("\nRuta a seguir: F -> B -> J -> A -> F")
        
            elif self.dist_FA.get() <= self.dist_FJ.get() and self.dist_FA.get() <= self.dist_FB.get() and self.dist_AJ.get() <= self.dist_BA.get():
                self.sum = int(self.dist_FA.get()) + int(self.dist_AJ.get()) + int(self.dist_BJ.get()) + int(self.dist_FB.get())
                self.result["text"] = "Ruta a seguir: F -> A -> J -> B -> F"
                #print("\nRuta a seguir: F -> A -> J -> B -> F")
        self.distance["text"] = f"Ruta optima: {self.sum}km."

    # Función al precionar el boton B
    def run_button_B(self):
        self.sum = 0
        if self.button_B:
            if self.dist_FB.get() <= self.dist_BA.get() and self.dist_FB.get() <= self.dist_BJ.get() and self.dist_FJ.get() <= self.dist_FA.get():
                self.sum = int(self.dist_FB.get()) + int(self.dist_FJ.get()) + int(self.dist_AJ.get()) + int(self.dist_BA.get())
                self.result["text"] = "Ruta a seguir: B -> F -> J -> A -> B"
                #print("\nRuta a seguir: B -> F -> J -> A -> B")
        
            elif self.dist_BJ.get() <= self.dist_BA.get() and self.dist_BJ.get() <= self.dist_FB.get() and self.dist_FJ.get() <= self.dist_AJ.get():
                self.sum = int(self.dist_BJ.get()) + int(self.dist_FJ.get()) + int(self.dist_FA.get()) + int(self.dist_BA.get())
                self.result["text"] = "Ruta a seguir: B -> J -> F -> A -> B"
                #print("\nRuta a seguir: B -> J -> F -> A -> B")
        
            elif self.dist_BA.get() <= self.dist_FB.get() and self.dist_BA.get() <= self.dist_BJ.get() and self.dist_AJ.get() <= self.dist_FA.get():
                self.sum = int(self.dist_BA.get()) + int(self.dist_AJ.get()) + int(self.dist_FJ.get()) + int(self.dist_FB.get())
                self.result["text"] = "Ruta a seguir: B -> A -> J -> F -> B"
                #print("\nRuta a seguir: B -> A -> J -> F -> B")
        
            elif self.dist_BA.get() <= self.dist_FB.get() and self.dist_BA.get() <= self.dist_BJ.get() and self.dist_FA.get() <= self.dist_AJ.get():
                self.sum = int(self.dist_BA.get()) + int(self.dist_FA.get()) + int(self.dist_FJ.get()) + int(self.dist_BJ.get())
                self.result["text"] = "Ruta a seguir: B -> A -> F -> J -> B"
                #print("\nRuta a seguir: B -> A -> F -> J -> B")
        
            elif self.dist_BJ.get() <= self.dist_BA.get() and self.dist_BJ.get() <= self.dist_FB.get() and self.dist_AJ.get() <= self.dist_FJ.get():
                self.sum = int(self.dist_BJ.get()) + int(self.dist_AJ.get()) + int(self.dist_FA.get()) + int(self.dist_FB.get())
                self.result["text"] = "Ruta a seguir: B -> J -> A -> F -> B"
                #print("\nRuta a seguir: B -> J -> A -> F -> B")
        
            elif self.dist_FB.get() <= self.dist_BA.get() and self.dist_FB.get() <= self.dist_BJ.get() and self.dist_FA.get() <= self.dist_FJ.get():
                self.sum = int(self.dist_FB.get()) + int(self.dist_FA.get()) + int(self.dist_AJ.get()) + int(self.dist_BJ.get())
                self.result["text"] = "Ruta a seguir: B -> F -> A -> J -> B"
                #print("\nRuta a seguir: B -> F -> A -> J -> B")
        self.distance["text"] = f"Ruta optima: {self.sum}km."
    
    # Función al presionar el boton J
    def run_button_J(self):
        self.sum = 0        
        if self.button_J:
            if self.dist_BJ.get() <= self.dist_FJ.get() and self.dist_BJ.get() <= self.dist_AJ.get() and self.dist_BA.get() <= self.dist_FB.get():
                self.sum = int(self.dist_BJ.get()) + int(self.dist_BA.get()) + int(self.dist_FA.get()) + int(self.dist_FJ.get())
                self.result["text"] = "Ruta a seguir: J -> B -> A -> F -> J"
                #print("\nRuta a seguir: J -> B -> A -> F -> J")
        
            elif self.dist_AJ.get() <= self.dist_FJ.get() and self.dist_AJ.get() <= self.dist_BJ.get() and self.dist_BA.get() <= self.dist_FA.get():
                self.sum = int(self.dist_AJ.get()) + int(self.dist_BA.get()) + int(self.dist_FB.get()) + int(self.dist_FJ.get())
                self.result["text"] = "Ruta a seguir: J -> A -> B -> F -> J"
                #print("\nRuta a seguir: J -> A -> B -> F -> J")
        
            elif self.dist_FJ.get() <= self.dist_BJ.get() and self.dist_FJ.get() <= self.dist_AJ.get() and self.dist_FB.get() <= self.dist_FA.get():
                self.sum = int(self.dist_FJ.get()) + int(self.dist_FB.get()) + int(self.dist_BA.get()) + int(self.dist_AJ.get())
                self.result["text"] = "Ruta a seguir: J -> F -> B -> A -> J"
                #print("\nRuta a seguir: J -> F -> B -> A -> J")
        
            elif self.dist_FJ.get() <= self.dist_BJ.get() and self.dist_FJ.get() <= self.dist_AJ.get() and self.dist_FA.get() <= self.dist_FB.get():
                self.sum = int(self.dist_FJ.get()) + int(self.dist_FA.get()) + int(self.dist_BA.get()) + int(self.dist_BJ.get())
                self.result["text"] = "Ruta a seguir: J -> F -> A -> B -> J"
                #print("\nRuta a seguir: J -> F -> A -> B -> J")
        
            elif self.dist_BJ.get() <= self.dist_FJ.get() and self.dist_BJ.get() <= self.dist_AJ.get() and self.dist_FB.get() <= self.dist_BA.get():
                self.sum = int(self.dist_BJ.get()) + int(self.dist_FB.get()) + int(self.dist_FA.get()) + int(self.dist_AJ.get())
                self.result["text"] = "Ruta a seguir: J -> B -> F -> A -> J"
                #print("\nRuta a seguir: J -> B -> F -> A -> J")
        
            elif self.dist_AJ.get() <= self.dist_FJ.get() and self.dist_AJ.get() <= self.dist_BJ.get() and self.dist_FA.get() <= self.dist_BA.get():
                self.sum = int(self.dist_AJ.get()) + int(self.dist_FA.get()) + int(self.dist_FB.get()) + int(self.dist_BJ.get())
                self.result["text"] = "Ruta a seguir: J -> A -> F -> B -> J"
                #print("\nRuta a seguir: J -> A -> F -> B -> J")
        self.distance["text"] = f"Ruta optima: {self.sum}km."
        
    # Función al precionar el boton A
    def run_button_A(self):
        self.sum = 0        
        if self.button_A:
            if self.dist_FA.get() <= self.dist_BA.get() and self.dist_FA.get() <= self.dist_AJ.get() and self.dist_FJ.get() <= self.dist_FB.get():
                self.sum = int(self.dist_FA.get()) + int(self.dist_FJ.get()) + int(self.dist_BJ.get()) + int(self.dist_BA.get())
                self.result["text"] = "Ruta a seguir: A -> F -> J -> B -> A"
                #print("\nRuta a seguir: A -> F -> J -> B -> A")
        
            elif self.dist_AJ.get() <= self.dist_BA.get() and self.dist_AJ.get() <= self.dist_FA.get() and self.dist_FJ.get() <= self.dist_BJ.get():
                self.sum = int(self.dist_AJ.get()) + int(self.dist_FJ.get()) + int(self.dist_FB.get()) + int(self.dist_BA.get())
                self.result["text"] = "Ruta a seguir: A -> J -> F -> B -> A"
                #print("\nRuta a seguir: A -> J -> F -> B -> A")
        
            elif self.dist_BA.get() <= self.dist_FA.get() and self.dist_BA.get() <= self.dist_AJ.get() and self.dist_FB.get() <= self.dist_BJ.get():
                self.sum = int(self.dist_BA.get()) + int(self.dist_FB.get()) + int(self.dist_FJ.get()) + int(self.dist_AJ.get())
                self.result["text"] = "Ruta a seguir: A -> B -> F -> J -> A"
                #print("\nRuta a seguir: A -> B -> F -> J -> A")
        
            elif self.dist_BA.get() <= self.dist_FA.get() and self.dist_BA.get() <= self.dist_AJ.get() and self.dist_BJ.get() <= self.dist_FB.get():
                self.sum = int(self.dist_BA.get()) + int(self.dist_BJ.get()) + int(self.dist_FJ.get()) + int(self.dist_FA.get())
                self.result["text"] = "Ruta a seguir: A -> B -> J -> F -> A"
                #print("\nRuta a seguir: A -> B -> J -> F -> A")
        
            elif self.dist_FA.get() <= self.dist_BA.get() and self.dist_FA.get() <= self.dist_AJ.get() and self.dist_FB.get() <= self.dist_FJ.get():
                self.sum = int(self.dist_FA.get()) + int(self.dist_FB.get()) + int(self.dist_BJ.get()) + int(self.dist_AJ.get())
                self.result["text"] = "Ruta a seguir: A -> F -> B -> J -> A"
                #print("\nRuta a seguir: A -> F -> B -> J -> A")
        
            elif self.dist_AJ.get() <= self.dist_BA.get() and self.dist_AJ.get() <= self.dist_FA.get() and self.dist_BJ.get() <= self.dist_FJ.get():
                self.sum = int(self.dist_AJ.get()) + int(self.dist_BJ.get()) + int(self.dist_FB.get()) + int(self.dist_FA.get())
                self.result["text"] = "Ruta a seguir: A -> J -> B -> F -> A"
                #print("\nRuta a seguir: A -> J -> B -> F -> A")
        self.distance["text"] = f"Ruta optima: {self.sum}km."

    def delete(self):
        self.dist_FB.delete(0, END)
        self.dist_FJ.delete(0, END)
        self.dist_FA.delete(0, END)
        self.dist_BA.delete(0, END)
        self.dist_BJ.delete(0, END)
        self.dist_AJ.delete(0, END)
# Aqui empieza a correr el codigo
if __name__ == '__main__':
    window = Tk()
    app = Foro(window)
    window.mainloop()