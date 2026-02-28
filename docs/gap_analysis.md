# Gap Analysis (Tafovutlar Tahlili) 

## 1. Standart Odoo bilan hal bo'ladigan muammolar 
* Ombor qoldiqlari va savdo buyurtmalarining avtomatik bog'lanishi.
* Mijozlar bazasini yagona joyda saqlash (res.partner).
* Sotuv va Xarid hujjatlarini standart chop etish formalari.

## 2. Maxsus ishlab chiqilgan funksiyalar (Customization) 
* **Mijoz qarz limiti (50 mln so'm):** Standart Odoo faqat ogohlantirish beradi. Bizda esa sotuvni qat'iy bloklash mantiqi qo'shildi.
* **Katta savdolar nazorati:** $10,000 dan oshgan buyurtmalar uchun avtomatik `sale.approval.request` yaratish tizimi.

## 3. Biznes jarayondagi o'zgarishlar 
* Sotuvchilar endi o'z Excel fayllarini yuritmaydilar, buyurtmalar faqat Odoo orqali kiritiladi.
* To'lovlar buxgalteriya tomonidan o'z vaqtida kiritilishi shart, aks holda tizim qarz limitini noto'g'ri hisoblab, sotuvni bloklab qo'yishi mumkin.