# importacion del controlador de Plan de Cuenta
from crud_cuenta.controllers.ctr_plancuenta import CtrPlanCuenta
# importacion  del modelo Plan de Cuenta
from crud_cuenta.models.model_plancuenta import PlanCuenta
# Importacion del Controlador de Grupos
from crud_cuenta.controllers.ctr_grupo import CtrGrupo
#Importacion para validar los registros
from crud_cuenta.controllers import ctr_validacion
# Instancia de los Objetos del Controlador
ctrgrup, ctrpcta = CtrGrupo(), CtrPlanCuenta()

# Funciones de Plan de Cuentas


def consultar_grupoplan():
    print('Ejemplo de Grupo para Asociar')
    grup = ctrgrup.consulta("")
    print('Codigo\t', 'Descripcion')
    for datos in grup:
        print('{}\t{}'.format(datos[0], datos[1]))
    return grup

# Funcion para ingresar datos al Plan  de Cuentas

def insertar_plan(rango):
    for i in range(int(rango)):
        codigo = input('Ingrese el codigo del Plan de Cuenta: ')
        result = consultar_grupoplan()
        condicion=1
        while condicion==1:
            grupo = input('Ingrese el número de Grupo que desea asociar: ')
            for valor in result:
                if str(valor[0])==str(grupo):
                    descripcion = input('Ingrese el nombre del Plan de Cuenta: ')
                    tupla_naturaleza = ('D','A')
                    while True:
                        naturaleza = input(
                            'Ingrese la letra de Naturaleza ejemplo:\n D: Deudora, A: Acredora: ')
                        if naturaleza.upper() in tupla_naturaleza:
                            condicion=0
                            break
                        else:
                            print('---Incorrecto la letra de naturaleza---')
            if condicion==1:print('---El id del Grupo no existe---')
        plan = PlanCuenta(codigo=codigo, grupo=grupo,
                          descripcion=descripcion, naturaleza=naturaleza.upper())
        verifica = ctr_validacion.mj_conf('Guardar')
        if verifica and ctrpcta.ingresar(plan):
            print('Registro Grabado Exitosamente')
        else:
            print('No se grabo el registro')

# Funcion para modificar datos el Plan  de Cuentas


def modificar_plan():
    while True:
        idcuenta = input('Ingrese el id del Plan de Cuenta: ')
        if ctr_validacion.verificar_registro(idcuenta):
            codigo = input('Ingrese el nuevo codigo del Plan de Cuenta: ')
            print('<<<Lista de Grupos>>>')
            result = consultar_grupoplan()
            condicion=1
            while condicion==1:
                grupo = input('Ingrese el nuevo numero de Grupo que desea asociar: ')
                for valor in result:
                    if str(valor[0])==str(grupo):
                        descripcion = input('Ingrese el nuevo nombre del Plan de Cuenta: ')
                        tupla_naturaleza = ('D','A')
                        while True:
                            naturaleza = input(
                            'Ingrese la letra de Naturaleza ejemplo:\n D: Deudora, A: Acredora: ')
                            if naturaleza.upper() in tupla_naturaleza:
                                condicion=0
                                break
                            else:
                                print('---Incorrecto la letra de naturaleza---')
                if condicion==1:print('---El id del Grupo no existe---')
            break          
    plan = PlanCuenta(idcuenta, codigo, grupo, descripcion, naturaleza.upper())
    verifica = ctr_validacion.mj_conf('Modificar')
    if  verifica and ctrpcta.modificar(plan):
        print('<<<Registro Modificado Exitosamente>>>')
    else:
        print('<<<No se modifico el registro>>>')

# Funcion para consultar los registros de Plan de Cuenta


def consultar_plancuentas():
    buscar = input('Ingrese el nombre del Plan de Cuenta a buscar: ')
    registros = ctrpcta.consulta(buscar)
    print('id | ', 'código | ', 'grupo |',
          'descripcion |\t', 'naturaleza |\t', 'estado')
    if len(registros)>0:
        for datos in registros:
            print('{}\t{}\t{}\t{}\t\t{}\t\t{}'.format(datos[0], datos[1], datos[2],
                                                    datos[3], datos[4], datos[5]))
    else:
        print('---Sin registros---')
# Funcion para eliminar el registro de Plan de Cuenta


def eliminar_plan():
    codigo = input('-----Ingrese el código-----: ')
    plan = PlanCuenta(idcuenta=codigo)
    if __buscar(codigo):
        verifica = ctr_validacion.mj_conf('Eliminar')
        if verifica and ctrpcta.eliminar(plan):
            print('<<<Registro Eliminado Exitosamente>>>')
    else:
       print('No existe el id el que desea eliminar')

  #Funcion para buscar el id que se procede a eliminar      
def __buscar(codigo):
    result = ctrpcta.consulta("")
    for datos in result:
        if str(datos[0])==str(codigo):
            print('id | ', 'código | ', 'grupo |',
                'descripcion |', 'naturaleza |', 'estado')
            print('{}\t{}\t{}\t{}\t\t{}\t\t{}\t'.format(datos[0], datos[1], datos[2],
                                                    datos[3], datos[4], datos[5]))
            return True
    return False
            