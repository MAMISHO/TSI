{
    "name": "Control de Asistencia",
    "version": "1.0",
    "depends": ["base", "hr", "hr_payroll"],
    "author": "MAMISHO",
    "category": "Recursos Humanos",
    "description": """
    Este modulo incluye :
    - Control de asistencia de empleados
    - Calcula atrasos en espacios de tiempo seleccionados
    - Integra decuentos en las nominas en concepto de asistencias.
    """,
    "init_xml": [],
    'update_xml': ["empleados_view.xml"], 
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}