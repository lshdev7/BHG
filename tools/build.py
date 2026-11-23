#!/usr/bin/env python3
"""Static site generator for the BHG SAR Government homepage .

Layout and information architecture follow the GovHK residents homepage
(header / language bar / search / mega menu / banner / quick links / online services /
forms / information & services / guidebooks / features / social groups / footer).
No HKSAR assets, logos or text are reused; all content is original.

Usage: python3 tools/build.py   ->  writes index.html, en/, ko/, zh/
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = [  # code, folder, <html lang>, label shown in the language bar
    ("en", "en", "en", "English"),
    ("ko", "ko", "ko", "한국어"),
    ("hant", "zh-hant", "zh-Hant", "繁體中文"),
    ("hans", "zh-hans", "zh-Hans", "简体中文"),
]
IDX = {"en": 0, "ko": 1, "hant": 2, "hans": 3}  # hans is derived from the Traditional text via T2S

# Traditional -> Simplified (char map generated once with OpenCC t2s; phrases override HK-style terms)
T2S = {
    "來":"来","個":"个","們":"们","傭":"佣","傳":"传","僱":"雇","兒":"儿","內":"内",
    "冊":"册","別":"别","劃":"划","動":"动","務":"务","勞":"劳","區":"区","員":"员",
    "問":"问","單":"单","園":"园","圖":"图","執":"执","報":"报","場":"场","婦":"妇",
    "學":"学","專":"专","尋":"寻","對":"对","峴":"岘","帶":"带","廢":"废","徑":"径",
    "徵":"征","憲":"宪","應":"应","換":"换","據":"据","數":"数","於":"于","書":"书",
    "會":"会","業":"业","構":"构","樂":"乐","樓":"楼","橫":"横","檔":"档","權":"权",
    "氣":"气","無":"无","熱":"热","營":"营","獎":"奖","環":"环","療":"疗","發":"发",
    "眾":"众","碼":"码","礙":"碍","稅":"税","簡":"简","簽":"签","約":"约","結":"结",
    "統":"统","網":"网","繳":"缴","聞":"闻","聯":"联","聲":"声","職":"职","與":"与",
    "舉":"举","處":"处","覽":"览","計":"计","訊":"讯","訓":"训","記":"记","訪":"访",
    "設":"设","診":"诊","註":"注","試":"试","話":"话","語":"语","說":"说","課":"课",
    "調":"调","請":"请","證":"证","護":"护","財":"财","責":"责","貿":"贸","資":"资",
    "質":"质","載":"载","連":"连","進":"进","選":"选","醫":"医","長":"长","門":"门",
    "開":"开","關":"关","隱":"隐","電":"电","頁":"页","預":"预","題":"题","額":"额",
    "館":"馆","駕":"驾","駛":"驶","體":"体","點":"点",
}
T2S_PHRASES = [
    ("流動通訊", "移动通信"), ("流動應用程式", "移动应用程序"), ("開放數據入門網站", "开放数据门户网站"),
    ("入門網站", "门户网站"), ("資訊保安", "信息安全"), ("資訊", "信息"), ("數碼", "数字"),
    ("通訊", "通信"), ("智方便", "智方便"),
]


def s2(text):
    for a, b in T2S_PHRASES:
        text = text.replace(a, b)
    return "".join(T2S.get(ch, ch) for ch in text)


# --------------------------------------------------------------------------- UI strings
UI = {
    "site_title": ("Baekhyeon Hwarang SAR Government", "백현화랑특별행정구 정부", "柏峴화랑特別行政區政府"),
    "site_short": ("GovBHG", "정부포털 BHG", "BHG政府入門網站"),
    "region": ("Baekhyeon Hwarang Special Administrative Region", "백현화랑특별행정구", "柏峴화랑特別行政區"),
    "skip": ("Skip to main content", "본문 바로가기", "跳至主要內容"),
    "text_size": ("Text Size", "글자 크기", "字體大小"),
    "languages": ("Languages", "언어", "語言"),
    "search": ("Search All Government", "정부 전체 검색", "搜尋所有政府網頁"),
    "search_btn": ("Search", "검색", "搜尋"),
    "search_none": ("No matching pages found.", "일치하는 페이지가 없습니다.", "找不到相符的網頁。"),
    "search_res": ("Search results", "검색 결과", "搜尋結果"),
    "menu": ("Main Menu", "주 메뉴", "主選單"),
    "toggle_menu": ("Toggle Menu", "메뉴 열기/닫기", "切換選單"),
    "toast": (
        "This page is under construction.",
        "이 페이지는 준비 중입니다.",
        "此頁面正在建設中。",
    ),
    "banner": ("Homepage Banner", "홈페이지 배너", "主頁橫額"),
    "prev": ("Go to previous page", "이전", "上一頁"),
    "next": ("Go to next page", "다음", "下一頁"),
    "quick": ("Quick Links", "바로가기", "快速連結"),
    "top_online": ("Top Online Services", "인기 온라인 서비스", "熱門網上服務"),
    "more_online": ("More Top Online Services >", "인기 온라인 서비스 더 보기 >", "更多熱門網上服務 >"),
    "top_forms": ("Top Government Forms", "인기 정부 서식", "熱門政府表格"),
    "more_forms": ("More Top Government Forms >", "인기 정부 서식 더 보기 >", "更多熱門政府表格 >"),
    "info": ("Government Information & Services", "정부 정보 및 서비스", "政府資訊及服務"),
    "guide": ("Guidebooks", "안내서", "指南"),
    "more_guide": ("More Guidebooks >", "안내서 더 보기 >", "更多指南 >"),
    "features": ("Features", "특집", "專題"),
    "check": ("Check it Out", "함께 보기", "精選推介"),
    "social": ("Social Groups", "사회 그룹", "社群"),
    "top": ("Back To Top", "맨 위로", "返回頁首"),
    "footer_menu": ("Footer Menu", "하단 메뉴", "頁尾選單"),
    "copyright": (
        "© 2026 Baekhyeon Hwarang SAR Government. All rights reserved.",
        "© 2026 백현화랑특별행정구 정부. 모든 권리 보유.",
        "© 2026 柏峴화랑特別行政區政府。版權所有。",
    ),
    "geo": (
        "Located in the Baekhyeon Maeul Complexes 3 and 4, Seongnam.",
        "경기도 성남시 백현마을 3단지·4단지 일대에 위치합니다.",
        "位於城南市柏峴마을 3、4社區一帶。",
    ),
}

TABS = [  # key, label
    ("res", ("Residents", "주민", "居民")),
    ("biz", ("Business & Trade", "비즈니스·무역", "工商貿易")),
    ("non", ("Non-Residents", "비거주자", "非居民")),
]

# Residents categories: (id, label, [sub items])
RES = [
    ("comm", ("Communications & Technology", "통신 및 기술", "通訊及科技"), [
        ("Information Security & Internet Services", "정보보안 및 인터넷 서비스", "資訊保安及互聯網服務"),
        ("Mobile Communications Services", "이동통신 서비스", "流動通訊服務"),
        ("e-Government", "전자정부", "電子政府"),
    ]),
    ("cult", ("Culture, Leisure & Sports", "문화·여가·체육", "文化、康樂及體育"), [
        ("Library Services", "도서관 서비스", "圖書館服務"),
        ("Heritage & Museums", "문화유산 및 박물관", "文物及博物館"),
        ("Parks, Trails & Recreation", "공원·산책로·여가", "公園、步行徑及康樂"),
    ]),
    ("edu", ("Education & Training", "교육 및 훈련", "教育及培訓"), [
        ("Primary & Secondary Education", "초·중등 교육", "小學及中學教育"),
        ("Post-Secondary Education", "고등교육", "專上教育"),
        ("Financial Assistance & Scholarships", "학자금 지원 및 장학금", "財政資助及獎學金"),
    ]),
    ("emp", ("Employment", "고용", "僱傭"), [
        ("Looking for a Job", "구직", "求職"),
        ("Labour Legislation & Guidelines", "노동 법령 및 지침", "勞工法例及指引"),
        ("Occupational Safety & Health", "산업안전보건", "職業安全及健康"),
    ]),
    ("env", ("Environment", "환경", "環境"), [
        ("Waste & Recycling", "폐기물 및 재활용", "廢物及回收"),
        ("Air Quality", "대기질", "空氣質素"),
        ("Nature Conservation", "자연 보전", "自然護理"),
    ]),
    ("gov", ("Government, Law & Order", "정부·법·치안", "政府、法律及秩序"), [
        ("Government Structure", "정부 조직", "政府架構"),
        ("Elections", "선거", "選舉"),
        ("Laws of the SAR", "특별행정구 법령", "區內法例"),
    ]),
    ("health", ("Health & Medical Services", "보건 및 의료 서비스", "衞生及醫療服務"), [
        ("Hospitals & Clinics", "병원 및 의원", "醫院及診所"),
        ("Communicable Diseases", "감염병", "傳染病"),
        ("Mental Health", "정신건강", "精神健康"),
    ]),
    ("house", ("Housing & Social Services", "주거 및 사회복지", "房屋及社會服務"), [
        ("Housing Schemes", "주택 제도", "房屋計劃"),
        ("Building Management", "건물 관리", "樓宇管理"),
        ("Social Security & Assistance", "사회보장 및 지원", "社會保障及援助"),
    ]),
    ("imm", ("Immigration Services", "출입경 서비스", "入境服務"), [
        ("Identity Cards and Right of Abode", "신분증 및 거주권", "身份證及居留權"),
        ("SAR Travel Documents", "특별행정구 여행증명서", "特區旅行證件"),
        ("Immigration Control", "출입경 관리", "入境管制"),
    ]),
    ("tax", ("Taxes & Duties", "세금 및 관세", "稅務及關稅"), [
        ("Salaries Tax & Personal Assessment", "근로소득세 및 개인 과세", "薪俸稅及個人入息課稅"),
        ("Profits Tax", "법인이윤세", "利得稅"),
        ("Tax Return Filing & Payment", "세금 신고 및 납부", "報稅及繳稅"),
    ]),
    ("trans", ("Transport & Motoring", "교통 및 운전", "交通及駕駛"), [
        ("Public Transport", "대중교통", "公共交通"),
        ("Driving Licences & Tests", "운전면허 및 시험", "駕駛執照及考試"),
        ("Cross-Boundary Travel", "경계 통과 이동", "跨境交通"),
    ]),
]

BIZ = [
    ("Business Facilitation", "기업 활동 지원", "營商便利措施"),
    ("Doing Business with the Government", "정부와의 거래", "與政府進行商業交易"),
    ("Registration & Licences", "등록 및 인허가", "註冊及牌照"),
    ("Import & Export", "수출입", "進出口"),
    ("Market Information & Statistics", "시장 정보 및 통계", "市場資訊及統計"),
    ("Support for Local & Foreign Enterprises", "내·외국 기업 지원", "對本地及外地企業的支援"),
    ("Taxes", "세금", "稅務"),
    ("Online Services for Business & Trade", "기업·무역 온라인 서비스", "工商貿易網上服務"),
]
NON = [
    ("Visiting the SAR", "특별행정구 방문", "訪問特區"),
    ("Working in the SAR", "특별행정구 근무", "在特區工作"),
    ("Studying in the SAR", "특별행정구 유학", "在特區升學"),
    ("Living in the SAR", "특별행정구 거주", "在特區生活"),
    ("Doing Business in the SAR", "특별행정구 사업", "在特區營商"),
    ("Online Services for Non-Residents", "비거주자 온라인 서비스", "非居民網上服務"),
]

SLIDES = [  # (title, sub, theme)
    (("The Basic Law of the Baekhyeon Hwarang SAR", "백현화랑특별행정구 기본법", "柏峴화랑特別行政區基本法"),
     ("The constitutional document of the Region", "특별행정구의 헌법적 문서", "特別行政區的憲制性文件"), "flag"),
    (("The Chief Executive's Policy Address", "행정장관 시정연설", "行政長官施政報告"),
     ("Priorities for the year ahead", "새해 시정 우선과제", "來年施政重點"), "a"),
    (("Apply for a SAR Passport", "특별행정구 여권 신청", "申請特區護照"),
     ("Issued by the Immigration Department", "출입경사무처 발급", "由入境事務處簽發"), "b"),
    (("The Regional Flag and Emblem", "특별행정구 기와 휘장", "區旗及區徽"),
     ("Symbols of the Baekhyeon Hwarang SAR", "백현화랑특별행정구의 상징", "柏峴화랑特別行政區的象徵"), "c"),
]

QUICK = [
    ("Press Releases", "보도자료", "新聞公報"),
    ("Public Holidays", "공휴일", "公眾假期"),
    ("Government Telephone Directory", "정부 전화번호부", "政府電話簿"),
    ("Open Data Portal", "공공데이터 포털", "開放數據入門網站"),
    ("Mobile Apps", "모바일 앱", "流動應用程式"),
    ("Webcast Archives", "웹캐스트 보관함", "網上直播檔案"),
    ("Download the Flag & Emblem", "기와 휘장 내려받기", "下載區旗及區徽"),
    ("\"BH Smart\" Resident Digital ID", "\"BH 스마트\" 주민 디지털 신원", "「BH智方便」居民數碼身份"),
]
ONLINE = [
    ("Apply for a SAR Passport", "특별행정구 여권 신청", "申請特區護照"),
    ("Book an Appointment for the Smart Identity Card", "스마트 신분증 신청 예약", "預約申請智能身份證"),
    ("Access the Individual Tax Portal", "개인 납세 포털 이용", "使用個人稅務入門網站"),
    ("Calculate Tax Liability", "납부 세액 계산", "計算稅款"),
]
FORMS = [
    ("Application for a SAR Passport", "특별행정구 여권 신청서", "特區護照申請表"),
    ("Application for a Smart Identity Card", "스마트 신분증 신청서", "智能身份證申請表"),
    ("Application for a Re-entry Permit", "재입경 허가 신청서", "回港證申請表"),
    ("Notification of Change of Address", "주소 변경 신고서", "更改地址通知書"),
    ("Birth Registration Form", "출생 등록 신청서", "出生登記表格"),
]
GUIDES = [
    ("Application for a SAR Passport", "특별행정구 여권 신청 안내", "申請特區護照指南"),
    ("Information on Recreation & Sports", "여가·체육 안내", "康樂及體育資訊指南"),
    ("Driving Test Appointment Booking", "운전시험 예약 안내", "駕駛考試預約指南"),
]
FEATURES = [
    ("Births Registration", "출생 등록", "出生登記"),
    ("Parenting", "육아", "育兒"),
    ("Marriage Registration", "혼인 등록", "婚姻登記"),
    ("Property", "부동산", "物業"),
    ("Elderly Services & Benefits", "노인 서비스 및 혜택", "長者服務及福利"),
    ("Deaths Registration", "사망 등록", "死亡登記"),
]
CHECK = [
    ("Baekhyeon Maeul at a Glance", "백현마을 한눈에 보기", "柏峴마을概覽"),
    ("Regional Flag Design", "기 도안 소개", "區旗設計簡介"),
    ("SAR Passport Features", "특별행정구 여권 안내", "特區護照特色"),
    ("2026 Population Survey", "2026 인구 조사", "2026年人口調查"),
]
SOCIAL = [
    ("Women's Commission", "여성위원회", "婦女事務委員會"),
    ("Youth Portal", "청년 포털", "青年網站"),
    ("Happy Family Info Hub", "행복한 가정 정보센터", "快樂家庭資訊站"),
    ("eElderly", "e-어르신", "長者電子網站"),
    ("Accessibility Hub", "접근성 허브", "無障礙資訊站"),
]
FOOTER = [
    ("About Us", "사이트 소개", "關於我們"),
    ("About Baekhyeon Hwarang", "백현화랑 소개", "關於柏峴화랑"),
    ("Accessibility", "접근성", "無障礙"),
    ("Help", "도움말", "說明"),
    ("Linking to GovBHG", "링크 안내", "連結本網站"),
    ("Copyright Notice", "저작권 안내", "版權公告"),
    ("Disclaimer", "면책 고지", "免責聲明"),
    ("Privacy Policy", "개인정보 처리방침", "私隱政策"),
]


def g(tup, i):
    """Raw (unescaped) text for language index i; index 3 = Simplified, derived from Traditional."""
    return s2(tup[2]) if i == 3 else tup[i]


def t(tup, i):
    return html.escape(g(tup, i))


def ph(label, i, cls="", extra=""):
    """Placeholder link (page under construction)."""
    c = f' class="{cls}"' if cls else ""
    return f'<a href="#" data-s{c}{extra}>{t(label, i)}</a>'


def build_page(code, folder, htmllang, i):
    u = lambda k: t(UI[k], i)
    # header language links
    lang_links = []
    for c, f, hl, lab in LANGS:
        if c == code:
            lang_links.append(f'<li><a class="cur" href="../{f}/" lang="{hl}" aria-current="true">{lab}</a></li>')
        else:
            lang_links.append(f'<li><a href="../{f}/" lang="{hl}" hreflang="{hl}">{lab}</a></li>')
    langs_html = "\n".join(lang_links)

    # mega menu panels
    res_cols = []
    for cid, lab, subs in RES:
        items = "".join(f"<li>{ph(s, i)}</li>" for s in subs)
        res_cols.append(f'<div class="mm-col"><h4>{ph(lab, i)}</h4><ul>{items}</ul></div>')
    res_panel = "".join(res_cols)
    biz_panel = '<div class="mm-col wide"><ul>' + "".join(f"<li>{ph(s, i)}</li>" for s in BIZ) + "</ul></div>"
    non_panel = '<div class="mm-col wide"><ul>' + "".join(f"<li>{ph(s, i)}</li>" for s in NON) + "</ul></div>"
    panels = {"res": res_panel, "biz": biz_panel, "non": non_panel}

    tabs_html = "".join(
        f'<li><button type="button" class="tab" aria-expanded="false" aria-controls="mm-{k}" data-panel="mm-{k}">{t(lab, i)}</button></li>'
        for k, lab in TABS
    )
    panels_html = "".join(
        f'<div class="mm-panel" id="mm-{k}" hidden><div class="wrap mm-grid">{panels[k]}</div></div>' for k, _ in TABS
    )

    slides_html = []
    for n, (title, sub, theme) in enumerate(SLIDES):
        extra = '<img class="slide-flag" src="../assets/flag.jpg" alt="" width="300" height="201">' if theme == "flag" else ""
        slides_html.append(
            f'<div class="slide theme-{theme}" role="group" aria-roledescription="slide" '
            f'aria-label="{n+1} / {len(SLIDES)}"{" hidden" if n else ""}>'
            f'<div class="slide-text"><h3><a href="#" data-s>{t(title, i)}</a></h3><p>{t(sub, i)}</p></div>{extra}</div>'
        )
    dots = "".join(
        f'<button type="button" class="dot{" on" if n == 0 else ""}" aria-label="{n+1}" data-i="{n}"></button>'
        for n in range(len(SLIDES))
    )

    def ul(items, cls=""):
        return f'<ul class="{cls}">' + "".join(f"<li>{ph(x, i)}</li>" for x in items) + "</ul>"

    tiles = "".join(
        f'<li><a href="#" data-s><span class="ico" aria-hidden="true">{t(lab, i)[0]}</span>{t(lab, i)}</a></li>'
        for _, lab, _ in RES
    ) + f'<li><a href="#" data-s><span class="ico" aria-hidden="true">★</span>{t(("Government Websites & Officers", "정부 웹사이트 및 담당 부서", "政府網站及人員"), i)}</a></li>'

    footer_html = "".join(f"<li>{ph(x, i)}</li>" for x in FOOTER)

    title = f'{g(UI["site_short"], i)} — {g(UI["site_title"], i)}'
    page = f"""<!doctype html>
