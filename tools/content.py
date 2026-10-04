# -*- coding: utf-8 -*-
"""Site content: games, policies, terms, FAQs. Everything is bilingual (en / tr).

Edit this file, then run `python3 tools/build.py` to regenerate the static pages.
"""

SITE = "https://serhatbilal.github.io"
STUDIO = "Serhat Bilal Studio"
EMAIL = "serhat.bilal92@gmail.com"
GITHUB = "https://github.com/serhatBilal"
UPDATED_EN = "4 October 2026"
UPDATED_TR = "4 Ekim 2026"

MAIL = '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)

GAMES = [
    # ------------------------------------------------------------------ THE FLIPSIDE
    {
        "slug": "the-flipside",
        "name": "The Flipside",
        "store_name": "The Flipside Run",
        "accent": ("#ff3b4e", "#3b82f6"),
        "glow": "#ff3b4e",
        "status": "live",
        "status_en": "Available now",
        "status_tr": "Yayında",
        "store_url": "https://apps.apple.com/us/app/the-flipside-run/id6764400397",
        "platform": ("iPhone & iPad (iOS)", "iPhone ve iPad (iOS)"),
        "price": ("Free · optional rewarded ads", "Ücretsiz · isteğe bağlı ödüllü reklam"),
        "version": "1.1.14",
        "kind": ("Endless runner", "Sonsuz koşu"),
        "tagline": ("Flip between two worlds. Outrun the dark.",
                    "İki dünya arasında çevril. Karanlığı geride bırak."),
        "summary": (
            "A fast, moody endless runner on a cracked road between two dimensions. Dodge obstacles, spend mana to flip the world, chain your abilities and climb a worldwide leaderboard.",
            "İki boyut arasındaki çatlak yolda hızlı ve atmosferik bir sonsuz koşu. Engellerden kaç, dünyayı çevirmek için mana harca, yeteneklerini zincirle ve dünya çapındaki liderlik tablosuna tırman.",
        ),
        "tags": [("Endless runner", "Sonsuz koşu"), ("Arcade", "Arcade"), ("Leaderboard", "Liderlik tablosu"), ("EN · TR", "EN · TR")],
        "shots": {"count": 6, "home": [4, 2, 5]},
        "features": [
            ("🌀", ("Two dimensions", "İki boyut"),
             ("Flip between the Normal world and the Flipside. Flipping drains your mana, so time it well.",
              "Normal dünya ile Flipside arasında geçiş yap. Çevirmek mananı tüketir; zamanlamayı iyi seç.")),
            ("⚡", ("Abilities that matter", "Önemli yetenekler"),
             ("Turbo, magnet, phase, shield and more. Chain them to survive longer and score higher.",
              "Turbo, mıknatıs, hayalet, kalkan ve daha fazlası. Daha uzun hayatta kalmak ve daha yüksek skor için zincirle.")),
            ("🏃", ("Pick your runner", "Koşucunu seç"),
             ("Choose from several runners, each with their own look.",
              "Her biri kendi görünümüne sahip birkaç koşucu arasından seç.")),
            ("🏆", ("Global leaderboard", "Global liderlik tablosu"),
             ("Get a callsign and see how your best run ranks worldwide. Report or hide anyone you don't want to see.",
              "Bir çağrı adı al ve en iyi koşunun dünyada kaçıncı olduğunu gör. Görmek istemediğin oyuncuları şikayet et veya gizle.")),
            ("🔁", ("Instant restarts", "Anında yeniden deneme"),
             ("Short, intense runs. Fail, tap, and you're running again.",
              "Kısa ve yoğun koşular. Düş, dokun, yeniden koşuyorsun.")),
            ("🌍", ("English & Türkçe", "English ve Türkçe"),
             ("Switch the interface language any time in Settings.",
              "Arayüz dilini istediğin zaman Ayarlar'dan değiştir.")),
        ],
        "glance": [
            ("No account or email needed", "Hesap veya e-posta gerekmez"),
            ("Anonymous leaderboard ID + public callsign", "Anonim liderlik ID'si + herkese açık çağrı adı"),
            ("Optional rewarded ads (Google AdMob)", "İsteğe bağlı ödüllü reklamlar (Google AdMob)"),
            ("No precise location", "Hassas konum yok"),
            ("Not directed to children under 13", "13 yaş altı çocuklara yönelik değildir"),
        ],
        "faq": [
            (("How do I play?", "Nasıl oynanır?"),
             ("Swipe to change lanes and tap the on-screen ability buttons. Flip to the other dimension when the road ahead looks better on the other side — but watch your mana.",
              "Şerit değiştirmek için kaydır, ekrandaki yetenek düğmelerine dokun. Yol diğer boyutta daha iyi göründüğünde çevril — ama mananı gözle.")),
            (("Where is my progress stored?", "İlerlemem nerede saklanıyor?"),
             ("Progress, settings and unlocks are stored on your device. Your best score is also synced to the leaderboard when you are online. Deleting the game or resetting your phone without a backup removes local progress.",
              "İlerleme, ayarlar ve kilitler cihazında saklanır. En iyi skorun çevrimiçiyken liderlik tablosuna da gönderilir. Oyunu silmek veya telefonu yedeksiz sıfırlamak yerel ilerlemeyi siler.")),
            (("How do I change my callsign?", "Çağrı adımı nasıl değiştiririm?"),
             ("Open the player profile from the main menu, type a new callsign (up to 18 characters) and save. Offensive names are not accepted.",
              "Ana menüden oyuncu profilini aç, yeni bir çağrı adı yaz (en fazla 18 karakter) ve kaydet. Uygunsuz adlar kabul edilmez.")),
            (("How do I report or hide a player?", "Bir oyuncuyu nasıl şikayet eder veya gizlerim?"),
             ("On the leaderboard, tap Report next to the runner and pick a reason (offensive name, cheating, other). The runner is hidden for you right away and the report is sent for review.",
              "Liderlik tablosunda oyuncunun yanındaki Şikayet'e dokun ve bir neden seç (uygunsuz ad, hile, diğer). Oyuncu hemen senin için gizlenir ve şikayet incelenmek üzere gönderilir.")),
            (("How do I delete my leaderboard data?", "Liderlik tablosu verilerimi nasıl sildiririm?"),
             ("Email %s with your callsign and approximate best score. I will remove your leaderboard profile and entries." % MAIL,
              "Çağrı adın ve yaklaşık en iyi skorunla %s adresine e-posta gönder. Liderlik tablosu profilini ve kayıtlarını sileceğim." % MAIL)),
            (("How do rewarded ads work?", "Ödüllü reklamlar nasıl çalışır?"),
             ("Ads are optional. You can choose to watch a short video to continue a run. Nothing is forced and there are no ads while you are running.",
              "Reklamlar isteğe bağlıdır. Bir koşuya devam etmek için kısa bir video izlemeyi seçebilirsin. Hiçbir şey zorunlu değildir ve koşarken reklam gösterilmez.")),
        ],
        "credits": (
            "Ability icons by Lorc from game-icons.net (CC BY 3.0). Fonts: Playfair Display, VT323 and Oxanium (SIL Open Font License 1.1). Built with the Godot Engine.",
            "Yetenek ikonları: game-icons.net'ten Lorc (CC BY 3.0). Yazı tipleri: Playfair Display, VT323 ve Oxanium (SIL Open Font License 1.1). Godot Engine ile yapılmıştır.",
        ),
        "support_include": [
            ("App version (see the App Store page)", "Uygulama sürümü (App Store sayfasında görünür)"),
            ("Your iPhone/iPad model and iOS version", "iPhone/iPad modelin ve iOS sürümün"),
            ("What happened and what you expected", "Ne olduğu ve ne beklediğin"),
            ("For leaderboard issues: your callsign", "Liderlik tablosu sorunlarında: çağrı adın"),
        ],
        "meta_desc": ("The Flipside — a fast endless runner between two dimensions for iPhone. Privacy policy, terms and support.",
                      "The Flipside — iPhone için iki boyut arasında hızlı bir sonsuz koşu. Gizlilik politikası, şartlar ve destek."),
    },
    # ------------------------------------------------------------------ MERGE SURVIVORS
    {
        "slug": "merge-survivors",
        "name": "Merge Survivors: Dark Dungeon",
        "short": "Merge Survivors",
        "accent": ("#9b4dff", "#ff8a1f"),
        "glow": "#9b4dff",
        "status": "dev",
        "status_en": "In development",
        "status_tr": "Geliştiriliyor",
        "store_url": None,
        "platform": ("Android first · iOS later", "Önce Android · sonra iOS"),
        "price": ("Free to play", "Ücretsiz oynanır"),
        "version": "in development",
        "kind": ("Survivors-like action roguelite", "Survivors tarzı aksiyon roguelite"),
        "tagline": ("Enter weak. Merge loot. Kill the Hollow King.",
                    "Zayıf gir. Ganimeti birleştir. Hollow King'i öldür."),
        "summary": (
            "A dark-fantasy survivors-like for mobile. Move, auto-attack the horde, merge duplicate gear into higher rarities and descend into cursed dungeons, then rebuild your dying sanctuary between runs.",
            "Mobil için karanlık fantezi bir survivors oyunu. Hareket et, sürüye otomatik saldır, aynı eşyaları daha yüksek nadirliğe birleştir, lanetli zindanlara in; koşular arasında ölmekte olan sığınağını yeniden inşa et.",
        ),
        "tags": [("Survivors-like", "Survivors tarzı"), ("Loot & merge", "Ganimet ve birleştirme"), ("Roguelite", "Roguelite"), ("Portrait", "Dikey")],
        "shots": None,
        "features": [
            ("⚔️", ("Power fantasy in seconds", "Saniyeler içinde güç hissi"),
             ("Move with one thumb, attack automatically and feel stronger within the first thirty seconds.",
              "Tek başparmakla hareket et, otomatik saldır ve ilk otuz saniyede güçlendiğini hisset.")),
            ("🧩", ("Loot you can merge", "Birleştirebileceğin ganimet"),
             ("Collect gear mid-fight and merge duplicates into increasingly powerful rarities.",
              "Savaş sırasında ekipman topla ve aynı eşyaları giderek güçlenen nadirliklere birleştir.")),
            ("🔥", ("Elemental builds", "Elementsel yapılar"),
             ("Stack relics and weapons into absurd, run-defining builds.",
              "Kalıntıları ve silahları koşuyu belirleyen çılgın yapılara dönüştür.")),
            ("👑", ("Cinematic bosses", "Sinematik boss'lar"),
             ("Fight your way to the Hollow King — the thing that killed everyone else.",
              "Herkesi öldüren yaratık Hollow King'e giden yolu savaşarak aç.")),
            ("🏚️", ("A sanctuary to rebuild", "Yeniden kurulacak bir sığınak"),
             ("Spend what you earn between runs to restore the sanctuary and unlock permanent upgrades.",
              "Kazandıklarını koşular arasında sığınağı onarmak ve kalıcı yükseltmelerin kilidini açmak için harca.")),
            ("📱", ("Built for mobile", "Mobil için tasarlandı"),
             ("Portrait, short sessions, no account wall and no tutorial novel before you play.",
              "Dikey ekran, kısa oturumlar, zorunlu hesap yok ve oynamadan önce uzun bir eğitim yok.")),
        ],
        "glance": [
            ("Current build: no personal data collected", "Mevcut sürüm: kişisel veri toplanmaz"),
            ("Progress saved on your device", "İlerleme cihazında saklanır"),
            ("No account required", "Hesap gerekmez"),
            ("Policy updated before ads or analytics go live", "Reklam veya analiz açılmadan önce politika güncellenir"),
        ],
        "faq": [
            (("When is the game coming out?", "Oyun ne zaman çıkacak?"),
             ("It is still in development. Android comes first and iOS later. There is no release date yet — this page will announce it.",
              "Oyun hâlâ geliştirme aşamasında. Önce Android, sonra iOS gelecek. Henüz bir çıkış tarihi yok — duyuru bu sayfada yapılacak.")),
            (("Will it be free?", "Ücretsiz olacak mı?"),
             ("Yes, the plan is a free-to-play game with optional rewarded ads. Ads and analytics are not active in the current build.",
              "Evet, plan isteğe bağlı ödüllü reklamlı, ücretsiz oynanan bir oyun. Reklam ve analiz mevcut sürümde aktif değil.")),
            (("Do I need an account?", "Hesap gerekli mi?"),
             ("No. You will be able to play right away; progress is saved on your device.",
              "Hayır. Hemen oynayabileceksin; ilerleme cihazında saklanır.")),
            (("I found a bug or have feedback", "Hata buldum veya geri bildirimim var"),
             ("Please email %s with your device model and a short description. Feedback shapes the game." % MAIL,
              "Lütfen cihaz modelin ve kısa bir açıklamayla %s adresine yaz. Geri bildirimler oyunu şekillendirir." % MAIL)),
        ],
        "credits": (
            "Built with the Godot Engine.",
            "Godot Engine ile yapılmaktadır.",
        ),
        "support_include": [
            ("Your device model and Android/iOS version", "Cihaz modelin ve Android/iOS sürümün"),
            ("Build or version number, if you have one", "Varsa sürüm numarası"),
            ("What happened and what you expected", "Ne olduğu ve ne beklediğin"),
        ],
        "meta_desc": ("Merge Survivors: Dark Dungeon — a dark-fantasy mobile survivors-like in development. Privacy policy, terms and support.",
                      "Merge Survivors: Dark Dungeon — geliştirilmekte olan karanlık fantezi mobil survivors oyunu. Gizlilik politikası, şartlar ve destek."),
    },
    # ------------------------------------------------------------------ TINY MAGE
    {
        "slug": "tiny-mage",
        "name": "Tiny Mage: Endless Run",
        "short": "Tiny Mage",
        "accent": ("#8b5cf6", "#fbbf24"),
        "glow": "#a78bfa",
        "status": "soon",
        "status_en": "Coming to the App Store",
        "status_tr": "App Store'a geliyor",
        "store_url": None,
        "platform": ("iPhone (iOS 16+)", "iPhone (iOS 16+)"),
        "price": ("Free · no ads · no purchases", "Ücretsiz · reklam yok · satın alma yok"),
        "version": "1.0.0",
        "kind": ("Endless runner", "Sonsuz koşu"),
        "tagline": ("Cast spells. Smash monsters.", "Büyü yap, canavarları yen."),
        "summary": (
            "Race down a magical three-lane road as the tiniest apprentice at the Moonlit Academy. Dodge, cast spells, collect gold and relight the shattered Moon Lantern. No ads, no purchases, no account.",
            "Ay Işığı Akademisi'nin en minik çırağı olarak üç şeritli büyülü yolda yarış. Kaç, büyü at, altın topla ve paramparça olan Ay Feneri'ni yeniden yak. Reklam yok, satın alma yok, hesap yok.",
        ),
        "tags": [("Endless runner", "Sonsuz koşu"), ("Low-poly 3D", "Düşük poligonlu 3D"), ("Offline", "Çevrimdışı"), ("EN · TR", "EN · TR")],
        "shots": {"count": 7, "home": [3, 1, 5]},
        "features": [
            ("🏃", ("Run, dodge, cast", "Koş, kaç, büyü at"),
             ("Swipe to dodge between three lanes and hold your finger down to cast spells at everything in your way.",
              "Üç şerit arasında kaçmak için kaydır, yoluna çıkan her şeye büyü atmak için parmağını basılı tut.")),
            ("👻", ("Monsters to blast", "Yenilecek canavarlar"),
             ("Spiders, ghosts, golems and dark wizards come alone, in pairs and in long columns. Every one drops gold.",
              "Örümcekler, hayaletler, golemler ve kara büyücüler tek tek, ikişer ikişer ve uzun sıralar halinde gelir. Her biri altın bırakır.")),
            ("🌲", ("Five magical zones", "Beş büyülü bölge"),
             ("From the Moonlit Forest to the Peak, the sky, scenery and monsters change as you go. Then it loops, only faster.",
              "Ay Işığı Ormanı'ndan Tepe'ye kadar gökyüzü, dekor ve canavarlar değişir. Sonra başa sarar, ama daha hızlı.")),
            ("🧹", ("Magic items", "Sihirli eşyalar"),
             ("Flying Broom, Bubble Shield and Sleepy Sand turn a bad run around.",
              "Uçan Süpürge, Balon Kalkan ve Uyku Kumu kötü giden bir koşuyu tersine çevirir.")),
            ("✨", ("Upgrade your wand", "Asanı geliştir"),
             ("Spend gold between runs on Spell Power, Quick Wand and Lucky Star.",
              "Koşular arasında altınını Büyü Gücü, Hızlı Asa ve Şans Yıldızı'na harca.")),
            ("📖", ("Quests and a story", "Görevler ve bir hikâye"),
             ("Three quests are always waiting, and star shards unlock six chapters of the Moon Lantern story.",
              "Seni her zaman üç görev bekler; yıldız parçaları Ay Feneri hikâyesinin altı bölümünü açar.")),
        ],
        "glance": [
            ("Data not collected", "Veri toplanmaz"),
            ("No ads, no analytics, no tracking", "Reklam, analiz veya takip yok"),
            ("No account, no in-app purchases", "Hesap ve uygulama içi satın alma yok"),
            ("Works fully offline", "Tamamen çevrimdışı çalışır"),
        ],
        "faq": [
            (("How do I play?", "Nasıl oynanır?"),
             ("Swipe left or right to change lane and hold your finger on the screen to cast spells. Collect gold from defeated monsters and star shards from the road.",
              "Şerit değiştirmek için sağa veya sola kaydır, büyü atmak için parmağını ekranda basılı tut. Yenilen canavarlardan altın, yoldan yıldız parçası topla.")),
            (("My progress is gone.", "İlerlemem kayboldu."),
             ("Progress is stored only on your device. Deleting the game, or resetting the phone without a backup, removes it.",
              "İlerleme yalnızca cihazında saklanır. Oyunu silmek veya telefonu yedeksiz sıfırlamak onu da siler.")),
            (("How do I change the language?", "Dili nasıl değiştiririm?"),
             ("Tap the gear icon on the main menu and choose English or Türkçe.",
              "Ana menüde dişli simgesine dokun ve English veya Türkçe'yi seç.")),
            (("Are there ads or purchases?", "Reklam veya satın alma var mı?"),
             ("No. Gold is earned only by playing and has no connection to real money.",
              "Hayır. Altın yalnızca oynayarak kazanılır ve gerçek parayla bağlantısı yoktur.")),
        ],
        "credits": (
            "Built with the Godot Engine.",
            "Godot Engine ile yapılmıştır.",
        ),
        "support_include": [
            ("Your iPhone model and iOS version", "iPhone modelin ve iOS sürümün"),
            ("What happened and what you expected", "Ne olduğu ve ne beklediğin"),
            ("A screenshot, if it helps", "Yardımcı olacaksa bir ekran görüntüsü"),
        ],
        "meta_desc": ("Tiny Mage: Endless Run — a cute 3D endless runner for iPhone with no ads and no purchases. Privacy policy, terms and support.",
                      "Tiny Mage: Endless Run — iPhone için reklamsız ve satın almasız sevimli 3D sonsuz koşu. Gizlilik politikası, şartlar ve destek."),
    },
]

