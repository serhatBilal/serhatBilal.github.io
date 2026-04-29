(function () {
  const data = window.APP_PORTFOLIO;
  const params = new URLSearchParams(window.location.search);
  const requestedLang = params.get("lang");
  const storedLang = window.localStorage.getItem("siteLang");
  const lang = requestedLang === "tr" || requestedLang === "en" ? requestedLang : storedLang || "en";
  const page = document.body.dataset.page || "home";
  const selectedSlug = params.get("app") || data.apps[0].slug;
  const selectedApp = data.apps.find((app) => app.slug === selectedSlug) || data.apps[0];

  const dictionary = {
    en: {
      navHome: "Home",
      navApps: "Apps",
      navCreator: "Creator",
      navPrivacy: "Privacy",
      navSupport: "Support",
      homeEyebrow: "Independent mobile developer",
      homeTitle: "<span>Mobile games and</span><span>useful apps,</span><span>built with care.</span>",
      homeText:
        "I build focused iOS and Android apps with clean support and privacy pages for every release.",
      homePrimary: "View Apps",
      visualStatus: "Building",
      avatarRole: "Software Developer",
      craftEyebrow: "What I build",
      craftTitle: "Small products with a complete release mindset.",
      craftText:
        "A good app is not only the binary uploaded to a store. It also needs a clear home, a real support path, and policy pages users can trust.",
      craftCardOneTitle: "Mobile Games",
      craftCardOneText: "Fast, replayable, touch-friendly game ideas for mobile players.",
      craftCardTwoTitle: "Useful Apps",
      craftCardTwoText: "Lean mobile tools with direct flows and simple maintenance.",
      craftCardThreeTitle: "Release Pages",
      craftCardThreeText: "Each app gets its own support and privacy policy links.",
      featuredEyebrow: "Featured app",
      featuredText: "A quick mobile game release focused on reflex, timing, and smooth arcade flow.",
      featuredAppsButton: "App Details",
      factPlatform: "Platform",
      factCategory: "Category",
      factGame: "Mobile Game",
      factPages: "Pages",
      factReady: "Support + Privacy",
      creatorEyebrow: "Creator",
      creatorText:
        "Software developer based in Bursa, building across back-end, mobile, Flutter, .NET and Python. This site is the public home for current and upcoming mobile releases.",
      creatorAppsButton: "Explore Apps",
      appsEyebrow: "Apps and games",
      appsTitle: "Released products, support links, and privacy pages.",
      appsText:
        "Every app has its own store link, support page, and privacy policy. New releases will appear here as the portfolio grows.",
      appStore: "App Store",
      privacyPolicy: "Privacy Policy",
      support: "Support",
      status: "Status",
      platform: "Platform",
      lastUpdated: "Last updated:",
      privacyEyebrow: "Privacy Policy",
      privacyInfoTitle: "Information We Process",
      privacyInfoText:
        "The app may process limited technical information required to operate core gameplay, improve stability, measure performance, show advertising, and respond to support requests.",
      privacyThirdTitle: "Advertising and Third-Party Services",
      privacyThirdText:
        "Some apps may use third-party services such as Google AdMob. These services may process data according to their own policies.",
      privacyChildrenTitle: "Children's Privacy",
      privacyChildrenText:
        "Our apps are not designed to knowingly collect personal information from children. If you are a parent or guardian and believe that a child has provided personal information, please contact us.",
      privacySecurityTitle: "Data Security",
      privacySecurityText:
        "We use reasonable technical and administrative measures to protect information. No internet transmission or storage method is completely secure.",
      privacyContactTitle: "Contact",
      privacyContactText: "For privacy questions or requests, contact us at",
      supportEyebrow: "Support",
      supportEmailTitle: "Email Support",
      supportEmailText:
        "Include the app name, device model, operating system version and a short description of the issue.",
      supportEmailButton: "Send support email",
      supportTopicsTitle: "Common Topics",
      supportIntro:
        "Need help with {app}? Send a support request with your device model, app version, and a short description of the issue.",
    },
    tr: {
      navHome: "Ana Sayfa",
      navApps: "Uygulamalar",
      navCreator: "Geliştirici",
      navPrivacy: "Gizlilik",
      navSupport: "Destek",
      homeEyebrow: "Bağımsız mobil geliştirici",
      homeTitle: "<span>Özenle geliştirilen</span><span>mobil oyunlar ve uygulamalar.</span>",
      homeText:
        "Her yayın için temiz destek ve gizlilik sayfalarıyla iOS ve Android uygulamaları geliştiriyorum.",
      homePrimary: "Uygulamaları Gör",
      visualStatus: "Üretimde",
      avatarRole: "Yazılım Geliştirici",
      craftEyebrow: "Ne üretiyorum",
      craftTitle: "Yayın sürecini tamamlayan küçük ürünler.",
      craftText:
        "İyi bir uygulama sadece markete yüklenen dosya değildir. Güven veren bir ana sayfa, gerçek bir destek yolu ve net politika sayfaları da gerekir.",
      craftCardOneTitle: "Mobil Oyunlar",
      craftCardOneText: "Mobil oyuncular için hızlı, tekrar oynanabilir ve dokunmatik dostu oyun fikirleri.",
      craftCardTwoTitle: "Faydalı Uygulamalar",
      craftCardTwoText: "Doğrudan akışlara ve kolay bakıma sahip yalın mobil araçlar.",
      craftCardThreeTitle: "Yayın Sayfaları",
      craftCardThreeText: "Her uygulama kendi destek ve gizlilik politikası bağlantılarına sahip olur.",
      featuredEyebrow: "Öne çıkan uygulama",
      featuredText: "Refleks, zamanlama ve akıcı arcade hissi üzerine kurulu hızlı bir mobil oyun yayını.",
      featuredAppsButton: "Uygulama Detayı",
      factPlatform: "Platform",
      factCategory: "Kategori",
      factGame: "Mobil Oyun",
      factPages: "Sayfalar",
      factReady: "Destek + Gizlilik",
      creatorEyebrow: "Geliştirici",
      creatorText:
        "Bursa merkezli yazılım geliştirici. Back-end, mobile, Flutter, .NET ve Python tarafında üretim yapıyor. Bu site mevcut ve gelecek mobil yayınların resmi evidir.",
      creatorAppsButton: "Uygulamaları İncele",
      appsEyebrow: "Uygulamalar ve oyunlar",
      appsTitle: "Yayınlanan ürünler, destek bağlantıları ve gizlilik sayfaları.",
      appsText:
        "Her uygulamanın kendi market bağlantısı, destek sayfası ve gizlilik politikası vardır. Yeni yayınlar portföy büyüdükçe burada görünecek.",
      appStore: "App Store",
      privacyPolicy: "Gizlilik Politikası",
      support: "Destek",
      status: "Durum",
      platform: "Platform",
      lastUpdated: "Son güncelleme:",
      privacyEyebrow: "Gizlilik Politikası",
      privacyInfoTitle: "İşlenen Bilgiler",
      privacyInfoText:
        "Uygulama; temel oyun deneyimini çalıştırmak, kararlılığı artırmak, performansı ölçmek, reklam göstermek ve destek taleplerine yanıt vermek için sınırlı teknik bilgiler işleyebilir.",
      privacyThirdTitle: "Reklamlar ve Üçüncü Taraf Servisleri",
      privacyThirdText:
        "Bazı uygulamalar Google AdMob gibi üçüncü taraf servisleri kullanabilir. Bu servisler verileri kendi politikalarına göre işleyebilir.",
      privacyChildrenTitle: "Çocukların Gizliliği",
      privacyChildrenText:
        "Uygulamalarımız bilerek çocuklardan kişisel bilgi toplamak için tasarlanmaz. Bir ebeveyn veya veli olarak çocuğun kişisel bilgi sağladığını düşünüyorsanız bizimle iletişime geçin.",
      privacySecurityTitle: "Veri Güvenliği",
      privacySecurityText:
        "Bilgileri korumak için makul teknik ve idari önlemler kullanırız. Hiçbir internet aktarımı veya saklama yöntemi tamamen güvenli değildir.",
      privacyContactTitle: "İletişim",
      privacyContactText: "Gizlilik soruları veya talepleri için bize şu adresten ulaşabilirsiniz:",
      supportEyebrow: "Destek",
      supportEmailTitle: "E-posta Desteği",
      supportEmailText:
        "Uygulama adı, cihaz modeli, işletim sistemi sürümü ve sorunun kısa açıklamasını ekleyin.",
      supportEmailButton: "Destek e-postası gönder",
      supportTopicsTitle: "Sık Görülen Konular",
      supportIntro:
        "{app} için yardıma mı ihtiyacınız var? Cihaz modeliniz, uygulama sürümünüz ve sorunun kısa açıklamasıyla destek talebi gönderebilirsiniz.",
    },
  };

  const t = (key) => dictionary[lang][key] || dictionary.en[key] || key;
  const localize = (value) => {
    if (!value || typeof value !== "object") return value || "";
    return value[lang] || value.en || "";
  };

  const makeUrl = (path, options = {}) => {
    const urlParams = new URLSearchParams();
    urlParams.set("lang", lang);
    if (options.app) urlParams.set("app", options.app);
    const hash = options.hash || "";
    return `${path}?${urlParams.toString()}${hash}`;
  };

  window.localStorage.setItem("siteLang", lang);
  document.documentElement.lang = lang;

  document.querySelectorAll("[data-i18n]").forEach((element) => {
    element.textContent = t(element.dataset.i18n);
  });

  document.querySelectorAll("[data-i18n-html]").forEach((element) => {
    element.innerHTML = t(element.dataset.i18nHtml);
  });

  document.querySelectorAll("[data-lang-option]").forEach((link) => {
    const nextLang = link.dataset.langOption;
    const nextParams = new URLSearchParams(window.location.search);
    nextParams.set("lang", nextLang);
    link.href = `${window.location.pathname}?${nextParams.toString()}${window.location.hash}`;
    link.classList.toggle("active", nextLang === lang);
  });

  document.querySelectorAll("[data-page-link]").forEach((link) => {
    const target = link.dataset.pageLink;
    if (target === "home") link.href = makeUrl("index.html");
    if (target === "apps") link.href = makeUrl("apps.html");
    if (target === "creator") link.href = makeUrl("index.html", { hash: "#creator" });
    if (target === "privacy") link.href = makeUrl("privacy.html", { app: selectedApp.slug });
    if (target === "support") link.href = makeUrl("support.html", { app: selectedApp.slug });
  });

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  const appGrid = document.getElementById("appGrid");
  if (appGrid) {
    appGrid.innerHTML = data.apps
      .map((app) => {
        const initials = app.name
          .split(" ")
          .slice(0, 2)
          .map((word) => word.charAt(0).toUpperCase())
          .join("");
        return `
          <article class="app-card-item" id="${app.slug}">
            <div class="app-card-head">
              <div class="app-art" aria-hidden="true">${initials}</div>
              <span class="app-state">${localize(app.status)}</span>
            </div>
            <span class="app-badge">${localize(app.type)}</span>
            <h3>${app.name}</h3>
            <p>${localize(app.summary)}</p>
            <dl class="app-meta">
              <div>
                <dt>${t("platform")}</dt>
                <dd>${app.platform}</dd>
              </div>
              <div>
                <dt>${t("status")}</dt>
                <dd>${localize(app.status)}</dd>
              </div>
            </dl>
            <div class="app-links">
              ${
                app.appStoreUrl
                  ? `<a href="${app.appStoreUrl}" target="_blank" rel="noopener">${t("appStore")}</a>`
                  : ""
              }
              <a href="${makeUrl("privacy.html", { app: app.slug })}">${t("privacyPolicy")}</a>
              <a href="${makeUrl("support.html", { app: app.slug })}">${t("support")}</a>
            </div>
          </article>
        `;
      })
      .join("");
  }

  const policyTitle = document.getElementById("policyTitle");
  const policyIntro = document.getElementById("policyIntro");
  const policyContent = document.getElementById("policyContent");
  const lastUpdated = document.getElementById("lastUpdated");
  const practiceList = document.getElementById("practiceList");
  const privacyEmail = document.getElementById("privacyEmail");

  if (policyTitle) policyTitle.textContent = localize(selectedApp.privacyTitle) || `${selectedApp.name} ${t("privacyPolicy")}`;
  if (policyIntro) policyIntro.textContent = localize(selectedApp.privacyNotes);
  if (policyContent && selectedApp.privacyPolicyHtml) {
    policyContent.innerHTML = localize(selectedApp.privacyPolicyHtml);
  }
  if (lastUpdated) lastUpdated.textContent = localize(data.lastUpdated);
  if (practiceList) {
    practiceList.innerHTML = localize(selectedApp.dataPractices)
      .map((item) => `<li>${item}</li>`)
      .join("");
  }
  if (privacyEmail) {
    privacyEmail.href = `mailto:${data.supportEmail}?subject=${encodeURIComponent(
      `${selectedApp.name} privacy request`,
    )}`;
    privacyEmail.textContent = data.supportEmail;
  }

  const supportTitle = document.getElementById("supportTitle");
  const supportIntro = document.getElementById("supportIntro");
  const supportEmail = document.getElementById("supportEmail");
  const supportTopics = document.getElementById("supportTopics");

  if (supportTitle) supportTitle.textContent = `${selectedApp.name} ${t("support")}`;
  if (supportIntro) supportIntro.textContent = t("supportIntro").replace("{app}", selectedApp.name);
  if (supportEmail) {
    supportEmail.href = `mailto:${data.supportEmail}?subject=${encodeURIComponent(
      `${selectedApp.name} support request`,
    )}`;
  }
  if (supportTopics) {
    supportTopics.innerHTML = localize(selectedApp.supportTopics)
      .map((item) => `<li>${item}</li>`)
      .join("");
  }
})();