<html lang="{htmllang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{u('site_title')}">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body class="lang-{code}" data-toast="{u('toast')}" data-nores="{u('search_none')}">
<a class="skip" href="#main">{u('skip')}</a>

<header class="top">
  <div class="bar">
    <div class="wrap bar-in">
      <ul class="tools">
        <li class="ts" aria-label="{u('text_size')}"><span>{u('text_size')}</span>
          <button type="button" data-size="0" aria-label="A-">A</button>
          <button type="button" data-size="1" aria-label="A" class="on">A</button>
          <button type="button" data-size="2" aria-label="A+">A</button></li>
        <li class="lg"><span>{u('languages')}</span><ul class="langs">{langs_html}</ul></li>
      </ul>
    </div>
  </div>
  <div class="wrap head">
    <a class="brand" href="./" aria-label="{u('site_short')}">
      <img src="../assets/flag.jpg" alt="" width="84" height="56">
      <span class="brand-t"><strong>{u('site_short')}</strong><em>{u('region')}</em></span>
    </a>
    <form class="search" role="search" id="sf">
      <label for="q" class="vh">{u('search')}</label>
      <input id="q" type="search" placeholder="{u('search')}" autocomplete="off">
      <button type="submit">{u('search_btn')}</button>
    </form>
    <button type="button" class="burger" aria-expanded="false" aria-controls="nav">{u('toggle_menu')}</button>
  </div>
  <nav class="nav" id="nav" aria-label="{u('menu')}">
    <div class="wrap"><ul class="tabs">{tabs_html}</ul></div>
    {panels_html}
  </nav>
