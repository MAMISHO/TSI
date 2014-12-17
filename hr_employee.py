from osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _rac_name='identification_id'
    _columns = {

                'id_tarjeta' : fields.one2many('tarjeta.rfid','id_empleado', 'Tarjetas'),
                #'id_tarjeta' : fields.oney2many('rel.employee.tarjeta', 'name_id ', 'Tarjetas'),
                'id_catalogo': fields.many2one('catalogo.asistencia','Catalogo'),
                'id_permiso' : fields.one2many('employee.permiso','id_empermi', 'Permisos'),
    }
hr_employee()
