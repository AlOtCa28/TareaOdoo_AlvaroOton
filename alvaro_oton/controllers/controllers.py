# -*- coding: utf-8 -*-
# from odoo import http


# class AlvaroOton(http.Controller):
#     @http.route('/alvaro_oton/alvaro_oton', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alvaro_oton/alvaro_oton/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alvaro_oton.listing', {
#             'root': '/alvaro_oton/alvaro_oton',
#             'objects': http.request.env['alvaro_oton.alvaro_oton'].search([]),
#         })

#     @http.route('/alvaro_oton/alvaro_oton/objects/<model("alvaro_oton.alvaro_oton"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alvaro_oton.object', {
#             'object': obj
#         })
