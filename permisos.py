from osv import fields, osv

class employee_permiso(osv.Model):
	_name = 'employee.permiso'
	_columns = {
		'id_permiso': fields.char('Id Permiso', size=20, required=True),
		'descripcion': fields.char('Descripcion', size=300, required=True),
		'id_empermi': fields.many2one('hr.employee','Empleado'),
	}
employee_permiso()