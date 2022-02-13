{
    'name': 'Report',
    'version': '1.0',
    'category': 'Sales/Invoices',
    'sequence': 15,
    'summary': 'Report Customization',
    'description': "",
    'website': '',
    'depends': [
        'web',
        'base',
        
    ],
    'data': [
        'views/report_templates.xml',
    ],
    
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}