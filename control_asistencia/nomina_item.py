from osv import fields, osv
import datetime
#from bsddb.dbtables import _columns

class nomina_item(osv.Model):
	
	def _calculo(self,  cr, uid, ids, name, arg, context = None):
		print(context)
		print ("Nomina item test")
		#total = 5.0
		clave = ids[0]
		cont = 0
		salario_total = 0.0
		bono = True
		
		for obj in self.browse(cr, uid, ids, context = context):
			#print(obj.id_nomina.name)
			emp = obj.id_nomina.employee_id
			#catalogo = {}
			#catalogo['he'] = emp.id_catalogo.hora_entrada
			#catalogo['hs'] = emp.id_catalogo.hora_salida
			#print(catalogo)
			#print(obj.id_nomina.date_from)
			#print(obj.id_nomina.date_to)
			print("Dentro de asistencia")
			#c_he = str(emp.id_catalogo.get_hora_entrada()).split()[1]
			#c_hs = str(emp.id_catalogo.get_hora_salida()).split()[1]
			c_he = self.normalizar_hora(emp.id_catalogo.hora_entrada)
			c_hs = self.normalizar_hora(emp.id_catalogo.hora_salida)
			c_at = self.normalizar_hora(emp.id_catalogo.atraso_tiempo)
			c_it = self.normalizar_hora(emp.id_catalogo.inasistencia_tiempo)
			c_dh = self.normalizar_hora(emp.id_catalogo.descuento_hora_tiempo)
			#c_he = c_he.split()[1]
			#c_hs = c_hs.split()[1]
			#catalogo = self._get_catalogo(emp.id_catalogo)
			#print("datos")
			#print(emp.id_catalogo.hora_entrada)
			#print(emp.id_catalogo.hora_salida)
			#print(emp.id_catalogo.atraso_tiempo)
			#print(emp.id_catalogo.atraso_multa)
			#print("Catalogo hora entrada " + str(c_he))
			#print("Catalogo hora salida " + str(c_hs))
			for t in emp.id_tarjeta:
				#print(t.estado)
				for a in t.id_asistencia:
					salario = 0.0
					if obj.id_nomina.date_from <= a.hora_entrada.split()[0] and a.hora_salida.split()[0]<= obj.id_nomina.date_to:
						a_he = self.get_tiempo(a.hora_entrada.split()[1])
						a_hs = self.get_tiempo(a.hora_salida.split()[1])
						#print(a.hora_entrada.split()[0])
						#print(a.hora_salida.split()[0])
						#print(str(c_at - a_he))
						#print(a_he.split(":")[0])
						#print("Asistencia hora entrada " + str(a_he))
						#print("Asistencia hora salida " + str(a_hs))
						#if a_he <= c_he:
						#	salario += emp.id_catalogo.hora_extra_costo
						print("Retraso")
						print("ASISTENCIA hora entrada :" + str(a_he))
						print("CATALOGO hora entrada : " + str(c_he))
						print("CATALOGO hora retraso : " + str(c_at))
						#c_at2 = self.normalizar_hora(c_at)
						#print("CATALOGO hora retraso : " + str(c_at2))
						if a_he <= c_it:
							if a_he > c_he:
								bono = False
								if a_he > c_at:
									m = float(a_he - c_at)/c_dh
									costo =m * emp.id_catalogo.descuento_hora_multa
									print("esta dentro de atraso")
									print(m)
									print(costo)
									salario = salario - (emp.id_catalogo.atraso_multa + costo)
									print(salario)
						else:
							bono = False
							print("entra en el else")
							salario = salario - emp.id_catalogo.inasistencia_multa
							print(salario)
					
					salario_total = salario_total + salario	
					print(salario_total)
			if bono is True:
				print("Tiene bono")
				salario_total += emp.id_catalogo.bono_asistencia
		res = {clave:salario_total}
		print(str(cont))
		print(str(salario_total))
		print ("Nomina item test: final")
		return res
	
	def _get_empleado(self,  cr, uid, ids, name, arg, context = None):
		print("esto es _get_empleado")
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= obj.id_nomina
		#aux  =  self.browse(cr, uid, ids, context = context).id_nomina
			#for x in aux.employee_id:
			print(aux.employee_id.identification_id)
			resul = aux.employee_id.identification_id
		res = {x:resul}
		print(res)
		return res

	def _get_departamento(self,  cr, uid, ids, name, arg, context = None):
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= obj.id_nomina
		#aux  =  self.browse(cr, uid, ids, context = context).id_nomina
			#for x in aux.employee_id:
			print(aux.employee_id.departament_id.name)
			#for obj in aux.beta.alpha:
			resul = aux.employee_id.departament_id.name
		res = {x:resul}
		print(res)
		return res

	def _get_dia_inicio(self,  cr, uid, ids, name, arg, context = None):
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= id_nomina.date_from
		res = {x:aux}
		print(res)
		return res

	def _get_dia_fin(self,  cr, uid, ids, name, arg, context = None):
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= id_nomina.date_to
		res = {x:aux}
		print(res)
		return res

	_name = 'nomina.item'
	_inherit = 'hr.payslip.input'
	_rec_name = 'id_empleado'
	_columns = {
    	'id_nomina': fields.many2one('hr.payslip','Nomina'),
        'descripcion': fields.char('Descripcion nomina', size=128),
        #'departamento': fields.function(_get_departamento, method = True, type = 'char', string ='Departamento'),
        'departamento': fields.char('Departamento', size=128),
        'testeo' : fields.function(_calculo, method = True, type = 'float', string ='Importe'), 
        'id_asistencias' : fields.one2many('asistencia','id_item_nomina', 'Asistencias'),
        #'dia_inicio': fields.function(_get_dia_inicio, method = True, type = 'char', string ='Dia Inicial'),
        #'dia_final': fields.function(_get_dia_fin, method = True, type = 'char', string ='Dia Final'),
        'dia_inicio':fields.datetime('Dia inicial', required=True),
        'dia_final': fields.datetime('Dia final', required=True),
        'id_empleado' : fields.function(_get_empleado, method = True, type = 'char', string ='Empleado'),#, store=True),
    }
	
	def get_tiempo(self, cat):
		print("getTiempo")
		print(cat)
		tiempo = 0.0
		hh = cat.split(":")[0]
		mm = cat.split(":")[1]
		print(hh)
		print(mm)
		tiempo = float(str(hh) + '.' + str(mm))
		print(tiempo)
		return tiempo
	
	def normalizar_hora(self, hr):
		hh = str(hr).split(".")[0]
		mm = str(hr).split(".")[1]
		mm = int(mm) * 60/100
		#print("Normalizar tiempo")
		#print(mm)
		return float(hh + '.' + str(mm))

	print ("Nomina item test : finaliza bien")
		
nomina_item()