from odoo import models, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            # Mijoz uchun aktiv limitni qidiramiz
            limit_rec = self.env['customer.credit.limit'].search([
                ('partner_id', '=', order.partner_id.id),
                ('active', '=', True)
            ], limit=1)

            if limit_rec:
                # Joriy qarz + yangi buyurtma summasi
                total_due = order.partner_id.credit + order.amount_total
                if total_due > limit_rec.credit_limit:
                    raise ValidationError(_(
                        "Mijoz limiti oshib ketdi! \n"
                        "Maksimal limit: %s \n"
                        "Joriy jami qarz: %s"
                    ) % (limit_rec.credit_limit, total_due))

        return super(SaleOrder, self).action_confirm()