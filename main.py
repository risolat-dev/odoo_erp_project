import sys
import os

# 1. Loyiha papkalarini aniqlash
root_path = os.path.dirname(os.path.abspath(__file__))
odoo_path = os.path.join(root_path, 'odoo')

# 2. Standart kutubxonalar bilan xatolik bo'lmasligi uchun
# Odoo papkasini ro'yxat oxiriga qo'shamiz
if odoo_path not in sys.path:
    sys.path.append(odoo_path)

import odoo

if __name__ == "__main__":
    # 3. Serverni ishga tushirish parametrlari
    args = [
        '--config=' + os.path.join(root_path, 'odoo.conf'),
        '--addons-path=' + f"{os.path.join(odoo_path, 'addons')},custom_modules",
        # Modullarni yangilash
        '-u', 'custom_credit_limit,sale_approval_request'
    ]

    odoo.cli.main(args)