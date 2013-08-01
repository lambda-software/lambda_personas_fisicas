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
	"name" : "Personas físicas",
	"version" : "1.00",
	"category" : "Base",
	"description": """
        Extensión para distinguir personas físicas de personas jurídicas
        Añade el campo empresa a res_partner que indica si el partner es una empresa, de no serlo aparecerán los campos nombre y apellidos además de dni
	""",
	"author" : "Lambda Software",
	"website" : "http://www.lambdasoftware.net",
	'depends': ['base'],
	'init_xml': [],
	'update_xml': [
		'res_partner.xml',
	],
	'demo_xml': [],
	'installable': True,
	'active': False,
}

