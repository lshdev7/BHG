# -*- coding: utf-8 -*-
"""Content for the Baekhyeon Hwarang SAR Government portal (GovBHG).

Every text is a tuple (English, Korean, Traditional Chinese). Simplified Chinese is derived
from the Traditional text at build time (see t2s_map.py / build.py).
Structure follows the GovHK information architecture; all wording is original.
"""

# ----------------------------------------------------------------------------- site UI
UI = {
    "site": ("GovBHG", "정부포털 BHG", "BHG政府一站通"),
    "site_full": ("Baekhyeon Hwarang SAR Government One-stop Portal", "백현화랑 특별행정구 정부 원스톱 포털", "柏峴화랑特別行政區政府一站通"),
    "wm_cn": ("柏峴화랑政府", "柏峴화랑政府", "柏峴화랑政府"),
    "skip": ("Skip to main content", "본문 바로가기", "跳至主要內容"),
    "text_size": ("Text Size", "글자 크기", "字體大小"),
    "languages": ("Languages", "언어", "語言"),
    "other_lang": ("Other languages", "다른 언어", "其他語言"),
    "search_ph": ("Search All Government", "정부 전체 검색", "搜尋所有政府網頁"),
    "search_btn": ("Search", "검색", "搜尋"),
    "hot": ("Hot searches:", "인기 검색어:", "熱門搜尋："),
    "adv": ("Advanced Search", "상세 검색", "進階搜尋"),
    "res_title": ("Search results", "검색 결과", "搜尋結果"),
    "no_res": ("No matching pages found.", "일치하는 페이지가 없습니다.", "找不到相符的網頁。"),
    "toggle": ("Toggle Menu", "메뉴", "選單"),
    "main_menu": ("Main Menu", "주 메뉴", "主選單"),
    "home": ("Home", "홈", "首頁"),
    "quick": ("Quick Links", "바로가기", "快速連結"),
    "top_online": ("Top Online Services", "인기 온라인 서비스", "熱門網上服務"),
    "top_forms": ("Top Government Forms", "인기 정부 서식", "熱門政府表格"),
    "more": ("More", "더 보기", "更多"),
    "info": ("Government Information & Services", "정부 정보 및 서비스", "政府資訊及服務"),
    "guide": ("Guidebooks", "안내서", "指南"),
    "features": ("Features", "특집", "專題"),
    "check": ("Check it Out", "함께 보기", "精選推介"),
    "social": ("Social Groups", "사회 그룹", "社群"),
    "top": ("Back To Top", "맨 위로", "返回頁首"),
    "expand_all": ("Expand All", "모두 펼치기", "全部展開"),
    "collapse_all": ("Collapse All", "모두 접기", "全部收合"),
    "prev": ("Previous", "이전", "上一頁"),
    "next": ("Next", "다음", "下一頁"),
    "helpful": ("Found this page helpful?", "이 페이지가 도움이 되었나요?", "本頁內容對你有幫助嗎？"),
    "review": ("Last review date: ", "최종 검토일: ", "修訂日期："),
    "review_val": ("November 2026", "2026년 11월", "2026年11月"),
    "related": ("Related Information", "관련 정보", "相關內容"),
    "stub": (
        "Information on this topic is being prepared. Please browse the related topics in the left-hand menu.",
        "이 주제의 정보는 준비 중입니다. 왼쪽 메뉴의 관련 주제를 이용해 주세요.",
        "此主題的資料現正準備中，請瀏覽左方選單的相關主題。",
    ),
    "stub_nomenu": (
        "Information on this topic is being prepared.",
        "이 주제의 정보는 준비 중입니다.",
        "此主題的資料現正準備中。",
    ),
    "copyright": (
        "© 2026 Baekhyeon Hwarang SAR Government. All rights reserved.",
        "© 2026 백현화랑 특별행정구 정부. 모든 권리 보유.",
        "© 2026 柏峴화랑特別行政區政府。版權所有。",
    ),
    "geo": (
        "Located in the Baekhyeon Maeul Complexes 3 and 4, Seongnam.",
        "경기도 성남시 백현마을 3단지·4단지 일대에 위치합니다.",
        "位於城南市柏峴마을 3、4社區一帶。",
    ),
}

TABS = [
    ("residents", ("Residents", "주민", "居民")),
    ("business", ("Business & Trade", "비즈니스·무역", "工商貿易")),
    ("nonresidents", ("Non-Residents", "비거주자", "非居民")),
]

HOT = [
    ("passport", ("Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권", "柏峴화랑特別行政區護照")),
    ("idcard", ("Smart Identity Card", "스마트 신분증", "智能身份證")),
    ("etax", ("Individual Tax Portal", "개인 납세 포털", "個人稅務入門網站")),
]

# ----------------------------------------------------------------------------- site tree
# tab -> list of (cat_slug, title, [(sub_slug, title), ...])
TREE = {}

