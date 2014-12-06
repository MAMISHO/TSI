from osv import fields, osv

class tarjeta_rfid(osv.Model):
	_name = 'tarjeta.rfid'
	_columns = {
		'id_tarjeta': fields.char('ID Tarjeta', size=20, required=True),
		'fecha_emitida': fields.datetime('Fecha emitida',required=True, autodate = True),
		'fecha_caduca': fields.datetime('Fecha caducidad',required=True, autodate = True),
		'id_permiso': fields.char('ID. Permiso', size=20, required=True),
		'estado': fields.selection([
			('activa','Activa'),
			('inactiva','Inactiva'),
			('perdida','Perdida'),
			],'Estado'),
		#'id_empleado': fields.char('ID Empleado', size=20, required=True),#aqui va la relacion con empleados many2many aunque seria one2many, pero como no existe, pues hacemos many2many
		'id_empleado' : fields.one2many('hr.employee', 'identification_id', 'Empleado'),
	}
tarjeta_rfid()