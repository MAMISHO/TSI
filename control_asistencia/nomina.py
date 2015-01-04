from osv import fields, osv

class nomina(osv.Model):
    def _prueba(self,  cr, uid, ids, name, arg, context = None):
        print ("Nomina item test")  
        total = ids[0]
        res = {total:0.0}
        res[total] += 3
        return res
    
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'
    _rec_name='employee_id'
    _columns = {
                'id_item' : fields.one2many('nomina.item','id_nomina', 'Item'),
                'total' : fields.function(_prueba, method = True, type = 'float', string ='Prueba test'),
    }

nomina()
