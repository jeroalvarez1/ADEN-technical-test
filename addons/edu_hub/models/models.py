# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

#fijarse como hacer para que un estudiante no se pueda inscribir dos veces en el mismo programa
class Student(models.Model):
    _name = 'edu_hub.student'
    _description = 'Student model'

    name = fields.Char(string="First name", required=True)
    last_name = fields.Char(string="Last name", required=True)
    birthdate = fields.Date(string="Birthdate", required=True)
    file_number = fields.Char(string="File number", required=True)
    email = fields.Char(string='Email', validate='^([\w\.-]+)@([\w\.-]+)\.(\w+)$', required=True)
    phone = fields.Char(string="Phone number")
    address = fields.Char(string="Adress") # ver forma de reemplezarlo
    country_id = fields.Many2one('res.country', string='Country', required=True)
    program = fields.Many2many(
        comodel_name="edu_hub.program",
        relation_name="inscription",
        column1="student_id",
        column2="program_id",
        string="Programs",
    )

class Program(models.Model):
    _name = 'edu_hub.program'
    _description = 'Program model'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    student = fields.Many2many(
        comodel_name="edu_hub.student",
        relation_name="inscription",
        column1="program_id",
        column2="student_id",
        string="Students"
    )