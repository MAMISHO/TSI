from osv import fields, osv

class nomina_item(osv.Model):
    _name = 'nomina.item'
    _columns = {
    	'id_nomina': fields.many2one('hr.payslip','Nomina'),
        'descripcion': fields.char('Descripcion nomina', size=128),
        'departamento': fields.selection([
            ('dep1','Departamento 1'),
            ('dep2','Departamento 2'),
            ('dep3','Departamento 3'),
            ],'Deparatmento'),
        'importe': fields.char('Importe nomina', size=10),  
    }


nomina_item()