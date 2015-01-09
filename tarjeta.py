from osv import fields, osv

class tarjeta_rfid(osv.Model):
		_name = 'tarjeta.rfid'
	
		#def asistencia_calc(self,cr,uid,ids, field, arg,context=None):
		#	res={}   
	        #for cl in self.browse(cr,uid,ids,context=context):        
	            #res[cl.id]=len(cl.id_asistencia)
	    #    print("entra")
	    #    return res
	
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
	        #'asis_cal': fields.function(asistencia_calc,type='integer',string='Total asistencia',store=True)
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
		print("Termina bien")
tarjeta_rfid()