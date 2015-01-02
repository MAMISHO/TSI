from osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _rac_name='identification_id'
    _columns = {
                #me vuelve a dar el mismo error si cambio id_tarjeta a ids_tarjeta tambien lo cambion el xml y me da error xml
                'id_tarjeta' : fields.one2many('tarjeta.rfid','id_empleado', 'Tarjetas'),
                'id_catalogo': fields.many2one('catalogo.asistencia','Catalogo'),
                #me vuelve a dar el mismo error si cambio id_permiso a ids_permiso tambien lo cambion el xml y me da error xml
                'id_permiso' : fields.one2many('employee.permiso','id_empermi', 'Permisos'),
    }
hr_employee()
