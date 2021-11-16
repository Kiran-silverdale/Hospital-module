# -*- coding: utf-8 -*-

from odoo import models, fields


class PrintAppointment(models.TransientModel):
    _name = 'print.appointment'
    _description = 'Print Appointment Report'

    patient_id = fields.Many2one('hospital.patient', string="Patient Name")
    date_from = fields.Date(string="From Date")
    date_to = fields.Date(string="To Date")


    def print_appointment_excel(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('appointment_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('appointment_date', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search_read(domain)
        print(appointments)
        data = {
            'model': 'print.appointment',
            'form': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('hospital.patient_report_xlx').report_action(self, data=data)


    def print_appointment_wizard(self):

        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('appointment_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('appointment_date', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search_read(domain)
        # print(appointments)
        data = {
            'model': 'print.appointment',
            'form': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('hospital.print_report').report_action(self, data=data)