TREE["residents"] = [
    ("communication", ("Communications & Technology", "통신 및 기술", "通訊及科技"), [
        ("infosec", ("Information Security & Internet Services", "정보보안 및 인터넷 서비스", "資訊保安及互聯網服務")),
        ("mobilecomm", ("Mobile Communications Services", "이동통신 서비스", "流動通訊服務")),
        ("governmentsupport", ("Government Support", "정부 지원", "政府支援")),
        ("publicresources", ("Public Facilities & Resources", "공공시설 및 자원", "公共設施及資源")),
        ("smartcity", ("Baekhyeon Hwarang Smart City", "백현화랑 스마트시티", "柏峴화랑智慧城市")),
        ("egovernment", ("e-Government", "전자정부", "電子政府")),
        ("tv", ("TV & Radio Broadcasting", "TV·라디오 방송", "電視及電台廣播")),
        ("fixedline", ("Fixed Line Services", "유선통신 서비스", "固網服務")),
    ]),
    ("culture", ("Culture, Leisure & Sports", "문화·여가·체육", "文化、康樂及體育"), [
        ("recreation", ("Recreation & Sports", "여가 및 체육", "康樂及體育")),
        ("reading", ("Library Services", "도서관 서비스", "圖書館服務")),
        ("performart", ("Culture & Arts", "문화·예술", "文化藝術")),
        ("fun", ("Fun in Baekhyeon Hwarang", "백현화랑 특별행정구 즐기기", "柏峴화랑特別行政區好去處")),
        ("museum", ("Heritage & Museums", "문화유산 및 박물관", "文物及博物館")),
        ("trail", ("Parks, Trails & Campgrounds", "공원·산책로·캠핑장", "公園、遠足徑及營地")),
        ("events", ("Major Events & Activities", "주요 행사 및 활동", "大型活動")),
        ("travel", ("Reminder of Travelling Outside Baekhyeon Hwarang", "백현화랑 특별행정구 밖 여행 안내", "離境外遊提示")),
        ("mobile", ("Mobile Apps", "모바일 앱", "流動應用程式")),
    ]),
    ("education", ("Education & Training", "교육 및 훈련", "教育及培訓"), [
        ("preprimary", ("Pre-Primary Education", "유아 교육", "學前教育")),
        ("primary", ("Primary Education", "초등교육", "小學教育")),
        ("secondary", ("Secondary Education", "중등교육", "中學教育")),
        ("postsecondary", ("Post-Secondary Education", "고등교육", "專上教育")),
        ("continuinged", ("Continuing Education, Vocational Training & Elderly Learning", "평생교육·직업훈련·노인학습", "持續教育、職業培訓及長者學習")),
        ("financialassistance", ("Financial Assistance & Scholarships", "학자금 지원 및 장학금", "財政資助及獎學金")),
        ("qf", ("Qualifications Framework", "자격체계", "資歷架構")),
        ("specialservice", ("Special & Other Education Services", "특수·기타 교육 서비스", "特殊及其他教育服務")),
        ("examination", ("Examinations & Assessments", "시험 및 평가", "考試及評核")),
        ("highlights", ("Highlights, Public Participation & Contacts", "주요 소식·시민 참여·연락처", "要點、公眾參與及聯絡")),
    ]),
    ("employment", ("Employment", "고용", "僱傭"), [
        ("jobsearch", ("Looking for a Job", "구직", "求職")),
        ("recruitment", ("Recruitment (Information for Employers)", "채용(고용주 안내)", "招聘（僱主資訊）")),
        ("mpf", ("Mandatory Provident Fund (MPF) System", "강제적립기금(MPF) 제도", "強制性公積金（強積金）制度")),
        ("labour", ("Labour Legislation & Guidelines", "노동 법령 및 지침", "勞工法例及指引")),
        ("employee", ("Employees' Protection & Compensation", "근로자 보호 및 보상", "僱員保障及補償")),
        ("safety", ("Occupational Safety & Health", "산업안전보건", "職業安全及健康")),
        ("retraining", ("Government Incentives & Retraining", "정부 지원금 및 재교육", "政府津貼及再培訓")),
        ("workingoutside", ("Working Outside Baekhyeon Hwarang", "백현화랑 특별행정구 밖 근무", "於柏峴화랑以外地區工作")),
        ("registration", ("Registration & Licensing", "등록 및 면허", "註冊及發牌")),
    ]),
    ("environment", ("Environment", "환경", "環境"), [
        ("public", ("Public Participation", "시민 참여", "公眾參與")),
        ("waste", ("Waste & Recycling", "폐기물 및 재활용", "廢物及回收")),
        ("air", ("Air Quality", "대기질", "空氣質素")),
        ("sustainable", ("Sustainable Development", "지속가능발전", "可持續發展")),
        ("noise", ("Noise", "소음", "噪音")),
        ("global", ("Global Environment", "지구 환경", "全球環境")),
        ("conservation", ("Nature Conservation", "자연 보전", "自然護理")),
        ("water", ("Water Quality", "수질", "水質")),
        ("compliance", ("Environmental Compliance", "환경 법규 준수", "環保合規")),
        ("eap", ("Environmental Assessment & Planning", "환경 평가 및 계획", "環境評估及規劃")),
        ("support", ("Industries & Trade Support", "산업·무역 지원", "工商業支援")),
    ]),
    ("government", ("Government, Law & Order", "정부·법·치안", "政府、法律及秩序"), [
        ("political", ("Government Structure", "정부 조직", "政府架構")),
        ("policy", ("Accounts of the Government and Government Reports", "정부 회계 및 보고서", "政府帳目及報告")),
        ("payment", ("Payments of Government Bills", "정부 청구서 납부", "繳付政府賬單")),
        ("publication", ("Government Information and Publications", "정부 정보 및 간행물", "政府資訊及刊物")),
        ("voting", ("Elections", "선거", "選舉")),
        ("external", ("External Affairs", "대외 업무", "對外事務")),
        ("law", ("Laws of Baekhyeon Hwarang", "백현화랑 특별행정구 법령", "柏峴화랑特別行政區法例")),
        ("legal", ("Legal Advice and Support", "법률 자문 및 지원", "法律意見及支援")),
        ("rights", ("Rights", "권리", "權利")),
        ("crime", ("Public Order", "공공질서", "公共秩序")),
    ]),
    ("health", ("Health & Medical Services", "보건 및 의료 서비스", "衞生及醫療服務"), [
        ("hosp", ("Hospitals & Clinics", "병원 및 의원", "醫院及診所")),
        ("chinesemedicine", ("Chinese Medicine", "한의학", "中醫藥")),
        ("foodsafe", ("Food Safety & Nutrition", "식품 안전 및 영양", "食物安全及營養")),
        ("medianddevice", ("Medicine & Medical Devices", "의약품 및 의료기기", "藥物及醫療器械")),
        ("commdiseases", ("Communicable Diseases", "감염병", "傳染病")),
        ("healthadvice", ("Health Advice & Disease Prevention", "건강 상담 및 질병 예방", "健康建議及疾病預防")),
        ("childhealth", ("Child Health", "아동 건강", "兒童健康")),
        ("mental", ("Mental Health", "정신건강", "精神健康")),
        ("addictions", ("Drug Abuse & Other Addictions", "약물 남용 및 중독", "濫用藥物及其他成癮")),
        ("sexedu", ("Sex & Reproductive Health", "성·생식 건강", "性與生殖健康")),
        ("rehab", ("Rehabilitation & Supports", "재활 및 지원", "復康及支援")),
        ("donation", ("Donation", "기증", "捐贈")),
    ]),
    ("housing", ("Housing & Social Services", "주거 및 사회복지", "房屋及社會服務"), [
        ("publichousing", ("Public Housing and Subsidised Home Ownership Schemes", "공공주택 및 보조 주택 소유 제도", "公共房屋及資助自置居所計劃")),
        ("private", ("Private Property & Building Management", "민간 부동산 및 건물 관리", "私人物業及樓宇管理")),
        ("water", ("Water & Sewage", "상하수도", "水務及排污")),
        ("maintenance", ("Home Maintenance, Hygiene & Safety", "주택 유지·위생·안전", "家居維修、衞生及安全")),
        ("postal", ("Postal Services", "우편 서비스", "郵政服務")),
        ("moving", ("Moving Home", "이사", "搬遷")),
        ("social", ("Social Services", "사회 서비스", "社會服務")),
        ("security", ("Social Security & Assistance", "사회보장 및 지원", "社會保障及援助")),
        ("charity", ("Charitable Activities", "자선 활동", "慈善活動")),
    ]),
    ("immigration", ("Immigration Services", "출입경 서비스", "入境服務"), [
        ("idcard", ("Identity Cards and Right of Abode", "신분증 및 거주권", "身份證及居留權")),
        ("traveldoc", ("Baekhyeon Hwarang SAR Travel Documents", "백현화랑 특별행정구 여행증명서", "柏峴화랑特別行政區旅行證件")),
        ("bdmreg", ("Births, Deaths and Marriage Registration", "출생·사망·혼인 등록", "出生、死亡及婚姻登記")),
        ("nonpermanent", ("Services for Non-permanent Residents", "비영주 주민 서비스", "非永久性居民服務")),
        ("control", ("Immigration Control", "출입경 관리", "入境管制")),
        ("outsidesar", ("Assistance Outside Baekhyeon Hwarang", "백현화랑 특별행정구 밖 지원", "柏峴화랑以外地區的協助")),
        ("nationality", ("Korean Nationality", "대한민국 국적", "大韓民國國籍")),
        ("records", ("Application for Personal Data / Information of Immigration Department", "출입경사무처 개인정보·자료 신청", "申請入境事務處的個人資料／資訊")),
    ]),
    ("taxes", ("Taxes & Duties", "세금 및 관세", "稅務及關稅"), [
        ("salaries", ("Salaries Tax & Personal Assessment", "근로소득세 및 개인 과세", "薪俸稅及個人入息課稅")),
        ("etax", ("eTAX - Individual Tax Portal (ITP)", "eTAX - 개인 납세 포털(ITP)", "稅務易 - 個人稅務入門網站")),
        ("profits", ("Profits Tax", "법인이윤세", "利得稅")),
        ("property", ("Property Tax", "재산세", "物業稅")),
        ("taxfiling", ("Tax Return Filing, Enquiry & Payment", "세금 신고·문의·납부", "報稅、查詢及繳稅")),
        ("stamp", ("Stamp Duty", "인지세", "印花稅")),
        ("commodities", ("Dutiable Commodities", "과세 물품", "應課稅品")),
        ("motortax", ("Motor Vehicle First Registration Tax", "자동차 최초 등록세", "汽車首次登記稅")),
    ]),
    ("transport", ("Transport & Motoring", "교통 및 운전", "交通及駕駛"), [
        ("publictransport", ("Public Transport in Baekhyeon Hwarang", "백현화랑 특별행정구 대중교통", "柏峴화랑特別行政區公共交通")),
        ("road", ("Road Network & Facilities", "도로망 및 시설", "道路網絡及設施")),
        ("traffic", ("Road and Traffic Conditions & Special Arrangements", "도로·교통 상황 및 특별 조치", "道路及交通消息和特別安排")),
        ("driving", ("Driving Licences & Tests", "운전면허 및 시험", "駕駛執照及考試")),
        ("vehicle", ("Vehicle Licence, Registration & Examination", "차량 면허·등록·검사", "車輛牌照、登記及檢驗")),
        ("crossboundary", ("Cross-Boundary Travel", "경계 통과 이동", "跨境交通")),
        ("air", ("Air Passenger Services", "항공 여객 서비스", "航空旅客服務")),
        ("vessel", ("Vessel Operator & Pilot Licensing", "선박 운영자·도선사 면허", "船隻營運人及引水員發牌")),
        ("safetyinfo", ("Safety Measures / Information", "안전 조치·정보", "安全措施／資訊")),
    ]),
]

