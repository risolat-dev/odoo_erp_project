from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError, UserError
import uuid


class TestSaleApproval(TransactionCase):

    def setUp(self):
        super(TestSaleApproval, self).setUp()
        self.partner = self.env['res.partner'].create({'name': 'Junior Plus Partner'})
        self.product = self.env['product.product'].create({
            'name': 'ERP Solution',
            'list_price': 15000,
        })

        suffix = str(uuid.uuid4())[:8]
        # 1. Oddiy sotuvchi
        self.salesman = self.env['res.users'].create({
            'name': 'Sotuvchi',
            'login': f'salesman_{suffix}',
            'groups_id': [(6, 0, [self.env.ref('sales_team.group_sale_salesman').id])]
        })
        # 2. Menejer
        self.manager = self.env['res.users'].create({
            'name': 'Menejer',
            'login': f'manager_{suffix}',
            'groups_id': [(6, 0, [self.env.ref('sales_team.group_sale_manager').id])]
        })

    def test_01_high_value_restriction(self):
        """19-qator: Sotuvchi 10k+ buyurtmani tasdiqlay olmasligini tekshirish"""
        order = self.env['sale.order'].with_user(self.salesman).create({
            'partner_id': self.partner.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
                'price_unit': 15000,
            })]
        })
        with self.assertRaises(AccessError):
            order.action_confirm()

    def test_02_approval_full_flow(self):
        """30, 34-38 qatorlar: Menejer oqimi va barcha edge-caselar"""
        order = self.env['sale.order'].with_user(self.manager).create({
            'partner_id': self.partner.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
                'price_unit': 15000,
            })]
        })

        if hasattr(order, 'action_request_approval'):
            order.action_request_approval()

        order.action_confirm()
        self.assertEqual(order.state, 'sale')

        with self.assertRaises(UserError):
            order.action_confirm()

    def test_03_approval_model_direct(self):
        """Approval Request modelini to'g'ridan-to'g'ri tekshirish"""
        order = self.env['sale.order'].create({'partner_id': self.partner.id})
        ApprovalModel = self.env.get('approval.request')
        if ApprovalModel is not None:
            request = ApprovalModel.create({
                'name': 'New',
                'sale_order_id': order.id,
            })
            request.action_approve()
            self.assertEqual(request.status, 'approved')
            request.action_cancel()
            self.assertEqual(request.status, 'cancel')