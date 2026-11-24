(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---- text size: cycles small / normal / large ---- */
  function setSize(n) {
    document.body.classList.remove("size-0", "size-1", "size-2");
    document.body.classList.add("size-" + n);
    store("bhg-size", String(n));
  }
  var sv = store("bhg-size");
  setSize(sv === "0" || sv === "2" ? sv : "1");
  var tsb = $("#textsize");
  if (tsb) tsb.addEventListener("click", function () {
    var cur = document.body.classList.contains("size-2") ? 2 : document.body.classList.contains("size-0") ? 0 : 1;
    setSize(cur === 1 ? 2 : cur === 2 ? 0 : 1);
  });

  /* ---- language menu ---- */
  var lb = $(".lg-btn"), lm = $("#langmenu");
  if (lb) {
    lb.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = lm.hidden; lm.hidden = !open; lb.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("click", function () { lm.hidden = true; lb.setAttribute("aria-expanded", "false"); });
  }

  /* ---- mega menu (inner header links open the panel on hover/focus, navigate on click) ---- */
  var panels = $$(".mm"), hideT = null;
  function place(p) {
    var h = $(".ihead") || $(".hhead");
    p.style.top = (h.getBoundingClientRect().bottom + window.pageYOffset) + "px";
  }
  function closeMM() { panels.forEach(function (p) { p.hidden = true; }); }
  $$("[data-mm]").forEach(function (a) {
    function open() {
      clearTimeout(hideT); closeMM();
      var p = document.getElementById(a.getAttribute("data-mm"));
      if (p) { place(p); p.hidden = false; }
    }
    a.addEventListener("mouseenter", open);
    a.addEventListener("focus", open);
  });
  panels.forEach(function (p) {
    p.addEventListener("mouseenter", function () { clearTimeout(hideT); });
    p.addEventListener("mouseleave", function () { hideT = setTimeout(closeMM, 250); });
  });
  $$(".ihead .inav, .tabs").forEach(function (n) {
    n.addEventListener("mouseleave", function () { hideT = setTimeout(closeMM, 250); });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMM(); });
  // home tabs: also open the category panel when hovering a tab
  $$(".tabs a").forEach(function (a) {
    var m = /t-(residents|business|nonresidents)/.exec(a.className);
    if (!m) return;
    a.addEventListener("mouseenter", function () {
      clearTimeout(hideT); closeMM();
      var p = document.getElementById("mm-" + m[1]);
      if (p) { place(p); p.hidden = false; }
    });
  });

  /* ---- mobile menu ---- */
  var burger = $(".burger");
  if (burger) burger.addEventListener("click", function () {
    var p = document.getElementById("mm-residents");
    var show = p.hidden; closeMM(); if (show) { place(p); p.hidden = false; }
  });

  /* ---- search ---- */
  var seen = {}, index = [];
  $$("main a, .side a, .mm a").forEach(function (a) {
    var t = a.textContent.trim().replace(/\s+/g, " ");
    if (t && !seen[t] && a.getAttribute("href") && a.getAttribute("href") !== "#") { seen[t] = 1; index.push({ t: t, h: a.getAttribute("href") }); }
  });
  var res = $("#results"), rlist = $("#rlist");
  var anchor = $(".ihead") || $(".hhead");
  if (res && anchor) anchor.parentNode.insertBefore(res, anchor.nextSibling);
  $$(".sform").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var q = f.querySelector("input").value.trim().toLowerCase();
      rlist.textContent = "";
      if (!q) { res.hidden = true; return; }
      var hits = index.filter(function (x) { return x.t.toLowerCase().indexOf(q) !== -1; }).slice(0, 40);
      if (!hits.length) {
        var li = document.createElement("li"); li.textContent = (window.BHG && window.BHG.nores) || ""; rlist.appendChild(li);
      } else hits.forEach(function (x) {
        var li = document.createElement("li"), a = document.createElement("a");
        a.href = x.h; a.textContent = x.t; li.appendChild(a); rlist.appendChild(li);
      });
      res.hidden = false;
    });
  });
  var is = $("#isearch"), isw = $("#isearch-w");
  if (is) is.addEventListener("click", function () {
    isw.hidden = !isw.hidden; if (!isw.hidden) $("#q").focus();
  });

  /* ---- carousels (scroll-snap tracks with a dot pill) ---- */
  function carousel(trackSel, dotSel, nextSel, auto) {
    var tr = $(trackSel), dots = $(dotSel);
    if (!tr || !dots) return;
    var items = $$(":scope > *", tr);
    var step = function () { return items.length > 1 ? items[1].offsetLeft - items[0].offsetLeft : tr.clientWidth; };
    var pages = function () { return Math.max(1, Math.min(items.length, Math.ceil((tr.scrollWidth - tr.clientWidth) / step()) + 1)); };
    function draw() {
      var n = pages(), cur = Math.round(tr.scrollLeft / step());
      dots.textContent = "";
      for (var i = 0; i < n; i++) {
        var b = document.createElement("button");
        b.type = "button"; b.setAttribute("aria-label", String(i + 1));
        if (i === Math.min(cur, n - 1)) b.className = "on";
        (function (k) { b.addEventListener("click", function () { tr.scrollTo({ left: k * step(), behavior: "smooth" }); }); })(i);
        dots.appendChild(b);
      }
    }
    tr.addEventListener("scroll", function () { clearTimeout(tr._t); tr._t = setTimeout(draw, 80); });
    window.addEventListener("resize", draw);
    draw();
    var nx = nextSel && $(nextSel);
    if (nx) nx.addEventListener("click", function () {
      var end = tr.scrollLeft + tr.clientWidth >= tr.scrollWidth - 4;
      tr.scrollTo({ left: end ? 0 : tr.scrollLeft + step() * 2, behavior: "smooth" });
    });
    if (auto && !(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches)) {
      var timer = setInterval(function () {
        var end = tr.scrollLeft + tr.clientWidth >= tr.scrollWidth - 4;
        tr.scrollTo({ left: end ? 0 : tr.scrollLeft + step(), behavior: "smooth" });
      }, 6000);
      ["mouseenter", "focusin", "touchstart"].forEach(function (ev) { tr.addEventListener(ev, function () { clearInterval(timer); }); });
    }
  }
  carousel("#cards", "#cdots", null, true);
  carousel("#ftrack", "#fdots", "#fnext", false);

  /* ---- accordion (travel documents) ---- */
  $$(".acc-h").forEach(function (b) {
    b.addEventListener("click", function () {
      var open = b.getAttribute("aria-expanded") === "true";
      b.setAttribute("aria-expanded", String(!open));
      document.getElementById(b.getAttribute("aria-controls")).hidden = open;
    });
  });

  /* ---- guidebook tabs, live clock, share links ---- */
  var gtabs = $$(".gtb");
  function showTab(id) {
    gtabs.forEach(function (b) {
      var on = b.getAttribute("data-tab") === id;
      b.classList.toggle("on", on); b.setAttribute("aria-selected", String(on));
    });
    $$(".gtab").forEach(function (p) { p.hidden = p.id !== id; });
  }
  gtabs.forEach(function (b) { b.addEventListener("click", function () { showTab(b.getAttribute("data-tab")); }); });
  var clocks = $$("[data-clock]");
  function tick() {
    var d = new Date(), z = function (n) { return (n < 10 ? "0" : "") + n; };
    var t = z(d.getHours()) + ":" + z(d.getMinutes()) + ":" + z(d.getSeconds());
    clocks.forEach(function (c) { c.textContent = t; });
  }
  if (clocks.length) { tick(); setInterval(tick, 1000); }
  var SH = {
    fb: "https://www.facebook.com/sharer/sharer.php?u=", tw: "https://twitter.com/intent/tweet?url=",
    wb: "https://service.weibo.com/share/share.php?url=", wa: "https://wa.me/?text=",
    ln: "https://social-plugins.line.me/lineit/share?url=", wc: "https://api.qrserver.com/v1/create-qr-code/?size=240x240&data="
  };
  $$("[data-share]").forEach(function (a) {
    a.target = "_blank"; a.rel = "noopener";
    a.addEventListener("click", function () { a.href = SH[a.getAttribute("data-share")] + encodeURIComponent(location.href); });
  });

  /* ---- FAQ accordion ---- */
  $$(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () {
      var open = q.getAttribute("aria-expanded") === "true";
      q.setAttribute("aria-expanded", String(!open));
      q.nextElementSibling.hidden = open;
    });
  });
  $$("[data-faq]").forEach(function (b) {
    b.addEventListener("click", function () {
      var open = b.getAttribute("data-faq") === "open";
      $$(".faq-q").forEach(function (q) { q.setAttribute("aria-expanded", String(open)); q.nextElementSibling.hidden = !open; });
    });
  });

  /* ---- government form catalogue: tabs, expand all, search ---- */
  $$(".cat-tabs button").forEach(function (b) {
    b.addEventListener("click", function () {
      $$(".cat-tabs button").forEach(function (x) { x.classList.toggle("on", x === b); });
      $$(".cat-p").forEach(function (p) { p.hidden = p.getAttribute("data-cp") !== b.getAttribute("data-ct"); });
    });
  });
  $$("[data-cea]").forEach(function (b) {
    b.addEventListener("click", function () {
      var ds = $$(".cat-p:not([hidden]) details"), open = ds.some(function (d) { return !d.open; });
      ds.forEach(function (d) { d.open = open; });
    });
  });
  var cq = $("#catq");
  function catSearch() {
    var q = cq.value.trim().toLowerCase(), box = $("#catres"), seen = {};
    box.textContent = "";
    if (!q) { box.hidden = true; $("#catnone").hidden = true; return; }
    var ul = document.createElement("ul");
    $$(".cat-p li[data-k]").forEach(function (li) {
      var k = li.getAttribute("data-k"), a = li.querySelector("a");
      if (k.indexOf(q) !== -1 && !seen[a.getAttribute("href")]) { seen[a.getAttribute("href")] = 1; ul.appendChild(li.cloneNode(true)); }
    });
    box.hidden = !ul.children.length; $("#catnone").hidden = !!ul.children.length;
    if (ul.children.length) box.appendChild(ul);
  }
  if (cq) {
    cq.addEventListener("input", catSearch);
    $$("[data-hot]").forEach(function (a) {
      a.addEventListener("click", function (e) { e.preventDefault(); cq.value = a.getAttribute("data-hot"); catSearch(); });
    });
  }

  var tt = $("#totop");
  if (tt) tt.addEventListener("click", function (e) { e.preventDefault(); window.scrollTo(0, 0); });
})();
