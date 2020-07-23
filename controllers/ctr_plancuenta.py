from crud_cuenta.dao.dao_plancuenta import DaoPlanCuenta
#importar archivos para acceder a la clase

class CtrPlanCuenta:
    def __init__(self,pcta=None):
        self.__objGrupo = DaoPlanCuenta()
        self.plancuenta = pcta
    
    def consulta(self,buscar):
        return self.__objGrupo.consultar(buscar)
    
    def ingresar(self,pcta):
        return self.__objGrupo.crud_opciones(pcta,"I")
    
    def modificar(self,pcta):
        return self.__objGrupo.crud_opciones(pcta,"M")
    
    def eliminar(self,pcta):
        return self.__objGrupo.crud_opciones(pcta,"E")
    
