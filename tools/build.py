#!/usr/bin/env python3
"""Static site generator for the Baekhyeon Hwarang SAR Government portal (GovBHG).

The layout, information architecture and visual design follow the GovHK portal
(home page, category / topic / service pages). All code, artwork and wording are original.

    python3 tools/build.py        # writes index.html, en/, ko/, zh-hant/, zh-hans/
"""
import html
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import data as D          # noqa: E402
import data_travel as T   # noqa: E402
import data_info as I     # noqa: E402
import data_esvc as E     # noqa: E402
import data_forms as FM    # noqa: E402
import json               # noqa: E402
from t2s_map import T2S, PHRASES  # noqa: E402

LANGS = [  # code, folder, <html lang>, label
    ("en", "en", "en", "English"),
    ("ko", "ko", "ko", "한국어"),
    ("hant", "zh-hant", "zh-Hant", "繁體中文"),
    ("hans", "zh-hans", "zh-Hans", "简体中文"),
]
IDX = {"en": 0, "ko": 1, "hant": 2, "hans": 3}


# ----------------------------------------------------------------------------- text helpers
def s2(text):
    for a, b in PHRASES:
        text = text.replace(a, b)
    return "".join(T2S.get(c, c) for c in text)


def g(tup, i):
    """Raw text of a trilingual tuple; i == 3 -> Simplified derived from Traditional."""
    return s2(tup[2]) if i == 3 else tup[i]


def t(tup, i):
    return html.escape(g(tup, i))


def U(key, i):
    return t(D.UI[key], i)


# ----------------------------------------------------------------------------- page registry
def depth(path):
    return len([p for p in path.split("/") if p])


def rel(cur, target):
    """Relative URL (inside one language folder) from page `cur` to page `target`."""
    up = "../" * depth(cur)
    if not target:
        return up or "./"
    return up + target + "/"


TD = "residents/immigration/traveldoc"
ARTICLES = {            # path -> content blocks of an article-style service page
    TD + "/passport/apply": D.PASSPORT_BLOCKS,
    TD + "/passport/book": T.BOOK_BLOCKS,
    TD + "/appstatus": T.STATUS_BLOCKS,
}
ETX = "residents/taxes/etax"
IMMD_BASE = "https://lshdev7.github.io/bhg_Immigration_Department/"
IMMD_TD = "immd:services/travel-documents"
TD_IMMD = {   # GovHK sends these to the Immigration Department website
    "faq": IMMD_TD + "/faq", "fees": IMMD_TD + "/fees", "photo": IMMD_TD + "/photo", "kiosk": IMMD_TD + "/kiosk",
    "aboutpassport": IMMD_TD + "/apply-passport", "aboutdocid": IMMD_TD + "/docid", "aboutreentry": IMMD_TD + "/reentry",
    "aboutseaman": IMMD_TD + "/seaman", "branches": "immd:contact/branch-offices", "hq": "immd:contact/hq-offices",
}
APPS = {   # GovHK-style hand-off pages that forward to the Immigration Department e-services
    "apps/immdapplypassport": ("immd:eservices/passport-application/loading", ("OWP form filling", "온라인 신청서 작성", "網上表格填寫")),
    "apps/immdtd_booking": ("immd:eservices/travel-document-booking/loading", ("Travel document appointment booking", "여행증명서 신청 예약", "預約申請旅行證件")),
}


def link(cur, target, i):
    """Relative link inside GovBHG, or absolute link to the Immigration Department site for "immd:" targets."""
    if target.startswith("immd:"):
        return IMMD_BASE + LANGS[i][1] + "/" + target[5:] + "/"
    return rel(cur, target)
PAYFAQ_PATH = "about/helpdesk/faq/payment"
ARTICLES.update({
    TD + "/lost": I.LOST,
    "residents/immigration/nonpermanent/appstatus": I.NONPERM,
    ETX: I.ETAX, ETX + "/taxcalc": I.TAXCALC_INFO, ETX + "/allowance": I.ALLOWANCE,
    PAYFAQ_PATH: I.PAYFAQ,
})
ESERVICES = {   # path -> (config key, title)
    "eservices/etax-login": ("etax-login", ("eTAX – Individual Tax Portal (ITP) Login", "eTAX – 개인 납세 포털(ITP) 로그인", "稅務易 – 個人稅務入門網站（ITP）登入")),
    "eservices/etax-register": ("etax-register", E.ETAX_REGISTER["title"]),
    "eservices/tax-payment": ("tax-payment", E.TAX_PAYMENT["title"]),
    "eservices/tax-calc": ("tax-calc", E.TAXCALC["title"]),
}
BLOCK_TARGET = {
    "apply": "apps/immdapplypassport", "appointment": "apps/immdtd_booking", "tdstatus": "immd:eservices/travel-document-status/loading",
    "appstatussvc": "immd:eservices/application-status/loading", "idbook": "immd:eservices/idcard-booking/loading",
    "photo": TD_IMMD["photo"], "payfaq": PAYFAQ_PATH, "passfaq": TD_IMMD["faq"], "faq": TD_IMMD["faq"], "fees": TD_IMMD["fees"],
    "etaxlogin": "eservices/etax-login", "etaxreg": "eservices/etax-register", "taxcalc": ETX + "/taxcalc",
    "allowance": ETX + "/allowance", "taxpay": "eservices/tax-payment",
}
LINK_TARGETS = {   # by English text of a "links" item
    "More information on Baekhyeon Hwarang SAR Passport": TD_IMMD["aboutpassport"],
    "More information on Baekhyeon Hwarang SAR Re-entry Permit": TD_IMMD["aboutreentry"],
    "More information on Baekhyeon Hwarang SAR Document of Identity for Visa Purposes": TD_IMMD["aboutdocid"],
    "More information on Baekhyeon Hwarang SAR Seaman's Identity Book": TD_IMMD["aboutseaman"],
    "Addresses and working hours of Immigration Offices at Immigration Headquarters": TD_IMMD["hq"],
    "Addresses and working hours of Immigration Offices at Immigration Branch Offices": TD_IMMD["branches"],
}
BOOK_PATH = TD + "/passport/book"
SLUG2FORM = {FM.FORMS[c]["slug"]: c for c in FM.ORDER}
GUIDE_PATH = "guidebook/passport"

MISC = {}          # slug -> title tuple   (generic pages under misc/)
PAGES = {}         # path -> dict


def reg(path, **kw):
    PAGES[path] = kw


