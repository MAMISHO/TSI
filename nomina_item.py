from osv import fields, osv

class nomina_item(osv.Model):
    _name = 'nomina.item'
    _inherit = 'hr.payslip.input'
    _columns = {
                
    }
    def calcula_importe():
		#aqui calculamos el importe dependiendo de los días trabajados y del departamento
		#al que pertence

		return 1;

nomina_item()