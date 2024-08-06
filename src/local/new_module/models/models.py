# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lesson(models.Model):
    _name = "wb.lesson"
    
    name = fields.Char("Name")
    start_time = fields.Datetime("Start time")
    end_time = fields.Datetime("End time")
    school_days = fields.Selection([
        ('even_days', 'even days'),
        ('odd_days', 'odd days'),
        ], srting="school days")
    cost = fields.Integer("cost")
    teacher_id = fields.Many2one("wb.teacher")
    

class student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    
    name = fields.Char("Name")
    surname = fields.Char("Surname")
    date = fields.Date("Date")
    number = fields.Integer("Phone number")
    balance = fields.Integer("Balance")
    lesson_id = fields.Many2many('wb.lesson',string="Lessons")
    
    

class teacher(models.Model):
    _name = "wb.teacher"
    
    name = fields.Char("Name")
    surname = fields.Char("Surname")
    type_of_lesson =fields.Char("Type of lesson")
    salary = fields.Integer("Salary")
    lesson_id = fields.One2many(comodel_name='wb.lesson', inverse_name='teacher_id', string='Lessons')
    
    
    