def build_registry():
    PAGES.clear()
    reg("", kind="home", tab="residents", title=D.UI["site_full"])
    reg("business", kind="home", tab="business", title=D.TABS[1][1])
    reg("nonresidents", kind="home", tab="nonresidents", title=D.TABS[2][1])
    for tab, _lab in D.TABS:
        for cslug, ctitle, subs in D.TREE[tab]:
            cp = "%s/%s" % (tab, cslug)
            reg(cp, kind="cat", tab=tab, cat=cslug, title=ctitle)
            for sslug, stitle in subs:
                sp = "%s/%s" % (cp, sslug)
                reg(sp, kind="traveldoc" if sp == TD else ("service" if sp in ARTICLES else "sub"), tab=tab, cat=cslug, sub=sslug, title=stitle)
                leaves = D.LEAVES.get((cslug, sslug), []) if tab == "residents" else []
                for lslug, ltitle in leaves:
                    lp = "%s/%s" % (sp, lslug)
                    reg(lp, kind="service" if lp in ARTICLES else "leaf", tab=tab, cat=cslug, sub=sslug, leaf=lslug, title=ltitle)
                    for xslug, xtitle in D.SUBLEAVES.get((cslug, sslug, lslug), []):
                        xp = "%s/%s" % (lp, xslug)
                        reg(xp, kind="service" if xp in ARTICLES else "leaf2", tab=tab, cat=cslug, sub=sslug, leaf=lslug, subleaf=xslug, title=xtitle)
        reg("%s/onlineservices" % tab, kind="list", tab=tab, title=D.ONLINE_PAGE, what="online")
        reg("%s/forms" % tab, kind="catalog", tab=tab, title=FM.CAT_TITLE)
    reg(PAYFAQ_PATH, kind="service", tab="residents", title=I.PAYFAQ_TITLE)
    for code in FM.ORDER:
        reg("forms/" + code, kind="form", tab="residents", title=FM.FORMS[code]["title"], code=code)
    for path, (target, title) in APPS.items():
        reg(path, kind="apps", tab="residents", title=title, target=target)
    for path, (key, title) in ESERVICES.items():
        reg(path, kind="eservice", tab="residents", title=title, esvc=key)
    for slug, title in (("itpforgot", ("Forgot ITP Password", "ITP 비밀번호 찾기", "忘記ITP密碼")), ("itpfile", ("File Tax Return", "세금 신고", "報稅"))):
        reg("misc/%s" % slug, kind="misc", tab="residents", title=title, slug=slug)
    # generic pages for every other linked item
    items = []
    items += [(s, tt) for s, tt in D.QUICK]
    for tab in D.ONLINE:
        items += list(D.ONLINE[tab]) + list(D.FORMS[tab])
    items += [(s, tt) for s, tt, _ in D.GUIDES]
    items += [(s, tt) for s, tt, _ in D.FEATURES]
    items += [(s, tt) for s, tt, _c in D.CHECK]
    items += list(D.SOCIAL) + list(D.FOOTER) + list(D.HOT)
    items += [("govsites", D.GOVSITES)]
    for slug, title in items:
        MISC.setdefault(slug, title)
    for slug, title in MISC.items():
        if slug in ("passport", "idcard", "etax", "etaxlogin", "appstatus", "taxcalc") or slug in SLUG2FORM:
            continue
        reg("misc/%s" % slug, kind="misc", tab="residents", title=title, slug=slug)
    for n, (title, _c, _k) in enumerate(D.HERO_CARDS):
        reg("misc/hero%d" % n, kind="misc", tab="residents", title=title, slug="hero%d" % n)
    reg("misc/advsearch", kind="misc", tab="residents", title=D.UI["adv"], slug="advsearch")
    reg("misc/guides", kind="misc", tab="residents", title=D.UI["guide"], slug="guides")
    reg("misc/apply", kind="misc", tab="residents", title=("Application through the Internet for Baekhyeon Hwarang SAR Passport", "인터넷 백현화랑 특별행정구 여권 신청", "透過互聯網申請柏峴화랑特別行政區護照"), slug="apply")
    reg(GUIDE_PATH, kind="guide", tab="residents", title=T.GB_TITLE)
    for slug, title in T.GB_CRUMBS:
        if slug != "guides":
            reg("misc/%s" % slug, kind="misc", tab="residents", title=title, slug=slug)
    for _gt, rows in T.TD_GROUPS:
        for key, title in rows:
            if not key.startswith("P:"):
                reg("misc/%s" % key, kind="misc", tab="residents", title=title, slug=key)
    for slug, title in (("appointment", ("Make an Appointment to Apply for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件")),
                        ("photo", ("Photograph Requirements", "사진 규격", "照片規格")),
                        ("faq", ("Frequently Asked Questions", "자주 묻는 질문", "常見問題")),
                        ("fees", ("Fees", "수수료", "費用"))):
        reg("misc/%s" % slug, kind="misc", tab="residents", title=title, slug=slug)


def target_of(slug):
    """Page path an item slug resolves to."""
    if slug == "passport":
        return "residents/immigration/traveldoc/passport/apply"
    if slug == "idcard":
        return "immd:services/identity-cards"
    if slug == "etax":
        return ETX
    if slug in SLUG2FORM:
        return "forms/" + SLUG2FORM[slug]
    if slug == "etaxlogin":
        return "eservices/etax-login"
    if slug == "appstatus":
        return "residents/immigration/nonpermanent/appstatus"
    if slug == "taxcalc":
        return ETX + "/taxcalc"
    return "misc/%s" % slug


# ----------------------------------------------------------------------------- icons
ICONS = {
    "wifi": '<g fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"><path d="M6 19a26 26 0 0136 0"/><path d="M14 28a15 15 0 0120 0"/></g><circle cx="24" cy="37" r="4"/>',
    "ball": '<circle cx="24" cy="24" r="20"/><path d="M24 13l8 6-3 9H19l-3-9z" fill="#fff"/><path d="M24 13V6M32 19l7-3M29 28l5 7M19 28l-5 7M16 19l-7-3" stroke="#fff" stroke-width="2.4" fill="none"/>',
    "cap": '<path d="M24 8L2 19l22 11 18-9v12h4V19z"/><path d="M11 27v8c0 3 6 6 13 6s13-3 13-6v-8l-13 6.5z"/>',
    "brief": '<rect x="4" y="14" width="40" height="27" rx="4"/><path d="M17 14v-4a3 3 0 013-3h8a3 3 0 013 3v4" fill="none" stroke="currentColor" stroke-width="4"/><rect x="4" y="25" width="40" height="3.4" fill="#fff"/><rect x="21" y="23" width="6" height="7" rx="1" fill="#fff"/>',
    "leaf": '<path d="M41 6C21 5 8 15 8 30c0 4 1.5 7 4 9l-4.5 5 3 2.5 5-5.5c2 .8 4 1 6.5 1 14 0 20-14 19-36z"/>',
    "scale": '<g fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M24 7v33M11 41h26M7 13h34"/><path d="M7 13L1.5 28a5.5 4 0 0011 0zM41 13l-5.5 15a5.5 4 0 0011 0z"/></g>',
    "heart": '<path d="M24 43S3 30 3 17a10.5 10.5 0 0121-3 10.5 10.5 0 0121 3c0 13-21 26-21 26z"/>',
    "house": '<path d="M24 5L2 25h6v17h11V30h10v12h11V25h6z"/>',
    "globepin": '<circle cx="21" cy="27" r="17"/><path d="M4 27h34M21 10c-8 8-8 26 0 34M21 10c8 8 8 26 0 34" stroke="#fff" fill="none" stroke-width="2.4"/><circle cx="37" cy="12" r="8.5" stroke="#fff" stroke-width="2.6"/><circle cx="37" cy="12" r="3" fill="#fff"/>',
    "coins": '<ellipse cx="24" cy="12" rx="15" ry="6"/><path d="M9 17v6c0 3 7 6 15 6s15-3 15-6v-6c0 3-7 6-15 6s-15-3-15-6z"/><path d="M9 27v6c0 3 7 6 15 6s15-3 15-6v-6c0 3-7 6-15 6s-15-3-15-6z"/>',
    "car": '<path d="M7 24l4-11c1-2 3-3 5-3h16c2 0 4 1 5 3l4 11c3 1 4 3 4 6v7h-5v3h-7v-3H17v3h-7v-3H5v-7c0-3 1-5 4-6z"/><circle cx="13" cy="31" r="2.5" fill="#fff"/><circle cx="35" cy="31" r="2.5" fill="#fff"/><path d="M13 22l2.5-7h17l2.5 7z" fill="#fff"/>',
    "globe": '<g fill="none" stroke="currentColor" stroke-width="3.4"><circle cx="24" cy="24" r="19.5"/><ellipse cx="24" cy="24" rx="9" ry="19.5"/><path d="M5 24h38M8 14h32M8 34h32"/></g>',
}
TILE_ICON = {
    "communication": "wifi", "culture": "ball", "education": "cap", "employment": "brief", "environment": "leaf",
    "government": "scale", "health": "heart", "housing": "house", "immigration": "globepin", "taxes": "coins",
    "transport": "car", "govsites": "globe",
    "csr": "heart", "korea": "globe", "businessgov": "brief", "ecommerce": "wifi", "global": "globe", "hr": "scale",
    "market": "coins", "registration": "brief", "support": "house",
    "visiting": "globepin", "working": "brief", "studying": "cap", "visarequire": "globepin", "living": "house",
    "doingbusiness": "coins",
}


def svg(name, cls=""):
    return '<svg class="ic %s" viewBox="0 0 48 48" fill="currentColor" aria-hidden="true" focusable="false">%s</svg>' % (cls, ICONS[name])


