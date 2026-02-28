# Biznes Jarayonlar Tahlili (BA)

## 1. Hozirgi holat (As-Is)
Kompaniya hozirda ulgurji savdo (Import + Wholesale) bilan shug'ullanadi. Amaldagi jarayon quyidagicha:
* Tovar Xitoydan import qilinadi va omborga keladi.
* Barcha hisob-kitoblar Excel orqali yuritiladi.
* Ombor nazorati yo'qligi sababli qoldiqlar tez-tez noto'g'ri chiqadi.
* Sotuvchilar o'z mijozlari uchun alohida hisob yuritishadi, bu esa qarzdorlikni chalkash qilib yuborgan.
* Faqatgina buxgalteriya qismi 1C tizimida yuritiladi.

## 2. Aniqlangan Muammolar 
* **Ma'lumotlar tarqoqligi:** Sotuv, ombor va buxgalteriya o'rtasida integratsiya yo'q.
* **Moliyaviy xatar:** Mijozlarning qarz limiti nazorat qilinmaydi, bu esa debitorlik qarzining o'sishiga sabab bo'ladi.
* **Inson omili:** Excel-da ma'lumotlarni qo'lda kiritish xatoliklarga boy.

## 3. Kelajakdagi holat (To-Be)
Odoo joriy qilinishi bilan barcha departamentlar yagona bazada ishlaydi:
* Import jarayonlari **Purchase** moduli orqali nazorat qilinadi.
* Ombor qoldiqlari **Inventory** moduli orqali real vaqtda ko'rinadi.
* **Credit Control** tizimi orqali mijoz 50 mln so'mdan ortiq qarz bo'lsa, sotuv bloklanadi.
* $10,000 dan yuqori savdolar menejer tasdig'idan o'tadi.