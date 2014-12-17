from osv import fields, osv

class nomina_item(osv.Model):
    _name = 'nomina.item'
    _columns = {
    	'id_nomina': fields.many2one('hr.payslip','Nomina'),
        #'id_item':fields.char(),
        'descripcion': fields.char('Descripcion nomina', size=128),
        'departamento': fields.char('Departamento', size=128),
        'importe': fields.char('Importe nomina', size=10),  
    }


nomina_item()