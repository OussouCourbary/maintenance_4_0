# -*- coding: utf-8 -*-
from odoo import http

# class Maintenance40(http.Controller):
#     @http.route('/maintenance_4_0/maintenance_4_0/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maintenance_4_0/maintenance_4_0/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('maintenance_4_0.listing', {
#             'root': '/maintenance_4_0/maintenance_4_0',
#             'objects': http.request.env['maintenance_4_0.maintenance_4_0'].search([]),
#         })

#     @http.route('/maintenance_4_0/maintenance_4_0/objects/<model("maintenance_4_0.maintenance_4_0"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maintenance_4_0.object', {
#             'object': obj
#         })