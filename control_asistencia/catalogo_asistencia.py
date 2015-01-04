from osv import fields, osv
<<<<<<< HEAD

class catalogo_asistencia(osv.Model):
	_name = 'catalogo.asistencia'
	_columns = {
		'id_empleado':fields.one2many('hr.employee','id_catalogo', 'Empleado'),
        'id_departamento': fields.char('ID Departamento', size=20, required=True),
		'descripcion': fields.char('Descripcion', size=300, required=False),
        'hora_entrada': fields.datetime('Hora de Entrada', required=True, autodate=True),
        'hora_salida': fields.datetime('Hora de Salida', required=True, autodate=True),
        'atraso_tiempo': fields.datetime('Retraso', required=True, autodate=True),
		'atraso_multa': fields.char('Multa retraso',required=True),
        'descuento_hora_tiempo': fields.datetime('Descuento por hora', required=True, autodate=True),
        'descuento_hora_multa': fields.char('Multa por hora', required=True),
        'inasistencia_tiempo': fields.datetime('Inasistencia por hora', required=True, autodate=True),
        'inasistencia_multa': fields.char('Multa por inasistencia', required=True),
        'hora_extra_tiempo': fields.datetime('Llegada a tiempo', required=True, autodate=True),
        'hora_extra_costo': fields.char('Paga por llegar a tiempo', required=True)
	}
=======
import datetime
import math

class catalogo_asistencia(osv.Model):
	_name = 'catalogo.asistencia'
	_rec_name='descripcion'
	_columns = {
		'id_empleado':fields.one2many('hr.employee','id_catalogo', 'Empleado'),
        'id_departamento':fields.many2one('hr.department', 'Departamento'),
        'descripcion': fields.char('Descripcion', size=300, required=False),
        'hora_entrada': fields.float('Hora de Entrada', required=True),
        'hora_salida': fields.float('Hora de Salida', required=True),
        'atraso_tiempo': fields.float('Retraso', required=True, digits=(2,2)),
        'atraso_multa': fields.float('Multa retraso',required=True),
        'descuento_hora_tiempo': fields.float('Descuento por hora', required=True),
        'descuento_hora_multa': fields.float('Multa por hora', required=True),
        'inasistencia_tiempo': fields.float('Inasistencia por hora', required=True),
        'inasistencia_multa': fields.float('Multa por inasistencia', required=True),
        'hora_extra_tiempo': fields.float('Hora extra', required=True),
        'hora_extra_costo': fields.float('Costo hora extra', required=True),
        'bono_asistencia' : fields.float('Bono de asistencia', required=True),
	}

        def get_hora_entrada(self, cr, uid, ids, context=None):
                for catalogo in self.browse(cr, uid, ids, context=context):
                        aux = catalogo.hora_entrada
                        mm,hh = math.modf(aux)
                        hora = datetime.datetime(2015,1,1,hh,mm,00)
                return hora

        def get_hora_salida(self, cr, uid, ids, context=None):
                for catalogo in self.browse(cr, uid, ids, context=context):
                        aux = catalogo.hora_salida
                        mm,hh = math.modf(aux)
                        hora = datetime.datetime(2015,1,1,hh,mm,00)
                return hora

        def get_atraso_tiempo(self, cr, uid, ids, context=None):
                for catalogo in self.browse(cr, uid, ids, context=context):
                        aux = catalogo.atraso_tiempo
                        mm,hh = math.modf(aux)
                        print(hh)
                        print(mm)
                        if mm < 1:
                                mm = mm*100
                        hora = datetime.datetime(2015,1,1,hh,mm,00)
                return hora

        def name_get(self, cr, uid, ids, context={}):
                if not len(ids):
                    return []
                res=[]
                x = ids[0]
                for obj in self.browse(cr, uid, ids,context=context):
                    compuesto = obj.id_departamento.name
                    res.append((x, compuesto))
                return res

>>>>>>> mamisho
catalogo_asistencia()