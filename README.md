# Serhat Bilal Studio

GitHub Pages uyumlu kişisel developer/studio sitesi.

Site yapısı:

- `index.html`: English-first developer landing page
- `apps.html`: Uygulama ve oyun listesi
- `privacy.html?app=the-flipside-run&lang=en`: Uygulama bazlı privacy policy
- `support.html?app=the-flipside-run&lang=en`: Uygulama bazlı support sayfası
- `app-ads.txt`: AdMob app doğrulama dosyası

## Yeni uygulama ekleme

`assets/app-data.js` dosyasındaki `apps` listesine yeni bir kayıt ekle:

```js
{
  slug: "my-new-game",
  name: "My New Game",
  type: {
    en: "Mobile Game",
    tr: "Mobil Oyun"
  },
  platform: "iOS and Android",
  status: {
    en: "Available",
    tr: "Yayında"
  },
  appStoreUrl: "https://apps.apple.com/...",
  tagline: {
    en: "Short English tagline.",
    tr: "Kısa Türkçe slogan."
  },
  summary: {
    en: "English app summary.",
    tr: "Türkçe uygulama özeti."
  },
  privacyNotes: {
    en: "App-specific privacy summary in English.",
    tr: "Uygulamaya özel Türkçe gizlilik özeti."
  },
  dataPractices: {
    en: ["Advertising may be provided through Google AdMob."],
    tr: ["Reklam gösterimi Google AdMob üzerinden sağlanabilir."]
  },
  supportTopics: {
    en: ["Bug reports and performance issues"],
    tr: ["Hata bildirimi ve performans sorunları"]
  }
}
```

Marketlerde kullanabileceğin adresler:

- Apps page: `https://kullanici-adin.github.io/repo-adi/apps.html`
- Privacy Policy: `https://kullanici-adin.github.io/repo-adi/privacy.html?app=my-new-game&lang=en`
- Support: `https://kullanici-adin.github.io/repo-adi/support.html?app=my-new-game&lang=en`

## AdMob

Mobil uygulamalar için AdMob'un beklediği dosya kök dizindeki `app-ads.txt` dosyasıdır:

```txt
google.com, pub-3384203635424437, DIRECT, f08c47fec0942fa0
```

Bu dosya site arayüzünde görünmez; sadece doğrulama için kökte yayınlanır.

## GitHub Pages

Bu proje build gerektirmeyen statik bir sitedir.

1. Dosyaları GitHub reposuna gönder.
2. Repository `Settings > Pages` bölümüne gir.
3. Source olarak `Deploy from a branch`, branch olarak `main`, folder olarak `/root` seç.
4. Yayına çıkan domaini App Store Connect, Google Play Console ve AdMob alanlarında kullan.
