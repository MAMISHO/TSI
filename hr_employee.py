from osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _columns = {
                'catalogo':fields.char('Catalogo de asistencia', size=128),#equi suponemos que vamos crear la relacion many2one con el modulo de tarjeta_rfid
                # 'id_tarjeta' : fields.one2many('tarjeta.rfid', 'id_tarjeta', 'Tarjeta'),
    }
hr_employee()
