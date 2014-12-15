from osv import fields, osv
#from numpy.ma.core import ids

class tarjeta_rfid(osv.Model):

       
	_name = 'tarjeta.rfid'
	_rac_name='id_employee'
	_columns = {
		#'id_tarjeta': fields.integer('ID Tarjeta', size=20, required=True),
		#'id_employee': fields.integer('ID Empleado', size=20, required=True),
		'fecha_emitida': fields.datetime('Fecha emitida',required=True, autodate = True),
		'fecha_caduca': fields.datetime('Fecha caducidad',required=True, autodate = True),
		#'id_permiso': fields.char('ID. Permiso', size=20, required=True),
		'estado': fields.selection([
			('activa','Activa'),
			('inactiva','Inactiva'),
			('perdida','Perdida'),
			],'Estado'),
		#'id_empleado': fields.char('ID Empleado', size=20, required=True),#aqui va la relacion con empleados many2many aunque seria one2many, pero como no existe, pues hacemos many2many
		'id_empleado' : fields.many2one('hr.employee','Empleado'),
		'id_asistencia' : fields.one2many('asistencia','id_tarjeta', 'Asistencia'),
		#'id_employee' : fields.related('id_empleado', 'resource_id', type='many2one', relation='hr.employee', string='El empleado'),
		#'id_tarjeta' : fields.related('id_empleado', 'resource_id', type='many2one', relation='hr.employee', string='El empleado'),
		#'id_tarjeta': fields.function(name_get, type="char", string='Name'),
	}
	# print _columns['id_empleado'] atributo de todos los elementos de formulario "attrs"
	# print "Esta es un aprueba"
	# print hr.employee
	

tarjeta_rfid()