TREE["business"] = [
    ("csr", ("Corporate Social Responsibility", "기업의 사회적 책임", "企業社會責任"), [
        ("involvement", ("Corporate Involvement in Community", "지역사회 참여", "企業參與社區")),
        ("ethics", ("Business Ethics", "기업 윤리", "商業道德")),
    ]),
    ("korea", ("Doing Business in/with the Rest of Korea", "대한민국 내 타 지역과의 사업", "與韓國其他地區營商"), [
        ("trade", ("Information on Domestic Trade", "국내 교역 정보", "國內貿易資訊")),
        ("arrangement", ("Closer Economic Partnership Arrangement", "경제협력 강화 협정", "更緊密經貿關係安排")),
    ]),
    ("businessgov", ("Doing Business with the Government", "정부와의 거래", "與政府進行商業交易"), [
        ("selling", ("Selling to the Government", "정부에 판매", "向政府供應貨品及服務")),
        ("buying", ("Buying from the Government", "정부로부터 구매", "向政府購買")),
        ("payment", ("Payment of Government Bills", "정부 청구서 납부", "繳付政府賬單")),
    ]),
    ("ecommerce", ("E-commerce & Information Security", "전자상거래 및 정보보안", "電子商貿及資訊保安"), [
        ("ecom", ("E-commerce", "전자상거래", "電子商貿")),
        ("infosec", ("Information Security", "정보보안", "資訊保安")),
    ]),
    ("global", ("Global Trade, Import & Export", "국제 무역·수출입", "環球貿易、進出口"), [
        ("importexport", ("Import & Export", "수출입", "進出口")),
        ("logistics", ("Logistics", "물류", "物流")),
        ("quality", ("Quality Assurance, Product Standards & Accreditation", "품질 보증·제품 표준·인증", "品質保證、產品標準及認可")),
    ]),
    ("hr", ("Human Resources", "인적 자원", "人力資源"), [
        ("equal", ("Equal Opportunities & Privacy Protection on Employment", "고용상 기회균등 및 사생활 보호", "僱傭的平等機會及私隱保障")),
        ("recruit", ("Recruitment", "채용", "招聘")),
    ]),
    ("market", ("Market Information & Statistics", "시장 정보 및 통계", "市場資訊及統計"), [
        ("economic", ("Economic Report & Business Statistics", "경제 보고서 및 기업 통계", "經濟報告及商業統計")),
        ("industry", ("Market & Industry Information", "시장·산업 정보", "市場及行業資訊")),
    ]),
    ("registration", ("Registration & Licences", "등록 및 인허가", "註冊及牌照"), [
        ("company", ("Business & Company Registration", "사업자·법인 등록", "商業及公司註冊")),
        ("licensing", ("Licensing & Permits", "인허가", "牌照及許可證")),
        ("ip", ("Intellectual Property", "지식재산", "知識產權")),
    ]),
    ("support", ("Support for Local & Foreign Enterprises", "내·외국 기업 지원", "對本地及外地企業的支援"), [
        ("local", ("Support for Local Enterprises & SMEs", "내국 기업·중소기업 지원", "對本地企業及中小企的支援")),
        ("foreign", ("Support for Foreign Enterprises", "외국 기업 지원", "對外地企業的支援")),
        ("funding", ("Government Funding Schemes", "정부 지원 사업", "政府資助計劃")),
    ]),
    ("taxes", ("Taxes", "세금", "稅務"), [
        ("profittax", ("Profits Tax", "법인이윤세", "利得稅")),
        ("obligations", ("Tax Obligations of Business Operators", "사업자의 납세 의무", "營商者的稅務責任")),
        ("employer", ("Tax Obligations of Employers", "고용주의 납세 의무", "僱主的稅務責任")),
    ]),
]

TREE["nonresidents"] = [
    ("visiting", ("Visiting Baekhyeon Hwarang", "백현화랑 특별행정구 방문", "訪問柏峴화랑特別行政區"), [
        ("attractions", ("City Attractions", "도시 명소", "城市景點")),
        ("travelinfo", ("Useful Travel Information", "여행 유용 정보", "實用旅遊資訊")),
        ("protection", ("Protection & Safety of Visitors", "방문객 보호 및 안전", "旅客保障及安全")),
    ]),
    ("working", ("Working in Baekhyeon Hwarang", "백현화랑 특별행정구 근무", "在柏峴화랑工作"), [
        ("employment", ("Employment in Baekhyeon Hwarang", "백현화랑 특별행정구 내 고용", "在柏峴화랑就業")),
        ("taxation", ("Taxation in Baekhyeon Hwarang", "백현화랑 특별행정구 세금", "柏峴화랑特別行政區稅務")),
    ]),
    ("studying", ("Studying in Baekhyeon Hwarang", "백현화랑 특별행정구 유학", "在柏峴화랑升學"), [
        ("eduinfo", ("Education Information", "교육 정보", "教育資訊")),
        ("support", ("Support & Financial Assistance", "지원 및 학자금", "支援及財政資助")),
    ]),
    ("visarequire", ("Immigration Services", "출입경 서비스", "入境服務"), [
        ("general", ("General Visa Requirements", "일반 비자 요건", "一般簽證規定")),
        ("visasentrypermits", ("Introduction & Application for Visas / Entry Permits", "비자·입경허가 안내 및 신청", "簽證／進入許可證簡介及申請")),
        ("echannel", ("Automated Immigration Clearance (e-Channel) Service for Visitors", "방문객 자동 출입경 심사(e-Channel)", "旅客自助出入境檢查（e-道）服務")),
        ("records", ("Application for Personal Data / Information of Immigration Department", "출입경사무처 개인정보·자료 신청", "申請入境事務處的個人資料／資訊")),
    ]),
    ("living", ("Living in Baekhyeon Hwarang", "백현화랑 특별행정구 생활", "在柏峴화랑生活"), [
        ("housing", ("Housing", "주거", "房屋")),
        ("health", ("Health & Medical Services", "보건 및 의료 서비스", "衞生及醫療服務")),
    ]),
    ("doingbusiness", ("Doing Business in Baekhyeon Hwarang", "백현화랑 특별행정구 사업", "在柏峴화랑營商"), [
        ("setup", ("Setting up a Business", "사업 시작", "開辦業務")),
        ("support", ("Business Support", "사업 지원", "營商支援")),
    ]),
]

