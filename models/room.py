# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalRooms(models.Model):
    _name = "hospital.room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Rooms"

    room_id = fields.Char(string='Room ID', required=True)
    type = fields.Char(string='Type')
    status = fields.Text(string='Status')