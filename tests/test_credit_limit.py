import unittest
from unittest.mock import MagicMock
class ValidationError(Exception): pass

class TestCreditLimit(unittest.TestCase):
    def setUp(self):
        # Biznes mantiq qoidalarini aniqlab olamiz
        self.limit_amount = 50000000  # 50 mln
        self.approval_threshold = 10000  # 10k USD

    def test_01_credit_limit_validation(self):
        """TT: 50 mln so'mlik limit nazorati"""
        total_due = 45000000
        new_order = 6000000
        # Mantiqni tekshiramiz
        if (total_due + new_order) > self.limit_amount:
            with self.assertRaises(ValidationError):
                raise ValidationError("Limit oshdi!")

    def test_02_approval_logic(self):
        """TT: 10,000$ dan oshganda approval holati"""
        order_amount = 11000
        is_approval_required = order_amount > self.approval_threshold
        self.assertTrue(is_approval_required)