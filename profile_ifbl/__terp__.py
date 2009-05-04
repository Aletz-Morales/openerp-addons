# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'IFBL Profile',
    'author' : 'Tiny SPRL',
    'version' : '0.0.2',
    'website' : 'http://www.openerp.com',
    'description' : 'Profile for the IFBL project',
    'category' : 'Profile',
    'depends' : [
        'training',
        'training_exam',
        'training_room',
        'crm',
        'project',
        'account_analytic_analysis',
        'document',
        'document_lock',
        'portal',
        'hr_expense',
        'hr_holidays',
        'portal_ifbl',
        'account_budget_project',
        'sale',
    ],
    'init_xml' : [],
    'update_xml' : [
        'base_contact_team_view.xml',
        'training_view.xml',
    ],
    'demo_xml' : [],
    'installable' : True,
    'active' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
