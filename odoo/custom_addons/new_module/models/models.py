# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lesson(models.Model):
    _name = "wb.lesson"
    
    name = fields.Char("name")
    start_time = fields.Datetime("start time")
    end_time = fields.Datetime("end time")
    school_days = fields.Selection([
        ('even_days', 'even days'),
        ('odd_days', 'odd days'),
        ], srting="school days")
    cost = fields.Integer("cost")
    teacher_id = fields.Many2one("wb.teacher")
    

class student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    
    name = fields.Char("name")
    surname = fields.Char("surname")
    date = fields.Date("date")
    number = fields.Integer("phone number")
    balance = fields.Integer("balance")
    lesson_id = fields.Many2many('wb.lesson',string="lessons")
    
    

class teacher(models.Model):
    _name = "wb.teacher"
    
    name = fields.Char("name")
    surname = fields.Char("surname")
    type_of_lesson =fields.Char("type of lesson")
    salary = fields.Integer("salary")
    lesson_id = fields.One2many(comodel_name='wb.lesson', inverse_name='teacher_id', string='Lessons')
    
    
    