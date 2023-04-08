# -*- coding: utf-8 -*-
# from odoo import http


# class Pdca(http.Controller):
#     @http.route('/pdca/pdca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pdca/pdca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pdca.listing', {
#             'root': '/pdca/pdca',
#             'objects': http.request.env['pdca.pdca'].search([]),
#         })

#     @http.route('/pdca/pdca/objects/<model("pdca.pdca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pdca.object', {
#             'object': obj
#         })
