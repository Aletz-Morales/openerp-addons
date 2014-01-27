# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _

class event_track_tag(osv.osv):
    _name = "event.track.tag"
    _columns = {
        'name': fields.char('Event Track Tag')
    }

class event_tag(osv.osv):
    _name = "event.tag"
    _columns = {
        'name': fields.char('Event Tag')
    }

#
# Tracks: conferences
#

class event_track_stage(osv.osv):
    _name = "event.track.stage"
    _order = 'sequence'
    _columns = {
        'name': fields.char('Track Stage'),
        'sequence': fields.integer('Sequence')
    }
    _defaults = {
        'sequence': 0
    }


class event_track_location(osv.osv):
    _name = "event.track.location"
    _columns = {
        'name': fields.char('Track Rooms')
    }

class event_track(osv.osv):
    _name = "event.track"
    _order = 'priority, date'
    _inherit = ['mail.thread', 'ir.needaction_mixin', 'website.seo.metadata']

    def _website_url(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, '')
        base_url = self.pool.get('ir.config_parameter').get_param(cr, uid, 'web.base.url')
        for track in self.browse(cr, uid, ids, context=context):
            res[track.id] = "%s/event/%d/track/%d" % (base_url, track.event_id.id, track.id)
        return res

    _columns = {
        'name': fields.char('Track Title', required=True),
        'user_id': fields.many2one('res.users', 'Responsible'),
        'speaker_ids': fields.many2many('res.partner', string='Speakers'),
        'tag_ids': fields.many2many('event.track.tag', string='Tags'),
        'stage_id': fields.many2one('event.track.stage'),
        'description': fields.html('Track Description'),
        'date': fields.datetime('Track Date'),
        'duration': fields.integer('Duration'),
        'location_id': fields.many2one('event.track.location', 'Location'),
        'show_attachments': fields.boolean('Show Documents'),
        'event_id': fields.many2one('event.event', 'Event', required=True),
        'color': fields.integer('Color Index'),
        'priority': fields.selection([('3','Low'),('2','Medium (*)'),('1','High (**)'),('0','Highest (***)')], 'Priority', required=True),
        'website_published': fields.boolean('Available in the website'),
        'website_url': fields.function(_website_url, string="Website url", type="char"),
    }
    def set_priority(self, cr, uid, ids, priority, context={}):
        return self.write(cr, uid, ids, {'priority' : priority})

    def _default_stage_id(self, cr, uid, context={}):
        stage_obj = self.pool.get('event.track.stage')
        ids = stage_obj.search(cr, uid, [], context=context)
        return ids and ids[0] or False

    _defaults = {
        'user_id': lambda self, cr, uid, ctx: uid,
        'website_published': lambda self, cr, uid, ctx: False,
        'show_attachments': lambda self, cr, uid, ctx: True,
        'duration': lambda *args: 60,
        'stage_id': _default_stage_id,
        'priority': '2'
    }
    def _read_group_stage_ids(self, cr, uid, ids, domain, read_group_order=None, access_rights_uid=None, context=None):
        stage_obj = self.pool.get('event.track.stage')
        result = stage_obj.name_search(cr, uid, '', context=context)
        return result, {}

    _group_by_full = {
        'stage_id': _read_group_stage_ids,
    }

#
# Events
#
class event_event(osv.osv):
    _inherit = "event.event"

    def _get_tracks_tag_ids(self, cr, uid, ids, field_names, arg=None, context=None):
        res = dict.fromkeys(ids, [])
        for event in self.browse(cr, uid, ids, context=context):
            for track in event.track_ids:
                res[event.id] += [tag.id for tag in track.tag_ids]
            res[event.id] = list(set(res[event.id]))
        return res
    _columns = {
        'tag_ids': fields.many2many('event.tag', string='Tags'),
        'track_ids': fields.one2many('event.track', 'event_id', 'Tracks'),
        'sponsor_ids': fields.one2many('event.sponsor', 'event_id', 'Sponsorships'),
        'blog_id': fields.many2one('blog.blog', 'Event Blog'),
        'show_track_proposal': fields.boolean('Talks Proposals'),
        'show_tracks': fields.boolean('Multiple Tracks'),
        'show_blog': fields.boolean('News'),
        'tracks_tag_ids': fields.function(_get_tracks_tag_ids, type='one2many', relation='event.track.tag', string='Tags of Tracks'),
        'allowed_track_tag_ids': fields.many2many('event.track.tag', string='Accepted Tags', help="List of available tags for track proposals."),
    }
    _defaults = {
        'show_track_proposal': False,
        'show_tracks': False,
        'show_blog': False,
    }
    def _get_new_menu_pages(self, cr, uid, event, context=None):
        context = context or {}
        result = super(event_event, self)._get_new_menu_pages(cr, uid, event, context=context)
        if event.show_tracks:
            result.append( (_('Talks'), '/event/%s/track/' % event.id))
            result.append( (_('Agenda'), '/event/%s/agenda/' % event.id))
        if event.blog_id:
            result.append( (_('News'), '/blogpost/'+str(event.blog_ig.id)))
        if event.show_track_proposal:
            result.append( (_('Talk Proposals'), '/event/%s/track_proposal/' % event.id))
        return result

#
# Sponsors
#

class event_sponsors_type(osv.osv):
    _name = "event.sponsor.type"
    _order = "sequence"
    _columns = {
        "name": fields.char('Sponsor Type', required=True),
        "sequence": fields.integer('Sequence')
    }

class event_sponsors(osv.osv):
    _name = "event.sponsor"
    _order = "sequence"
    _columns = {
        'event_id': fields.many2one('event.event', 'Event', required=True),
        'sponsor_type_id': fields.many2one('event.sponsor.type', 'Sponsoring Type', required=True),
        'partner_id': fields.many2one('res.partner', 'Sponsor/Customer', required=True),
        'sequence': fields.related('sponsor_type_id', 'sequence', string='Sequence', store=True),
    }

    def has_access_to_partner(self, cr, uid, ids, context=None):
        try:
            partner = self.pool.get("res.partner")
            partner.check_access_rights(cr, uid, 'read')
            partner_id = self.browse(cr, uid, ids[0], context=context).partner_id.id
            partner.check_access_rule(cr, uid, [partner_id], 'read', context=context)
            return True
        except:
            return False

