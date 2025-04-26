#!/usr/bin/env python
"""
Script to populate the database with initial data.
Run this after migrations: python setup_data.py
"""
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.front.models import Entrepreneur, Business, CoreValue, PortfolioItem
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile


def setup_data():
    # Create entrepreneur
    entrepreneur, created = Entrepreneur.objects.get_or_create(
        name="Rahmatullo Sohibnazarov",
        defaults={
            'slogan': "Sanoat va jamiyatlarni o'zgartiruvchi barqaror bizneslarni qurish.",
            'mission': "Mening vazifam nafaqat manfaatdor tomonlar uchun qiymat yaratadigan, balki ular xizmat ko'rsatadigan jamoalarga ijobiy ta'sir ko'rsatadigan barqaror bizneslarni qurishdir. Innovatsiya, sifat va axloqiy biznes amaliyotlariga e'tibor qaratib, men vaqt sinovidan o'tadigan va sezilarli ta'sir ko'rsatadigan korxonalarni yaratishga intilyapman.",
            'vision': "Men o'z bizneslarim o'z sohalarida innovatsiya va barqarorlik namunasi bo'lib xizmat qiladigan kelajakni ko'ryapman. Yangi texnologiyalarni qabul qilish, samarali jarayonlarni joriy qilish va doimiy takomillashtirish madaniyatini shakllantirish orqali men namuna bo'lib xizmat qiladigan va boshqalarni mukammallikka intilishga ilhomlantiradigan korxonalar portfelini yaratishga intilyapman.",
            'email': "rahmatullo****@****.com",
            'phone': "+998 91 *** ****",
            'address': "123 Business Avenue, Enterprise City, EC 12345",
        }
    )

    # Create placeholder image for entrepreneur if needed
    if not entrepreneur.photo:
        # Create a simple placeholder image
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (200, 200), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((100, 100), "AM", fill=(255, 255, 255))

        # Save to a ContentFile
        import io
        img_io = io.BytesIO()
        img.save(img_io, format='JPEG')
        img_content = ContentFile(img_io.getvalue(), 'alexander_mitchell.jpg')

        # Save to model
        entrepreneur.photo.save('alexander_mitchell.jpg', img_content, save=True)

    # Create businesses
    businesses_data = [
        {
            'name': 'Logistika kompaniyasi',
            'description': 'Yuk tashish va yetkazib berish xizmatlarida ixtisoslashgan, mintaqa bo\'ylab samarali va ishonchli logistika yechimlari taqdim etadi.',
            'icon': 'truck',
        },
        {
            'name': 'Plastik quti ishlab chiqarish',
            'description': 'Saqlash va tashish uchun chidamli plastik savatlar (korzinka) ishlab chiqaradi, turli sohalarda uzoq muddat va amaliy foydalanish uchun mo\'ljallangan.',
            'icon': 'package',
        },
        {
            'name': 'Bog\' (Meva bog\'i)',
            'description': 'Eng yaxshi mahsulotlarni ta\'minlash uchun barqaror qishloq xo\'jaligi amaliyotlaridan foydalangan holda olmalar, shaftoli va boshqa yuqori sifatli mevalarni yetishtiradi.',
            'icon': 'apple',
        },
        {
            'name': 'Katta hajmli sovutgichli saqlash',
            'description': 'Meva va sabzavotlar uchun sanoat sovutgichli saqlash xizmatini taqdim etadi, yangiligini saqlash va saqlash muddatini uzaytirish uchun optimal sharoitlarni ta\'minlaydi.',
            'icon': 'snowflake',
        },
    ]

    for business_data in businesses_data:
        Business.objects.get_or_create(
            name=business_data['name'],
            defaults={
                'description': business_data['description'],
                'icon': business_data['icon'],
            }
        )

    # Create core values
    core_values_data = [
        {
            'name': 'Innovatsiya',
            'description': 'Doimiy ravishda yaxshilash va rivojlanishning yangi usullarini izlash.',
        },
        {
            'name': 'Halollik',
            'description': 'Barcha operatsiyalarda eng yuqori axloqiy standartlarni saqlash.',
        },
        {
            'name': 'Barqarorlik',
            'description': 'Atrof-muhitni hurmat qilgan holda uzoq muddatli rivojlanadigan bizneslarni qurish.',
        },
        {
            'name': 'Mukammallik',
            'description': 'Mahsulot va xizmatlarda eng yuqori sifatga intilish.',
        },
    ]

    for value_data in core_values_data:
        CoreValue.objects.get_or_create(
            name=value_data['name'],
            defaults={
                'description': value_data['description'],
            }
        )

    # Create portfolio items with Uzbek titles
    portfolio_items_data = [
        {
            'title': 'Logistika floti',
            'category': 'Logistics',
        },
        {
            'title': 'Plastik quti ishlab chiqarish',
            'category': 'Manufacturing',
        },
        {
            'title': 'Olma bog\'i',
            'category': 'Agriculture',
        },
        {
            'title': 'Sovutgichli saqlash inshooti',
            'category': 'Storage',
        },
        {
            'title': 'Yetkazib berish operatsiyalari',
            'category': 'Logistics',
        },
        {
            'title': 'Meva hosili',
            'category': 'Agriculture',
        },
    ]

    for item_data in portfolio_items_data:
        portfolio_item, created = PortfolioItem.objects.get_or_create(
            title=item_data['title'],
            defaults={
                'category': item_data['category'],
            }
        )

        # Create placeholder image if needed
        if created or not portfolio_item.image:
            # Create a simple placeholder image
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (800, 600), color=(100, 150, 200))
            d = ImageDraw.Draw(img)
            d.text((400, 300), item_data['title'], fill=(255, 255, 255))

            # Save to a ContentFile
            import io
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG')
            img_content = ContentFile(img_io.getvalue(), f"{item_data['title'].lower().replace(' ', '_')}.jpg")

            # Save to model
            portfolio_item.image.save(f"{item_data['title'].lower().replace(' ', '_')}.jpg", img_content, save=True)

    print("Dastlabki ma'lumotlar o'rnatish tugallandi!")


if __name__ == "__main__":
    setup_data()
