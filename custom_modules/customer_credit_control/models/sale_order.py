from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            limit_rec = self.env['customer.credit.limit'].search([
                ('partner_id', '=', order.partner_id.id),
                ('active', '=', True)
            ], limit=1)

            if limit_rec:
                if (limit_rec.total_due + order.amount_total) > limit_rec.credit_limit:
                    raise ValidationError(_(
                        "Credit Limit Exceeded! \n"
                        "Customer: %s \n"
                        "Limit: %s \n"
                        "Total Due + This Order: %s"
                    ) % (order.partner_id.name, limit_rec.credit_limit, (limit_rec.total_due + order.amount_total)))
        return super(SaleOrder, self).action_confirm()