# ----------------------------------------------------------------------------- home content
HERO_CARDS = [  # (title, color, image or None)
    (("The First Five-Year Plan for Economic and Social Development of the Baekhyeon Hwarang Special Administrative Region (2026 - 2030)",
      "백현화랑 특별행정구 경제·사회 발전 제1차 5개년 계획(2026-2030)",
      "柏峴화랑特別行政區經濟社會發展第一個五年規劃（2026-2030）"), "#0b4fa3", None),
    (("The Chief Executive's 2026 Policy Address", "행정장관 2026년 시정연설", "行政長官2026年施政報告"), "#cfe8d2", "dark"),
    (("Founding of the Baekhyeon Hwarang Special Administrative Region", "백현화랑 특별행정구 출범", "柏峴화랑特別行政區成立"), "#b3001b", None),
    (("The Basic Law of the Baekhyeon Hwarang SAR", "백현화랑 특별행정구 기본법", "柏峴화랑特別行政區基本法"), "#17294f", "flag"),
    (("The Regional Flag and Emblem", "백현화랑 특별행정구 기와 휘장", "區旗及區徽"), "#0e2c5a", "flag"),
    (("Apply for a Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照"), "#24407a", None),
    (("2026 Population Census", "2026 인구총조사", "2026年人口普查"), "#d8c8e8", "dark"),
    (("Smart Identity Card Appointment Booking", "스마트 신분증 예약 신청", "預約申領智能身份證"), "#3a6ea5", None),
]

QUICK = [
    ("flag", ("Download the Regional Flag & Emblem", "기와 휘장 내려받기", "下載區旗及區徽")),
    ("crossboundary", ("Cross-boundary Public Services", "경계 통과 공공서비스", "跨境公共服務")),
    ("press", ("Press Releases", "보도자료", "新聞公報")),
    ("news", ("News Centre", "뉴스센터", "新聞網")),
    ("holidays", ("Public Holidays", "공휴일", "公眾假期")),
    ("directory", ("Government Telephone Directory", "정부 전화번호부", "政府電話簿")),
    ("opendata", ("Open Data Portal", "공공데이터 포털", "開放數據入門網站")),
    ("apps", ("Mobile Apps", "모바일 앱", "流動應用程式")),
    ("webcast", ("Webcast Archives", "웹캐스트 보관함", "網上直播檔案")),
    ("bhsmart", ("\"BH Smart\"", "\"BH 스마트\"", "「BH智方便」")),
]

ONLINE = {
    "residents": [
        ("etaxlogin", ("Access eTAX - Individual Tax Portal (ITP) Services", "eTAX - 개인 납세 포털(ITP) 서비스 이용", "使用稅務易 - 個人稅務入門網站（ITP）服務")),
        ("passport", ("Apply for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照")),
        ("idcard", ("Book Appointment to Apply for BHG Smart Identity Card", "스마트 신분증 신청 예약", "預約申領柏峴화랑智能身份證")),
        ("appstatus", ("Enquire about Application Status (Application for visas, entry permits or verification of eligibility for permanent identity card)", "신청 현황 조회(비자·입경허가 신청 또는 영구 신분증 자격 확인)", "查詢申請進度（簽證、進入許可證申請或永久性居民身份證資格核實）")),
        ("taxcalc", ("Calculate Tax Liability under Salaries Tax and Personal Assessment", "근로소득세 및 개인 과세 납부 세액 계산", "計算薪俸稅及個人入息課稅的稅款")),
    ],
    "business": [
        ("brapply", ("Apply for Business Registration", "사업자 등록 신청", "申請商業登記")),
        ("etaxbiz", ("Access eTAX - Business Tax Portal", "eTAX - 기업 납세 포털 이용", "使用稅務易 - 商業稅務入門網站")),
        ("tradedecl", ("Submit Trade Declaration", "무역 신고 제출", "提交貿易報關")),
        ("licenceapp", ("Apply for Licences and Permits", "인허가 신청", "申請牌照及許可證")),
        ("tender", ("Search Government Tender Notices", "정부 입찰 공고 검색", "搜尋政府招標公告")),
    ],
    "nonresidents": [
        ("visaapply", ("Apply for a Visa / Entry Permit", "비자·입경허가 신청", "申請簽證／進入許可證")),
        ("appstatus", ("Enquire about Application Status", "신청 현황 조회", "查詢申請進度")),
        ("echannel", ("Enrol for the e-Channel Service for Visitors", "방문객 e-Channel 등록", "登記使用旅客e-道服務")),
        ("travelinfo", ("Check Travel Information", "여행 정보 확인", "查閱旅遊資訊")),
        ("holidays", ("Check Public Holidays", "공휴일 확인", "查閱公眾假期")),
    ],
}
FORMS = {
    "residents": [
        ("govjobs", ("Apply for Government Jobs", "정부 일자리 지원", "申請政府職位")),
        ("pa", ("Election for Personal Assessment and Claim for Deductions & Allowances", "개인 과세 선택 및 공제·감면 신청", "選擇個人入息課稅及申索扣除與免稅額")),
        ("vehiclerenew", ("Renew Vehicle Licence", "차량 면허 갱신", "續領車輛牌照")),
        ("drivinglic", ("Apply for Full Driving Licence & Driving Instructor's Licence", "정식 운전면허 및 운전강사 면허 신청", "申請正式駕駛執照及駕駛導師執照")),
        ("addresschange", ("Notification of Change of Postal Address", "우편 주소 변경 신고", "更改郵寄地址通知書")),
    ],
    "business": [
        ("brform", ("Business Registration Application Form", "사업자 등록 신청서", "商業登記申請表")),
        ("taxreturn", ("Profits Tax Return", "법인이윤세 신고서", "利得稅報稅表")),
        ("employerreturn", ("Employer's Return of Remuneration and Pensions", "고용주 보수·연금 신고서", "僱主填報僱員薪酬及退休金報稅表")),
        ("importlic", ("Import Licence Application", "수입 허가 신청서", "進口許可證申請表")),
        ("changeparticulars", ("Notification of Change of Business Particulars", "사업 사항 변경 신고서", "更改業務資料通知書")),
    ],
    "nonresidents": [
        ("visaform", ("Visa / Entry Permit Application Form", "비자·입경허가 신청서", "簽證／進入許可證申請表")),
        ("extension", ("Application for Extension of Stay", "체류 연장 신청서", "延長逗留期限申請表")),
        ("reentry", ("Application for Re-entry Permit", "재입경 허가 신청서", "回港證申請表")),
        ("taxnonres", ("Tax Return for Non-Residents", "비거주자 소득세 신고서", "非居民報稅表")),
        ("addresschange", ("Notification of Change of Address", "주소 변경 신고서", "更改地址通知書")),
    ],
}

