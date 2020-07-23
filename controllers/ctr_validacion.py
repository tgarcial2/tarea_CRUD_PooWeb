from crud_cuenta.dao.dao_plancuenta import DaoPlanCuenta


def verificar_registro(pcta):
    objGrupo = DaoPlanCuenta()
    if objGrupo.crud_opciones(pcta, 'CI'):
        return True
    else:
        print("---El id que desea modificar no existe:---")
        return False


def mj_conf(titulo):
    mensaje = input('Estas seguro que deseas '+titulo +
                    ' los datos presione (y/n): ')
    if mensaje.lower() == 'y':
        return True
    else:
        return False
        
def salida_menu():
    mensaje = input('Estas seguro que deseas Salir del sistema..! presione (y/n): ')
    if mensaje.lower() == 'y':
        return True
    else:
        return False
