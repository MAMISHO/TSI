from osv import fields, osv

class tarjeta_rfid(osv.Model):
	_name = 'tarjeta.rfid'
	#_rec_name='id'
	_columns = {
		#'id_tarjeta': fields.related('ID Tarjeta', size=20, required=True),
        #'name_related': fields.related('id_empleado', 'name_related', type='char', string='Name', readonly=True, store=True),
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
    
        def name_get(self, cr, uid, ids, context={}):#redefine _rec_name     
            if not len(ids):
                return []

            res=[]
            print("Entra tarjeta test")
            for tar in self.browse(cr, uid, ids,context=context):
                # print(tar.id)
                # for emp in tar.id_empleado:
                identificador = (str(tar.id)).decode('unicode-escape') + '-' + (str(tar.id_empleado.identification_id)).decode('unicode-escape')
                res.append((tar.id, identificador))
            print("sale tarjeta test")
            return res

tarjeta_rfid()