BY_SLUG = {g["slug"]: g for g in GAMES}


def _g(g):
    return g["short"] if g.get("short") else g["name"]


# =====================================================================================
# PRIVACY POLICIES
# each: dict(intro=(en,tr), callout=(title_en,title_tr,body_en,body_tr), sections=[(id,h_en,h_tr,body_en,body_tr)])
# =====================================================================================

GODOT_EN = '<a href="https://godotengine.org/privacy-policy" target="_blank" rel="noopener">Godot Engine</a>'

PRIVACY = {}

# ---------------- Tiny Mage
PRIVACY["tiny-mage"] = {
    "intro": (
        "Tiny Mage is a single-player game for iPhone made by an independent developer. This page explains what happens to your data when you play it.",
        "Tiny Mage, bağımsız bir geliştirici tarafından yapılmış, iPhone için tek oyunculu bir oyundur. Bu sayfa, oyunu oynarken verilerine ne olduğunu açıklar.",
    ),
    "callout": (
        "Short version", "Kısaca",
        "Tiny Mage does not collect, store on a server, share or sell any personal data. There is no account, no ads, no analytics, no in-app purchases and the game does not use the network.",
        "Tiny Mage hiçbir kişisel veriyi toplamaz, bir sunucuda saklamaz, paylaşmaz veya satmaz. Oyunda hesap, reklam, analiz aracı, uygulama içi satın alma yoktur ve ağ bağlantısı kullanılmaz.",
    ),
    "sections": [
        ("device", "What is stored on your device", "Cihazında saklananlar",
         "<p>To remember your progress, the game saves a small file on your iPhone: gold and star shards, upgrade levels, items, quest and story progress, best score and statistics, and your sound and language settings.</p><p>This file never leaves your device. It is deleted when you delete the game.</p>",
         "<p>İlerlemeni hatırlamak için oyun iPhone'unda küçük bir dosya tutar: altın ve yıldız parçaları, geliştirme seviyeleri, eşyalar, görev ve hikâye ilerlemesi, en iyi skor ve istatistikler ile ses ve dil ayarların.</p><p>Bu dosya cihazından hiç çıkmaz ve oyunu sildiğinde silinir.</p>"),
        ("not-collected", "What is not collected", "Toplanmayanlar",
         "<ul><li>No name, email address, phone number or other identifier</li><li>No location, contacts, photos, camera or microphone data</li><li>No advertising identifier and no tracking of any kind</li><li>No analytics or crash-reporting services</li></ul>",
         "<ul><li>Ad, e-posta, telefon numarası veya başka bir kimlik bilgisi</li><li>Konum, kişiler, fotoğraflar, kamera veya mikrofon verisi</li><li>Reklam kimliği ve herhangi bir takip</li><li>Analiz veya hata raporlama hizmetleri</li></ul>"),
        ("third", "Third parties", "Üçüncü taraflar",
         "<p>Tiny Mage includes no third-party advertising, analytics or social SDKs. It is built with the open-source %s, which does not send data anywhere from the game.</p>" % GODOT_EN,
         "<p>Tiny Mage üçüncü taraf reklam, analiz veya sosyal ağ SDK'sı içermez. Oyundan hiçbir yere veri göndermeyen, açık kaynaklı <a href=\"https://godotengine.org/privacy-policy\" target=\"_blank\" rel=\"noopener\">Godot</a> oyun motoruyla yapılmıştır.</p>"),
        ("children", "Children", "Çocuklar",
         "<p>The game is suitable for all ages. Because nothing is collected, there is no personal information from children to protect or delete.</p>",
         "<p>Oyun her yaştan oyuncuya uygundur. Hiçbir şey toplanmadığı için çocuklara ait korunacak veya silinecek kişisel bilgi yoktur.</p>"),
        ("rights", "Your rights and deleting your data", "Haklarının kullanımı ve verilerin silinmesi",
         "<p>Since I hold no personal data about you, there is nothing to access, correct or delete on my side. You can erase everything the game stores by deleting it from your iPhone. If you still have a privacy question or request (for example under GDPR or the Turkish KVKK), write to me at %s." % MAIL + "</p>",
         "<p>Hakkında kişisel veri tutmadığım için benim tarafımda erişilecek, düzeltilecek veya silinecek bir şey yoktur. Oyunun sakladığı her şeyi oyunu iPhone'undan silerek kaldırabilirsin. Yine de bir gizlilik sorun veya talebin varsa (örneğin GDPR veya KVKK kapsamında) bana %s adresinden yaz.</p>" % MAIL),
        ("changes", "Changes to this policy", "Bu politikadaki değişiklikler",
         "<p>If this ever changes (for example if ads are added in a future version), this page and the App Privacy details on the App Store will be updated before that version is released.</p>",
         "<p>İleride bu durum değişirse (örneğin sonraki bir sürüme reklam eklenirse), o sürüm yayınlanmadan önce bu sayfa ve App Store'daki Uygulama Gizliliği bilgileri güncellenir.</p>"),
        ("contact", "Contact", "İletişim",
         "<p>Questions about privacy: %s</p>" % MAIL,
         "<p>Gizlilik soruları için: %s</p>" % MAIL),
    ],
}

