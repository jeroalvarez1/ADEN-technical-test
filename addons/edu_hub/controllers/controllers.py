# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class EduHub(http.Controller):

    @http.route('/edu_hub/program/<int:program_id>/students', auth='public', type='http', website=True, methods=['GET'], csrf=False)
    def get_program_students(self, program_id, **kwargs):
        try:
            students = request.env['edu_hub.student'].sudo().search([('inscription_ids.program_id', 'in', [program_id])])
            student_data = [{
                'name': student.name,
                'last_name': student.last_name,
                'file_number': student.file_number,
                'birthdate': f'{student.birthdate}',
                'email': student.email,
                'phone': student.phone if student.phone else None,
                'country': {
                    'id': student.country_id.id,
                    'name': student.country_id.name
                }
            } for student in students]
            return json.dumps(student_data)
        except Exception as e:
            return json.dumps({'error': str(e)})