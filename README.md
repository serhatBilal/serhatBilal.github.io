# Serhat Bilal Studio

Statik (build gerektirmeyen) GitHub Pages sitesi: https://serhatbilal.github.io

Oyunlar: **The Flipside**, **Merge Survivors: Dark Dungeon**, **Tiny Mage: Endless Run**.
Her oyunun kendi sayfası, gizlilik politikası, kullanım şartları ve destek sayfası vardır (EN/TR, sayfa içi dil değiştirici).

## Linkler (App Store Connect / Google Play Console için)

| Oyun | Gizlilik | Şartlar | Destek |
|---|---|---|---|
| The Flipside | `/games/the-flipside/privacy/` | `/games/the-flipside/terms/` | `/games/the-flipside/support/` |
| Merge Survivors | `/games/merge-survivors/privacy/` | `/games/merge-survivors/terms/` | `/games/merge-survivors/support/` |
| Tiny Mage | `/games/tiny-mage/privacy/` | `/games/tiny-mage/terms/` | `/games/tiny-mage/support/` |

Hepsini tek yerden kopyalamak için: `/legal/`.
Eski adresler (`privacy.html?app=the-flipside-run`, `support.html`, `apps.html`) yeni sayfalara yönlendirilir.

## Yapı

- `tools/content.py` — tüm metinler (oyunlar, gizlilik, şartlar, SSS), EN + TR
- `tools/build.py` — sayfaları üretir: `python3 tools/build.py`
- `tools/make_og.py` — paylaşım görseli ve touch-icon (Pillow)
- `assets/style.css`, `assets/site.js` — tasarım sistemi ve küçük JS
- `assets/img/<oyun>/` — ikonlar ve ekran görüntüleri (WebP)
- `games/`, `legal/`, `index.html`, `404.html` — **üretilmiş çıktı**, elle düzenleme; `content.py` / `build.py` değiştirip yeniden üret.

## Yeni oyun ekleme

1. `assets/img/<slug>/icon.webp` (+ varsa `shot-en-N.webp`, `shot-tr-N.webp`) ekle.
2. `tools/content.py` içindeki `GAMES` listesine kayıt, `PRIVACY` ve `TERMS_CFG` içine girişleri ekle.
3. `python3 tools/build.py` çalıştır.

Yerel önizleme: `python3 -m http.server 8000` (kök dizinde).

## AdMob

`ads.txt` ve `app-ads.txt` kökte yayınlanır (AdMob doğrulaması).

## Yayın

Settings → Pages → Deploy from branch → `main` / `/ (root)`.
