# -*- encoding: utf-8 -*-
'''
Created on 3/12/2014

@author: manolo
'''
from osv import osv
from osv import fields

class asistencia(osv.osv):
 
    _name = 'asistencia'
    _description = 'asistencia de empleados '
    _columns = {
            'hora_salida':fields.datetime('hora salida'),
            'hora_entrada': fields.datetime('Hora entrada', required=True),
            'tipo_departamento':fields.char('tipo de departamento ', size=64, required=True),            
            'id_asistencia':fields.char('tarjeta','Subject', required=True)      #onetomany  
        }