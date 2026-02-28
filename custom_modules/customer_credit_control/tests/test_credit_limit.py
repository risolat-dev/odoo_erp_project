from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestCreditLimit(TransactionCase):

    def setUp(self):
        super(TestCreditLimit, self).setUp()
        # 1. Test uchun mijoz yaratamiz
        self.customer = self.env['res.partner'].create({'name': 'Test Mijoz'})

        # 2. Mijozga 1000 so'mlik limit belgilaymiz
        self.credit_limit = self.env['customer.credit.limit'].create({
            'partner_id': self.customer.id,
            'credit_limit': 1000.0,
            'active': True
        })

    def test_credit_limit_exceeded(self):
        """Limitdan oshgan sotuv bloklanishini tekshirish"""
        # 3. 1500 so'mlik Sale Order yaratamiz (limit 1000)
        sale_order = self.env['sale.order'].create({
            'partner_id': self.customer.id,
            'order_line': [(0, 0, {
                'product_id': self.env.ref('product.product_product_4').id,
                'product_uom_qty': 1,
                'price_unit': 1500.0,
            })]
        })

        # 4. Tasdiqlashga urunganda ValidationError chiqishini kutamiz
        with self.assertRaises(ValidationError):
            sale_order.action_confirm()