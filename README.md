# Tadbirkor Portfoliosi - Django loyihasi

To'rt xil biznesga ega tadbirkor uchun Django-da qurilgan toza, minimalistik portfolio veb-sayti.

## Xususiyatlar

- Tadbirkorning ismi, surati va shiori bilan bosh sahifa
- Piktogramma va tavsiflar bilan to'rtta biznesni ko'rsatadigan biznes bo'limi
- Biznes toifasi bo'yicha filtrlash imkoniyati bilan portfolio galereyasi
- Vazifa va ko'rish bayonotlari bilan haqida bo'limi
- Tekshirish va yuborish boshqaruvi bilan aloqa shakli
- Barcha ekran o'lchamlari uchun moslashuvchan dizayn
- Kontent boshqaruvi uchun admin interfeysi

## O'rnatish yo'riqnomasi

1. Repozitoriyani klonlash
2. Virtual muhit yaratish:
   \`\`\`
   python -m venv venv
   source venv/bin/activate  # Windows-da: venv\Scripts\activate
   \`\`\`
3. Bog'liqliklarni o'rnatish:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`
4. Migratsiyalarni bajarish:
   \`\`\`
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`
5. Superuser yaratish:
   \`\`\`
   python manage.py createsuperuser
   \`\`\`
6. Dastlabki ma'lumotlarni yuklash:
   \`\`\`
   python setup_data.py
   \`\`\`
7. Ishlab chiqish serverini ishga tushirish:
   \`\`\`
   python manage.py runserver
   \`\`\`
8. Brauzeringizda http://127.0.0.1:8000/ manziliga tashrif buyuring
9. Admin interfeysiga http://127.0.0.1:8000/admin/ orqali kirish

## Loyiha tuzilishi

- `portfolio_project/` - Django loyiha sozlamalari
- `entrepreneur/` - Asosiy Django ilovasi
  - `models.py` - Tadbirkor, bizneslar va boshqalar uchun ma'lumotlar modellari
  - `views.py` - Ko'rish funktsiyalari
  - `forms.py` - Aloqa shakli uchun shakl boshqaruvi
  - `templates/` - HTML shablonlar
  - `admin.py` - Admin interfeysi konfiguratsiyasi

## Foydalanilgan texnologiyalar

- Django 4.2
- HTML5/CSS3
- Tailwind CSS (CDN orqali)
- Alpine.js (interaktivlik uchun)
- AOS - Animate On Scroll kutubxonasi
