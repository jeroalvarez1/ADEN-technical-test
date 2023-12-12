# -*- coding: utf-8 -*-
# from odoo import http


# class EduHub(http.Controller):
#     @http.route('/edu_hub/edu_hub', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_hub/edu_hub/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_hub.listing', {
#             'root': '/edu_hub/edu_hub',
#             'objects': http.request.env['edu_hub.edu_hub'].search([]),
#         })

#     @http.route('/edu_hub/edu_hub/objects/<model("edu_hub.edu_hub"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_hub.object', {
#             'object': obj
#         })