GUIDES = [
    ("passport", ("Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照"), "passport"),
    ("rs", ("Information on Recreation & Sports", "여가·체육 안내", "康樂及體育資訊"), "calendar"),
    ("drivetest", ("Driving Test Appointment Booking Service", "운전시험 예약 서비스", "駕駛考試預約服務"), "car"),
]
FEATURES = [
    ("births", ("Births Registration", "출생 등록", "出生登記"), "baby"),
    ("parenting", ("Parenting", "육아", "育兒"), "heart"),
    ("specialedu", ("Special Education", "특수교육", "特殊教育"), "book"),
    ("marriage", ("Marriage Registration", "혼인 등록", "婚姻登記"), "rings"),
    ("reproductive", ("Reproductive Health", "생식 건강", "生殖健康"), "heart"),
    ("propertyf", ("Property", "부동산", "物業"), "house"),
    ("elderly", ("Elderly Services & Benefits", "노인 서비스 및 혜택", "長者服務及福利"), "heart"),
    ("elderlyhousing", ("Housing for the Elderly", "노인 주거", "長者房屋"), "house"),
    ("deaths", ("Deaths Registration", "사망 등록", "死亡登記"), "book"),
]
CHECK = [
    ("maeul", ("Baekhyeon Maeul Complexes 3 & 4", "백현마을 3단지·4단지", "柏峴마을3、4社區"), "#2d6a8f"),
    ("infographic", ("Infographic Design Competition", "인포그래픽 디자인 공모전", "資訊圖表設計比賽"), "#e08a1e"),
    ("passportf", ("Baekhyeon Hwarang SAR Passport Features", "백현화랑 특별행정구 여권 안내", "柏峴화랑特別行政區護照特色"), "#0e2c5a"),
    ("census", ("2026 Population Census", "2026 인구총조사", "2026年人口普查"), "#b79ad0"),
]
SOCIAL = [
    ("women", ("Women's Commission", "여성위원회", "婦女事務委員會")),
    ("youth", ("Youth Portal", "청년 포털", "青年網站")),
    ("family", ("Happy Family Info Hub", "행복한 가정 정보센터", "快樂家庭資訊站")),
    ("eelderly", ("eElderly", "e-어르신", "長者電子網站")),
    ("accessibility", ("Accessibility Hub", "접근성 허브", "無障礙資訊站")),
]
FOOTER = [
    ("aboutus", ("About Us", "사이트 소개", "關於我們")),
    ("abouthk", ("About Baekhyeon Hwarang", "백현화랑 소개", "關於柏峴화랑")),
    ("accessibility", ("Accessibility", "접근성", "無障礙")),
    ("help", ("Help", "도움말", "說明")),
    ("linking", ("Linking to GovBHG", "링크 안내", "連結本網站")),
    ("copyright", ("Copyright Notice", "저작권 안내", "版權公告")),
    ("disclaimer", ("Disclaimer", "면책 고지", "免責聲明")),
    ("privacy", ("Privacy Policy", "개인정보 처리방침", "私隱政策")),
]
GOVSITES = ("Government Websites & Officers", "정부 웹사이트 및 담당 부서", "政府網站及人員")
ONLINE_PAGE = ("Online Services", "온라인 서비스", "網上服務")
FORMS_PAGE = ("Government Forms", "정부 서식", "政府表格")

# ----------------------------------------------------------------------------- full pages
# block types: ("p", T) ("h2", T) ("h3", T) ("ol", [T]) ("ul", [T]) ("btn", T, target) ("plain", T)
def B(kind, *a):
    return (kind,) + a

PASSPORT_TITLE = ("Online Application for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 온라인 신청", "網上申請柏峴화랑特別行政區護照")

PHOTO_STEP = (
    "upload your recent colour photograph in plain white background that can meet the standard requirements. Whether the successfully uploaded photograph meets the requirements has yet to be determined. If necessary, we may request you to submit another photograph to process your application",
    "표준 규격을 충족하는, 흰색 배경의 최근 컬러 사진을 업로드합니다. 업로드에 성공했더라도 규격 충족 여부는 별도로 확정됩니다. 필요한 경우 신청 처리를 위해 사진을 다시 제출하도록 요청할 수 있습니다",
    "上載背景為白色的彩色近照，照片須符合特定規格。成功上載的照片是否符合規格仍有待確定。如有需要，本處可能要求你提交另一張照片，以便處理你的申請",
)
CHILD_PHOTO = (
    "upload the child's recent colour photograph in plain white background that can meet the standard requirements. Whether the successfully uploaded photograph meets the requirements has yet to be determined. If necessary, we may request you to submit another photograph to process your application",
    "자녀의 최근 컬러 사진(흰색 배경)을 표준 규격에 맞게 업로드합니다. 업로드에 성공했더라도 규격 충족 여부는 별도로 확정됩니다. 필요한 경우 신청 처리를 위해 사진을 다시 제출하도록 요청할 수 있습니다",
    "上載該兒童的彩色近照（背景為白色），照片須符合特定規格。成功上載的照片是否符合規格仍有待確定。如有需要，本處可能要求你提交另一張照片，以便處理你的申請",
)
FORM_STEP = ("complete online application form", "온라인 신청서를 작성합니다", "填妥網上申請書")
PARENT_DOC = (
    "upload a copy of your consenting parent or legal guardian's valid travel document (if he/she is not a Baekhyeon Hwarang SAR resident)",
    "동의하는 부모 또는 법정대리인의 유효한 여행증명서 사본을 업로드합니다(백현화랑 특별행정구 주민이 아닌 경우)",
    "上載同意這項申請的父、母或合法監護人的有效旅行證件副本（如他／她不是柏峴화랑特別行政區居民）",
)
BIRTH_DOC = (
    "upload a copy of your birth certificate (not required if you were born in Baekhyeon Hwarang) to prove the relationship between you and your consenting parent, or a copy of court order, if appropriate, to prove that the consenting legal guardian has custodial rights in respect of you",
    "본인과 동의하는 부모의 관계를 증명하는 출생증명서 사본(백현화랑 특별행정구에서 출생한 경우 불필요) 또는, 해당되는 경우 동의하는 법정대리인의 양육권을 증명하는 법원 명령서 사본을 업로드합니다",
    "上載你的出生證明書副本（如在柏峴화랑出生則無需提交），以證明同意這項申請的父、母與你的關係，或法庭頒令副本（如適用），以證明同意這項申請的合法監護人對你擁有管養權",
)
CHILD_PARENT_DOC = (
    "upload a copy of the consenting parent or legal guardian's valid travel document (if he/she is not a Baekhyeon Hwarang SAR resident)",
    "동의하는 부모 또는 법정대리인의 유효한 여행증명서 사본을 업로드합니다(백현화랑 특별행정구 주민이 아닌 경우)",
    "上載同意這項申請的父、母或合法監護人的有效旅行證件副本（如他／她不是柏峴화랑特別行政區居民）",
)
CHILD_BIRTH_DOC = (
    "upload a copy of the child's birth certificate (not required if the child was born in Baekhyeon Hwarang) to prove the relationship between the consenting parent and the child, or a copy of court order, if appropriate, to prove that the consenting legal guardian has custodial rights in respect of the child",
    "동의하는 부모와 자녀의 관계를 증명하는 자녀의 출생증명서 사본(백현화랑 특별행정구에서 출생한 경우 불필요) 또는, 해당되는 경우 동의하는 법정대리인의 양육권을 증명하는 법원 명령서 사본을 업로드합니다",
    "上載該兒童的出生證明書副本（如在柏峴화랑出生則無需提交），以證明同意這項申請的父、母與該兒童的關係，或法庭頒令副本（如適用），以證明同意這項申請的合法監護人對該兒童擁有管養權",
)
SCHOOL_DOC = (
    "upload a copy of the child's latest school document bearing the child's photograph authenticated by the school (e.g. student handbook or school record, bearing the child's name, date of birth and photograph) or other proof of identity. If such school document or proof of identity is not available, a completed Form for Countersignature (ID 641) together with a photocopy of identity document of the person countersigning the form",
    "학교가 확인한 자녀의 사진이 있는 최신 학교 서류(자녀의 이름·생년월일·사진이 있는 학생 수첩 또는 학적부 등) 또는 기타 신원 증명서 사본을 업로드합니다. 이러한 서류가 없는 경우 작성한 확인 서명 서식(ID 641)과 서명 확인인의 신분증명서 사본을 제출합니다",
    "上載經學校蓋印認證並附有該兒童照片的最近學校證明文件（例如載有兒童姓名、出生日期及照片的學生手冊或學校紀錄卡）或其他身份證明文件副本。若未能提供該等學校證明文件或身份證明，則須提交已填妥的副署事項表格（ID 641）及副署人的身份證明文件副本",
)


