# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalRooms(models.Model):
    _name = "hospital.room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Rooms"

    room_id = fields.Char(string='Room ID', required=True, copy=False, index=True, default=lambda self: _('New'))
    room_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], required=True, default='a', tracking=True)
    state = fields.Selection([('vacant', 'Vacant'),
                              ('occupied', 'Occupied')],
                             default='vacant',
                             string="Status", tracking=True)
    room_charges = fields.Integer(string="Room Charges")

    @api.model
    def create(self, vals):
        if vals.get('room_id', _('New')) == _('New'):
            vals['room_id'] = self.env['ir.sequence'].next_by_code('hospital.room') or _('New')
        if vals.get('room_type') == 'a':
            vals['room_charges'] = 1000
        elif vals.get('room_type') == 'b':
            vals['room_charges'] = 2000
        else:
            vals['room_charges'] = 3000
        return super(HospitalRooms, self).create(vals)

    def action_vacant(self):
        self.state = 'vacant'

    def action_occupy(self):
        self.state = 'occupied'

    def name_get(self):
        result = []
        for rec in self:
            name =rec.room_id
            result.append((rec.id, name))
        return result