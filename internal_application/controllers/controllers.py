# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/internalApplication(http.Controller):
#     @http.route('/custom_addons/internal_application/custom_addons/internal_application', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/internal_application/custom_addons/internal_application/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/internal_application.listing', {
#             'root': '/custom_addons/internal_application/custom_addons/internal_application',
#             'objects': http.request.env['custom_addons/internal_application.custom_addons/internal_application'].search([]),
#         })

#     @http.route('/custom_addons/internal_application/custom_addons/internal_application/objects/<model("custom_addons/internal_application.custom_addons/internal_application"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/internal_application.object', {
#             'object': obj
#         })

