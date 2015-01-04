from osv import fields, osv

class hr_employee(osv.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _columns = {

                'id_tarjeta' : fields.one2many('tarjeta.rfid','id_empleado', 'Tarjetas'),
<<<<<<< HEAD
                #'id_tarjeta' : fields.oney2many('rel.employee.tarjeta', 'name_id ', 'Tarjetas'),
                'id_catalogo': fields.many2one('catalogo.asistencia','Catalogo'),
                'id_permiso' : fields.one2many('employee.permiso','id_empermi', 'Permisos'),
=======
                'id_catalogo': fields.many2one('catalogo.asistencia','Catalogo'),
                'id_permiso' : fields.one2many('employee.permiso','id_empermi', 'Permisos'),
                'identification_id': fields.char('Identification No', size=32, required=True),
                'id_item_nomina' : fields.one2many('nomina.item','id_nomina', 'Item'),
>>>>>>> mamisho
    }
    _sql_constraints = [('identification_id_unique','unique(identification_id)', 'DNI ya existe')]
    
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []

        res=[]

        for emp in self.browse(cr, uid, ids,context=context):
            compuesto = emp.name + ' - ' + (str(emp.identification_id)).decode('unicode-escape')
            res.append((emp.id, compuesto))
        return res

hr_employee()
