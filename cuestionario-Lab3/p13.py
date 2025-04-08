class ListaOrdenada:
    def __init__(self):
        self.lista = []
    
    def insertar(self, valor):
        self.lista.append(valor)
        self.lista.sort()  # Mantiene la invariante de orden
        
    def mostrar(self):
        print(self.lista)

lista = ListaOrdenada()
lista.insertar(5)
lista.insertar(2)
lista.insertar(8)
lista.mostrar()  # Salida: [2, 5, 8]
