from osv import fields, osv
from numpy.ma.core import ids

class tarjeta_rfid(osv.Model):
	_name = 'tarjeta.rfid'
	_columns = {
		'fecha_emitida': fields.datetime('Fecha emitida',required=True, autodate = True),
		'fecha_caduca': fields.datetime('Fecha caducidad',required=True, autodate = True),
		'estado': fields.selection([
			('activa','Activa'),
			('inactiva','Inactiva'),
			('perdida','Perdida'),
			],'Estado'),
		'id_empleado' : fields.many2one('hr.employee','Empleado'),
        'ids_asistencia' : fields.one2many('asistencia','id_tarjeta', 'Asistencia'),
	}

tarjeta_rfid()