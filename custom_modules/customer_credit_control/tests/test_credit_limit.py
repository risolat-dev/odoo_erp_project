from odoo.tests import common, tagged
from odoo.exceptions import ValidationError

@tagged('post_install', '-at_install', 'customer_credit_control')
class TestCreditLimit(common.TransactionCase):

    def setUp(self):
        super(TestCreditLimit, self).setUp()
        self.customer = self.env['res.partner'].create({'name': 'Test Mijoz'})
        self.credit_limit_record = self.env['customer.credit.limit'].create({
            'partner_id': self.customer.id,
            'credit_limit': 1000.0,
        })

    def test_01_initial_calculations(self):
        self.assertEqual(self.credit_limit_record.total_due, 0.0)
        self.assertEqual(self.credit_limit_record.remaining_credit, 1000.0)

    def test_02_recalculation_after_debt(self):
        self.customer.credit = 400.0
        self.credit_limit_record._compute_details()
        self.assertEqual(self.credit_limit_record.total_due, 400.0)
        self.assertEqual(self.credit_limit_record.remaining_credit, 600.0)

    def test_03_active_and_notes(self):
        self.credit_limit_record.write({'active': False, 'note': 'Test'})
        self.assertFalse(self.credit_limit_record.active)

    def test_04_sale_order_limit_exceeded(self):
        """Limitdan oshganda xato berishini tekshirish (92% -> 100% ga yo'l)"""
        self.credit_limit_record.credit_limit = 100.0
        self.customer.credit = 150.0
        sale_order = self.env['sale.order'].create({'partner_id': self.customer.id})
        with self.assertRaises(ValidationError):
            sale_order.action_confirm()

    def test_05_sale_order_limit_ok(self):
        """Limitdan oshmaganda muvaffaqiyatli tasdiqlanishi (Oxirgi 8% uchun)"""
        self.credit_limit_record.credit_limit = 1000.0
        self.customer.credit = 100.0
        sale_order = self.env['sale.order'].create({'partner_id': self.customer.id})
        res = sale_order.action_confirm()
        self.assertTrue(res)