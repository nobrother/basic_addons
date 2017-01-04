# -*- coding: utf-8 -*-
from openerp import http

# class OmcBasicConfig(http.Controller):
#     @http.route('/omc_basic_config/omc_basic_config/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/omc_basic_config/omc_basic_config/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('omc_basic_config.listing', {
#             'root': '/omc_basic_config/omc_basic_config',
#             'objects': http.request.env['omc_basic_config.omc_basic_config'].search([]),
#         })

#     @http.route('/omc_basic_config/omc_basic_config/objects/<model("omc_basic_config.omc_basic_config"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('omc_basic_config.object', {
#             'object': obj
#         })