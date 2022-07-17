from razon.procesar import Procesar

if __name__=="__main__":
    archivo=input('Introduzca el archivo a mostrar con su extension: ')
    if archivo[-5:].lower() != ".json":
        print("Debes ingresar un archivo de tipo json")
    else:
        try:
         Procesar(archivo.lower())
         print('El archivo HTML se generó exitosamente')
        except FileNotFoundError:
            print ('El archivo no se pudo encontrar')

