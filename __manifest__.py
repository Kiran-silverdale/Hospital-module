# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'author': "Silverdale",
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'website': 'https://silverdaletech.odoo.com/',
    'version': '1.0',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail',
        'report_xlsx',
        'website'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'data/sequence.xml',
        'data/email_template.xml',
        'wizard/create_appointment.xml',
        'wizard/print_report.xml',
        'views/patient.xml',
        'views/sales.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'views/lab_records.xml',
        'views/room.xml',
        'views/bill.xml',
        'views/template.xml',
        'views/appointment.xml',
        # 'views/dashboard.xml',
        # 'views/email.xml',
        'views/menu.xml',
        'report/patient_card.xml',
        'report/patient_appointments.xml',
        'report/patient_details.xml',
        'report/print_report.xml',
        'report/report.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}