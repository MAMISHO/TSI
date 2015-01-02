from osv import fields, osv

class catalogo_asistencia(osv.Model):
	_name = 'catalogo.asistencia'
	_columns = {
		'ids_empleado':fields.one2many('hr.employee','id_catalogo', 'Empleado'),
        'id_departamento': fields.char('ID Departamento', size=20, required=True),
		'descripcion': fields.char('Descripcion', size=300, required=False),
        'hora_entrada': fields.datetime('Hora de Entrada', required=True, autodate=True),
        'hora_salida': fields.datetime('Hora de Salida', required=True, autodate=True),
        'atraso_tiempo': fields.datetime('Retraso', required=True, autodate=True),
		'atraso_multa': fields.char('Multa retraso',required=True),
        'descuento_hora_tiempo': fields.datetime('Descuento por hora', required=True, autodate=True),
        'descuento_hora_multa': fields.char('Multa por hora', required=True),
        'inasistencia_tiempo': fields.datetime('Inasistencia por hora', required=True, autodate=True),
        'inasistencia_multa': fields.char('Multa por inasistencia', required=True),
        'hora_extra_tiempo': fields.datetime('Llegada a tiempo', required=True, autodate=True),
        'hora_extra_costo': fields.char('Paga por llegar a tiempo', required=True)
	}
catalogo_asistencia()