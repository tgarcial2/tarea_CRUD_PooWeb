import sys
import pymysql


class Conexion:
    def __init__(self, server='localhost', usuario='root', password='',
                 basedato='bd_cuenta'):
        self.__server = server
        self.__usuario = usuario
        self.__password = password
        self.__basedato = basedato
        self.__conn = ''
        self.__conector = ''

    def conectar(self):
        try:
            self.__conn = pymysql.connect(host=self.__server, user=self.__usuario, password=self.__password,
                                          database=self.__basedato)
            self.__conector = self.__conn.cursor()
            #print('Conexion Exitosa')
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print('Error al establecer la conexión a la base de datos', e)
            sys.exit(1)

    def cerrar(self):
        self.__conn.close()
        self.__conector.close()

    @property
    def conector(self):
        return self.__conector
    
    @property
    def conn(self):
        return self.__conn