</header>

<section id="results" class="results" hidden aria-live="polite">
  <div class="wrap"><h2>{u('search_res')}</h2><ul id="results-list"></ul></div>
</section>

<main id="main">
  <h1 class="vh">{u('site_title')}</h1>

  <section class="wrap hero" aria-label="{u('banner')}" aria-roledescription="carousel">
    <div class="banner">
      {''.join(slides_html)}
      <button type="button" class="nav-b prev" aria-label="{u('prev')}">‹</button>
      <button type="button" class="nav-b next" aria-label="{u('next')}">›</button>
      <div class="dots">{dots}</div>
    </div>
    <aside class="quick">
      <h3>{u('quick')}</h3>
      {ul(QUICK)}
    </aside>
  </section>

  <section class="wrap cols">
    <div class="box">
      <h3>{u('top_online')}</h3>
      {ul(ONLINE)}
      <p class="more"><a href="#" data-s>{u('more_online')}</a></p>
    </div>
    <div class="box">
      <h3>{u('top_forms')}</h3>
      {ul(FORMS)}
      <p class="more"><a href="#" data-s>{u('more_forms')}</a></p>
    </div>
  </section>

  <section class="wrap info">
    <h3>{u('info')}</h3>
    <ul class="tiles">{tiles}</ul>
  </section>

  <section class="wrap cols three">
    <div class="box"><h3>{u('guide')}</h3>{ul(GUIDES)}<p class="more"><a href="#" data-s>{u('more_guide')}</a></p></div>
    <div class="box"><h3>{u('features')}</h3>{ul(FEATURES, 'two')}</div>
    <div class="box"><h3>{u('check')}</h3>{ul(CHECK)}</div>
  </section>

  <section class="wrap social">
    <h3>{u('social')}</h3>
    {ul(SOCIAL, 'inline')}
  </section>
