import sys
from crud_cuenta.dao.conexion import Conexion

class DaoPlanCuenta(Conexion):
    def __init__(self):
        super().__init__()
    # Consultar todos los cuentas asociadas a un grupo ingresados

    def consultar(self, buscar):
        result = False
        try:
            sql = "SELECT p.id,p.codigo,g.id grupo,p.descripcion,p.naturaleza,p.estado FROM plancuenta p\
            INNER JOIN grupo AS g ON p.grupo=g.id \
            WHERE p.estado=1 AND p.descripcion LIKE '%" + str(buscar)+"%' ORDER BY p.id"
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
    def __consulta_indi(self, id):
        try:
            sql = "SELECT IF( EXISTS(SELECT * FROM plancuenta p WHERE p.id=%s),1,0) AS resul"
            self.conectar()
            self.conector.execute(sql,id)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print('Error al procesar la consulta de Grupos Cuenta', e)
            self.conn.rollback()
        finally:
            self.cerrar()

        return True if result[0][0]==1 else False

        # Metodo para ingresar

    def __ingresar(self, pcta):
        correcto = True
        try:
            sql = "INSERT INTO plancuenta(codigo,grupo,descripcion,naturaleza,estado)\
             VALUES(%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(
                sql, (pcta.codigo, pcta.grupo, pcta.descripcion, pcta.naturaleza, 1))
            self.conn.commit()
        except Exception as e:
            print('Error al ingresar', e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
    # Metodo para modificar

    def __modificar(self, pcta):
            correcto = True
            try:
                sql = 'UPDATE plancuenta SET codigo = %s, grupo = %s, descripcion=%s,\
                    naturaleza=%s WHERE id = %s'
                self.conectar()
                self.conector.execute(sql, (pcta.codigo, pcta.grupo, pcta.descripcion,
                                            pcta.naturaleza, pcta.idcuenta))
                self.conn.commit()
            except Exception as e:
                print('Error al modificar', e)
                correcto = False
                self.conn.rollback()
            finally:
                self.cerrar()
    
            return correcto

    # Metodo para eliminar

    def __eliminar(self, pcta):
        correcto = True
        if self.__consulta_indi(pcta.idcuenta):
            try:
                sql = "UPDATE plancuenta p SET p.estado=%s WHERE p.id=%s"
                self.conectar()
                self.conector.execute(sql,(0,pcta.idcuenta))
                self.conn.commit()
            except Exception as e:
                print('Error en eliminar', e)
                correcto = False
                self.conn.rollback()
            finally:
                self.cerrar()
          
        return correcto
#Obtiene los resultados de los metodos encapsulados ingresar,modificar,eliminar 
# que solo pueden acceder la propia clase 
    def crud_opciones(self,pcta,opcion):
        if opcion=='I':
            return self.__ingresar(pcta)
        elif opcion=='M':
            return self.__modificar(pcta)
        elif opcion=='E':
            return self.__eliminar(pcta)
        elif opcion=='CI':
            return self.__consulta_indi(pcta)