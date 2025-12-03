# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloBebidaCafe(http.Controller):
#     @http.route('/modulo_bebida_cafe/modulo_bebida_cafe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_bebida_cafe/modulo_bebida_cafe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_bebida_cafe.listing', {
#             'root': '/modulo_bebida_cafe/modulo_bebida_cafe',
#             'objects': http.request.env['modulo_bebida_cafe.modulo_bebida_cafe'].search([]),
#         })

#     @http.route('/modulo_bebida_cafe/modulo_bebida_cafe/objects/<model("modulo_bebida_cafe.modulo_bebida_cafe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_bebida_cafe.object', {
#             'object': obj
#         })

