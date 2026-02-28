def calculate_remaining_limit(limit, total_sales):
    """Kredit limitidan qolgan summani hisoblash (oddiy mantiq)"""
    return limit - total_sales


def test_limit_calculation():
    # Test ma'lumotlari
    limit = 1000
    sales = 400

    # Kutilayotgan natija: 600
    result = calculate_remaining_limit(limit, sales)

    assert result == 600
    assert result > 0


def test_limit_exceeded():
    limit = 1000
    sales = 1200
    result = calculate_remaining_limit(limit, sales)

    assert result < 0  # Limitdan oshib ketganini bildiradi


def check_customer_status(customer_id, get_data_func):
    """Mijoz ma'lumotini tashqi funksiyadan olib tekshiradi"""
    data = get_data_func(customer_id)
    if data['debt'] > 1000:
        return "Blocked"
    return "Active"


def test_customer_blocked_with_mock(mocker):
    fake_data_func = mocker.Mock(return_value={'debt': 1500})
    status = check_customer_status(1, fake_data_func)

    # Tekshiruv
    assert status == "Blocked"
    fake_data_func.assert_called_once_with(1)


def test_customer_active_status():
    # Qarzi kam bo'lgan mijozni tekshiramiz
    fake_data = {'debt': 500}
    status = check_customer_status(2, lambda x: fake_data)

    assert status == "Active"