# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    
    name = fields.Char("name")
    name1 = fields.Char("name1")
    name2 = fields.Char("name2")
    name3 = fields.Char("name3")
    name4 = fields.Char("name4")