from odoo import models, fields, api


class CustomerCreditLimit(models.Model):
    _name = 'customer.credit.limit'
    _description = 'Customer Credit Limit'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    active = fields.Boolean(default=True)
    note = fields.Text(string="Notes")

    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.company.currency_id)

    credit_limit = fields.Monetary(string="Credit Limit", currency_field='currency_id', required=True)
    total_due = fields.Monetary(string="Total Due", currency_field='currency_id', compute="_compute_details")
    remaining_credit = fields.Monetary(string="Remaining Credit", currency_field='currency_id',
                                       compute="_compute_details")

    @api.depends('partner_id', 'credit_limit', 'partner_id.credit')
    def _compute_details(self):
        for rec in self:
            rec.total_due = rec.partner_id.credit if rec.partner_id else 0.0
            rec.remaining_credit = rec.credit_limit - rec.total_due