def _pp():
    P = []
    P.append(B("p", (
        "If you are a Korean citizen, and a permanent resident of the Baekhyeon Hwarang SAR holding a valid Baekhyeon Hwarang SAR permanent identity card / Acknowledgement of application for a Baekhyeon Hwarang SAR permanent identity card, you may apply for a Baekhyeon Hwarang SAR Passport through the Internet.",
        "대한민국 국민이면서 유효한 백현화랑 특별행정구 영구 신분증 또는 영구 신분증 신청 확인서를 소지한 백현화랑 특별행정구 영주권자는 인터넷으로 백현화랑 특별행정구 여권을 신청할 수 있습니다.",
        "若你是大韓民國國民，並且持有有效柏峴화랑特別行政區永久性居民身份證／「申請柏峴화랑永久性居民身份證收據」的特別行政區永久性居民，你便可以透過互聯網申請柏峴화랑特別行政區護照。")))
    P.append(B("p", (
        "The application through the Internet is applicable to first application and replacement (except for replacement of a passport which has been lost/damaged/defaced/is not available or amendment of personal particulars in a passport).",
        "인터넷 신청은 최초 신청 및 교체 발급에 적용됩니다(분실·훼손·오손·사용 불가 여권의 교체 또는 여권상 인적사항 정정은 제외).",
        "透過互聯網申請適用於首次申請及換領（因遺失、損毀、殘破、無法使用舊護照或更改護照上個人資料而需換領護照的申請除外）。")))
    P.append(B("btn", ("Application through the Internet for Baekhyeon Hwarang SAR Passport", "인터넷으로 백현화랑 특별행정구 여권 신청", "透過互聯網申請柏峴화랑特別行政區護照"), "apply"))
    P.append(B("p", (
        "Note: You can also make an appointment through the Internet to apply for a Baekhyeon Hwarang SAR Passport at the Immigration Headquarters or any of the Immigration Branch Offices.",
        "참고: 인터넷으로 예약하여 출입경사무처 본부 또는 지소에서 백현화랑 특별행정구 여권을 신청할 수도 있습니다.",
        "提示：你亦可透過互聯網預約在入境事務處總部或任何一間入境事務處分區辦事處申請柏峴화랑特別行政區護照。")))
    P.append(B("btn", ("Make an Appointment to Apply for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件"), "appointment"))
    P.append(B("p", (
        "To ensure fair use of this online service, an applicant who uses computer programs or automated tools to interfere with the normal operation of the system or to make appointment bookings/online applications shall be deemed to have improperly used the system. The Immigration Department may immediately block his/her access to the system without prior notice.",
        "이 온라인 서비스의 공정한 이용을 위해, 컴퓨터 프로그램이나 자동화 도구로 시스템의 정상 운영을 방해하거나 예약·온라인 신청을 하는 신청인은 시스템을 부당하게 사용한 것으로 봅니다. 출입경사무처는 사전 통지 없이 해당 신청인의 시스템 접근을 즉시 차단할 수 있습니다.",
        "為確保公平使用此項網上服務，申請人如以電腦程式或自動化工具干擾系統的正常運作或進行預約／網上申請，即作不當使用系統論。入境事務處可即時封鎖申請人使用系統的權限，無須預先通知。")))

    P.append(B("h2", ("Documentary Requirements", "필요 서류", "所需的文件")))
    P.append(B("p", ("If you are <strong>aged 18 or above</strong>, you need to:", "<strong>만 18세 이상</strong>인 경우:", "<strong>十八歲或以上</strong>的申請人需：")))
    P.append(B("ol", [
        ("complete online application form; and", "온라인 신청서를 작성하고,", "填妥網上申請書；及"),
        (PHOTO_STEP[0] + ".", PHOTO_STEP[1] + ".", PHOTO_STEP[2] + "。"),
    ]))
    P.append(B("p", ("If you are <strong>aged 16 or 17</strong>, you need to:", "<strong>만 16세 또는 17세</strong>인 경우:", "<strong>十六及十七歲</strong>的申請人需：")))
    P.append(B("ol", [
        (FORM_STEP[0] + ";", FORM_STEP[1] + ".", FORM_STEP[2] + "；"),
        (PHOTO_STEP[0] + ";", PHOTO_STEP[1] + ".", PHOTO_STEP[2] + "；"),
        (PARENT_DOC[0] + "; and", PARENT_DOC[1] + ".", PARENT_DOC[2] + "；及"),
        (BIRTH_DOC[0] + ".", BIRTH_DOC[1] + ".", BIRTH_DOC[2] + "。"),
    ]))
    P.append(B("p", (
        "If you are married, only a copy of your marriage certificate (not required if you got married in Baekhyeon Hwarang) is required. Parental or legal guardian's consent and items (3) and (4) are not required.",
        "기혼자인 경우 혼인증명서 사본(백현화랑 특별행정구에서 혼인한 경우 불필요)만 제출하면 되며, 부모 또는 법정대리인의 동의와 위 (3), (4)항 서류는 필요하지 않습니다.",
        "如屬已婚人士，則只須上載你的結婚證書副本（如在柏峴화랑結婚則無需提交），無須父、母或合法監護人的同意及上載第(3)及(4)項的文件。")))
    P.append(B("p", ("If the child is <strong>aged between 11 and 15</strong>, the consenting parent / legal guardian needs to:", "자녀가 <strong>만 11세 이상 15세 이하</strong>인 경우, 동의하는 부모·법정대리인은:", "如為<strong>十一至十五歲</strong>兒童申請，同意這項申請的父、母或合法監護人需：")))
    P.append(B("ol", [
        (FORM_STEP[0] + ";", FORM_STEP[1] + ".", FORM_STEP[2] + "；"),
        (CHILD_PHOTO[0] + ";", CHILD_PHOTO[1] + ".", CHILD_PHOTO[2] + "；"),
        (CHILD_PARENT_DOC[0] + "; and", CHILD_PARENT_DOC[1] + ".", CHILD_PARENT_DOC[2] + "；及"),
        (CHILD_BIRTH_DOC[0] + ".", CHILD_BIRTH_DOC[1] + ".", CHILD_BIRTH_DOC[2] + "。"),
    ]))
    P.append(B("p", ("If the child is <strong>aged below 11 with Baekhyeon Hwarang SAR permanent identity card</strong>, the consenting parent / legal guardian needs to:", "자녀가 <strong>만 11세 미만이며 백현화랑 특별행정구 영구 신분증을 소지</strong>한 경우, 동의하는 부모·법정대리인은:", "如為<strong>十一歲以下並持有柏峴화랑永久性居民身份證</strong>的兒童申請，同意這項申請的父、母或合法監護人需：")))
    P.append(B("ol", [
        (FORM_STEP[0] + ";", FORM_STEP[1] + ".", FORM_STEP[2] + "；"),
        (CHILD_PHOTO[0] + ";", CHILD_PHOTO[1] + ".", CHILD_PHOTO[2] + "；"),
        (CHILD_PARENT_DOC[0] + ";", CHILD_PARENT_DOC[1] + ".", CHILD_PARENT_DOC[2] + "；"),
        (CHILD_BIRTH_DOC[0] + "; and", CHILD_BIRTH_DOC[1] + ".", CHILD_BIRTH_DOC[2] + "；及"),
        (SCHOOL_DOC[0] + ".", SCHOOL_DOC[1] + ".", SCHOOL_DOC[2] + "。"),
    ]))
    P.append(B("p", ("Additional documents or information may also be required, if necessary.", "필요한 경우 추가 서류나 정보를 요구할 수 있습니다.", "如有需要，本處可能要求你提交補充文件及資料。")))
    P.append(B("p", ("Acceptable file formats of digital photograph and supporting documents are listed below:", "디지털 사진 및 증빙서류에 허용되는 파일 형식은 다음과 같습니다.", "數碼照片及補充資料副本可接納的特定檔案格式如下：")))
    P.append(B("h3", ("Acceptable File Format of Digital Photograph for Application through the Internet", "인터넷 신청용 디지털 사진의 허용 파일 형식", "透過互聯網申請可接納的數碼照片特定檔案格式")))
    P.append(B("plain", ("Image type: JPEG<br>File size: 5MB or below<br>Acceptable dimension:", "이미지 형식: JPEG<br>파일 크기: 5MB 이하<br>허용 규격:", "圖像類別：JPEG<br>檔案大小：5MB 或以下<br>合適尺寸：")))
    P.append(B("ul", [
        ("Captured by scanner (600dpi) - Photograph size: 40 mm(W) x 50 mm(H)", "스캐너(600dpi)로 촬영 - 사진 크기: 40mm(가로) x 50mm(세로)", "由掃瞄器（600dpi）擷取 – 照片大小：40毫米（闊）X 50毫米（高）"),
        ("Captured by digital camera - Image size: at least 1200 px(W) x 1600 px(H)", "디지털 카메라로 촬영 - 이미지 크기: 최소 1200px(가로) x 1600px(세로)", "由數碼相機擷取 – 圖像大小：最少1200像素（闊）X 1600像素（高）"),
    ]))
    P.append(B("link", ("Photograph Requirements for Applying for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청 사진 규격", "申請柏峴화랑特別行政區護照的照片規格"), "photo"))
    P.append(B("h3", ("Acceptable File Format of Supporting Document Copies for Application through the Internet", "인터넷 신청용 증빙서류 사본의 허용 파일 형식", "透過互聯網申請可接納的補充資料副本特定檔案規格")))
    P.append(B("plain", ("Image type: JPEG, GIF or TIF (RAW, LZW, JPEG, CCITT-G4)<br>File size: 2Mbytes or below for each file", "이미지 형식: JPEG, GIF 또는 TIF(RAW, LZW, JPEG, CCITT-G4)<br>파일 크기: 파일당 2MB 이하", "圖像類別：JPEG, GIF 或TIF (RAW, LZW, JPEG, CCITT-G4)<br>檔案大小：每個檔案2Mbytes 或以下")))

    P.append(B("h2", ("Payment Method", "납부 방법", "繳費方法")))
    P.append(B("p", (
        "Passport fee is payable at the time of application by paying online through the online payment service or by credit card (VISA, Mastercard and JCB only).",
        "여권 수수료는 신청 시 온라인 결제 서비스 또는 신용카드(VISA, Mastercard, JCB만 가능)로 납부합니다.",
        "護照費用須於遞交網上申請時，透過網上繳費服務或信用卡（只接受VISA、萬事達卡及JCB）繳付。")))
    P.append(B("link", ("FAQs about Online Payment Service", "온라인 결제 서비스 자주 묻는 질문", "網上付款常見問題"), "payfaq"))
    P.append(B("link", ("More on fees for Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 수수료 안내", "更多關於柏峴화랑特別行政區護照的申請費用資料"), "fees"))
    P.append(B("p", (
        "The collection of fees does not constitute any assurance that the passport application will be approved.",
        "수수료를 납부했다고 해서 여권 신청이 승인되는 것은 아닙니다.",
        "收取費用並不保證護照申請一定會獲得批准。")))

    P.append(B("h2", ("Processing Time", "처리 기간", "處理申請的時間")))
    P.append(B("p", (
        "Processing an application for a Baekhyeon Hwarang SAR Passport normally takes 5 working days (working days denote Monday to Friday excluding General Holidays) after all necessary documents, application fee and photograph have been received. For application through the Internet, an extra 2 to 3 working days may be required for handling formalities. A Collection Notice specifying the period of collection and the office for collection of the new passport will then be sent to you. Whether this pledge can be met will also depend on the circumstances of individual applications and the number of applications received at a particular time. An application through the Internet without a standard photograph, full supporting documents or payment will not be processed.",
        "백현화랑 특별행정구 여권 신청은 필요한 서류, 신청 수수료 및 사진이 모두 접수된 후 통상 5근무일(월~금요일, 일반 공휴일 제외)이 소요됩니다. 인터넷 신청의 경우 절차 처리를 위해 2~3근무일이 추가로 필요할 수 있습니다. 이후 새 여권의 수령 기간과 수령 사무소가 적힌 수령 통지서가 발송됩니다. 이 처리 기한을 지킬 수 있는지는 개별 신청의 사정과 해당 시기의 접수 건수에 따라 달라질 수 있습니다. 규격 사진, 전체 증빙서류 또는 수수료 납부가 없는 인터넷 신청은 처리되지 않습니다.",
        "一般而言，入境事務處承諾於收妥全部所需文件、申請費用及照片後的五個工作天內（工作天是指星期一至星期五，公眾假期除外）完成處理護照申請的程序。若透過互聯網申請，則須預留額外兩至三個工作天處理相關手續。本處稍後會向你發出領證通知，通知你領取新護照的日期及地點。此服務承諾能否達到，須視乎個別申請情況，以及在該段時間內所收到的申請數目等因素而定。如沒有上載符合標準規格的照片、所有有關的證明文件或繳付護照費用，入境事務處將不受理該申請。")))

    P.append(B("h2", ("Passport Collection", "여권 수령", "領取護照")))
    P.append(B("p", (
        "You must collect your new passport in person by producing your Baekhyeon Hwarang SAR permanent identity card and the original supporting documents (if any) submitted in the application for verification, your existing Baekhyeon Hwarang SAR Passport or Document of Identity for Visa Purposes (if any) for cancellation.",
        "새 여권은 반드시 본인이 직접 수령해야 하며, 확인을 위해 백현화랑 특별행정구 영구 신분증과 신청 시 제출한 증빙서류 원본(해당되는 경우)을, 말소를 위해 기존 백현화랑 특별행정구 여권 또는 비자용 신분증명서(해당되는 경우)를 제시해야 합니다.",
        "你必須親身領取護照。領證時，必須出示柏峴화랑永久性居民身份證及申請時所遞交證明文件（如適用）的正本，以供核實。同時你必須於領取新護照時出示原有柏峴화랑特別行政區護照或現有簽證身份書（如適用），以便註銷。")))
    P.append(B("p", ("If only the Acknowledgement for a Baekhyeon Hwarang SAR permanent identity card was available upon application:", "신청 시 영구 신분증 신청 확인서만 있었던 경우:", "若申請時只持有「申請柏峴화랑永久性居民身份證收據」：")))
    P.append(B("ul", [
        ("The original Baekhyeon Hwarang SAR permanent identity card should be produced for verification upon collection of passport.", "여권 수령 시 확인을 위해 백현화랑 특별행정구 영구 신분증 원본을 제시해야 합니다.", "你須在領證時出示柏峴화랑永久性居民身份證正本，以便核實。"),
        ("The Acknowledgement for a Baekhyeon Hwarang SAR permanent identity card should be produced for cancellation upon collection of the identity card.", "신분증 수령 시 말소를 위해 영구 신분증 신청 확인서를 제출해야 합니다.", "你必須在領取身份證時交回「申請柏峴화랑永久性居民身份證收據」，以便註銷。"),
    ]))
    P.append(B("p", (
        "Upon collection, you / the consenting parent or legal guardian, if applicable, is required to make a declaration to confirm the correctness of information furnished upon application through the Internet. For children aged below 16 and unmarried persons aged 16 or 17, the consenting parent or legal guardian must accompany the child/applicant for collection of passport in person, for appending his/her signature on the application form.",
        "수령 시 본인(해당되는 경우 동의하는 부모 또는 법정대리인)은 인터넷 신청 시 제공한 정보가 정확함을 확인하는 선서를 해야 합니다. 만 16세 미만 아동과 만 16~17세 미혼 신청인의 경우, 동의하는 부모 또는 법정대리인이 신청서에 서명하기 위해 아동·신청인과 함께 직접 방문하여 수령해야 합니다.",
        "你／同意這項申請的父、母或合法監護人在領取護照時須作出聲明，確認透過互聯網申請時所申報的資料正確無誤。如你為十六歲以下兒童或十六至十七歲的未婚人士，同意這項申請的父、母或合法監護人必須陪同該兒童／申請人親身領取護照，以便在申請書上簽署。")))
    P.append(B("h3", ("Application submitted in Baekhyeon Hwarang", "백현화랑 특별행정구 내에서 제출한 신청", "於柏峴화랑遞交申請")))
    P.append(B("p", ("If you apply in Baekhyeon Hwarang, you can choose to collect the passport in person at the selected Immigration Office or the selected Korean Diplomatic and Consular Mission. The collection arrangement will be sent by Short Message Service (SMS) notification prior to the collection period. Applicant is therefore advised to provide a mobile phone number subscribed with SMS.",
                     "백현화랑 특별행정구 내에서 신청한 경우, 선택한 출입경사무소 또는 선택한 재외공관에서 직접 여권을 수령할 수 있습니다. 수령 방법은 수령 기간 전에 문자메시지(SMS)로 안내되므로, SMS를 수신할 수 있는 휴대전화 번호를 제공해 주시기 바랍니다.",
                     "若你在柏峴화랑遞交申請，你可選擇親身到所選定的入境事務辦事處或所選定的大韓民國駐外使領館領取護照。有關領證安排將於領證期限前以短訊方式通知，因此申請人需提供可接收短訊的流動電話號碼。")))

    P.append(B("h3", ("Application submitted outside Baekhyeon Hwarang", "백현화랑 특별행정구 밖에서 제출한 신청", "於柏峴화랑以外地區遞交申請")))
    P.append(B("p", ("If you submit your application outside Baekhyeon Hwarang, you must collect the passport in person at:", "백현화랑 특별행정구 밖에서 신청한 경우 다음 장소에서 직접 여권을 수령해야 합니다.", "若你在柏峴화랑以外地區遞交申請，你須親身到以下地點領取護照：")))
    P.append(B("ul", [
        ("the Travel Documents (Issue) Section, Immigration Headquarters, Baekhyeon Hwarang Special Administrative Region; or", "백현화랑 특별행정구 출입경사무처 본부 여행증명서(발급) 과, 또는", "柏峴화랑特別行政區入境事務處總部旅行證件（簽發）組；或"),
        ("the selected Korean Diplomatic and Consular Mission.", "선택한 재외공관.", "所選定的大韓民國駐外使領館。"),
    ]))
    P.append(B("p", ("You are required to make a declaration upon collection to confirm the correctness of information furnished upon application through the Internet.", "수령 시 인터넷 신청 때 제출한 정보가 정확함을 확인하는 선서를 해야 합니다.", "你在領取護照時須作出聲明，確認你透過互聯網申請時所申報的資料正確無誤。")))
    P.append(B("h2", ("Support and Further Information", "지원 및 상세 정보", "支援及詳細資料")))
    P.append(B("p", (
        "If you need technical support when using the online service, please contact the e-services support of the Immigration Department.",
        "온라인 서비스 이용 중 기술 지원이 필요하면 출입경사무처 전자서비스 지원 창구에 문의해 주세요.",
        "如你於使用網上服務時需要技術支援，請聯絡入境事務處電子服務支援。")))
    P.append(B("p", (
        "General enquiries may be made to the Immigration Department during office hours (Monday to Friday, excluding public holidays).",
        "일반 문의는 공휴일을 제외한 월~금요일 근무 시간에 출입경사무처로 하시기 바랍니다.",
        "一般查詢可於辦公時間（星期一至五，公眾假期除外）向入境事務處查詢。")))
    P.append(B("p", ("For details of this service, please visit the FAQs.", "이 서비스에 대한 자세한 내용은 자주 묻는 질문을 참고하세요.", "有關此服務的詳細資料，可以瀏覽常見問題。")))
    P.append(B("link", ("FAQs about Application for Baekhyeon Hwarang SAR Passport through the Internet", "인터넷 백현화랑 특별행정구 여권 신청 자주 묻는 질문", "透過互聯網申請柏峴화랑特別行政區護照的常見問題"), "passfaq"))
    return P


