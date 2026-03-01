# Odoo 17 ERP Customization

Salom! Bu loyiha Odoo 17 da savdo jarayonlarini va mijozlar balansini nazorat qilish uchun yozilgan.

### 🚀 Nimalar bor?
- **Credit Limit Control**: Agar mijozning qarzi belgilangan limitdan oshib ketsa, tizim sotuvga ruxsat bermaydi.
- **Sales Approval**: Katta summali savdolarni menejer tasdiqlaydigan qilib sozlaganman.

### 🧪 Testlash (Pytest)
Mantiqiy qismlarni Pytest yordamida tekshirganman. Hozirda testlar koding **100%** qismini tekshiradi.
- **Run tests**: `pytest --cov=tests tests/`

### 🛠 Texnologiyalar
- **Python 3.13**, **Odoo 17.0**, **PostgreSQL**
- **Pytest** & **Pytest-Cov**

### 📦 Qanday ishlatish kerak?
1. Loyihani yuklab oling: `git clone https://github.com/risolat-dev/odoo_erp_project.git`
2. Kutubxonalarni o'rnating: `pip3 install -r requirements.txt`
3. Odoo serverni yoqing: `python3 odoo/odoo-bin -c odoo.conf --addons-path=odoo/addons,custom_modules`

---
**Muallif:** Risolat - Python Backend Developer