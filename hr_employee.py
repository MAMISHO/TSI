'''
Created on 29/11/2014

@author: MAMISHO
'''
from osv import fields, osv

class hr_employee(osv.osv):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _columns = {
                'emp_file':fields.char('Employee File Number', size='128'),

    }
hr_employee()
