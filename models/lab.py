# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalLabs(models.Model):
    _name = "hospital.lab"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital labs"

    lab_id = fields.Char(string='Lab No.', required=True, copy=False, index=True, default=lambda self: _('New'))
    lab_name = fields.Char(string='Name', required=True, tracking=True)
    user_id = fields.Many2one('res.users', string="Responsible")


    @api.model
    def create(self, vals):
        if vals.get('lab_id', _('New')) == _('New'):
            vals['lab_id'] = self.env['ir.sequence'].next_by_code('hospital.lab') or _('New')
        return super(HospitalLabs, self).create(vals)

    def name_get(self):
        result = []
        for rec in self:
            name = rec.lab_name
            result.append((rec.id, name))
        return result