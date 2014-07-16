# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011-2014  Cristian S. Rocha
#
#    Modified: Francisco Lercari <flercari@lertech.com.ve>,
#
#    Created: 2013-09-21
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
    'name': 'Venezuela - Formato Factura',
    'version': '0.4',
    'author': 'LerTech',
    'category': 'Venezuela/Invoices',
    'website': 'http://www.lertech.com.ve/',
    'license': 'GPL-3',
    'description': """
Formato de Factura para Venezuela.
    - Reporte "Factura" adaptado a las normas de Venezuela.
""",
    'depends': [
        'sale',
        'l10n_ve_fiscal_requirements',
    ],
    'init_xml': [],
    'demo_xml': [],
    'test': [],
    'update_xml': [
        'data/reports.xml',
    ],
    'active': False,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: