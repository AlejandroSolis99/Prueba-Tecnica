import requests

#clase principal que contiene todos metodos
class main():

    def __init__(self, url):
        self.url = url
        self.llamado()

    # metodo que realiza la peticion HTTP mediante el paquete request
    def llamado(self):
        datos = []
        GetData = requests.get(self.url)
        data = GetData.json()
        for f in data:
            datos.append(f)

        self.Publicaciones(datos)
        self.Titulos(datos)

    # metodo que realiza el calculo de publicaciones realizadas por cada uno de los usuarios
    def Publicaciones(self, datos):
        usuarios =[] #creacion de una lista vacia donde se almacenara los userId
        PubUsuario ={} #creacion de un diccionario vacio donde se almacenara el resultado del calculo de los userId

        for elem in datos:
            usuarios.append(elem['userId'])

        for i in range(1,11):
            PubUsuario[i] = usuarios.count(i)

        print("Publicaciones realizadas por los usuarios:")
        for d in PubUsuario.items():
            print(d)

    # metodo que identifica y almacena los 3 primeros titulos mas largos
    def Titulos(self, datos):

        PubTitulos = [] #creacion de una lista vacia donde se almacenara el resultado de la busqueda de los titulos
        Titulos1 = [] #creacion de un diccionario vacio donde se almacenara la primera busqueda
        Titulos2 = [] #creacion de un diccionario vacio donde se almacenara la segunda busqueda
        Titulos3 =[] #creacion de un diccionario vacio donde se almacenara la tercera busqueda
        for i in range(1,3):
            if len(PubTitulos) == 0: # primera busqueda tomando como valor de referencia el primer titulo
                dict = datos[0]
                Id = dict['id']
                Titulo = dict['title']
                cuenta = len(Titulo.split())
                for c in datos:
                    Id2 = c['id']
                    Titulo2 = c['title']
                    cuenta2 = len(Titulo2.split())
                    if cuenta > cuenta2:
                        id = Id
                        Mtitulo = Titulo
                        cuenta = cuenta
                    elif cuenta < cuenta2:
                        id = Id2
                        Mtitulo = Titulo2
                        cuenta = cuenta2
                    elif cuenta == cuenta2:
                        id = Id
                        Mtitulo = Titulo
                        cuenta = cuenta

                Titulos1.append(id)
                Titulos1.append(Mtitulo)
                PubTitulos.append(Titulos1)

            elif len(PubTitulos) != 0: #segunda y tercera busqueda tomando como referencia el primer titulo encontrado
                dict = datos[0]
                Titulo = dict['title']
                cuenta = len(Titulo.split())
                for c in datos:
                    Id2 = c['id']
                    Titulo2 = c['title']
                    cuenta2 = len(Titulo2.split())
                    if cuenta == cuenta2: # comparacion del numero de palabras del primer titulo con el resto de publicaciones
                        Title = PubTitulos[0]
                        if Title[1] != Titulo2: # comparacion primer titulo con el titulo con mismo numero de palabras
                            if len(PubTitulos) == 1:
                                Titulos2.append(Id2)
                                Titulos2.append(Titulo2)
                                PubTitulos.append(Titulos2)

                            elif len(PubTitulos) == 2:
                                Title2 = PubTitulos[1]
                                if Title[1] != Titulo2 and Title2[1] != Titulo2: # comparacion primer titulo y el segundo titulo con el titulo con mismo numero de palabras
                                    Titulos3.append(Id2)
                                    Titulos3.append(Titulo2)
                                    PubTitulos.append(Titulos3)
                                    break
        print("\nTitulos más largos y sus id de publicacion :")
        for item in PubTitulos:
            for d in item:
                print(d)

if __name__ == '__main__':
    main("https://jsonplaceholder.typicode.com/posts")

# Autor: Alejandro Solis Ortega
# Correo: alejandrosolis972@gmail.com