# ---------------- The Flipside
PRIVACY["the-flipside"] = {
    "intro": (
        "This policy applies to The Flipside mobile game (also listed on the App Store as “The Flipside Run”), made by Serhat Bilal (“the developer”). It explains what information the game uses, why, and what choices you have.",
        "Bu politika, Serhat Bilal (“geliştirici”) tarafından yapılan The Flipside mobil oyunu için geçerlidir (App Store'da “The Flipside Run” adıyla da listelenir). Oyunun hangi bilgileri neden kullandığını ve hangi seçeneklere sahip olduğunu açıklar.",
    ),
    "callout": (
        "Short version", "Kısaca",
        "No account or email is needed. Your progress stays on your device. If you use the online leaderboard, an anonymous ID and a public callsign are stored with your best score. Optional rewarded ads are served by Google AdMob. No precise location is collected.",
        "Hesap veya e-posta gerekmez. İlerlemen cihazında kalır. Çevrimiçi liderlik tablosunu kullanırsan, en iyi skorunla birlikte anonim bir ID ve herkese açık bir çağrı adı saklanır. İsteğe bağlı ödüllü reklamları Google AdMob sunar. Hassas konum toplanmaz.",
    ),
    "sections": [
        ("collect", "Information the game uses", "Oyunun kullandığı bilgiler",
         """<h3>Stored only on your device</h3>
<p>Progress, best score, coins and shards, unlocked and selected runner, settings (sound, language) and the list of leaderboard runners you have hidden. This data stays on your device and is removed when you uninstall the game.</p>
<h3>Leaderboard profile (when you are online)</h3>
<p>The game signs you in anonymously using Google Firebase Authentication, which creates a random user ID that is not linked to your name or email. To take part in the leaderboard the game stores in Google Cloud Firestore:</p>
<ul><li>your anonymous user ID</li><li>your callsign (public name — generated for you, and editable up to 18 characters)</li><li>your best score, longest distance and number of games played</li><li>the runner you selected and timestamps of updates</li></ul>
<p><strong>Public:</strong> your callsign, best score, distance and runner are visible to other players on the leaderboard. Please do not put personal information in your callsign.</p>
<h3>Reports</h3>
<p>If you report a leaderboard entry, the game sends the reported runner's ID and callsign, your anonymous ID and the reason you chose, so the report can be reviewed. Hiding a runner is stored only on your device.</p>
<h3>Advertising</h3>
<p>The game can offer optional rewarded video ads (for example to continue a run) through Google AdMob. Google may collect and use device and advertising identifiers, IP address, device and app information and ad interaction data to deliver, measure and secure ads. Where required by law (for example in the EEA and the UK), the game asks for your consent through Google's User Messaging Platform before ads are requested.</p>
<h3>Not collected</h3>
<p>The game does not collect your name, email address, phone number, precise location, contacts, photos, camera or microphone data, and does not use AI to process your data.</p>
<h3>Technical data</h3>
<p>Like any online service, Google's servers used by the leaderboard and ads receive your IP address and basic device information as part of normal network requests.</p>""",
         """<h3>Yalnızca cihazında saklananlar</h3>
<p>İlerleme, en iyi skor, jeton ve parçalar, açılan ve seçili koşucu, ayarlar (ses, dil) ve gizlediğin liderlik tablosu oyuncularının listesi. Bu veriler cihazında kalır ve oyunu kaldırdığında silinir.</p>
<h3>Liderlik tablosu profili (çevrimiçiyken)</h3>
<p>Oyun, Google Firebase Authentication ile seni anonim olarak oturum açtırır; bu işlem adına veya e-postana bağlı olmayan rastgele bir kullanıcı ID'si oluşturur. Liderlik tablosuna katılabilmen için oyun Google Cloud Firestore'da şunları saklar:</p>
<ul><li>anonim kullanıcı ID'n</li><li>çağrı adın (herkese açık ad — sana otomatik üretilir ve en fazla 18 karakter olacak şekilde düzenlenebilir)</li><li>en iyi skorun, en uzun mesafen ve oynadığın oyun sayısı</li><li>seçtiğin koşucu ve güncelleme zamanları</li></ul>
<p><strong>Herkese açık:</strong> çağrı adın, en iyi skorun, mesafen ve koşucun liderlik tablosunda diğer oyunculara görünür. Lütfen çağrı adına kişisel bilgi yazma.</p>
<h3>Şikayetler</h3>
<p>Bir liderlik tablosu kaydını şikayet edersen oyun, şikayet edilen oyuncunun ID ve çağrı adını, anonim ID'ni ve seçtiğin nedeni inceleme için gönderir. Bir oyuncuyu gizlemek yalnızca cihazında saklanır.</p>
<h3>Reklamlar</h3>
<p>Oyun, Google AdMob aracılığıyla isteğe bağlı ödüllü video reklamlar (örneğin bir koşuya devam etmek için) sunabilir. Google; reklamları sunmak, ölçmek ve güvenliğini sağlamak için cihaz ve reklam kimliklerini, IP adresini, cihaz ve uygulama bilgilerini ve reklam etkileşim verilerini toplayıp kullanabilir. Yasaların gerektirdiği yerlerde (örneğin AEA ve Birleşik Krallık) reklamlar istenmeden önce oyun, Google'ın Kullanıcı Mesajlaşma Platformu (UMP) üzerinden onayını ister.</p>
<h3>Toplanmayanlar</h3>
<p>Oyun adını, e-posta adresini, telefon numaranı, hassas konumunu, kişilerini, fotoğraflarını, kamera veya mikrofon verini toplamaz ve verilerini işlemek için yapay zekâ kullanmaz.</p>
<h3>Teknik veriler</h3>
<p>Her çevrimiçi hizmet gibi, liderlik tablosu ve reklamlar için kullanılan Google sunucuları normal ağ istekleri kapsamında IP adresini ve temel cihaz bilgilerini alır.</p>"""),
        ("use", "How the information is used", "Bilgilerin kullanımı",
         "<ul><li>To run the leaderboard and show your best run</li><li>To review reports and keep the leaderboard fair (offensive names, cheating)</li><li>To show optional rewarded ads and measure them</li><li>To keep the game working, fix problems and prevent abuse</li><li>To reply when you contact the developer</li></ul><p>Your information is not sold.</p>",
         "<ul><li>Liderlik tablosunu işletmek ve en iyi koşunu göstermek</li><li>Şikayetleri incelemek ve liderlik tablosunu adil tutmak (uygunsuz adlar, hile)</li><li>İsteğe bağlı ödüllü reklamları göstermek ve ölçmek</li><li>Oyunun çalışmasını sağlamak, sorunları gidermek ve kötüye kullanımı önlemek</li><li>Geliştiriciyle iletişime geçtiğinde yanıt vermek</li></ul><p>Bilgilerin satılmaz.</p>"),
        ("third", "Third-party services", "Üçüncü taraf hizmetler",
         """<p>The game uses third-party services that have their own privacy policies:</p>
<ul><li><a href="https://firebase.google.com/support/privacy" target="_blank" rel="noopener">Google Firebase</a> (Authentication, Cloud Firestore) — anonymous sign-in and leaderboard</li><li><a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">Google AdMob</a> and <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Privacy Policy</a> — rewarded ads and consent</li><li><a href="https://godotengine.org/privacy-policy" target="_blank" rel="noopener">Godot Engine</a> — the open-source game engine</li><li>Apple App Store — distribution; Apple's own privacy practices apply to your store account</li></ul>""",
         """<p>Oyun, kendi gizlilik politikaları olan üçüncü taraf hizmetler kullanır:</p>
<ul><li><a href="https://firebase.google.com/support/privacy" target="_blank" rel="noopener">Google Firebase</a> (Authentication, Cloud Firestore) — anonim giriş ve liderlik tablosu</li><li><a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">Google AdMob</a> ve <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Gizlilik Politikası</a> — ödüllü reklamlar ve onay</li><li><a href="https://godotengine.org/privacy-policy" target="_blank" rel="noopener">Godot Engine</a> — açık kaynaklı oyun motoru</li><li>Apple App Store — dağıtım; mağaza hesabın için Apple'ın kendi gizlilik uygulamaları geçerlidir</li></ul>"""),
        ("sharing", "Sharing and disclosure", "Paylaşım ve ifşa",
         "<p>Your information is shared only with the service providers above, who process it on the developer's behalf or as independent providers under their own terms, and in these cases:</p><ul><li>when required by law, subpoena or similar legal process;</li><li>when disclosure is necessary in good faith to protect rights, safety, investigate fraud or respond to a government request.</li></ul>",
         "<p>Bilgilerin yalnızca yukarıdaki hizmet sağlayıcılarla (geliştirici adına veya kendi şartları çerçevesinde bağımsız olarak işleyenler) ve şu durumlarda paylaşılır:</p><ul><li>yasa, mahkeme celbi veya benzeri yasal süreç gerektirdiğinde;</li><li>hakları ve güvenliği korumak, dolandırıcılığı araştırmak veya resmi bir talebe yanıt vermek için iyi niyetle gerekli olduğunda.</li></ul>"),
        ("retention", "Retention and deletion", "Saklama ve silme",
         "<p>Local data stays on your device until you uninstall the game. Leaderboard profile data is kept while your profile is active and for a reasonable period afterwards. Because the leaderboard uses an anonymous ID, uninstalling does not by itself remove your online entry — to have it deleted, email %s with your callsign and approximate best score and I will remove it within a reasonable time.</p>" % MAIL,
         "<p>Yerel veriler, oyunu kaldırana kadar cihazında kalır. Liderlik tablosu profil verileri profilin aktif olduğu sürece ve sonrasında makul bir süre saklanır. Liderlik tablosu anonim bir ID kullandığı için oyunu kaldırmak çevrimiçi kaydını kendiliğinden silmez — sildirmek için çağrı adın ve yaklaşık en iyi skorunla %s adresine e-posta gönder; makul bir süre içinde sileceğim.</p>" % MAIL),
        ("choices", "Your choices and rights", "Seçeneklerin ve haklarının",
         "<ul><li>Change your callsign any time, or choose not to open the leaderboard.</li><li>Hide or report runners you do not want to see.</li><li>Ads are optional — you can simply not watch them. Manage ad tracking in iOS <em>Settings → Privacy &amp; Security → Tracking</em> and through the consent form where it is shown.</li><li>Uninstall the game to stop all collection on your device.</li><li>You may ask to access, correct or delete your data, or object to its processing (for example under GDPR or the Turkish KVKK). Email %s.</li></ul>" % MAIL,
         "<ul><li>Çağrı adını istediğin zaman değiştir veya liderlik tablosunu hiç açma.</li><li>Görmek istemediğin oyuncuları gizle veya şikayet et.</li><li>Reklamlar isteğe bağlıdır — izlemeyebilirsin. Reklam takibini iOS <em>Ayarlar → Gizlilik ve Güvenlik → İzleme</em> bölümünden ve gösterildiği yerlerde onay formundan yönetebilirsin.</li><li>Cihazındaki tüm veri toplamayı durdurmak için oyunu kaldır.</li><li>Verilerine erişmeyi, düzeltmeyi veya silmeyi ya da işlenmesine itiraz etmeyi (örneğin GDPR veya KVKK kapsamında) talep edebilirsin. %s adresine yaz.</li></ul>" % MAIL),
        ("children", "Children", "Çocuklar",
         "<p>The game is not directed to children under 13 and the developer does not knowingly collect personal information from them. If you are a parent or guardian and believe your child has provided information through the leaderboard, contact %s and it will be deleted.</p>" % MAIL,
         "<p>Oyun 13 yaşın altındaki çocuklara yönelik değildir ve geliştirici onlardan bilerek kişisel bilgi toplamaz. Ebeveyn veya veliysen ve çocuğunun liderlik tablosu aracılığıyla bilgi sağladığını düşünüyorsan %s adresiyle iletişime geç; bilgiler silinecektir.</p>" % MAIL),
        ("security", "Security and international transfers", "Güvenlik ve uluslararası aktarım",
         "<p>Reasonable technical and organisational measures are used to protect information. Google may process data on servers in countries other than yours; Google's safeguards apply. No method of transmission or storage is perfectly secure.</p>",
         "<p>Bilgileri korumak için makul teknik ve idari önlemler kullanılır. Google verileri senin ülken dışındaki ülkelerde bulunan sunucularda işleyebilir; Google'ın güvenceleri geçerlidir. Hiçbir iletim veya saklama yöntemi tamamen güvenli değildir.</p>"),
        ("changes", "Changes to this policy", "Bu politikadaki değişiklikler",
         "<p>This policy may be updated from time to time. Changes are posted on this page with a new date. Continued use after a change means you accept the updated policy. Effective: %s.</p>" % UPDATED_EN,
         "<p>Bu politika zaman zaman güncellenebilir. Değişiklikler yeni bir tarihle bu sayfada yayımlanır. Değişiklikten sonra kullanmaya devam etmen, güncellenmiş politikayı kabul ettiğin anlamına gelir. Yürürlük tarihi: %s.</p>" % UPDATED_TR),
        ("contact", "Contact", "İletişim",
         "<p>Questions about privacy or this policy: %s</p>" % MAIL,
         "<p>Gizlilik veya bu politikayla ilgili sorular için: %s</p>" % MAIL),
    ],
}