</main>

<footer class="foot">
  <div class="wrap">
    <p class="toplink"><a href="#top" id="totop">▲ {u('top')}</a></p>
    <nav aria-label="{u('footer_menu')}"><ul class="fmenu">{footer_html}</ul></nav>
    <p class="geo">{u('geo')}</p>
    <p class="copy">{u('copyright')}</p>
  </div>
</footer>
<div id="toast" role="status" aria-live="polite" hidden></div>
<script src="../assets/site.js"></script>
</body>
</html>
"""
    return page


ROOT_INDEX = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GovBHG — Baekhyeon Hwarang SAR Government</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<noscript><meta http-equiv="refresh" content="0; url=en/"></noscript>
<script>
(function () {
  var l = (navigator.language || "en").toLowerCase(), d = "en/";
  if (l.indexOf("ko") === 0) d = "ko/";
  else if (l.indexOf("zh") === 0) d = /zh-(cn|sg|hans)/.test(l) ? "zh-hans/" : "zh-hant/";
  location.replace(d);
})();
</script>
</head>
<body style="font-family:sans-serif;padding:2em">
<p><a href="en/">English</a> · <a href="ko/">한국어</a> · <a href="zh-hant/">繁體中文</a> · <a href="zh-hans/">简体中文</a></p>
</body>
</html>
"""


def main():
    for code, folder, hl, _ in LANGS:
        d = os.path.join(ROOT, folder)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(build_page(code, folder, hl, IDX[code]))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_INDEX)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("built:", ", ".join(f[1] for f in LANGS))


if __name__ == "__main__":
    main()
