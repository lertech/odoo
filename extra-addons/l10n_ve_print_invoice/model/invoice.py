# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Francisco Lercari <flercari@lertech.com.ve>
#
#    Created: 2013-10-22
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

from openerp.osv import osv, fields
from openerp.tools.translate import _


class account_invoice(osv.osv):
    _name='account.invoice'
    """
    Calculo del los totales para Venezuela segun la 
    providencia 00071 del SENIAT
    
    def _amount_all_ve(self, cr, uid, ids, name, args, context=None):
        res = {} 
        for invoice in self.browse(cr, uid, ids, context=context):
            res[invoice.id] = {
                    'amount_sub': 0.0,
                               }
            for line in invoice.invoice_line:
                res[invoice.id]['amount_sub'] += line.price_unit * line.quantity
        return res
    """
    _inherit = 'account.invoice'
    def invoice_print(self, cr, uid, ids, context=None):
        res = super(account_invoice, self).invoice_print( cr, uid, ids,context) #self, cr, uid, ids, context)
        res["report_name"] = "ve.account.invoice"
        return res
    
    """_columns = {
        'amount_sub':fields.function(_amount_all_ve, type='float', string='Sub Total'),
        
                    }
    """
account_invoice()
