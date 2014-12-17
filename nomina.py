from osv import fields, osv

class nomina(osv.Model):
    _name = 'nomina'
    _inherit = 'hr.payslip'
    _columns = {
                #'id_tarjeta' : fields.one2many('tarjeta.rfid', 'id_empleado', 'Tarjetas'),
                'id_item' : fields.one2many('nomina.item','id_nomina', 'Item'),
    }
nomina()
