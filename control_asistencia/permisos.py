from osv import fields, osv

class permiso(osv.Model):
	_name = 'tarjeta.rfid'
	_columns = {
		'id_permiso': fields.char('Id Permiso', size=20, required=True),
		'descripcion': fields.char('Descripcion', size=300, required=True),
	}
permiso()