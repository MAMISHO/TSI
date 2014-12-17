from osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _rac_name='identification_id'
    _columns = {
                'catalogo':fields.char('Catalogo de asistencia', size=128),#equi suponemos que vamos crear la relacion many2one con el modulo de tarjeta_rfid
                'id_tarjeta' : fields.one2many('tarjeta.rfid','id_empleado', 'Tarjetas'),
                #'id_tarjeta' : fields.oney2many('rel.employee.tarjeta', 'name_id ', 'Tarjetas'),
                'id_catalogo': fields.many2one('catalogo.asistencia','Catalogo'),
                'id_permiso' : fields.one2many('employee.permiso','id_empermi', 'Permisos'),
    }
hr_employee()