PASSPORT_BLOCKS = _pp()
PASSPORT_RELATED = [
    ("Protection for Travellers Abroad", "해외 여행자 보호", "外遊旅客的保障"),
    ("Notes for Air Passengers", "항공 승객 안내", "飛機乘客須知"),
    ("Immigration Control Points", "출입경 관리소", "出入境管制站"),
    ("World Weather Information", "세계 날씨 정보", "世界天氣資訊"),
]

# Leaf pages under a subtopic: (cat, sub) -> [(leaf_slug, title), ...]
import data_info as _I  # noqa: E402

LEAVES = {
    ("immigration", "traveldoc"): [
        ("passport", ("Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권", "柏峴화랑特別行政區護照")),
        ("appstatus", ("Online Travel Document Application Status Enquiry", "여행증명서 신청 현황 온라인 조회", "網上查詢旅行證件申請進度")),
        ("lost", _I.LOST_TITLE),
    ],
    ("immigration", "idcard"): [
        ("permid", ("Baekhyeon Hwarang Identity Cards", "백현화랑 신분증", "柏峴화랑身份證")),
        ("abode", ("Right of Abode", "거주권", "居留權")),
        ("certentitle", ("Application for Certificate of Entitlement", "자격증명서 신청", "申請登記證")),
    ],
    ("immigration", "nonpermanent"): [("appstatus", _I.NONPERM_TITLE)],
    ("taxes", "etax"): [("taxcalc", _I.TAXCALC_INFO_TITLE), ("allowance", _I.ALLOWANCE_TITLE)],
}
# sub-leaves: (cat, sub, leaf) -> [(slug, title)]
SUBLEAVES = {
    ("immigration", "traveldoc", "passport"): [
        ("apply", PASSPORT_TITLE),
        ("book", ("Book Appointment to Apply for Travel Documents", "여행증명서 신청 예약", "預約申請旅行證件")),
    ],
}