GUIDE_ICON = {
    "passport": '<rect x="9" y="4" width="30" height="40" rx="3"/><circle cx="24" cy="21" r="8"/><path d="M16 21h16M24 13c-4 4-4 12 0 16M24 13c4 4 4 12 0 16M15 36h18"/>',
    "calendar": '<rect x="5" y="8" width="38" height="34" rx="3"/><path d="M5 18h38M14 4v8M34 4v8M13 26h5M22 26h5M31 26h5M13 34h5M22 34h5"/>',
    "car": '<path d="M7 28l4-11c1-2 3-3 5-3h16c2 0 4 1 5 3l4 11v9H7z"/><path d="M5 28h38M13 33h4M31 33h4M10 37v4h6v-4M32 37v4h6v-4"/>',
}
FEAT_ICON = {
    "baby": '<circle cx="24" cy="24" r="7"/><path d="M16 38c3-5 13-5 16 0M20 21h.01M28 21h.01"/>',
    "heart": '<path d="M24 36S11 28 11 19a6.5 6.5 0 0113-2 6.5 6.5 0 0113 2c0 9-13 17-13 17z"/>',
    "book": '<path d="M10 14h12c2 0 2 2 2 2v20c0-2-2-2-2-2H10zM38 14H26c-2 0-2 2-2 2v20c0-2 2-2 2-2h12z"/>',
    "rings": '<circle cx="19" cy="28" r="8"/><circle cx="29" cy="28" r="8"/><path d="M21 14l3-4 3 4-3 4z"/>',
    "house": '<path d="M10 25L24 12l14 13M14 23v14h20V23"/><circle cx="24" cy="30" r="3.5"/>',
}


def search_icon():
    return ('<svg class="sicon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="6.5" fill="none" '
            'stroke="currentColor" stroke-width="2.2"/><path d="M15 15l6 6" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>')


def logo_html(i, big):
    cn1 = "柏岘화랑政府" if i == 3 else "柏峴화랑政府"
    return (
        '<a class="logo%s" href="%%HOME%%" aria-label="%s">'
        '<img class="logo-flag" src="%%ASSETS%%flag.jpg" alt="" width="%d" height="%d">'
        '<span class="logo-txt"><span class="g1">Gov</span><span class="g2">BHG</span>'
        '<span class="g3">%s</span><span class="g4">一站通</span></span></a>'
        % (" big" if big else "", html.escape(D.UI["site"][0]), 120 if big else 60, 80 if big else 40, cn1)
    )


# ----------------------------------------------------------------------------- shared chunks
def top_bar(i, cur):
    langs = []
    for code, folder, hl, label in LANGS:
        up = "../" * (depth(cur) + 1)
        href = "%s%s/%s" % (up, folder, (cur + "/") if cur else "")
        cls = ' class="cur"' if IDX[code] == i else ""
        langs.append('<li><a href="%s" lang="%s" hreflang="%s"%s>%s</a></li>' % (href, hl, hl, cls, label))
    return (
        '<div class="topbar"><div class="wrap topbar-in"><ul class="tools">'
        '<li class="ts"><button type="button" id="textsize">%s</button></li>'
        '<li class="lg"><button type="button" class="lg-btn" aria-expanded="false" aria-controls="langmenu">'
        '<svg viewBox="0 0 24 24" class="globe" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.6"/>'
        '<path d="M3 12h18M12 3c-4 4-4 14 0 18M12 3c4 4 4 14 0 18" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
        '<span>%s</span><i class="caret"></i></button>'
        '<ul class="langmenu" id="langmenu" hidden>%s</ul></li></ul></div></div>'
        % (U("text_size", i), U("languages", i), "".join(langs))
    )


def mega_panels(i, cur):
    out = []
    for tab, lab in D.TABS:
        cols = []
        items = D.TREE[tab]
        half = (len(items) + 1) // 2
        for chunk in (items[:half], items[half:]):
            li = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, "%s/%s" % (tab, cs)), t(ct, i)) for cs, ct, _ in chunk)
            cols.append('<ul class="mm-col">%s</ul>' % li)
        bottom = (
            '<ul class="mm-bottom"><li><a href="%s">%s<span class="vh"> %s</span></a></li>'
            '<li><a href="%s">%s<span class="vh"> %s</span></a></li>'
            '<li><a href="%s">%s</a></li></ul>'
            % (rel(cur, "%s/onlineservices" % tab), t(D.ONLINE_PAGE, i), t(lab, i),
               rel(cur, "%s/forms" % tab), t(D.FORMS_PAGE, i), t(lab, i),
               rel(cur, "misc/govsites"), t(D.GOVSITES, i))
        )
        out.append('<div class="mm t-%s" id="mm-%s" hidden><div class="wrap mm-in"><div class="mm-cols">%s</div>%s</div></div>'
                   % (tab, tab, "".join(cols), bottom))
    return "".join(out)


def search_block(i, cur):
    hot = "".join('<a href="%s">%s</a>' % (link(cur, target_of(s), i), t(tt, i)) for s, tt in D.HOT)
    return (
        '<div class="searchblock"><form class="sform" id="sf" role="search"><label class="vh" for="q">%s</label>'
        '<span class="sbar">%s<input id="q" type="search" placeholder="%s" autocomplete="off"></span>'
        '<button class="vh" type="submit">%s</button></form>'
        '<div class="hot"><span class="hot-l">%s</span><span class="hot-i">%s</span>'
        '<a class="adv" href="%s">%s<i class="chev"></i></a></div></div>'
        % (U("search_ph", i), search_icon(), U("search_ph", i), U("search_btn", i), U("hot", i), hot,
           rel(cur, "misc/advsearch"), U("adv", i))
    )


def footer(i, cur):
    links = "".join('<li><a href="%s">%s</a></li>' % (link(cur, target_of(s), i), t(tt, i)) for s, tt in D.FOOTER)
    return (
        '<footer class="foot"><div class="wrap">'
        '<p class="totop"><a href="#top" id="totop">%s<i class="up"></i></a></p>'
        '<div class="foot-row"><nav aria-label="Footer"><ul class="fmenu">%s</ul></nav>'
        '<div class="foot-r"><p class="geo">%s</p><p class="copy">%s</p></div></div>'
        '</div></footer>' % (U("top", i), links, U("geo", i), U("copyright", i))
    )


def head(i, hl, title, cur):
    up = "../" * (depth(cur) + 1)
    return (
        '<!doctype html><html lang="%s"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title><meta name="description" content="%s">'
        '<link rel="icon" href="%sassets/favicon.svg" type="image/svg+xml">'
        '<link rel="stylesheet" href="%sassets/site.css"></head>' % (hl, html.escape(title), U("site_full", i), up, up)
    )


def finish(htmltxt, cur):
    up = "../" * (depth(cur) + 1)
    return htmltxt.replace("%ASSETS%", up + "assets/").replace("%HOME%", rel(cur, ""))


def tail(i, cur, extra=""):
    return (
        '<div id="results" class="results" hidden><div class="wrap"><h2>%s</h2><ul id="rlist"></ul></div></div>'
        '<script>window.BHG={nores:"%s"};</script><script src="%%ASSETS%%site.js"></script>%s</body></html>'
        % (U("res_title", i), g(D.UI["no_res"], i), extra)
    )


# ----------------------------------------------------------------------------- home pages
def hero_cards(i, cur):
    out = []
    for n, (title, color, kind) in enumerate(D.HERO_CARDS):
        if kind == "flag":
            img = '<div class="c-img flag" style="background-image:url(%ASSETS%flag.jpg)"></div>'
        else:
            dark = " dark" if kind == "dark" else ""
            short = html.escape(g(D.HERO_SHORT[n] or title, i))
            img = '<div class="c-img%s" style="background:%s"><span>%s</span></div>' % (dark, color, short)
        out.append('<div class="card"><a href="%s">%s<h3>%s</h3></a></div>' % (rel(cur, "misc/hero%d" % n), img, t(title, i)))
    return "".join(out)


