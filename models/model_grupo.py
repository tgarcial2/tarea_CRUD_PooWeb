class Grupo:
    def __init__(self, codigo=0, descripcion=''):
        #Encapsulamiento de los atributos
        self.__codigo = codigo
        self.__descripcion = descripcion

    # Metodos get y set de la clase
    @property
    def codigo(self):
        return self.__codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