# ---------------- Merge Survivors
PRIVACY["merge-survivors"] = {
    "intro": (
        "This policy applies to Merge Survivors: Dark Dungeon, a mobile game made by Serhat Bilal (“the developer”) that is currently in development. It explains how the game treats your information.",
        "Bu politika, Serhat Bilal (“geliştirici”) tarafından yapılan ve şu anda geliştirilmekte olan Merge Survivors: Dark Dungeon mobil oyunu için geçerlidir. Oyunun bilgilerini nasıl ele aldığını açıklar.",
    ),
    "callout": (
        "Short version", "Kısaca",
        "In its current build the game collects no personal data, needs no account and keeps your progress only on your device. Rewarded ads and anonymous analytics are planned; this policy will be updated — and the store privacy answers with it — before either goes live.",
        "Oyun mevcut sürümünde kişisel veri toplamaz, hesap gerektirmez ve ilerlemeni yalnızca cihazında tutar. Ödüllü reklamlar ve anonim analiz planlanmaktadır; bunlardan biri devreye girmeden önce bu politika — ve onunla birlikte mağaza gizlilik cevapları — güncellenecektir.",
    ),
    "sections": [
        ("device", "What is stored on your device", "Cihazında saklananlar",
         "<p>The game saves a small file on your device: your meta-progression (sanctuary upgrades, currencies, unlocked items), settings and run statistics. This file stays on your device and is deleted when you uninstall the game.</p>",
         "<p>Oyun cihazında küçük bir dosya saklar: meta ilerlemen (sığınak yükseltmeleri, para birimleri, açılan eşyalar), ayarların ve koşu istatistikleri. Bu dosya cihazında kalır ve oyunu kaldırdığında silinir.</p>"),
        ("not-collected", "What is not collected", "Toplanmayanlar",
         "<ul><li>No name, email address, phone number or account</li><li>No location, contacts, photos, camera or microphone data</li><li>No advertising identifier and no tracking in the current build</li></ul>",
         "<ul><li>Ad, e-posta adresi, telefon numarası veya hesap</li><li>Konum, kişiler, fotoğraflar, kamera veya mikrofon verisi</li><li>Mevcut sürümde reklam kimliği ve takip yok</li></ul>"),
        ("planned", "Planned features: ads and analytics", "Planlanan özellikler: reklam ve analiz",
         "<p>The game is designed to be free to play. Before release the developer may add:</p><ul><li><strong>Rewarded ads</strong> (for example to double a run reward) through Google AdMob. Google may use device and advertising identifiers, IP address and ad interaction data to deliver and measure ads; where required, you will be asked for consent first. Ads are always optional.</li><li><strong>Anonymous gameplay analytics</strong> (for example run start and end, dungeon, level reached, merges and boss events) to balance and improve the game. No names or contact details are part of these events.</li></ul><p>None of this is active in the current build. If it is added, this page and the app-store privacy information will be updated <strong>before</strong> that version is released.</p>",
         "<p>Oyun ücretsiz oynanacak şekilde tasarlanmıştır. Yayından önce geliştirici şunları ekleyebilir:</p><ul><li>Google AdMob aracılığıyla <strong>ödüllü reklamlar</strong> (örneğin bir koşu ödülünü ikiye katlamak için). Google, reklamları sunmak ve ölçmek için cihaz ve reklam kimliklerini, IP adresini ve reklam etkileşim verilerini kullanabilir; gerektiğinde önce onayın istenir. Reklamlar her zaman isteğe bağlıdır.</li><li>Oyunu dengelemek ve geliştirmek için <strong>anonim oynanış analizi</strong> (örneğin koşu başlangıç ve bitişi, zindan, ulaşılan seviye, birleştirmeler ve boss olayları). Bu olaylarda ad veya iletişim bilgisi yer almaz.</li></ul><p>Bunların hiçbiri mevcut sürümde aktif değildir. Eklenirse, bu sayfa ve mağaza gizlilik bilgileri o sürüm yayınlanmadan <strong>önce</strong> güncellenecektir.</p>"),
        ("third", "Third parties", "Üçüncü taraflar",
         "<p>The current build contains no third-party advertising, analytics or social SDKs. It is built with the open-source %s, which does not send data anywhere from the game.</p>" % GODOT_EN,
         "<p>Mevcut sürüm üçüncü taraf reklam, analiz veya sosyal ağ SDK'sı içermez. Oyundan hiçbir yere veri göndermeyen, açık kaynaklı <a href=\"https://godotengine.org/privacy-policy\" target=\"_blank\" rel=\"noopener\">Godot</a> oyun motoruyla yapılmıştır.</p>"),
        ("children", "Children", "Çocuklar",
         "<p>The game is not directed to children under 13 and the developer does not knowingly collect personal information from them. If you believe a child has provided information, contact %s and it will be deleted.</p>" % MAIL,
         "<p>Oyun 13 yaşın altındaki çocuklara yönelik değildir ve geliştirici onlardan bilerek kişisel bilgi toplamaz. Bir çocuğun bilgi sağladığını düşünüyorsan %s adresiyle iletişime geç; bilgiler silinecektir.</p>" % MAIL),
        ("rights", "Your rights and deleting your data", "Haklarının kullanımı ve verilerin silinmesi",
         "<p>You can erase everything the game stores by uninstalling it. You may also ask to access, correct or delete any data held about you, or object to its processing (for example under GDPR or the Turkish KVKK), by writing to %s.</p>" % MAIL,
         "<p>Oyunun sakladığı her şeyi oyunu kaldırarak silebilirsin. Hakkında tutulan verilere erişmeyi, düzeltmeyi veya silmeyi ya da işlenmesine itiraz etmeyi (örneğin GDPR veya KVKK kapsamında) %s adresine yazarak talep edebilirsin.</p>" % MAIL),
        ("changes", "Changes to this policy", "Bu politikadaki değişiklikler",
         "<p>This policy may be updated, in particular when ads or analytics are added. Changes are posted on this page with a new date. Effective: %s.</p>" % UPDATED_EN,
         "<p>Bu politika, özellikle reklam veya analiz eklendiğinde güncellenebilir. Değişiklikler yeni bir tarihle bu sayfada yayımlanır. Yürürlük tarihi: %s.</p>" % UPDATED_TR),
        ("contact", "Contact", "İletişim",
         "<p>Questions about privacy: %s</p>" % MAIL,
         "<p>Gizlilik soruları için: %s</p>" % MAIL),
    ],
}