def tiles(i, cur, tab):
    out = []
    for cs, ct, _ in D.TREE[tab]:
        out.append('<li><a href="%s">%s<span>%s</span></a></li>' % (rel(cur, "%s/%s" % (tab, cs)), svg(TILE_ICON.get(cs, "globe")), t(ct, i)))
    out.append('<li><a href="%s">%s<span>%s</span></a></li>' % (rel(cur, "misc/govsites"), svg("globe"), t(D.GOVSITES, i)))
    return "".join(out)


def ul_links(items, i, cur):
    return "".join('<li><a href="%s">%s</a></li>' % (link(cur, target_of(s), i), t(tt, i)) for s, tt in items)


def home_page(i, hl, cur, info):
    tab = info["tab"]
    tab_html = []
    for key, lab in D.TABS:
        href = rel(cur, "" if key == "residents" else key)
        on = ' class="on t-%s" aria-current="page"' % key if key == tab else ' class="t-%s"' % key
        tab_html.append('<li><a href="%s"%s><span>%s</span><i class="tcaret"></i></a></li>' % (href, on, t(lab, i)))
    quick = ul_links(D.QUICK, i, cur)
    online = ul_links(D.ONLINE[tab], i, cur)
    forms = ul_links(D.FORMS[tab], i, cur)
    more = U("more", i)
    guides = "".join(
        '<li><a href="%s"><svg class="gi" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg><span>%s</span><i class="gch"></i></a></li>'
        % (rel(cur, GUIDE_PATH if s == "passport" else target_of(s)), GUIDE_ICON[ic], t(tt, i)) for s, tt, ic in D.GUIDES)
    feats = "".join(
        '<li><a href="%s"><span class="fc"><svg viewBox="0 0 48 48" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg></span><span class="fl">%s</span></a></li>'
        % (link(cur, target_of(s), i), FEAT_ICON[ic], t(tt, i)) for s, tt, ic in D.FEATURES)
    checks = "".join(
        '<li class="card"><a href="%s"><div class="c-img" style="background:%s"></div><h3>%s</h3></a></li>'
        % (link(cur, target_of(s), i), col, t(tt, i)) for s, tt, col in D.CHECK)
    social = ul_links(D.SOCIAL, i, cur)
    page = head(i, hl, "%s — %s" % (g(D.UI["site"], i), g(D.UI["site_full"], i)), cur)
    page += '<body class="home t-%s lang-%s"><a class="skip" href="#main" id="top">%s</a>' % (tab, LANGS[i][0], U("skip", i))
    page += top_bar(i, cur)
    page += '<header class="hhead"><div class="wrap hhead-in">%s%s</div>' % (logo_html(i, True), search_block(i, cur))
    page += '<nav class="tabs" aria-label="%s"><div class="wrap"><ul>%s</ul></div></nav></header>' % (U("main_menu", i), "".join(tab_html))
    desk_a = ('<svg class="deco" viewBox="0 0 100 100" fill="none" stroke="#fff" stroke-width="2.5" aria-hidden="true">'
              '<rect x="8" y="10" width="84" height="56" rx="4"/><path d="M30 86h40M50 66v20M18 22h20M18 34h12M44 22h12M44 34h12M66 22h16"/></svg>')
    desk_b = ('<svg class="deco" viewBox="0 0 100 100" fill="none" stroke="#fff" stroke-width="2.5" aria-hidden="true">'
              '<rect x="12" y="14" width="56" height="76" rx="5"/><path d="M26 34h30M26 48h30M26 62h18M72 20l14 6-14 58-6-2z"/></svg>')
    page += (
        '<main id="main"><h1 class="vh">%s</h1>'
        '<section class="hero"><div class="hero-city"></div>'
        '<div class="hero-in"><div class="track" id="cards">%s</div>'
        '<div class="pill" id="cdots"></div></div></section>'
        '<section class="wrap quick"><h2>%s</h2><ul>%s</ul></section>'
        '<section class="wrap boxes"><div class="rbox"><h2>%s</h2><ul>%s<li class="more"><a href="%s">%s&nbsp;&nbsp;&gt;</a></li></ul>%s</div>'
        '<div class="rbox"><h2>%s</h2><ul>%s<li class="more"><a href="%s">%s&nbsp;&nbsp;&gt;</a></li></ul>%s</div></section>'
        '<section class="wrap info"><h2>%s</h2><ul class="tiles">%s</ul></section>'
        '<section class="guide"><div class="wrap"><h2>%s</h2><ul class="gcards">%s</ul><p class="gmore"><a class="pillbtn" href="%s">%s</a></p></div></section>'
        '<section class="feat"><div class="wrap"><h2>%s</h2><div class="ftrack-w"><ul class="ftrack" id="ftrack">%s</ul>'
        '<button type="button" class="fnext" id="fnext" aria-label="%s"><i></i></button></div><div class="pill small" id="fdots"></div></div></section>'
        '<section class="check"><div class="wrap"><h2>%s</h2><ul class="ccards">%s</ul></div></section>'
        '<section class="social"><div class="wrap social-in"><h2>%s</h2><ul>%s</ul></div></section>'
        '</main>'
        % (g(D.UI["site_full"], i), hero_cards(i, cur),
           U("quick", i), quick,
           U("top_online", i), online, rel(cur, "%s/onlineservices" % tab), more, desk_a,
           U("top_forms", i), forms, rel(cur, "%s/forms" % tab), more, desk_b,
           U("info", i), tiles(i, cur, tab),
           U("guide", i), guides, rel(cur, "misc/guides"), more,
           U("features", i), feats, U("next", i),
           U("check", i), checks, U("social", i), social)
    )
    page += footer(i, cur) + mega_panels(i, cur) + tail(i, cur)
    return finish(page, cur)


# ----------------------------------------------------------------------------- inner pages
def find_cat(tab, cat):
    return [c for c in D.TREE[tab] if c[0] == cat][0]


def breadcrumb(i, cur, info):
    parts = [(rel(cur, ""), U("home", i))]
    tab = info.get("tab", "residents")
    tl = dict(D.TABS)[tab]
    kind = info["kind"]
    if kind == "guide":
        parts.append((rel(cur, "misc/guides"), t(T.GB_CRUMBS[0][1], i)))
        parts.append((rel(cur, "misc/travel"), t(T.GB_CRUMBS[1][1], i)))
        parts.append((rel(cur, "misc/traveldocument"), t(T.GB_CRUMBS[2][1], i)))
    else:
        parts.append((rel(cur, "" if tab == "residents" else tab), t(tl, i)))
    if kind in ("sub", "traveldoc", "leaf", "service", "leaf2") and info.get("cat"):   # ancestors only; the page itself is the last crumb
        cp = "%s/%s" % (tab, info["cat"])
        c = find_cat(tab, info["cat"])
        parts.append((rel(cur, cp), t(c[1], i)))
        if info.get("leaf"):
            sp = "%s/%s" % (cp, info["sub"])
            st = [x for x in c[2] if x[0] == info["sub"]][0][1]
            parts.append((rel(cur, sp), t(st, i)))
            if info.get("subleaf"):
                lp = "%s/%s" % (sp, info["leaf"])
                lt = dict(D.LEAVES[(info["cat"], info["sub"])])[info["leaf"]]
                parts.append((rel(cur, lp), t(lt, i)))
    lis = "".join('<li><a href="%s">%s</a></li>' % h for h in parts)
    return '<nav class="bc" aria-label="Breadcrumb"><div class="wrap"><ol>%s<li class="cur" aria-current="page">%s</li></ol></div></nav>' % (lis, t(info["title"], i))


def sidebar(i, cur, info):
    tab = info.get("tab", "residents")
    cat = info.get("cat")
    if not cat:
        return ""
    out = []
    for ss, st in find_cat(tab, cat)[2]:
        on = ' class="on"' if info.get("sub") == ss else ""
        out.append('<li%s><a href="%s">%s</a></li>' % (on, rel(cur, "%s/%s/%s" % (tab, cat, ss)), t(st, i)))
    return '<aside class="side"><ul>%s</ul></aside>' % "".join(out)


