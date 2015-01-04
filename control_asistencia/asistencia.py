# -*- encoding: utf-8 -*-
'''
Created on 3/12/2014

@author: manolo
'''
from osv import osv
from osv import fields

class asistencia(osv.Model):

    def _get_departamento(self,  cr, uid, ids, name, arg, context = None):
        x = ids[0]
        for obj in self.browse(cr, uid, ids, context = context):
            print(obj.id_tarjeta.id_empleado.department_id.name)
            resul = obj.id_tarjeta.id_empleado.department_id.name
        res = {x:resul}
        print(res)
        return res

    _name = 'asistencia'
    _rec_name = 'id_tarjeta'
    _description = 'asistencia de empleados '
    _columns = {
            'hora_salida':fields.datetime('Hora salida'),
            'hora_entrada': fields.datetime('Hora entrada', required=True),
            'tipo_departamento':fields.function(_get_departamento, method = True, type = 'char', string ='Departamento', store=True),
            'id_tarjeta': fields.many2one('tarjeta.rfid', 'Tarjetas'),
            'id_item_nomina' : fields.many2one('nomina.item','Item Nomina'),
        }
    
asistencia()