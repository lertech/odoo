# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: LerTech <desarrollo@lertech.com.ve>
#
#    Created: 2013-09-21
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

import time
from openerp.report import report_sxw


class account_invoice(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(account_invoice, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_rif': self._get_rif
        })

    def _get_rif(self, vat=''):
        if not vat:
            return []
        return ("%s-%s-%s" % (vat[2:3], vat[3:11], vat[11:])).replace(' ','')
    

report_sxw.report_sxw(
    'report.ve.account.invoice',
    'account.invoice',
    'addons/l10n_ve_print_invoice/report/account_print_invoice.rml',
    parser=account_invoice
)
