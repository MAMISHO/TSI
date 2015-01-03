from osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    #_rec_name='identification_id'
    _columns = {

                'id_tarjeta' : fields.one2many('tarjeta.rfid','id_empleado', 'Tarjetas'),
                #'id_tarjeta' : fields.oney2many('rel.employee.tarjeta', 'name_id ', 'Tarjetas'),
                'id_catalogo': fields.many2one('catalogo.asistencia','Catalogo'),
                'id_permiso' : fields.one2many('employee.permiso','id_empermi', 'Permisos'),
                'identification_id': fields.char('Identification No', size=32, required=True),
                #'nomina_id' : fields.one2many('hr.payslip', 'employee_id', 'Nomina'),
                'id_item_nomina' : fields.one2many('nomina.item','id_nomina', 'Item'),
    }
    _sql_constraints = [('identification_id_unique','unique(identification_id)', 'DNI ya existe')]
    
    
    def name_get(self, cr, uid, ids, context={}):#redefine _rec_name     
        if not len(ids):
            return []

        res=[]

        for emp in self.browse(cr, uid, ids,context=context):
            #compuesto = str(emp.name) + ', ' + str(emp.identification_id)
            #res.append((emp.id, compuesto))
            #res.append((emp.id, emp.name))# + ', ' + emp.identification_id))     
            res.append((emp.id, emp.name))
        return res

hr_employee()
