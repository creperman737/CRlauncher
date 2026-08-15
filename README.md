# CRLauncher

**CRLauncher** — Minecraft uchun maxsus, yengil va tezkor launcher. Python'da yozilgan, hozircha **Alpha** bosqichida.

```
========================================
        CRLauncher Alpha
========================================
Minecraft directory:
C:\Users\...\AppData\Roaming\.minecraft

Java:
✓ Found

Minecraft versions:
✓ 1.20.1
✓ 1.21.8
✓ Snapshot

CR Skin:
Ready
```

## 🚀 CRLauncher nima

CRLauncher — o'rnatilgan Minecraft versiyalarini avtomatik aniqlaydigan, Java'ni topib beradigan va custom skin tizimiga ega bo'lgan shaxsiy launcher loyihasi. Vanilla, Forge, OptiFine va aralash (modified) versiyalarni bir joyda ko'rsatadi.

## 🎯 Asosiy maqsad

- Minecraft'ni ishga tushirishni soddalashtirish — versiyalarni qo'lda qidirmasdan, avtomatik topish
- Har xil OS'larda (Windows, Linux, macOS) bir xilda ishlashi
- Kompyuter quvvatiga qarab optimallashtirilgan sozlamalarni taklif qilish
- O'ziga xos skin tizimi orqali qulaylik yaratish

## ⭐ CR Skin System — flagship feature

Loyihaning asosiy xususiyati. Username orqali skin URL'ni olib, PNG formatida yuklab beradi va resource-pack sifatida generatsiya qiladi — hatto snapshot versiyalarda ham ishlaydi.

## 🖥️ PC/Minecraft detection

CRLauncher quyidagilarni avtomatik aniqlaydi:

- O'rnatilgan Java (`java.exe` yo'li)
- `.minecraft` papkasi joylashuvi
- Mavjud barcha versiyalar: vanilla, Forge, OptiFine, snapshot va modified profillar

### 💻 OS bo'yicha `.minecraft` joylashuvi

| OS | Yo'l |
|---|---|
| Windows | `%APPDATA%/.minecraft` |
| Linux | `~/.minecraft` |
| macOS | `~/Library/Application Support/minecraft` |

## 🧩 Snapshot resource-pack tizimi

Snapshot versiyalar uchun resource-pack va skin moslashuvini alohida boshqaradigan tizim (ishlab chiqilmoqda).

## ⚡ Smart Optimization

Kompyuterning CPU/RAM/GPU imkoniyatlarini hisobga olib, versiyaga mos optimal sozlamalarni taklif qiladigan modul (rejalashtirilgan).

## 🌐 CR Skin API

Username asosida skin ma'lumotlarini olish va PNG ko'rinishida qaytarish uchun API qatlami.

## 📁 Loyiha strukturasi

```
CRlauncher/
├── api/            # CR Skin API bilan ishlash
├── launcher/        # Asosiy launcher logikasi (versiya, Java, launch)
├── optimizer/        # Smart Optimization (CPU/RAM/GPU detection)
├── skin/            # Skin tizimi
├── main.py           # Kirish nuqtasi
├── requirements.txt   # Python bog'liqliklari
└── LICENSE
```

## 🗺️ Development roadmap

| Bosqich | Vazifa | Holat |
|---|---|---|
| **Alpha 0.1** | OS aniqlash | ✅ |
| | `.minecraft` topish | ✅ |
| | Java aniqlash | 🔜 |
| | Minecraft versiyalarini o'qish | 🔜 |
| **Alpha 0.2** | Minecraft version tanlash | ⏳ |
| | Launch tizimi | ⏳ |
| | RAM sozlamasi | ⏳ |
| **Alpha 0.3** | 🌐 CR Skin API | ⏳ |
| | Username → skin URL | ⏳ |
| | PNG downloader | ⏳ |
| **Alpha 0.4** | ⭐ CR Skin System | ⏳ |
| | Resource-pack generator | ⏳ |
| | Snapshot skin testlari | ⏳ |
| **Alpha 0.5** | ⚡ Smart Optimization | ⏳ |
| | CPU/RAM/GPU detection | ⏳ |
| | Version-specific profiles | ⏳ |
| **Beta 1.0** | 🖥️ GUI | ⏳ |
| | Settings | ⏳ |
| | Version manager | ⏳ |
| | Skin manager | ⏳ |
| | Optimization manager | ⏳ |

## ⚖️ Minecraft/Mojang bilan bog'liq huquqiy chegaralar

CRLauncher — Mojang Studios yoki Microsoft bilan hech qanday rasmiy bog'liqligi bo'lmagan mustaqil (fan-made) loyiha. Minecraft — Mojang Studios'ning ro'yxatdan o'tgan savdo belgisi. Ushbu loyiha o'yin fayllarini tarqatmaydi — foydalanuvchining o'zida mavjud, qonuniy sotib olingan Minecraft nusxasi bilan ishlaydi.

## 📌 O'rnatish

```bash
git clone https://github.com/creperman737/CRlauncher.git
cd CRlauncher
pip install -r requirements.txt
python main.py
```

## 📄 Litsenziya

Ushbu loyiha [LICENSE](LICENSE) fayli ostida tarqatiladi.