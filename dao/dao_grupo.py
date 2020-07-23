import sys
from crud_cuenta.dao.conexion import Conexion


class DaoGrupo(Conexion):
    def __init__(self):
        super().__init__()
    # Consultar todos los grupos ingresados

    def consultar(self, buscar):
        result = False
        try:
            sql = "SELECT id cod, descripcion FROM grupo \
            WHERE descripcion LIKE '%" + str(buscar)+"%' ORDER BY id"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print('Error al procesar la consulta de Grupos Cuenta', e)
            self.conn.rollback()
        finally:
            self.cerrar()

        return result

        #Consulta Indivodual para verificar si existe el id a modificar o eliminar
    def __consulta_indi(self, grup):
        try:
            sql = "SELECT IF( EXISTS(SELECT * FROM grupo g WHERE g.id=%s),1,0) AS resul"
            self.conectar()
            self.conector.execute(sql,grup.codigo)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print('Error al procesar la consulta de Grupos Cuenta', e)
            self.conn.rollback()
        finally:
            self.cerrar()

        return True if result[0][0]==1 else False
     
       # Metodo para ingresar

    def __ingresar(self, grup):
        correcto = True
        try:
            sql = "INSERT INTO grupo(descripcion) VALUES('{}')".format(
                grup.descripcion)
            self.conectar()
            self.conector.execute(sql)
            self.conn.commit()
        except Exception as e:
            print('Error al ingresar', e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
    # Metodo para modificar

    def __modificar(self, grup):
        correcto = True
        if self.__consulta_indi(grup):
            try:
                sql = "UPDATE grupo SET descripcion = '{}' WHERE id = {}".format(
                    grup.descripcion, grup.codigo)
                self.conectar()
                self.conector.execute(sql)
                self.conn.commit()
            except Exception as e:
                print('Error al modificar', e)
                correcto = False
                self.conn.rollback()
            finally:
                self.cerrar()
        else:
             correcto = False
             print('<<<---No existe el id del Grupo a modificar--->>>')
        return correcto

    # Metodo para eliminar

    def __eliminar(self, grup):
        correcto = True
        if self.__consulta_indi(grup):
            try:
                sql = "DELETE FROM grupo WHERE id={}".format(grup.codigo)
                self.conectar()
                self.conector.execute(sql)
                self.conn.commit()
            except Exception as e:
                print('Error en eliminar', 'Este id de Grupo ya se encuentra usado en el PLan de Cuentas')
                correcto = False
                self.conn.rollback()
            finally:
                self.cerrar()
          
        return correcto
#Obtiene los resultados de los metodos encapsulados ingresar,modificar,eliminar 
# que solo pueden acceder la propia clase 
    def crud_opciones(self,grup,opcion):
        if opcion=='I':
            return self.__ingresar(grup)
        elif opcion=='M':
            return self.__modificar(grup)
        elif opcion=='E':
            return self.__eliminar(grup)