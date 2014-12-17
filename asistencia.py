# -*- encoding: utf-8 -*-
'''
Created on 3/12/2014

@author: manolo
'''
from osv import osv
from osv import fields

class asistencia(osv.Model):
 
    _name = 'asistencia'
    #_rec_name = 'id_asistencia'
    _description = 'asistencia de empleados '
    _columns = {
            'hora_salida':fields.datetime('Hora salida'),
            'hora_entrada': fields.datetime('Hora entrada', required=True),
            'tipo_departamento':fields.char('Tipo de departamento ', size=64, required=True),            
            'id_tarjeta': fields.many2one('tarjeta.rfid', 'Tarjetas'),
        }
asistencia()