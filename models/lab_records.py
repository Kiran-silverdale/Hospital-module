# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalLabRecord(models.Model):
    _name = "hospital.lab.record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Lab Records"

    test_id = fields.Char(string='Test ID', required=True, copy=False, index=True, default=lambda self: _('New'))
    test_date = fields.Date(string="Test Date")
    patient_id = fields.Many2one('hospital.patient', string="Patient Name", required=True, tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor Name", tracking=True)
    age = fields.Integer(string='Age', tracking=True, related="patient_id.age", readonly=True)
    gender = fields.Selection(string='Gender', tracking=True, related="patient_id.gender", readonly=True)
    address = fields.Text(string='Address', tracking=True, related="patient_id.address", readonly=True)
    disease = fields.Char(string='Disease', tracking=True, related="patient_id.disease", readonly=True)
    note = fields.Text(string='Description', tracking=True)
    Amount = fields.Integer(string='Amount', default=1000, tracking=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('sample', 'Sample'),
                              ('test', 'Test'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')],
                             default='draft', string="Status", tracking=True)

    # test_lines = fields.One2many('hospital.lab.record.lines', 'test_id', string='Test Lines')

    def action_draft(self):
        self.state = 'draft'

    def action_sample(self):
        self.state = 'sample'

    def action_test(self):
        self.state = 'test'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('test_id', _('New')) == _('New'):
            vals['test_id'] = self.env['ir.sequence'].next_by_code('hospital.lab.record') or _('New')
        return super(HospitalLabRecord, self).create(vals)

    def name_get(self):
        result = []
        for rec in self:
            name = '[' + rec.test_id + '] ' + rec.patient_id.name
            result.append((rec.id, name))
        return result
    # class HospitaltestLines(models.Model):
    #     _name = 'hospital.lab.record.lines'
    #     _description = 'Test Lines'
    #
    #     product_id = fields.Many2one('product.product', string='Medicine')
    #     product_qty = fields.Integer(string="Quantity")
    #     appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
    #     display_type = fields.Selection([
    #         ('line_section', "Section"),
    #         ('line_note', "Note")], default=False, help="Technical field for UX purpose.")