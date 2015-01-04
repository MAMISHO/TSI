from osv import fields, osv

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
        'id_asistencia' : fields.one2many('asistencia','id_tarjeta', 'Asistencia'),
<<<<<<< HEAD
		#'id_employee' : fields.related('id_empleado', 'resource_id', type='many2one', relation='hr.employee', string='El empleado'),
		#'id_tarjeta' : fields.related('id_empleado', 'resource_id', type='many2one', relation='hr.employee', string='El empleado'),
		#'id_tarjeta': fields.function(name_get, type="char", string='Name'),
	}
	# print _columns['id_empleado'] atributo de todos los elementos de formulario "attrs"
	# print "Esta es un aprueba"
	# print hr.employee
	
=======
        }
    
        def name_get(self, cr, uid, ids, context={}):
            if not len(ids):
                return []

            res=[]
            print("Entra tarjeta test")
            for tar in self.browse(cr, uid, ids,context=context):
                identificador = (str(tar.id)).decode('unicode-escape') + '-' + (str(tar.id_empleado.identification_id)).decode('unicode-escape')
                res.append((tar.id, identificador))
            print("sale tarjeta test")
            return res
>>>>>>> mamisho

tarjeta_rfid()