def poll(i, aside=False):
    return (
        '<div class="below"><div class="helpful"><strong>%s</strong>'
        '<label><input type="radio" name="h"><span class="face g"></span></label>'
        '<label><input type="radio" name="h"><span class="face y"></span></label>'
        '<label><input type="radio" name="h"><span class="face r"></span></label></div>'
        '<p class="review">%s%s</p></div>' % (U("helpful", i), U("review", i), U("review_val", i))
    )


def boxes(items, i, cur, base):
    lis = "".join('<li><a href="%s"><span>%s</span><i class="plus"></i></a></li>' % (rel(cur, "%s/%s" % (base, s)), t(tt, i)) for s, tt in items)
    return '<ul class="topics">%s</ul>' % lis


SHARE = [("fb", "#3b5998", "f"), ("tw", "#1da1f2", "t"), ("wb", "#e6162d", "w"), ("wa", "#25d366", "w"), ("ln", "#00b900", "L"), ("wc", "#07c160", "c")]


def share_html(i):
    ic = []
    for k, col, ch in SHARE:
        ic.append('<a href="#" class="sh" data-share="%s" aria-label="%s"><svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="%d" fill="%s"/>'
                  '<text x="12" y="17" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" font-family="Arial">%s</text></svg></a>'
                  % (k, k, 5 if k in ("fb", "ln") else 12, col, ch))
    return '<div class="share"><span>%s</span>%s</div>' % (t(T.GB_SHARE, i), "".join(ic))


def block_href(slug, cur, i=0):
    return link(cur, BLOCK_TARGET.get(slug, "misc/" + slug), i)


