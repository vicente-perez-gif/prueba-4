productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],                       
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], 
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], 
            'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'], 
            'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],                      
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], 
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], 
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}
stock = {'2175HD': [327990,4], 
        'JjfFHD': [424990,1],               
        'fgdxFHD': [664990,21],
        '123FHD': [290890,32], 
        '342FHD': [444990,7], 
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0], 
} 

def buscar_por_marca(modelo):
    False
    for modelo in productos.values():
        modelo.append == productos.items
        total = modelo[0]
        print(f"Queda en stock" , total)
        

def buscar_por_precio():
    for minimo in stock.values():
        minimo == productos.keys()
        total = minimo[0]
        print("Queda en stock", total )
def eliminar_producto(modelo):
    False
    for modelo in productos.values():
        if modelo == productos:
            modelo.pop == productos.keys()
            print("El producto se a elimanado con exito ")
            return

opcion = 0
while opcion != 4:
    print("Bienvenido")        
    print("1.- Mostrar stock")
    print("2.- Buscar por precio")        
    print("3.- eliminar producto")        
    print("4.- salir")
    opcion = int(input("Que opcion quiere utilizar  "))
    match opcion:
        case 1:
            modelo = input("Ingrese la marca que desea buscar   ")
            buscar_por_marca(modelo)
        case 2:
            minimo = int(input("Ingrese monto minimo "))
            maximo = int(input("Ingrese monto maximo "))
            buscar_por_precio
        case 3:
            modelo = input("ingrese el modelo que quiere eliminar   ")
            eliminar_producto(modelo)
        case 4:
            print("Programa Finalizado")
            break
        case _:
            print("Favor de ingresar un numero valido")      
