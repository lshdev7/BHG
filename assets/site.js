(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---- text size (remembered per browser, optional) ---- */
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function setSize(n) {
    document.body.classList.remove("size-0", "size-1", "size-2");
    document.body.classList.add("size-" + n);
    $$(".ts button").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-size") === String(n)); });
    store("bhg-size", String(n));
  }
  var saved = store("bhg-size");
  setSize(saved === "0" || saved === "2" ? saved : "1");
  $$(".ts button").forEach(function (b) {
    b.addEventListener("click", function () { setSize(b.getAttribute("data-size")); });
  });

  /* ---- mega menu ---- */
  var tabs = $$(".tab");
  function closeAll() {
    tabs.forEach(function (t) { t.setAttribute("aria-expanded", "false"); });
    $$(".mm-panel").forEach(function (p) { p.hidden = true; });
  }
  tabs.forEach(function (t) {
    t.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = t.getAttribute("aria-expanded") === "true";
      closeAll();
      if (!open) {
        t.setAttribute("aria-expanded", "true");
        $("#" + t.getAttribute("data-panel")).hidden = false;
      }
    });
  });
  document.addEventListener("click", function (e) { if (!e.target.closest(".nav")) closeAll(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeAll(); });
  var burger = $(".burger");
  burger.addEventListener("click", function () {
    var o = $("#nav").classList.toggle("open");
    burger.setAttribute("aria-expanded", String(o));
  });

  /* ---- banner carousel ---- */
  var slides = $$(".slide"), dots = $$(".dot"), cur = 0, timer = null;
  function show(n) {
    cur = (n + slides.length) % slides.length;
    slides.forEach(function (s, i) { s.hidden = i !== cur; });
    dots.forEach(function (d, i) { d.classList.toggle("on", i === cur); });
  }
  function play() {
    if (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    stop(); timer = setInterval(function () { show(cur + 1); }, 6000);
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }
  $(".prev").addEventListener("click", function () { show(cur - 1); });
  $(".next").addEventListener("click", function () { show(cur + 1); });
  dots.forEach(function (d) { d.addEventListener("click", function () { show(+d.getAttribute("data-i")); }); });
  var banner = $(".banner");
  banner.addEventListener("mouseenter", stop); banner.addEventListener("mouseleave", play);
  banner.addEventListener("focusin", stop); banner.addEventListener("focusout", play);
  play();

  /* ---- placeholder links ---- */
  var toastEl = $("#toast"), toastT = null;
  function toast(msg) {
    toastEl.textContent = msg; toastEl.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.hidden = true; }, 2200);
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[href='#']");
    if (a) { e.preventDefault(); toast(document.body.getAttribute("data-toast")); }
  });

  /* ---- search over the links on this page ---- */
  var seen = {};
  var index = $$("a[data-s]").map(function (a) { return a.textContent.trim(); })
    .filter(function (t) { if (!t || seen[t]) return false; seen[t] = 1; return true; });
  $("#sf").addEventListener("submit", function (e) {
    e.preventDefault();
    var q = $("#q").value.trim().toLowerCase(), box = $("#results"), list = $("#results-list");
    list.textContent = "";
    if (!q) { box.hidden = true; return; }
    var hits = index.filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
    if (!hits.length) {
      var li = document.createElement("li"); li.textContent = document.body.getAttribute("data-nores"); list.appendChild(li);
    } else {
      hits.forEach(function (t) {
        var li = document.createElement("li"), a = document.createElement("a");
        a.href = "#"; a.textContent = t; li.appendChild(a); list.appendChild(li);
      });
    }
    box.hidden = false;
    box.scrollIntoView({ block: "nearest" });
  });

  $("#totop").addEventListener("click", function (e) { e.preventDefault(); window.scrollTo(0, 0); });
})();