def render_blocks(blocks, i, cur):
    out = []
    for b in blocks:
        k = b[0]
        if k == "p":
            out.append("<p>%s</p>" % g(b[1], i))
        elif k == "plain":
            out.append('<p class="plain">%s</p>' % g(b[1], i))
        elif k == "strong":
            out.append("<p><strong>%s</strong></p>" % html.escape(g(b[1], i)))
        elif k == "h2":
            out.append("<h2>%s</h2>" % html.escape(g(b[1], i)))
        elif k == "h2id":
            out.append('<h2 id="%s">%s</h2>' % (b[1], html.escape(g(b[2], i))))
        elif k == "h3":
            out.append("<h3>%s</h3>" % html.escape(g(b[1], i)))
        elif k in ("ol", "ul"):
            out.append("<%s>%s</%s>" % (k, "".join("<li>%s</li>" % html.escape(g(x, i)) for x in b[1]), k))
        elif k == "olr":
            out.append('<ol class="roman">%s</ol>' % "".join("<li>%s</li>" % html.escape(g(x, i)) for x in b[1]))
        elif k == "btn":
            out.append('<p class="btnp"><a class="gbtn" href="%s"><span>%s</span><i class="gch2"></i></a></p>' % (block_href(b[2], cur, i), html.escape(g(b[1], i))))
        elif k == "link":
            out.append('<p class="lnk"><a href="%s">%s</a></p>' % (block_href(b[2], cur, i), html.escape(g(b[1], i))))
        elif k == "ulink":
            out.append('<ul class="bl"><li><a href="%s">%s</a></li></ul>' % (b[2], html.escape(g(b[1], i))))
        elif k == "links":
            out.append('<ul class="bl">%s</ul>' % "".join('<li><a href="%s">%s</a></li>' % (link(cur, LINK_TARGETS.get(x[0], TD_IMMD["faq"]), i), html.escape(g(x, i))) for x in b[1]))
        elif k == "links2":
            out.append('<ul class="bl">%s</ul>' % "".join('<li><a href="%s">%s</a></li>' % (block_href(slug, cur, i), html.escape(g(x, i))) for x, slug in b[1]))
        elif k == "calclinks":
            out.append('<ul class="bl yrs">%s</ul>' % "".join('<li><a href="%s">%s</a></li>' % (rel(cur, "eservices/tax-calc"), y) for y in b[1]))
        elif k == "table":
            head = "".join("<th>%s</th>" % html.escape(g(c, i)) for c in b[1])
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % g(c, i) for c in r) for r in b[2])
            out.append('<div class="tblw"><table class="dt"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, rows))
        elif k == "faq":
            items = []
            for n, (q, a) in enumerate(b[1], 1):
                items.append('<li><button type="button" class="faq-q" aria-expanded="false"><span>Q%d. %s</span><i class="plus"></i></button><div class="faq-a" hidden><p>%s</p></div></li>'
                             % (n, html.escape(g(q, i)), html.escape(g(a, i))))
            out.append('<div class="faq"><p class="faqtools"><button type="button" data-faq="open">%s +</button><button type="button" data-faq="close">%s −</button></p><ul>%s</ul></div>'
                       % (U("expand_all", i), U("collapse_all", i), "".join(items)))
    return "".join(out)


def inner_header(i, cur, info):
    tab = info.get("tab", "residents")
    nav = []
    for key, lab in D.TABS:
        href = rel(cur, "" if key == "residents" else key)
        cls = ' class="nt on"' if key == tab else ' class="nt"'
        nav.append('<li><a href="%s"%s data-mm="mm-%s">%s</a></li>' % (href, cls, key, t(lab, i)))
    return (
        '<header class="ihead"><div class="wrap ihead-in">%s<nav class="inav" aria-label="%s"><ul>%s'
        '<li><button type="button" class="isearch" id="isearch" aria-label="%s">%s</button></li></ul></nav>'
        '<button type="button" class="burger" aria-label="%s"><span></span></button></div>'
        '<div class="wrap isearch-w" id="isearch-w" hidden>%s</div></header>'
        % (logo_html(i, False), U("main_menu", i), "".join(nav), U("search_ph", i), search_icon(), U("toggle", i), search_block(i, cur))
    )


def related_block(i, cur):
    rel_links = "".join('<li><a href="%s">%s</a></li>' % (rel(cur, "misc/travelinfo"), t(x, i)) for x in T.RELATED_LINKS)
    online = ul_links(D.ONLINE["residents"], i, cur)
    return ('<div class="relwrap"><section class="rel"><h2>%s</h2><h3>%s</h3><ul>%s</ul></section>'
            '<section class="rel"><h3>%s</h3><ul>%s</ul><p class="relmore"><a href="%s">%s&nbsp;&gt;</a></p></section></div>'
            % (U("related", i), g(("Related Links", "관련 링크", "相關連結"), i), rel_links,
               g(("Top Online Services", "인기 온라인 서비스", "常用網上服務"), i), online,
               rel(cur, "residents/onlineservices"), U("more", i)))


def traveldoc_main(i, cur):
    banner = ('<a class="tdbanner" href="%s"><svg viewBox="0 0 48 48" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" aria-hidden="true">%s</svg>'
              '<span>%s</span><i class="gch3"></i></a>' % (rel(cur, GUIDE_PATH), GUIDE_ICON["passport"], t(T.TD_BANNER, i)))
    items = []
    for n, (gt, rows) in enumerate(T.TD_GROUPS):
        lis = []
        for key, title in rows:
            last = key.rsplit("/", 1)[-1]
            if key.startswith("P:") and key[2:] not in PAGES and last in TD_IMMD:
                href = link(cur, TD_IMMD[last], i)
            else:
                href = rel(cur, key[2:]) if key.startswith("P:") else rel(cur, "misc/" + key)
            lis.append('<li><a href="%s">%s</a></li>' % (href, t(title, i)))
        blurb = ""
        if gt[0] in T.TD_BLURB:
            blurb = "<p>%s</p>" % t(T.TD_BLURB[gt[0]], i)
        items.append('<li class="acc-i"><button type="button" class="acc-h" aria-expanded="false" aria-controls="acc%d"><span>%s</span><i class="plus"></i></button>'
                     '<div class="acc-b" id="acc%d" hidden>%s<ul>%s</ul></div></li>' % (n, t(gt, i), n, blurb, "".join(lis)))
    return banner + '<ul class="acc">%s</ul>' % "".join(items) + poll(i)


def loc(o, i):
    """Localise every 3-tuple of strings inside a config structure."""
    if isinstance(o, tuple) and len(o) == 3 and all(isinstance(x, str) for x in o):
        return g(o, i)
    if isinstance(o, (list, tuple)):
        return [loc(x, i) for x in o]
    if isinstance(o, dict):
        return {k: loc(v, i) for k, v in o.items()}
    return o


def esvc_cfg(key, i, cur):
    link = lambda p: rel(cur, p)
    raw = {
        "passport": lambda: E.PASSPORT, "td-booking": lambda: E.booking("td"), "id-booking": lambda: E.booking("id"),
        "td-status": lambda: E.TD_STATUS, "app-status": lambda: E.VISA_STATUS, "etax-login": lambda: E.etax_login(link),
        "etax-register": lambda: E.ETAX_REGISTER, "tax-payment": lambda: E.TAX_PAYMENT, "tax-calc": lambda: E.TAXCALC,
    }[key]()
    cfg = loc(raw, i)
    cfg["L"] = loc(E.L, i)
    cfg["cur"] = E.CUR
    cfg.setdefault("offices", loc(E.OFFICES, i))
    return cfg


def inner_page(i, hl, cur, info):
    kind = info["kind"]
    tab = info.get("tab", "residents")
    title = info["title"]
    h1 = title
    main = ""
    extra = ""
    if kind == "cat":
        subs = find_cat(tab, info["cat"])[2]
        main += boxes(subs, i, cur, "%s/%s" % (tab, info["cat"])) + poll(i)
    elif kind == "traveldoc":
        h1 = find_cat(tab, info["cat"])[1]
        main += traveldoc_main(i, cur)
    elif kind == "sub":
        h1 = find_cat(tab, info["cat"])[1]
        leaves = D.LEAVES.get((info["cat"], info["sub"]), []) if tab == "residents" else []
        main += (boxes(leaves, i, cur, cur) if leaves else '<div class="box"><p>%s</p></div>' % U("stub", i)) + poll(i)
    elif kind == "leaf":
        subs = D.SUBLEAVES.get((info["cat"], info["sub"], info["leaf"]), [])
        main += (boxes(subs, i, cur, cur) if subs else '<div class="box"><p>%s</p></div>' % U("stub", i)) + poll(i)
    elif kind == "service":
        main += share_html(i) + '<div class="box article">%s</div>' % render_blocks(ARTICLES[cur], i, cur)
        main += poll(i) + related_block(i, cur)
    elif kind == "leaf2":
        main += '<div class="box"><p>%s</p></div>' % U("stub", i) + poll(i)
    elif kind == "eservice":
        blob = json.dumps(esvc_cfg(info["esvc"], i, cur), ensure_ascii=False).replace("</", "<\\/")
        main += '<div id="svc" class="svc"></div><script type="application/json" id="svc-cfg">%s</script>' % blob
        extra = '<script src="%ASSETS%svc.js"></script>'
    elif kind == "catalog":
        main += share_html(i) + catalog_main(i, cur, tab)
    elif kind == "list":
        src = D.ONLINE if info["what"] == "online" else D.FORMS
        lis = "".join('<li><a href="%s">%s</a></li>' % (link(cur, target_of(s), i), t(tt, i)) for s, tt in src[tab])
        main += '<div class="box"><ul class="plainlist">%s</ul></div>' % lis + poll(i)
    else:  # misc
        main += '<div class="box"><p>%s</p></div>' % U("stub_nomenu", i) + poll(i)

    side = catalog_side(i, cur, tab) if kind == "catalog" else sidebar(i, cur, info)
    page = head(i, hl, "%s — %s" % (g(title, i), g(D.UI["site"], i)), cur)
    page += '<body class="inner t-%s lang-%s"><a class="skip" href="#main" id="top">%s</a>' % (tab, LANGS[i][0], U("skip", i))
    page += top_bar(i, cur) + inner_header(i, cur, info) + mega_panels(i, cur)
    page += breadcrumb(i, cur, info)
    big = " big" if kind in ("cat", "sub", "traveldoc") else ""   # GovHK shows the category title at 40px
    page += '<main id="main" class="wrap %s">%s<div class="content%s"><h1>%s%s</h1>%s</div></main>' % (
        "layout" if side else "layout noside", side, big, html.escape(g(h1, i)), svg("globepin", "h1ic"), main)
    page += footer(i, cur) + tail(i, cur, extra)
    return finish(page, cur)


def apps_page(i, hl, cur, info):
    """GovHK-style hand-off page: blank page with a spinner that forwards to the Immigration Department after 3 seconds."""
    url = link(cur, info["target"], i)
    return ('<!doctype html><html lang="%s"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow">'
            '<meta http-equiv="Refresh" content="3;URL=%s"><meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta http-equiv="Cache-Control" content="no-cache"><title>GovBHG: %s</title>'
            '<style>body{margin:0;background:#fff}.loader{position:absolute;top:50%%;left:50%%;margin:-30px 0 0 -30px;border:5px solid #f3f3f3;'
            'border-top:5px solid #cc4c02;border-radius:50%%;width:50px;height:50px;animation:spin 1.6s linear infinite}'
            '@keyframes spin{to{transform:rotate(360deg)}}</style></head><body><div class="loader" role="progressbar" aria-label="Loading"></div></body></html>'
            % (hl, html.escape(url), html.escape(g(info["title"], i))))


# ----------------------------------------------------------------------------- government forms
def bil(tup, i):
    """Primary text in the page language plus the secondary language in small type, as on bilingual forms."""
    sec = 2 if i == 0 else 0
    return '%s <small>%s</small>' % (t(tup, i), t(tup, sec))


def form_item(it, i):
    k = it[0]
    if k == "part":
        return '<div class="fpart">%s</div>' % bil(it[1], i)
    if k == "note":
        return '<p class="fnote">%s</p>' % bil(it[1], i)
    if k == "text":
        w = it[2] if len(it) > 2 else "full"
        return '<label class="ff w-%s"><span class="fl">%s</span><input type="text"></label>' % (w, bil(it[1], i))
    if k == "boxes":
        return '<div class="ff w-full"><span class="fl">%s</span><span class="cbx">%s</span></div>' % (bil(it[1], i), '<input maxlength="1" aria-label="%d">' * it[2] % tuple(range(1, it[2] + 1)))
    if k == "check":
        return '<div class="ff w-full"><span class="fl">%s</span><span class="opts">%s</span></div>' % (bil(it[1], i), "".join('<label><input type="checkbox"> %s</label>' % bil(o, i) for o in it[2]))
    if k == "yn":
        return '<div class="ff w-full yn"><span class="fl">%s</span><span class="opts">%s</span></div>' % (bil(it[1], i), "".join('<label><input type="checkbox"> %s</label>' % bil(o, i) for o in (FM.YES, FM.NO)))
    if k == "money":
        return '<label class="ff w-full money"><span class="fl">%s</span><span class="cur">BH$</span><input type="text" inputmode="decimal"></label>' % bil(it[1], i)
    if k == "date":
        return '<div class="ff w-full"><span class="fl">%s</span><span class="dmy">%s</span></div>' % (bil(it[1], i), "".join('<label><input type="text" maxlength="4"> %s</label>' % t(x, i) for x in (FM.DAY, FM.MONTH, FM.YEAR)))
    if k == "pair":
        return '<div class="ff w-full"><span class="fl">%s</span><span class="pair">%s</span></div>' % (bil(it[1], i), "".join('<label><em>%s</em><input type="text"></label>' % t(x, i) for x in it[2]))
    if k == "addr":
        A = FM.ADDR
        return ('<fieldset class="ff w-full addr"><legend class="fl">%s</legend><span class="opts">%s</span>'
                '<span class="arow"><label><em>%s</em><input type="text"></label><label><em>%s</em><input type="text"></label><label><em>%s</em><input type="text"></label></span>'
                '<label><em>%s</em><input type="text"></label><label><em>%s</em><input type="text"></label><label><em>%s</em><input type="text"></label></fieldset>'
                % (bil(it[1], i), "".join('<label><input type="checkbox"> %s</label>' % t(o, i) for o in A["areas"]),
                   t(A["flat"], i), t(A["floor"], i), t(A["block"], i), t(A["bldg"], i), t(A["street"], i), t(A["district"], i)))
    if k == "table":
        head_ = "".join("<th>%s</th>" % bil(c, i) for c in it[1])
        if isinstance(it[2], int):
            rows = "".join("<tr>%s</tr>" % "".join('<td><input type="text"></td>' for _ in it[1]) for _ in range(it[2]))
        else:
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % t(c, i) for c in r) for r in it[2])
        return '<div class="ff w-full"><table class="ftab"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head_, rows)
    if k == "sign":
        return '<div class="ff w-full sign">%s</div>' % "".join('<label><input type="text"><em>%s</em></label>' % bil(x, i) for x in it[1])
    return ""


