from osv import fields, osv

class nomina(osv.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'
    _columns = {
                'id_item' : fields.one2many('nomina.item','id_nomina', 'Item'),
    }
nomina()
