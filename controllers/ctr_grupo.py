from crud_cuenta.dao.dao_grupo import DaoGrupo
#importar archivos para acceder a la clase

class CtrGrupo:
    def __init__(self,grup=None):
        self.__objGrupo = DaoGrupo()
        self.grupo = grup
    
    def consulta(self,buscar):
        return self.__objGrupo.consultar(buscar)
    
    def ingresar(self,grup):
        return self.__objGrupo.crud_opciones(grup,'I')
    
    def modificar(self,grup):
        return self.__objGrupo.crud_opciones(grup,'M')
    
    def eliminar(self,grup):
        return self.__objGrupo.crud_opciones(grup,'E')