def form_page(i, hl, cur, info):
    F = FM.FORMS[info["code"]]
    dname, daddr = FM.DEPT[F["dept"]]
    V = FM.VIEWER
    up = "../" * (depth(cur) + 1)
    body = "".join(form_item(it, i) for it in F["items"])
    return finish(
        '<!doctype html><html lang="%s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title><link rel="icon" href="%sassets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="%sassets/site.css"></head>'
        '<body class="pdfv lang-%s"><div class="pv-bar"><span class="pv-file">%s</span><span class="pv-sp"></span>'
        '<button type="button" onclick="window.print()">%s</button><button type="button" onclick="window.print()">%s</button><a href="%s">%s</a></div>'
        '<main class="pv-doc"><article class="sheet"><header class="fh"><div class="fdept"><img src="%%ASSETS%%flag.jpg" alt="" width="44" height="44">'
        '<span><strong>%s</strong><em>%s</em></span></div><div class="fno">%s<span class="fofficial">%s</span></div></header>'
        '<h1 class="ftitle">%s</h1><p class="fintro">%s</p><form class="fgrid" onsubmit="return false">%s</form>'
        '<footer class="ffoot"><span>%s</span><span>%s 1</span></footer></article></main></body></html>'
        % (hl, html.escape(F["file"]), up, up, LANGS[i][0], html.escape(F["file"]), t(V["print"], i), t(V["save"], i), rel(cur, ""), t(V["back"], i),
           bil(dname, i), t(daddr, i), html.escape(F["no"]), t(V["official"], i), bil(F["title"], i), t(F["intro"], i), body, html.escape(F["no"]), t(V["page"], i)),
        cur)


def catalog_side(i, cur, tab):
    lis = "".join('<li%s><a href="%s">%s</a></li>' % (' class="on"' if k == tab else "", rel(cur, k + "/forms"), t(tt, i)) for k, tt in FM.CAT_USERS)
    return '<aside class="side"><ul>%s</ul></aside>' % lis


def form_li(code, i, cur):
    F = FM.FORMS[code]
    return ('<li data-k="%s"><a href="%s">%s (%s)</a> <span class="fmt">PDF</span></li>'
            % (html.escape((g(F["title"], i) + " " + F["no"] + " " + F["title"][0]).lower()), rel(cur, "forms/" + code), t(F["title"], i), html.escape(F["no"].split(" (")[0])))


def catalog_main(i, cur, tab):
    hot = ", ".join('<a href="#" data-hot="%s">%s</a>' % (t(w, i), t(w, i)) for w in FM.CAT_HOT_WORDS)
    fmts = "".join('<span class="fmtl"><span class="fmt">%s</span>%s</span>' % ({"Adobe PDF": "PDF", "Online Form": "WEB", "Microsoft Word": "DOC"}[x[0]], t(x, i)) for x in FM.CAT_FMT)
    acc = []
    if tab == "residents":
        for cs, ct, _subs in D.TREE["residents"]:
            groups = FM.CAT_SVC.get(cs, [])
            inner = "".join("<h4>%s</h4><ul>%s</ul>" % (t(h, i), "".join(form_li(c, i, cur) for c in codes)) for h, codes in groups) or "<p>%s</p>" % t(FM.CAT_EMPTY, i)
            acc.append('<details><summary>%s</summary><div class="cat-b">%s</div></details>' % (t(ct, i), inner))
        life = "".join('<details><summary>%s</summary><div class="cat-b"><ul>%s</ul></div></details>' % (t(h, i), "".join(form_li(c, i, cur) for c in codes)) for h, codes in FM.CAT_LIFE)
    else:
        items = "".join('<li data-k="%s"><a href="%s">%s</a> <span class="fmt">PDF</span></li>' % (html.escape(g(tt, i).lower()), rel(cur, target_of(s_)), t(tt, i)) for s_, tt in D.FORMS[tab])
        acc.append('<details open><summary>%s</summary><div class="cat-b"><ul>%s</ul></div></details>' % (t(dict(D.TABS)[tab], i), items))
        life = acc[0]
    tabs = "".join('<button type="button" data-ct="%s" class="%s">%s</button>' % (k, "on" if k == "svc" else "", t(tt, i)) for k, tt in FM.CAT_TABS)
    return ('<div class="cat"><h2 class="cat-s">%s</h2><form class="catq" onsubmit="return false"><input type="search" id="catq" placeholder="%s" aria-label="%s">%s</form>'
            '<p class="cat-hot"><strong>%s</strong> %s</p><div class="cat-res" id="catres" hidden></div><hr><p>%s</p><p>%s</p><p class="fmts">%s</p><hr>'
            '<h2 class="cat-h">%s</h2><div class="cat-tabs">%s</div><p class="cat-ea"><button type="button" data-cea>%s +</button></p>'
            '<div class="cat-p" data-cp="svc">%s</div><div class="cat-p" data-cp="life" hidden>%s</div><p class="cat-none" id="catnone" hidden>%s</p></div>'
            % (t(FM.CAT_SEARCH, i), t(FM.CAT_PH, i), t(FM.CAT_PH, i), search_icon(), t(FM.CAT_HOT, i), hot, t(FM.CAT_INTRO, i), t(FM.CAT_FORMATS, i), fmts,
               t(FM.CAT_COMMON, i), tabs, U("expand_all", i), "".join(acc), life, t(FM.CAT_NONE, i)))


# ----------------------------------------------------------------------------- guidebook page
SEC_ICON = {
    "forms": '<rect x="9" y="5" width="26" height="36" rx="2"/><path d="M15 15h14M15 22h14M15 29h8"/><path d="M29 31l8 8M37 31l-8 8" opacity="0"/>',
    "means": '<path d="M6 30c4-2 8-2 12 0l8 4 12-6c3-1 5 2 2 4l-14 8-14-4-6 2z"/><circle cx="31" cy="14" r="8"/><path d="M31 10v8M28 12h6"/>',
    "collect": '<path d="M24 6a12 12 0 0112 12c0 9-12 22-12 22S12 27 12 18A12 12 0 0124 6z"/><circle cx="24" cy="18" r="4"/>',
    "proc": '<circle cx="24" cy="24" r="17"/><path d="M24 12v13l9 5"/>',
}


def sec_h2(key, i):
    return ('<h2 class="gsec"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>%s</h2>'
            % (SEC_ICON[key], t(T.GB_SEC[key], i)))


def idlink(txt):
    import re
    return re.sub(r"(ID \d+A?)", r'<a href="#" class="idl">\1</a>', html.escape(txt))


