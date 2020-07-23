# importar las funciones del Crud Grupos
from crud_cuenta.views.funciones_plan import insertar_plan,\
    modificar_plan, eliminar_plan, consultar_grupoplan, consultar_plancuentas
# importar las funciones del Crud Plan de Cuentas
from crud_cuenta.views.funciones_grupo import insertar_grup,\
    modificar_grup, eliminar_grup, consultar_grup
#importar el archivo de validacion para llamar ala funcion salida_menu
from crud_cuenta.controllers.ctr_validacion import salida_menu
# importacion de la libreria os para acceder al DOS los comandos
import os


def menuprincipal():
    opc = ''
    while True:
        opc = str(
            __menu(['Grupos de cuentas', 'Plan de cuentas', 'Salir'], 'MENU PRINCIPAL'))
        if opc == '1':
            __submenu('MENU GRUPO CUENTAS', 1)
        elif opc == '2':
            __submenu('MENU PLAN DE CUENTAS', 2)
        elif opc == '3':
            if salida_menu():
                print('<<<Gracias por usar el sistema>>>')
                input('Presione un tecla para continuar')
                break
        elif opc != '3':
            print('Seleccione una opcion correcta')
        input('Presione una tecla para continuar')
        os.system('cls')

# Dibujar el submenu


def __submenu(titulo, opcion):
    opc = ''
    while True:
        opc = str(__menu(['Ingresar', 'Consultar', 'Modificar', 'Eliminar',
                        'Retornar Menu Principal'], str(titulo)))
        if opc == '1':
            print('\n<<<Insertar datos>>>')
            valor = input('-Ingrese la cantidad de datos a Ingresar: ')
            insertar_grup(valor) if opcion == 1 else insertar_plan(valor)
        elif opc == '2':
            print('\n<<<Consultar datos>>>')
            consultar_grup() if opcion == 1 else consultar_plancuentas()
        elif opc == '3':
            print('\n<<<Modificar datos>>>')
            modificar_grup() if opcion == 1 else modificar_plan()
        elif opc == '4':
            print('\n<<<Eliminar datos>>>')
            eliminar_grup() if opcion == 1 else eliminar_plan()
        elif opc == '5':
            print('<<<Saliendo de {}>>>'.format(titulo))
            break
        elif opc != '5':
            print('Seleccione una opcion correcta')
        input('Presione una tecla para continuar')

       # os.system('cls')
#Dibuja las opciones del Menu
def __menu(opciones, titulo):
    print('*'*22)
    print('{}'.format(titulo))
    print('*'*22)
    for i in range(0, len(opciones)):
        print("{}) {}".format(i+1, opciones[i]))
    op = input('Elija la Opcion [1...{}]: '.format(len(opciones)))
    return op

# Llamando a la función
menuprincipal()
