(function () {
  var root = document.documentElement;
  root.classList.remove("no-js");

  function store(key, val) {
    try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); } catch (e) {}
    return null;
  }

  // ---- language ----
  function setLang(lang, persist) {
    if (lang !== "en" && lang !== "tr") lang = "en";
    root.setAttribute("lang", lang);
    if (persist) store("sbs-lang", lang);
    document.title = (document.documentElement.getAttribute("data-title-" + lang)) || document.title;
    var url = new URL(location.href);
    if (url.searchParams.has("lang")) {
      url.searchParams.set("lang", lang);
      history.replaceState(null, "", url.toString());
    }
  }
  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.getAttribute("data-set"), true); });
  });
  // keep ?lang= when moving between pages
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href^='/']");
    if (!a) return;
    var q = new URL(location.href).searchParams.get("lang");
    if (q && !/[?&]lang=/.test(a.getAttribute("href"))) {
      var u = new URL(a.href); u.searchParams.set("lang", q); a.href = u.toString();
    }
  });
  var titled = document.documentElement.getAttribute("data-title-" + root.getAttribute("lang"));
  if (titled) document.title = titled;

  // ---- mobile menu ----
  var mb = document.querySelector(".menu-btn"), nl = document.querySelector(".nav-links");
  if (mb && nl) {
    mb.addEventListener("click", function () {
      var open = nl.classList.toggle("open");
      mb.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nl.addEventListener("click", function (e) { if (e.target.tagName === "A") nl.classList.remove("open"); });
  }

  // ---- reveal on scroll ----
  var rv = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add("in"); }); }

  // ---- TOC scroll-spy ----
  var tocLinks = document.querySelectorAll(".toc a");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove("on"); });
          var a = map[en.target.id]; if (a) a.classList.add("on");
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    document.querySelectorAll(".doc section[id]").forEach(function (s) { spy.observe(s); });
  }

  // ---- copy buttons ----
  document.querySelectorAll(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () {
        btn.classList.add("ok");
        var old = btn.innerHTML; btn.innerHTML = "✓";
        setTimeout(function () { btn.classList.remove("ok"); btn.innerHTML = old; }, 1400);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, done);
      else {
        var t = document.createElement("textarea"); t.value = text; document.body.appendChild(t); t.select();
        try { document.execCommand("copy"); } catch (e) {} document.body.removeChild(t); done();
      }
    });
  });

  // ---- subtle pointer parallax on hero stack ----
  var stack = document.querySelector(".stack");
  if (stack && window.matchMedia("(hover: hover)").matches && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    stack.addEventListener("pointermove", function (e) {
      var r = stack.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
      stack.querySelectorAll("a").forEach(function (a, i) {
        var d = (i + 1) * 8; a.style.marginLeft = (x * d) + "px"; a.style.marginTop = (y * d) + "px";
      });
    });
    stack.addEventListener("pointerleave", function () { stack.querySelectorAll("a").forEach(function (a) { a.style.marginLeft = ""; a.style.marginTop = ""; }); });
  }

  // ---- year ----
  document.querySelectorAll(".year").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
