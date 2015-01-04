from osv import fields, osv
import datetime

class nomina_item(osv.Model):
<<<<<<< HEAD
    _name = 'nomina.item'
    _columns = {
    	'id_nomina': fields.many2one('hr.payslip','Nomina'),
        #'id_item':fields.char(),
        'descripcion': fields.char('Descripcion nomina', size=128),
        'departamento': fields.char('Departamento', size=128),
        'importe': fields.char('Importe nomina', size=10),  
    }

=======
	
	def _calculo(self,  cr, uid, ids, name, arg, context = None):
		print(context)
		print ("Nomina item test")
		clave = ids[0]
		cont = 0
		salario_total = 0.0
		bono = True
		
		for obj in self.browse(cr, uid, ids, context = context):
			emp = obj.id_nomina.employee_id
			print("Dentro de asistencia")
			c_he = self.normalizar_hora(emp.id_catalogo.hora_entrada)
			c_hs = self.normalizar_hora(emp.id_catalogo.hora_salida)
			c_at = self.normalizar_hora(emp.id_catalogo.atraso_tiempo)
			c_it = self.normalizar_hora(emp.id_catalogo.inasistencia_tiempo)
			c_dh = self.normalizar_hora(emp.id_catalogo.descuento_hora_tiempo)
			for t in emp.id_tarjeta:
				for a in t.id_asistencia:
					salario = 0.0
					if obj.id_nomina.date_from <= a.hora_entrada.split()[0] and a.hora_salida.split()[0]<= obj.id_nomina.date_to:
						a_he = self.get_tiempo(a.hora_entrada.split()[1])
						a_hs = self.get_tiempo(a.hora_salida.split()[1])
						print("Retraso")
						print("ASISTENCIA hora entrada :" + str(a_he))
						print("CATALOGO hora entrada : " + str(c_he))
						print("CATALOGO hora retraso : " + str(c_at))
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
			print(aux.employee_id.identification_id)
			resul = aux.employee_id.identification_id
		res = {x:resul}
		print(res)
		return res

	def _get_departamento(self,  cr, uid, ids, name, arg, context = None):
		print("Esto es get departamento")
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= obj.id_nomina
			print(aux.employee_id.department_id.name)
			resul = aux.employee_id.department_id.name
		res = {x:resul}
		print(res)
		return res

	def _get_dia_inicio(self,  cr, uid, ids, name, arg, context = None):
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= obj.id_nomina.date_from
		res = {x:aux}
		print(res)
		return res

	def _get_dia_fin(self,  cr, uid, ids, name, arg, context = None):
		x = ids[0]
		for obj in self.browse(cr, uid, ids, context = context):
			aux= obj.id_nomina.date_to
		res = {x:aux}
		print(res)
		return res

	_name = 'nomina.item'
	#_inherit = 'hr.payslip.input'
	_rec_name = 'id_empleado'
	_columns = {
    	'id_nomina': fields.many2one('hr.payslip','Nomina'),
        'descripcion': fields.char('Descripcion nomina', size=128),
        'departamento': fields.function(_get_departamento, method = True, type = 'char', string ='Departamento', store=True),
        'testeo' : fields.function(_calculo, method = True, type = 'float', string ='Importe', store=True), 
        'id_asistencias' : fields.one2many('asistencia','id_item_nomina', 'Asistencias'),
        'dia_inicio': fields.function(_get_dia_inicio, method = True, type = 'char', string ='Dia Inicial', store=True),
        'dia_final': fields.function(_get_dia_fin, method = True, type = 'char', string ='Dia Final', store=True),
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
		return float(hh + '.' + str(mm))
>>>>>>> mamisho

	print ("Nomina item test : finaliza bien")
		
nomina_item()