# =====================================================================================
# TERMS OF USE (generated from per-game switches)
# =====================================================================================

TERMS_CFG = {
    "the-flipside": dict(store="apple", currency=("coins, shards and other in-game items", "jetonlar, parçalar ve diğer oyun içi öğeler"),
                         ads="rewarded", leaderboard=True),
    "merge-survivors": dict(store="both", currency=("currencies, loot and other in-game items", "para birimleri, ganimetler ve diğer oyun içi öğeler"),
                            ads="planned", leaderboard=False),
    "tiny-mage": dict(store="apple", currency=("gold, star shards and other in-game items", "altın, yıldız parçaları ve diğer oyun içi öğeler"),
                      ads="none", leaderboard=False),
}


def terms_sections(slug):
    g = BY_SLUG[slug]
    c = TERMS_CFG[slug]
    n = g["name"]
    cur_en, cur_tr = c["currency"]
    s = []

    s.append(("accept", "Acceptance of these terms", "Şartların kabulü",
              "<p>These Terms of Use form an agreement between you and Serhat Bilal (“the developer”) for %s (“the game”). By downloading, installing or playing the game you agree to them. If you do not agree, please do not use the game.</p>" % n,
              "<p>Bu Kullanım Şartları, sen ve Serhat Bilal (“geliştirici”) arasında %s (“oyun”) için bir sözleşme oluşturur. Oyunu indirerek, yükleyerek veya oynayarak bu şartları kabul etmiş olursun. Kabul etmiyorsan lütfen oyunu kullanma.</p>" % n))

    store_en = ""
    store_tr = ""
    if c["store"] in ("apple", "both"):
        store_en += " If you obtained the game from the Apple App Store, Apple's Licensed Application End User License Agreement also applies. Apple is not a party to these terms and is not responsible for the game or its support."
        store_tr += " Oyunu Apple App Store'dan edindiysen Apple'ın Lisanslı Uygulama Son Kullanıcı Lisans Sözleşmesi de geçerlidir. Apple bu şartların tarafı değildir ve oyundan veya desteğinden sorumlu değildir."
    if c["store"] in ("google", "both"):
        store_en += " If you obtained the game from Google Play, Google Play's terms of service also apply."
        store_tr += " Oyunu Google Play'den edindiysen Google Play hizmet şartları da geçerlidir."
    s.append(("license", "License", "Lisans",
              "<p>The developer grants you a limited, personal, non-exclusive, non-transferable and revocable license to install and play the game on devices you own or control, for your own non-commercial entertainment.%s</p>" % store_en,
              "<p>Geliştirici sana, oyunu sahibi olduğun veya kontrol ettiğin cihazlara yüklemek ve kendi ticari olmayan eğlencen için oynamak üzere sınırlı, kişisel, münhasır olmayan, devredilemez ve geri alınabilir bir lisans verir.%s</p>" % store_tr))

    s.append(("use", "Acceptable use", "Kabul edilebilir kullanım",
              "<p>You agree not to:</p><ul><li>copy, modify, decompile, reverse-engineer or extract assets from the game, except where the law allows it;</li><li>cheat, exploit bugs, use bots, scripts or tampered builds, or interfere with the game's or its services' normal operation;</li><li>sell, rent, sublicense or redistribute the game or its content;</li><li>use the game for any unlawful purpose.</li></ul>",
              "<p>Şunları yapmamayı kabul edersin:</p><ul><li>yasanın izin verdiği durumlar dışında oyunu kopyalamak, değiştirmek, kaynak koda çevirmek, tersine mühendislik yapmak veya içeriklerini çıkarmak;</li><li>hile yapmak, hatalardan faydalanmak, bot, betik veya değiştirilmiş sürümler kullanmak ya da oyunun veya hizmetlerinin normal işleyişine müdahale etmek;</li><li>oyunu veya içeriğini satmak, kiralamak, alt lisanslamak veya yeniden dağıtmak;</li><li>oyunu yasa dışı bir amaçla kullanmak.</li></ul>"))

    s.append(("items", "In-game items", "Oyun içi öğeler",
              "<p>%s have no real-world value, cannot be exchanged for money or transferred, and may be adjusted, reset or lost (for example through an update, a bug or loss of your device data). The game is %s</p>" % (
                  cur_en[0].upper() + cur_en[1:],
                  "free to play and contains no in-app purchases at this time." if slug != "merge-survivors" else "planned as free to play; if purchases are ever added, these terms and the store listing will say so before release."),
              "<p>%s gerçek dünyada bir değere sahip değildir, paraya çevrilemez veya devredilemez; ayrıca bir güncelleme, hata veya cihaz verisi kaybı gibi nedenlerle ayarlanabilir, sıfırlanabilir veya kaybolabilir. Oyun %s</p>" % (
                  cur_tr[0].upper() + cur_tr[1:],
                  "ücretsiz oynanır ve şu anda uygulama içi satın alma içermez." if slug != "merge-survivors" else "ücretsiz oynanacak şekilde planlanmıştır; ileride satın alma eklenirse bu şartlar ve mağaza sayfası bunu yayından önce belirtecektir.")))

    if c["ads"] == "rewarded":
        s.append(("ads", "Ads", "Reklamlar",
                  "<p>The game may show optional rewarded video ads provided by Google AdMob. Watching them is your choice. Ads are provided by third parties; the developer is not responsible for their content. How ad data is handled is described in the <a href=\"../privacy/\">Privacy Policy</a>.</p>",
                  "<p>Oyun, Google AdMob tarafından sağlanan isteğe bağlı ödüllü video reklamlar gösterebilir. Bunları izlemek senin tercihindir. Reklamlar üçüncü taraflarca sağlanır; geliştirici içeriklerinden sorumlu değildir. Reklam verilerinin nasıl işlendiği <a href=\"../privacy/\">Gizlilik Politikası</a>'nda açıklanmıştır.</p>"))
    elif c["ads"] == "planned":
        s.append(("ads", "Ads", "Reklamlar",
                  "<p>The game is planned to offer optional rewarded ads. They are not active in the current build. If added, watching them will always be your choice, and data handling will be described in the <a href=\"../privacy/\">Privacy Policy</a> before release.</p>",
                  "<p>Oyunda isteğe bağlı ödüllü reklamlar sunulması planlanmaktadır. Mevcut sürümde aktif değildir. Eklenirse izlemek her zaman senin tercihin olacak ve veri işleme yayından önce <a href=\"../privacy/\">Gizlilik Politikası</a>'nda açıklanacaktır.</p>"))
    else:
        s.append(("ads", "No ads", "Reklam yok",
                  "<p>The game contains no advertising. If that ever changes, these terms and the <a href=\"../privacy/\">Privacy Policy</a> will be updated before the change is released.</p>",
                  "<p>Oyun reklam içermez. Bu durum değişirse, değişiklik yayınlanmadan önce bu şartlar ve <a href=\"../privacy/\">Gizlilik Politikası</a> güncellenecektir.</p>"))

    if c["leaderboard"]:
        s.append(("leaderboard", "Leaderboard and callsigns", "Liderlik tablosu ve çağrı adları",
                  "<p>The leaderboard is public. Your callsign must not be offensive, hateful, sexual, impersonate someone or contain personal information. Scores obtained by cheating or tampering may be removed. The developer may change or remove a callsign, hide or delete entries, and reset or remove a profile at any time to keep the leaderboard fair. You can report other runners from the leaderboard.</p>",
                  "<p>Liderlik tablosu herkese açıktır. Çağrı adın saldırgan, nefret içerikli, cinsel içerikli olmamalı, başkasını taklit etmemeli ve kişisel bilgi içermemelidir. Hile veya müdahaleyle elde edilen skorlar kaldırılabilir. Geliştirici, liderlik tablosunu adil tutmak için bir çağrı adını değiştirebilir veya kaldırabilir, kayıtları gizleyebilir veya silebilir, bir profili istediği zaman sıfırlayabilir veya kaldırabilir. Liderlik tablosundan diğer oyuncuları şikayet edebilirsin.</p>"))

    cred_en, cred_tr = g["credits"]
    s.append(("ip", "Intellectual property and credits", "Fikri mülkiyet ve atıflar",
              "<p>The game, including its code, art, music, sound and design, is owned by the developer or used under license and is protected by copyright and other laws. These terms give you no ownership of any of it. Third-party components remain under their own licenses. %s</p>" % cred_en,
              "<p>Kodu, görselleri, müziği, sesleri ve tasarımı dahil oyun, geliştiriciye aittir veya lisansla kullanılmaktadır ve telif hakkı ile diğer yasalarla korunur. Bu şartlar sana bunların hiçbirinin mülkiyetini vermez. Üçüncü taraf bileşenler kendi lisansları kapsamında kalır. %s</p>" % cred_tr))

    s.append(("third", "Third-party services", "Üçüncü taraf hizmetler",
              "<p>The game may depend on third-party platforms and services (for example app stores%s). Their availability and terms are outside the developer's control.</p>" % (
                  ", Google Firebase and Google AdMob" if slug == "the-flipside" else (" and, in the future, ad and analytics providers" if slug == "merge-survivors" else "")),
              "<p>Oyun, üçüncü taraf platform ve hizmetlere (örneğin uygulama mağazaları%s) bağlı olabilir. Bunların erişilebilirliği ve şartları geliştiricinin kontrolü dışındadır.</p>" % (
                  ", Google Firebase ve Google AdMob" if slug == "the-flipside" else (" ve ileride reklam ve analiz sağlayıcıları" if slug == "merge-survivors" else ""))))

    s.append(("updates", "Updates and availability", "Güncellemeler ve erişilebilirlik",
              "<p>The game may be updated, changed, suspended or discontinued at any time. Updates may be required to keep playing. The developer does not promise that the game will be available without interruption or free of errors.</p>",
              "<p>Oyun istediği zaman güncellenebilir, değiştirilebilir, askıya alınabilir veya sonlandırılabilir. Oynamaya devam etmek için güncelleme gerekebilir. Geliştirici, oyunun kesintisiz veya hatasız olacağını taahhüt etmez.</p>"))

    s.append(("termination", "Termination", "Fesih",
              "<p>You may stop using the game at any time by uninstalling it. The developer may restrict or end your access if you breach these terms. Sections that by their nature should survive termination (such as intellectual property, disclaimers and limitation of liability) will survive.</p>",
              "<p>Oyunu kaldırarak istediğin zaman kullanmayı bırakabilirsin. Bu şartları ihlal edersen geliştirici erişimini kısıtlayabilir veya sonlandırabilir. Niteliği gereği fesihten sonra da geçerli olması gereken bölümler (fikri mülkiyet, sorumluluk reddi ve sorumluluğun sınırlandırılması gibi) geçerliliğini korur.</p>"))

    s.append(("warranty", "Disclaimer of warranties", "Garanti reddi",
              "<p>To the extent permitted by law, the game is provided “as is” and “as available”, without warranties of any kind, express or implied, including fitness for a particular purpose and non-infringement. Nothing here limits rights you have under mandatory consumer law.</p>",
              "<p>Yasaların izin verdiği ölçüde oyun, belirli bir amaca uygunluk ve ihlal etmeme dahil açık veya zımni hiçbir garanti olmaksızın “olduğu gibi” ve “mevcut haliyle” sunulur. Buradaki hiçbir hüküm, emredici tüketici mevzuatından doğan haklarını sınırlamaz.</p>"))

    s.append(("liability", "Limitation of liability", "Sorumluluğun sınırlandırılması",
              "<p>To the extent permitted by law, the developer is not liable for indirect, incidental or consequential damages, or for loss of data, progress or in-game items, arising from your use of the game. Where liability cannot be excluded, it is limited to the amount you paid for the game, which for a free game is zero. Nothing excludes liability that cannot be excluded by law.</p>",
              "<p>Yasaların izin verdiği ölçüde geliştirici, oyunu kullanmandan kaynaklanan dolaylı, arızi veya sonuç olarak ortaya çıkan zararlardan ya da veri, ilerleme veya oyun içi öğe kaybından sorumlu değildir. Sorumluluğun hariç tutulamadığı hâllerde, sorumluluk oyun için ödediğin tutarla sınırlıdır; ücretsiz bir oyun için bu tutar sıfırdır. Yasayla hariç tutulamayan sorumluluk hiçbir şekilde hariç tutulmaz.</p>"))

    s.append(("law", "Governing law", "Uygulanacak hukuk",
              "<p>These terms are governed by the laws of the Republic of Türkiye. Consumers keep the benefit of the mandatory consumer-protection rules of their country of residence, and the competence of consumer courts and arbitration committees under applicable law is not affected.</p>",
              "<p>Bu şartlar Türkiye Cumhuriyeti hukukuna tabidir. Tüketiciler, yerleşik oldukları ülkenin emredici tüketici koruma kurallarından yararlanmaya devam eder; yürürlükteki mevzuata göre tüketici mahkemeleri ve hakem heyetlerinin yetkisi saklıdır.</p>"))

    s.append(("changes", "Changes to these terms", "Şartlardaki değişiklikler",
              "<p>These terms may be updated from time to time. The new version is posted on this page with a new date, and continued use of the game after a change means you accept it. Effective: %s.</p>" % UPDATED_EN,
              "<p>Bu şartlar zaman zaman güncellenebilir. Yeni sürüm yeni bir tarihle bu sayfada yayımlanır ve değişiklikten sonra oyunu kullanmaya devam etmen, değişikliği kabul ettiğin anlamına gelir. Yürürlük tarihi: %s.</p>" % UPDATED_TR))

    s.append(("contact", "Contact", "İletişim",
              "<p>Questions about these terms: %s</p>" % MAIL,
              "<p>Bu şartlarla ilgili sorular için: %s</p>" % MAIL))
    return s


TERMS_INTRO = (
    "Please read these terms before you play. They are short and written to be understood.",
    "Oynamadan önce lütfen bu şartları oku. Kısadır ve anlaşılır olacak şekilde yazılmıştır.",
)
