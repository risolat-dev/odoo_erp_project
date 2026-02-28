from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Approval tekshiruvi
        if not self.env.context.get('skip_approval_check') and self.amount_total > 10000:
            approval = self.env['sale.approval.request'].search([
                ('sale_order_id', '=', self.id),
                ('state', '=', 'approved')
            ])
            if not approval:
                # Approval request yaratish
                self.env['sale.approval.request'].create({
                    'sale_order_id': self.id,
                    'state': 'submitted'
                })
                raise UserError(_("Order amount exceeds $10,000. Approval request has been sent to Manager."))

        return super(SaleOrder, self).action_confirm()

    def action_view_approval(self):
        action = self.env.ref('sale_approval_custom.action_sale_approval_request').read()[0]
        approval = self.env['sale.approval.request'].search([('sale_order_id', '=', self.id)], limit=1)
        if approval:
            action['res_id'] = approval.id
            action['view_mode'] = 'form'
        return action