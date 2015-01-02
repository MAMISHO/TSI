from osv import fields, osv

class nomina(osv.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'
    _columns = {
                #cambie el nombre id_item por ids_item en la vista tambien pero siempre me salia error de xml
                'id_item' : fields.one2many('nomina.item','id_nomina', 'Item'),
    }
nomina()
