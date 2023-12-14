# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
from datetime import date

class Student(models.Model):
    _name = 'edu_hub.student'
    _description = 'Student model'

    name = fields.Char(string="First name", required=True)
    last_name = fields.Char(string="Last name", required=True)
    birthdate = fields.Date(string="Birthdate", required=True)
    file_number = fields.Char(string="File number", required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string="Phone number")
    address = fields.Char(string="Adress")
    country_id = fields.Many2one('res.country', string='Country', required=True)
    inscription_ids = fields.One2many('edu_hub.inscription', 'student_id', string='Inscriptions', ondelete='restrict')

    _sql_constraints = [
        ('file_number_unique',
         'UNIQUE(file_number)',
         "The file number must be unique.")
    ]

    @api.constrains('email')
    def _check_email(self):
        email_regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for record in self:
            if record.email and not re.match(email_regex, record.email):
                raise ValidationError("Please enter a valid email address.")

    @api.constrains('birthdate')
    def _check_birthdate(self):
        for record in self:
            today = date.today()
            age = today.year - record.birthdate.year - ((today.month, today.day) < (record.birthdate.month, record.birthdate.day))
            if age < 14:
                raise ValidationError("Must be over 14 years old.")

class Program(models.Model):
    _name = 'edu_hub.program'
    _description = 'Program model'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    inscription_ids = fields.One2many('edu_hub.inscription', 'program_id', string='Inscriptions', ondelete='restrict')

class Inscription(models.Model):
    _name = 'edu_hub.inscription'
    _description = 'Many-to-many relationship between Program and Student'

    student_id = fields.Many2one('edu_hub.student', string='Student', required=True)
    program_id = fields.Many2one('edu_hub.program', string='Program', required=True)
    is_active = fields.Boolean(string='Is active?', default=True)
    activation_date = fields.Datetime(string="Last activation date")
    desactivation_date = fields.Datetime(string="Last desactivation date")

    @api.model
    def create(self, vals):
        existing_inscription = self.search([
            ('student_id', '=', vals.get('student_id')),
            ('program_id', '=', vals.get('program_id'))
        ])
        if existing_inscription:
            raise ValidationError("There is already an enrollment for this student and program.")

        if vals.get('is_active', True):
            vals['activation_date'] = fields.Datetime.now()
        else:
            vals['desactivation_date'] = fields.Datetime.now()
        return super(Inscription, self).create(vals)

    def write(self, vals):
        current_is_active = vals.get('is_active', None)
        if current_is_active is not None:
            for record in self:
                if current_is_active:
                    vals['activation_date'] = fields.Datetime.now()
                else:
                    vals['desactivation_date'] = fields.Datetime.now()
        return super(Inscription, self).write(vals)
        