# importacion del controlador Grupo
from crud_cuenta.controllers.ctr_grupo import CtrGrupo
# importacion del modelo Grupo
from crud_cuenta.models.model_grupo import Grupo
#Importacion para validar los registros
from crud_cuenta.controllers import ctr_validacion

#Instancia del objeto del Controlador Grupo
ctrgrup= CtrGrupo()
# Funcion para ingresar al Grupo de Cuentas

def insertar_grup(rango):
    for i in range(int(rango)):
        descripcion = input('Ingrese el nombre del Grupo: ')
        grupo = Grupo(descripcion=descripcion)
        verifica = ctr_validacion.mj_conf('Guardar')
        if verifica and ctrgrup.ingresar(grupo):
            print('<<<Registro Grabado Exitosamente>>>')
        else:
            print('<<<No se grabo el registro>>>')
# Funcion para modificar al Grupo de Cuentas


def modificar_grup():
    codigo = input('Ingrese el código: ')
    descripcion = input('Ingrese el nombre del Grupo: ')
    grupo = Grupo(codigo, descripcion)
    verifica = ctr_validacion.mj_conf('Modificar')
    if verifica and ctrgrup.modificar(grupo):
        print('<<<Registro Modificado Exitosamente>>>')
    else:
        print('<<<No se modifico el registro>>>')

# Funcion para eliminar al Grupo de Cuentas


def eliminar_grup():
    codigo = input('-----Ingrese el código-----: ')
    grupo = Grupo(codigo=codigo)
    if __buscar(codigo):
        verifica = ctr_validacion.mj_conf('Eliminar')
        if verifica and ctrgrup.eliminar(grupo): 
            print('<<<Registro Eliminado Exitosamente>>>')
    else:
        print('No existe el id el que desea eliminar')

# Funcion para consultar los Grupo de Cuentas


def consultar_grup():
    buscar = input('Ingrese el nombre del Grupo a buscar: ')
    grup = ctrgrup.consulta(buscar)
    print('Codigo|\t', 'Descripcion')
    if len(grup)>0:
        for datos in grup:
            print('{}\t{}'.format(datos[0], datos[1]))
    else:
        print('---Sin registros---')

#Funcion para buscar el id que se procede a eliminar y 
# tambien se imprime los resgistros   
def __buscar(codigo):
    grup = ctrgrup.consulta("")
    for datos in grup:
        if str(datos[0])==str(codigo):
            print('Codigo\t', 'Descripcion')
            print('{}\t{}'.format(datos[0], datos[1]))
            return True
    return False
            