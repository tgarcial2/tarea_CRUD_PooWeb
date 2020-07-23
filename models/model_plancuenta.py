class PlanCuenta:
    def __init__(self, idcuenta=0, codigo='', grupo=0, descripcion='', naturaleza='', estado=True):
       #Encapsulamiento de los atributos
        self.__idcuenta = idcuenta
        self.__codigo = codigo
        self.__grupo = grupo
        self.__descripcion = descripcion
        self.__naturaleza = naturaleza
        self.__estado = estado

    # Metodos get de la clase
    @property
    def idcuenta(self):
        return self.__idcuenta

    @property
    def codigo(self):
        return self.__codigo

    @property
    def grupo(self):
        return self.__grupo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def naturaleza(self):
        return self.__naturaleza

    @property
    def estado(self):
        return self.__estado

    # Metodos set de la clase
    @idcuenta.setter
    def idcuenta(self, idcuenta):
        self.__idcuenta = idcuenta

    @codigo.setter
    def codigo(self, codigo=''):
        self.__codigo = codigo

    @grupo.setter
    def grupo(self, grupo):
        self.__grupo = grupo

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @naturaleza.setter
    def naturaleza(self, naturaleza):
        self.__naturaleza = naturaleza

    @estado.setter
    def estado(self, estado):
        self.__estado = estado
