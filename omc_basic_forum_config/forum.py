# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class Post(osv.Model):

    _inherit = 'forum.post'

    # Always allow to view every post
    def _get_post_karma_rights(self, cr, uid, ids, field_name, arg, context=None):
        res = super(Post, self)._get_post_karma_rights(cr, uid, ids, field_name, arg, context)

        for post_id in res:
            res[post_id].update({
                'can_view': True
            })

        return res

    _columns = {
        'can_view': fields.function(_get_post_karma_rights, string='Can View', type='boolean'),
    }