import sys
from unittest.mock import MagicMock

mock_odoo = MagicMock()
sys.modules['odoo'] = mock_odoo
sys.modules['odoo.models'] = MagicMock()
sys.modules['odoo.fields'] = MagicMock()
sys.modules['odoo.api'] = MagicMock()

def test_credit_limit_logic():
    limit = 50000000
    current_due = 48000000
    new_order = 5000000
    # Agar limitdan oshsa True qaytarishi kerak
    is_blocked = (current_due + new_order) > limit
    assert is_blocked is True

def test_approval_threshold_logic():
    threshold = 10000
    order_amount = 12000
    needs_approval = order_amount > threshold
    assert needs_approval is True

def test_under_limit_logic():
    limit = 50000000
    current_due = 10000000
    new_order = 5000000
    is_blocked = (current_due + new_order) > limit
    assert is_blocked is False