# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalEmail(models.Model):
    _name = "hospital.email"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Email sender"

    patient_id = fields.Many2one('hospital.patient', string="Patient Name", required=True, tracking=True)
    receiver_id = fields.Char(string='Send to', tracking=True, related="patient_id.email", readonly=True)
    sender_id = fields.Char(string="Send from", default="kiran.ibrahim@gmail.com", required=True, tracking=True)

    def send_email(self):
        # sending the patient report to patient via email
        template_id = self.env.ref('hospital.patient_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)


    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
    #     return super(HospitalAppointments, self).create(vals)
    #
    # class HospitalAppointmentLines(models.Model):
    #     _name = 'hospital.appointment.lines'
    #     _description = 'Appointment Lines'
    #
    #     product_id = fields.Many2one('product.product', string='Medicine')
    #     product_qty = fields.Integer(string="Quantity")
    #     appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
    #     display_type = fields.Selection([
    #         ('line_section', "Section"),
    #         ('line_note', "Note")], default=False, help="Technical field for UX purpose.")