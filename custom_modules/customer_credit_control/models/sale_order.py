from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            # Mijozning limitini qidiramiz
            limit_rec = self.env['customer.credit.limit'].search([
                ('partner_id', '=', order.partner_id.id),
                ('active', '=', True)
            ], limit=1)

            if limit_rec:
                # Mijozning jami qarzi + yangi buyurtma summasi
                total_due = order.partner_id.credit + order.amount_total

                # AGAR limit oshsa VA foydalanuvchi ADMIN bo'lmasa
                if total_due > limit_rec.credit_limit:
                    is_manager = self.env.user.has_group('sales_team.group_sale_manager')

                    if not is_manager:
                        raise ValidationError(_(
                            "Credit Limit Exceeded! Current Due: %s. Limit: %s. "
                            "Please contact your Manager."
                        ) % (total_due, limit_rec.credit_limit))

        return super(SaleOrder, self).action_confirm()