ABOUT_TEXT = {
    "aboutus": (
        ("GovBHG is the one-stop portal of the Baekhyeon Hwarang Special Administrative Region Government, providing information and services of government bureaux and departments in one place.",
         "정부포털 BHG는 백현화랑 특별행정구 정부의 원스톱 포털로, 정부 부처와 기관의 정보와 서비스를 한곳에서 제공합니다.",
         "BHG政府一站通是柏峴화랑特別行政區政府的一站式入門網站，於同一處提供各政策局及部門的資訊與服務。"),
    ),
}

# Short captions printed on the hero-card artwork (None = flag artwork, no caption)
HERO_SHORT = [
    ("The First Five-Year Plan (2026-2030)", "제1차 5개년 계획 (2026-2030)", "第一個五年規劃（2026-2030）"),
    ("The Chief Executive's 2026 Policy Address", "행정장관 2026년 시정연설", "行政長官2026年施政報告"),
    ("Founding of Baekhyeon Hwarang", "백현화랑 특별행정구 출범", "特別行政區成立"),
    None,
    None,
    ("Apply for a Baekhyeon Hwarang SAR Passport", "백현화랑 특별행정구 여권 신청", "申請柏峴화랑特別行政區護照"),
    ("2026 Population Census", "2026 인구총조사", "2026年人口普查"),
    ("Smart ID Card Booking", "스마트 신분증 예약", "預約智能身份證"),
]
