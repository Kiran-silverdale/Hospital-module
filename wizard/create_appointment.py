# -*- coding: utf-8 -*-

from odoo import models, fields, _ , api


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment Wizard'

    appointment_date = fields.Date(string="Appointment Date")
    patient_id = fields.Many2one('hospital.patient', string="Patient Name")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor Name")
    age = fields.Integer(string='Age', related="patient_id.age", readonly=True)
    gender = fields.Selection(string='Gender', related="patient_id.gender", readonly=True)
    disease = fields.Char(string='Disease', related="patient_id.disease", readonly=True)
    appointment_id = fields.Char(string='Reference', required=True, copy=False, index=True,
                                 default=lambda self: _('New'))
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')],
                             default='draft',
                             string="Status")

    @api.model
    def default_get(self, fields):
        res = super(CreateAppointment, self).default_get(fields)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id' : self.doctor_id.id,
            'appointment_date': self.appointment_date,
            'note': self.patient_id.note,
            'state': 'draft'
        }
        self.patient_id.message_post(body="Test string ", subject="Appointment Creation")
        new_appointment = self.env['hospital.appointment'].create(vals)
        context = dict(self.env.context)
        import logging
        _logger = logging.getLogger(__name__)
        _logger.info("account.py cornerstone_account calling")
        context['form_view_initial_mode'] = 'edit'
        return {'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'hospital.appointment',
                'res_id': new_appointment.id,
                'context': context
                }

    # def get_data(self):
    #     appointments = self.env['hospital.appointment'].search([])
    #     for rec in appointments:
    #         print("Appointment Name", rec.name)
    #     return{
    #         "type": "ir.actions.do_nothing"
    #     }
