from odoo import models, fields, api, _


class SaleApprovalRequest(models.Model):
    _name = 'sale.approval.request'
    _description = 'Sale Order Approval Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)
    requested_by = fields.Many2one('res.users', string="Requested By", default=lambda self: self.env.user,
                                   readonly=True)
    approved_by = fields.Many2one('res.users', string="Approved By", readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', tracking=True)

    total_amount = fields.Monetary(related='sale_order_id.amount_total', store=True, string="Total Amount")
    currency_id = fields.Many2one(related='sale_order_id.currency_id')
    reject_reason = fields.Text(string="Reject Reason")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.approval.request') or _('New')
        return super(SaleApprovalRequest, self).create(vals)

    def action_submit(self):
        self.state = 'submitted'

    def action_approve(self):
        self.write({
            'state': 'approved',
            'approved_by': self.env.user
        })
        # Avtomatik Sale Orderni confirm qilish
        if self.sale_order_id.state in ['draft', 'sent']:
            self.sale_order_id.with_context(skip_approval_check=True).action_confirm()

    def action_reject(self):
        self.state = 'rejected'