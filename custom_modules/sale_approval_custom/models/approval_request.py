from odoo import models, fields, api

class ApprovalRequest(models.Model):
    _name = 'approval.request'
    _description = 'Sale Approval Request'

    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default='New')
    sale_order_id = fields.Many2one('sale.order', string="Sales Order", required=True)
    amount = fields.Float(string="Total Amount")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('cancel', 'Cancelled')
    ], default='draft', string="Status")

    def action_approve(self):
        for record in self:
            record.status = 'approved'

    def action_cancel(self):
        for record in self:
            record.status = 'cancel'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('approval.request') or 'New'
        return super(ApprovalRequest, self).create(vals_list)