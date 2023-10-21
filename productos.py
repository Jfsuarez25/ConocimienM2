"""

Usando pycharm , cree una Clase que permita registrar un producto. Contiene los siguientes atributos 
id, nombre, descripcion, costo, cantidad , precio_de_venta. Cree un metodo que permita registrar el 
producto y mediante un callback se le debe asignar el precio de venta de acuerdo a la siguiente formula: 
pv = costo/ (1- margen_de_venta), los productos al ser creados se guardaran en un diccionario. Cree un 
tercer metodo que permita imprimir el listado de productos. En la respuesta pegue el enlace del repositorio 
de Git Hub donde subió el ejercicio.

"""

import os

# Función para limpiar consola

def limpiar_consola():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

class Products:
    
    def __init__(self):
        
        self.productos = {}
    
    def RegisterProducts(self):
        limpiar_consola()
        
        id = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        costo = float(input("Ingrese el costo del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        margen_de_venta = 0.2  # Margen de venta predeterminado
        
        precio_venta = round(costo / (1 - margen_de_venta), 2)  # Se agrega un "2" para mostrar los decimales
        
        producto = {
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'precio_venta': precio_venta
        }
        
        self.productos[id] = producto
        
        print("Producto registrado exitosamente!")
        limpiar_consola()
        

    def PrintProducts(self):
        
        print("\n" + "Listado de productos:")
        
        for id, producto in self.productos.items():
            
            print("\n" + f" Identificación: {id} \n Nombre: {producto['nombre']} \n Descripción: {producto['descripcion']} \n Costo: {producto['costo']} \n Cantidad: {producto['cantidad']} \n Precio de venta: {producto['precio_venta']} \n")
            

registro = Products()

# Menú

while True:
    print("\n" + "-----------------------------")
    print("\n" + "----- Menú -----")
    print("1. Registrar productos")
    print("2. Ver productos registrados")
    print("3. Salir")
    print("\n" + "-----------------------------")
    
    
    opcion = int(input("\n" + "Ingrese una opción: "))
    
    if opcion == 1:
        registro.RegisterProducts()
        
    elif opcion == 2:
        
        registro.PrintProducts()
        
    elif opcion == 3:
        
        limpiar_consola()
        print("\n" + "Saliendo del programa... \n")
        break
    
    else:
        
        limpiar_consola()
        print("Opción inválida. Por favor, intente nuevamente.")