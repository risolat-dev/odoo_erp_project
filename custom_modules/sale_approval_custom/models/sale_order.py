from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved')
    ], string="Approval Status", default='draft')

    def action_confirm(self):
        for order in self:
            if order.amount_total > 10000:
                # Huquqni tekshiramiz
                if not self.env.user.has_group('sales_team.group_sale_manager'):
                    raise AccessError(_("Sizda 10,000 dan yuqori buyurtmani tasdiqlash huquqi yo'q!"))

                # Statusni tekshiramiz
                if order.approval_status != 'approved':
                    # Menejer tasdiqlayotgan bo'lsa, statusni avtomaticheskiy 'approved' qilamiz
                    order.write({'approval_status': 'approved'})

        return super(SaleOrder, self).action_confirm()


    def action_view_approval(self):
        return True


    def action_request_approval(self):
        for order in self:
            if order.amount_total > 10000:
                order.write({'approval_status': 'to_approve'})
            else:
                order.write({'approval_status': 'approved'})