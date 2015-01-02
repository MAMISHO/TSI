# -*- encoding: utf-8 -*-
'''
Created on 3/12/2014

@author: manolo
'''
from osv import osv
from osv import fields

class asistencia(osv.Model):
    _name = 'asistencia'
    _description = 'asistencia de empleados '
    _columns = {
            'hora_salida':fields.datetime('Hora salida', required=True, autodate=True),
            'hora_entrada': fields.datetime('Hora entrada', required=True, autodate=True),
            'tipo_departamento': fields.selection([
            ('dep1','Departamento 1'),
            ('dep2','Departamento 2'),
            ('dep3','Departamento 3'),
            ],'Deparatmento'),            
            'id_tarjeta': fields.many2one('tarjeta.rfid', 'Tarjetas'),
        }
asistencia()