def gb_tab(i, cur, tab, active):
    cols, rows, note, has_kiosk, _x = tab["means"]
    out = ['<section class="gtab" id="tab-%s" role="tabpanel"%s>' % (tab["id"], "" if active else " hidden")]
    out.append('<h2 class="gtitle">%s</h2>' % t(tab["title"], i))
    # forms
    out.append(sec_h2("forms", i))
    items = []
    for head, body in tab["forms"]:
        b = ('<span class="gb">%s</span>' % idlink(g(head, i)))
        if body:
            b += '<span class="gd">%s</span>' % t(body, i)
        items.append("<li>%s</li>" % b)
    docs = []
    for head, lines in tab["docs"]:
        docs.append('<span class="gu">%s</span>' % t(head, i))
        for lab, txt in lines:
            docs.append('<span class="gl">%s%s</span>' % (lab, t(txt, i)))
    items.append('<li><span class="gb">%s</span><span class="gd">%s</span></li>' % (
        t(("Supporting documents", "증빙서류", "證明文件"), i), "".join(docs)))
    out.append('<ul class="gl1">%s</ul>' % "".join(items))
    out.append('<p class="gm"><a href="%s">%s</a></p>' % (link(cur, TD_IMMD["aboutpassport"], i), t(T.GB_MORE["docs"], i)))
    # means table
    out.append(sec_h2("means", i))
    head = '<tr><th class="clk"><span data-clock></span></th>%s</tr>' % "".join('<th class="c%d">%s</th>' % (n, t(c, i)) for n, c in enumerate(cols))
    body = []
    for lab, marks in rows:
        body.append('<tr><th scope="row">%s</th>%s</tr>' % (t(lab, i), "".join('<td class="c%d">%s</td>' % (n, "✓" if m else "") for n, m in enumerate(marks))))
    out.append('<div class="tblw"><table class="pay"><thead>%s</thead><tbody>%s</tbody></table></div>' % (head, "".join(body)))
    out.append('<p class="fn">%s</p><p class="fn"><a href="%s">%s</a></p>' % (t(note, i), rel(cur, PAYFAQ_PATH), t(T.GB_MORE["faqpay"], i)))
    out.append('<p class="fn addr">%s<br>%s</p>' % (t(T.GB_ADDR[0], i), "<br>".join(t(x, i) for x in T.GB_ADDR[1])))
    out.append('<p class="gm"><a href="%s">%s</a></p>' % (link(cur, TD_IMMD["fees"], i), t(T.GB_MORE["means"], i)))
    # collection
    out.append(sec_h2("collect", i))
    out.append('<ul class="gl1">%s</ul>' % "".join('<li><span class="gb">%s</span><span class="gd">%s</span></li>' % (t(h, i), t(b, i)) for h, b in tab["collect"]))
    out.append('<p class="gm"><a href="%s">%s</a></p>' % (link(cur, TD_IMMD["kiosk"], i), t(T.GB_MORE["collect"], i)))
    # processing
    out.append(sec_h2("proc", i))
    for txt, plain in tab["proc"]:
        if plain:
            out.append('<p class="pr">%s</p>' % t(txt, i))
        else:
            first, rest = g(txt, i).split(":" if i != 2 and i != 3 else "：", 1)
            out.append('<p class="pr"><span class="note">%s%s</span>%s</p>' % (html.escape(first), ":" if i < 2 else "：", html.escape(rest)))
    out.append('<p class="gm"><a href="%s">%s</a></p>' % (link(cur, TD_IMMD["faq"], i), t(T.GB_MORE["proc"], i)))
    out.append("</section>")
    return "".join(out)


def guide_page(i, hl, cur, info):
    title = info["title"]
    tabs_btn = "".join('<button type="button" role="tab" class="gtb%s" data-tab="tab-%s" aria-selected="%s">%s</button>'
                       % (" on" if n == 0 else "", tb["id"], "true" if n == 0 else "false", t(tb["title"], i)) for n, tb in enumerate(T.GB_TABS))
    elig = "".join("<li>%s</li>" % t(x, i) for x in T.GB_ELIG)
    panels = "".join(gb_tab(i, cur, tb, n == 0) for n, tb in enumerate(T.GB_TABS))
    page = head(i, hl, "%s — %s" % (g(title, i), g(D.UI["site"], i)), cur)
    page += '<body class="inner guide t-residents lang-%s"><a class="skip" href="#main" id="top">%s</a>' % (LANGS[i][0], U("skip", i))
    page += top_bar(i, cur) + inner_header(i, cur, info) + mega_panels(i, cur) + breadcrumb(i, cur, info)
    page += ('<main id="main" class="wrap gmain"><h1>%s</h1><p class="gintro">%s</p><ul class="elig">%s</ul>'
             '<p class="gm"><a href="#">%s</a></p><div class="gtabs" role="tablist">%s</div>%s%s'
             '<p class="gmorebtn"><a class="obtn" href="%s">%s</a></p>%s</main>'
             % (html.escape(g(title, i)), t(T.GB_INTRO, i), elig, t(T.GB_MORE_ELIG, i), tabs_btn, panels,
                share_html(i), rel(cur, "misc/guides"), t(T.GB_MOREBTN, i), poll(i)))
    page += footer(i, cur) + tail(i, cur)
    return finish(page, cur)


# ----------------------------------------------------------------------------- skyline art
def skyline_svg():
    """Original illustration: stylised apartment blocks by the water."""
    import random
    rnd = random.Random(7)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 260" preserveAspectRatio="xMidYMax slice">',
             '<defs><pattern id="w" width="14" height="16" patternUnits="userSpaceOnUse">'
             '<rect x="3" y="4" width="7" height="8" fill="#ffffff" opacity=".38"/></pattern>'
             '<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6fb3d6"/><stop offset="1" stop-color="#2f78a6"/></linearGradient></defs>']
    parts.append('<path d="M0 150 C200 110 360 140 560 120 S980 90 1200 125 S1500 110 1600 130 V260 H0z" fill="#8fb59a" opacity=".75"/>')
    x = -20
    cols = ["#6f8fb5", "#8aa6c6", "#a3bbd6", "#5d7ea8", "#7d9cbf"]
    while x < 1620:
        w = rnd.choice([54, 64, 76, 90, 60])
        h = rnd.randint(70, 190)
        c = rnd.choice(cols)
        y = 214 - h
        parts.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>' % (x, y, w, h, c))
        parts.append('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#w)"/>' % (x, y, w, h))
        if rnd.random() < .4:
            parts.append('<rect x="%d" y="%d" width="%d" height="8" fill="%s"/>' % (x + 6, y - 8, w - 12, c))
        x += w + rnd.choice([-6, 2, 6, 12])
    parts.append('<rect y="214" width="1600" height="46" fill="url(#sea)"/></svg>')
    return "".join(parts)


# ----------------------------------------------------------------------------- main
ROOT_INDEX = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GovBHG - Baekhyeon Hwarang SAR Government</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<noscript><meta http-equiv="refresh" content="0; url=en/"></noscript>
<script>
(function () {
  var l = (navigator.language || "en").toLowerCase(), d = "en/";
  if (l.indexOf("ko") === 0) d = "ko/";
  else if (l.indexOf("zh") === 0) d = /zh-(cn|sg|hans)/.test(l) ? "zh-hans/" : "zh-hant/";
  location.replace(d);
})();
</script></head>
<body style="font-family:sans-serif;padding:2em">
<p><a href="en/">English</a> &middot; <a href="ko/">한국어</a> &middot; <a href="zh-hant/">繁體中文</a> &middot; <a href="zh-hans/">简体中文</a></p>
</body></html>
"""


def main():
    build_registry()
    for _code, folder, _hl, _label in LANGS:
        shutil.rmtree(os.path.join(ROOT, folder), ignore_errors=True)
    shutil.rmtree(os.path.join(ROOT, "zh"), ignore_errors=True)  # legacy folder
    count = 0
    for code, folder, hl, _label in LANGS:
        i = IDX[code]
        for path, info in PAGES.items():
            out_dir = os.path.join(ROOT, folder, path)
            os.makedirs(out_dir, exist_ok=True)
            if info["kind"] == "home":
                txt = home_page(i, hl, path, info)
            elif info["kind"] == "guide":
                txt = guide_page(i, hl, path, info)
            elif info["kind"] == "apps":
                txt = apps_page(i, hl, path, info)
            elif info["kind"] == "form":
                txt = form_page(i, hl, path, info)
            else:
                txt = inner_page(i, hl, path, info)
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(txt)
            count += 1
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_INDEX)
    with open(os.path.join(ROOT, "assets", "skyline.svg"), "w", encoding="utf-8") as f:
        f.write(skyline_svg())
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("built %d pages (%d per language)" % (count, len(PAGES)))


if __name__ == "__main__":
    main()
