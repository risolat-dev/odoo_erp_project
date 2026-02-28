from odoo.tests.common import TransactionCase

class TestSaleApproval(TransactionCase):

    def setUp(self):
        super(TestSaleApproval, self).setUp()
        self.customer = self.env['res.partner'].create({'name': 'Katta Mijoz'})

    def test_approval_creation(self):
        """$10,000 dan oshsa Approval Request yaratilishini tekshirish"""
        # 1. 11,000 dollarlik buyurtma yaratamiz
        sale_order = self.env['sale.order'].create({
            'partner_id': self.customer.id,
            'order_line': [(0, 0, {
                'product_id': self.env.ref('product.product_product_4').id,
                'product_uom_qty': 1,
                'price_unit': 11000.0,
            })]
        })

        # 2. Tasdiqlash funksiyasini chaqiramiz
        sale_order.action_confirm()

        # 3. Buyurtma tasdiqlanmasdan 'draft' holatida qolishi kerak
        self.assertEqual(sale_order.state, 'draft')

        # 4. Avtomatik Approval Request yaratilganini tekshiramiz
        approval = self.env['sale.approval.request'].search([('sale_order_id', '=', sale_order.id)])
        self.assertTrue(approval, "Approval Request yaratilmadi!")