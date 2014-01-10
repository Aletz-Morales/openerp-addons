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

{
    'name': 'Calendar',
    'version': '1.0',
    'depends': ['base', 'mail', 'base_action_rule','web_calendar'],
    'summary': 'Personal & Shared Calendar',
    'description': """
This is a full-featured calendar system.
========================================

It supports:
------------
    - Calendar of events
    - Recurring events

If you need to manage your meetings, you should install the CRM module.
    """,
    'author': 'OpenERP SA',
    'category': 'Hidden/Dependency',
    'website': 'http://www.openerp.com',
    'demo': ['calendar_demo.xml'],
    'data': [
        'security/calendar_security.xml',
        'security/ir.model.access.csv',
        'calendar_view.xml',
        'contacts_view.xml',
        'calendar_data.xml',        
    ],
    'js': [
        'static/src/js/*.js'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'css': [
        'static/src/css/calendar.css'
    ],
    'test' : [
              'test/calendar_test.yml',
              'test/test_crm_recurrent_meeting_case2.yml'
              ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['images/calendar1.jpeg','images/calendar2.jpeg','images/calendar3.jpeg','images/calendar4.jpeg'],
}


