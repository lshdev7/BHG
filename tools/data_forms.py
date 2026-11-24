# -*- coding: utf-8 -*-
"""Fillable government forms (rendered as printable A4 sheets) and the Government Form Catalogue.
Tuples are (English, Korean, Traditional Chinese). Item types:
  ("part", T)  ("text", T[, "full"|"half"|"third"])  ("boxes", T, n)  ("check", T, [T...])  ("yn", T)
  ("money", T)  ("date", T)  ("addr", T)  ("note", T)  ("table", [T...], rows)  ("sign", [T...])  ("pair", T, [T, T])
"""

YES, NO = ("Yes", "예", "是"), ("No", "아니요", "否")
DAY, MONTH, YEAR = ("Day", "일", "日"), ("Month", "월", "月"), ("Year", "년", "年")
ADDR = {"flat": ("Flat/Room", "호", "室"), "floor": ("Floor", "층", "樓"), "block": ("Block/Tower", "동", "座"),
        "bldg": ("Name of Building/Estate", "건물·단지명", "大廈／屋苑名稱"), "street": ("Number and Name of Street", "도로명 및 번지", "街道號碼及名稱"),
        "district": ("District", "지역", "地區"), "area": ("Area", "구역", "區域"),
        "areas": [("Baekhyeon Maeul Complex 3", "백현마을 3단지", "柏峴마을3社區"), ("Baekhyeon Maeul Complex 4", "백현마을 4단지", "柏峴마을4社區"), ("Others", "기타", "其他")]}
TITLES = [("Mr.", "Mr.", "先生"), ("Mrs.", "Mrs.", "太太"), ("Miss", "Miss", "小姐"), ("Ms.", "Ms.", "女士")]
ID_NO = ("Baekhyeon Hwarang Identity Card No.", "백현화랑 신분증 번호", "柏峴화랑身份證號碼")
NAME_EN = ("Name in English (Surname first, then Other Names, in BLOCK LETTERS)", "영문 성명(성 먼저, 대문자)", "英文姓名（先填姓氏，請用正楷）")
NAME_LOCAL = ("Name in Chinese / Korean", "한글·한자 성명", "中文／韓文姓名")
TEL = ("Day-time Contact Telephone No.", "주간 연락처", "日間聯絡電話號碼")
EMAIL = ("Email Address", "이메일 주소", "電郵地址")
SIGN = [("Signature", "서명", "簽署"), ("Date", "날짜", "日期")]

DEPT = {
    "csb": (("Civil Service Bureau", "공무원사무국", "公務員事務局"), ("Baekhyeon Hwarang Special Administrative Region Government", "백현화랑 특별행정구 정부", "柏峴화랑特別行政區政府")),
    "ird": (("Inland Revenue Department", "국세청", "稅務局"), ("Inland Revenue Centre, Baekhyeon Maeul Complex 4, Baekhyeon Hwarang", "백현화랑 백현마을 4단지 국세센터", "柏峴화랑柏峴마을4社區稅務中心")),
    "td": (("Transport Department", "운수국", "運輸署"), ("Licensing Office, Baekhyeon Maeul Complex 3, Baekhyeon Hwarang", "백현화랑 백현마을 3단지 면허사무소", "柏峴화랑柏峴마을3社區牌照事務處")),
}

FORMS = {}

FORMS["gf340"] = {
    "slug": "govjobs", "no": "G.F. 340 (Rev. 2026)", "dept": "csb", "file": "GF340.pdf",
    "title": ("Application for Government Employment", "정부 공무원 채용 지원서", "應徵政府職位申請表"),
    "intro": ("Please read the recruitment advertisement and the notes before completing this form. Complete in BLOCK LETTERS and insert a ✓ in the appropriate box(es).",
              "이 서식을 작성하기 전에 채용 공고와 안내 사항을 읽어 주세요. 대문자로 작성하고 해당란에 ✓ 표시하세요.",
              "填寫本表格前，請先細閱招聘廣告及注意事項。請用正楷填寫，並在適當的方格內加上「✓」號。"),
    "items": [
        ("part", ("Part I  Post Applied For", "제1부  지원 직위", "第I部  應徵職位")),
        ("text", ("Post Title", "직위명", "職位名稱"), "half"), ("text", ("Bureau / Department", "부처·기관", "政策局／部門"), "half"),
        ("text", ("Reference No. of Recruitment Advertisement", "채용 공고 참조번호", "招聘廣告參考編號"), "half"),
        ("part", ("Part II  Personal Particulars", "제2부  인적사항", "第II部  個人資料")),
        ("check", ("Title", "호칭", "稱謂"), TITLES),
        ("text", NAME_EN, "full"), ("text", NAME_LOCAL, "half"), ("boxes", ID_NO, 10),
        ("text", TEL, "half"), ("text", EMAIL, "half"), ("addr", ("Correspondence Address", "우편 주소", "通訊地址")),
        ("part", ("Part III  Academic Qualifications", "제3부  학력", "第III部  學歷")),
        ("table", [("Name of Institution", "학교명", "院校名稱"), ("Qualification Obtained / to be Obtained", "취득(예정) 학위·자격", "已取得／將取得的資歷"), ("Major / Minor", "전공·부전공", "主修／副修"), ("From (MM/YYYY)", "시작(월/년)", "由（月/年）"), ("To (MM/YYYY)", "종료(월/년)", "至（月/年）")], 4),
        ("yn", ("I have attained / will attain in the current academic year a Bachelor's degree or equivalent.", "학사 학위 또는 이에 상당하는 학위를 취득했거나 이번 학년도에 취득할 예정입니다.", "本人已取得／將於本學年取得學士學位或同等學歷。")),
        ("pair", ("Best results in public examinations", "공인 시험 최고 성적", "公開考試最佳成績"), [("Chinese / Korean Language", "국어", "中文／韓文"), ("English Language", "영어", "英文")]),
        ("part", ("Part IV  Professional Qualifications", "제4부  전문 자격", "第IV部  專業資格")),
        ("table", [("Professional Qualification / Membership", "전문 자격·회원 자격", "專業資格／會員資格"), ("Awarding Body", "수여 기관", "頒授機構"), ("Date Obtained (MM/YYYY)", "취득일(월/년)", "取得日期（月/年）")], 3),
        ("part", ("Part V  Working Experience (most recent first)", "제5부  경력(최근 순)", "第V部  工作經驗（由最近開始）")),
        ("table", [("Name of Employer", "고용주", "僱主名稱"), ("Post Title", "직위", "職位"), ("Full-time / Part-time", "전일제·시간제", "全職／兼職"), ("From (MM/YYYY)", "시작(월/년)", "由（月/年）"), ("To (MM/YYYY)", "종료(월/년)", "至（月/年）")], 4),
        ("part", ("Part VI  Other Information", "제6부  기타 정보", "第VI部  其他資料")),
        ("yn", ("Are you serving or have you served in the Baekhyeon Hwarang SAR Government?", "현재 백현화랑 특별행정구 정부에 재직 중이거나 재직한 적이 있습니까?", "閣下現時或曾否任職柏峴화랑特別行政區政府？")),
        ("text", ("If yes, please state the post title and department", "예인 경우 직위와 부처를 적어 주세요", "如是，請註明職位及部門"), "full"),
        ("part", ("Part VII  Declaration", "제7부  선서", "第VII部  聲明")),
        ("note", ("I declare that the information given in this application is, to the best of my knowledge and belief, true, complete and accurate. I understand that any misrepresentation or omission of material facts may lead to disqualification or dismissal.",
                  "본인은 이 지원서에 기재한 정보가 본인이 아는 한 사실이며 완전하고 정확함을 선서합니다. 중요한 사실을 허위로 기재하거나 누락하면 자격 박탈 또는 해고될 수 있음을 이해합니다.",
                  "本人聲明，據本人所知所信，本申請表所填報的資料均屬真實、完整及準確。本人明白如對重要事實作出失實陳述或有所遺漏，可被取消資格或解僱。")),
        ("sign", SIGN),
    ],
}

FORMS["ir76c"] = {
    "slug": "pa", "no": "IR76C", "dept": "ird", "file": "ir76c.pdf",
    "title": ("Election for Personal Assessment and Claim for Deductions & Allowances", "개인 과세 선택 및 공제·인적 공제 신청서", "選擇以個人入息課稅及申索扣除與免稅額"),
    "intro": ("In any communication please quote the file number. Delete whichever is inapplicable for items marked with *.", "문의할 때는 파일 번호를 적어 주세요. * 표시 항목은 해당하지 않는 것을 지우세요.", "如有任何查詢，請引述檔案號碼。有「*」號的項目，請刪去不適用者。"),
    "items": [
        ("text", ("File No.", "파일 번호", "檔案號碼"), "half"), ("text", ("Year of Assessment", "과세연도", "課稅年度"), "half"),
        ("note", ("I / I and my spouse* wish to elect for Personal Assessment for the above year of assessment.", "본인 / 본인과 배우자*는 위 과세연도에 대해 개인 과세를 선택합니다.", "本人／本人及配偶*欲選擇以個人入息課稅方式評稅。")),
        ("part", ("Part 1  Personal Particulars", "제1부  인적사항", "第1部  個人資料")),
        ("pair", ("1. Name in English (Surname first, BLOCK LETTERS)", "1. 영문 성명(성 먼저, 대문자)", "1. 英文姓名（先填姓氏，請用正楷）"), [("Self", "본인", "本人"), ("Spouse", "배우자", "配偶")]),
        ("pair", ("2. Name in Chinese / Korean", "2. 한글·한자 성명", "2. 中文／韓文姓名"), [("Self", "본인", "本人"), ("Spouse", "배우자", "配偶")]),
        ("pair", ("3. Baekhyeon Hwarang Identity Card Number", "3. 백현화랑 신분증 번호", "3. 柏峴화랑身份證號碼"), [("Self", "본인", "本人"), ("Spouse", "배우자", "配偶")]),
        ("yn", ("4(a) I am eligible and wish to elect for Personal Assessment myself / separately from my spouse.", "4(a) 본인은 자격이 있으며 단독으로 / 배우자와 별도로 개인 과세를 선택합니다.", "4(a) 本人符合資格並欲自行／與配偶分開選擇以個人入息課稅。")),
        ("yn", ("4(b) Both of us had assessable income during the year. We wish to elect for Personal Assessment jointly.", "4(b) 우리 부부 모두 해당 연도에 과세 소득이 있었으며 합산하여 개인 과세를 선택합니다.", "4(b) 本人及配偶在該年度均有應評稅入息，我們欲合併選擇以個人入息課稅。")),
        ("part", ("Part 2  Deductions & Allowances", "제2부  공제 및 인적 공제", "第2部  扣除及免稅額")),
        ("money", ("5. Approved charitable donations not claimed in the Tax Return - Individuals", "5. 개인 세금 신고서에서 신청하지 않은 승인 기부금", "5. 未在個別人士報稅表申索的認可慈善捐款")),
        ("text", ("6.(1) Location of property (for interest payments / domestic rents)", "6.(1) 부동산 소재지(이자·임차료 공제용)", "6.(1) 物業地址（申索利息／住宅租金扣除）"), "full"),
        ("yn", ("6.(2) A loan has been obtained for acquiring the property and secured by a mortgage or charge.", "6.(2) 부동산 취득을 위한 대출을 받았으며 저당권이 설정되어 있습니다.", "6.(2) 已為購置該物業取得貸款，並以按揭或押記作抵押。")),
        ("pair", ("6.(2)(iii) Share of ownership (%)", "6.(2)(iii) 소유 지분(%)", "6.(2)(iii) 業權份數（%）"), [("Self", "본인", "本人"), ("Spouse", "배우자", "配偶")]),
        ("money", ("6.(4) Home loan interest payments", "6.(4) 주택대출 이자", "6.(4) 居所貸款利息")),
        ("money", ("6.(5) Amount of domestic rents claimed", "6.(5) 신청하는 주거 임차료", "6.(5) 申索的住宅租金")),
        ("money", ("7. Qualifying premiums paid under the Voluntary Health Insurance Scheme", "7. 자발적 건강보험 적격 보험료", "7. 自願醫保計劃的合資格保費")),
        ("money", ("8. Qualifying annuity premiums and tax deductible MPF voluntary contributions", "8. 적격 연금 보험료 및 강제적립기금 자발적 납입액", "8. 合資格年金保費及可扣稅強積金自願性供款")),
        ("money", ("9. Elderly residential care expenses", "9. 노인 요양시설 비용", "9. 長者住宿照顧開支")),
        ("pair", ("10. Child allowance – number of children", "10. 자녀 공제 – 자녀 수", "10. 子女免稅額 – 子女數目"), [("Born before the year", "해당 연도 이전 출생", "在該年度以前出生"), ("Born during the year", "해당 연도 출생", "在該年度出生")]),
        ("table", [("11. Dependent parent / grandparent – Name", "11. 부양 부모·조부모 – 성명", "11. 供養父母／祖父母 – 姓名"), ("Identity Card No.", "신분증 번호", "身份證號碼"), ("Relationship", "관계", "關係"), ("Resided with me (Yes/No)", "동거 여부(예/아니요)", "與本人同住（是／否）")], 2),
        ("part", ("Declaration", "선서", "聲明")),
        ("note", ("I declare that the information given in this form is true, correct and complete.", "본인은 이 서식에 기재한 정보가 사실이며 정확하고 완전함을 선서합니다.", "本人聲明本表格所填報的資料均屬真實、正確及完整。")),
        ("sign", [("Signature of Self", "본인 서명", "本人簽署"), ("Signature of Spouse", "배우자 서명", "配偶簽署"), ("Date", "날짜", "日期")]),
    ],
}

FORMS["td558"] = {
    "slug": "vehiclerenew", "no": "TD558 (Rev. 2026)", "dept": "td", "file": "td558_e-fillable_eng.pdf",
    "title": ("Application for Renewal of Vehicle Licence", "차량 면허 갱신 신청서", "續領車輛牌照申請書"),
    "intro": ("Please read the notes overleaf and complete all items in BLOCK LETTERS. Please enter ✓ in the appropriate box(es) and delete whichever is inapplicable for items marked with *.",
              "뒷면의 안내를 읽고 모든 항목을 대문자로 작성하세요. 해당란에 ✓ 표시하고, * 표시 항목은 해당하지 않는 것을 지우세요.",
              "請細閱背頁的注意事項，並用正楷填寫所有項目。請在適當的方格內加上「✓」號，並刪去有「*」號項目中不適用者。"),
    "items": [
        ("text", ("Vehicle Registration Mark", "차량 등록번호", "車輛登記號碼"), "half"),
        ("check", ("Licence Validity Period Applied for", "신청하는 면허 유효기간", "申請的牌照有效期"), [("12 months", "12개월", "12個月"), ("4 months", "4개월", "4個月")]),
        ("part", ("Particulars of Registered Owner", "등록 소유자 인적사항", "登記車主資料")),
        ("check", ("Title", "호칭", "稱謂"), TITLES + [("Co.", "법인", "公司")]),
        ("text", NAME_EN, "full"), ("text", NAME_LOCAL, "half"),
        ("text", ("Identity Document Number / Company Registration Number", "신분증 번호 / 법인 등록번호", "身份證明文件號碼／公司註冊號碼"), "half"),
        ("text", ("Contact person of company (if using company as registered vehicle owner)", "법인 담당자(법인이 등록 소유자인 경우)", "公司聯絡人（如以公司為登記車主）"), "full"),
        ("text", ("E-contact means: Mobile Phone Number or Email Address (for receiving notification by SMS or Email)", "전자 연락처: 휴대전화 번호 또는 이메일(SMS·이메일 통지 수신용)", "電子聯絡方法：流動電話號碼或電郵地址（以接收短訊或電郵通知）"), "full"),
        ("addr", ("Residential / Company Address", "주소 / 법인 주소", "住址／公司地址")),
        ("text", TEL, "half"),
        ("addr", ("Correspondence Address (if different)", "우편 주소(다른 경우)", "通訊地址（如不同）")),
        ("part", ("Valid Third Party Risks Insurance", "유효한 제3자 책임보험", "有效的第三者風險保險")),
        ("text", ("Name of Insurance Company (not agent)", "보험회사명(대리점 제외)", "保險公司名稱（不是代理）"), "half"), ("text", ("Policy / Cover Note No.", "보험증권·임시증권 번호", "保單／暫保單號碼"), "half"),
        ("pair", ("Period of insurance", "보험 기간", "保險期"), [("From", "시작", "由"), ("To", "종료", "至")]),
        ("part", ("Declaration", "선서", "聲明")),
        ("note", ("I declare that the information given in this application is true and correct, and that the vehicle is covered by a valid third party risks insurance policy.", "본인은 이 신청서의 정보가 사실이며 정확하고, 해당 차량이 유효한 제3자 책임보험에 가입되어 있음을 선서합니다.", "本人聲明本申請書所填報的資料均屬真實及正確，而該車輛已有有效的第三者風險保險。")),
        ("sign", [("Signature of Registered Owner", "등록 소유자 서명", "登記車主簽署"), ("Date", "날짜", "日期")]),
    ],
}

FORMS["td557"] = {
    "slug": "drivinglic", "no": "TD557 (Rev. 2026)", "dept": "td", "file": "td557_e-fillable_eng.pdf",
    "title": ("Application for New Issue, Renewal & Addition – Full Driving Licence & Driving Instructor's Licence", "정식 운전면허 및 운전강사 면허 신규 발급·갱신·종류 추가 신청서", "申請簽發、續期及加簽正式駕駛執照及駕駛教師執照"),
    "intro": ("Please read the notes overleaf and complete the form in BLOCK LETTERS. Please enter ✓ in the appropriate box(es).", "뒷면의 안내를 읽고 대문자로 작성하세요. 해당란에 ✓ 표시하세요.", "請細閱背頁的注意事項，並用正楷填寫本表格。請在適當的方格內加上「✓」號。"),
    "items": [
        ("part", ("Part A  Particulars of Applicant", "A부  신청인 인적사항", "A部  申請人資料")),
        ("check", ("Title", "호칭", "稱謂"), TITLES),
        ("text", NAME_EN, "full"), ("text", NAME_LOCAL, "half"), ("text", ("Identity Document No.", "신분증 번호", "身份證明文件號碼"), "half"),
        ("addr", ("Residential Address", "주소", "住址")), ("text", TEL, "half"),
        ("addr", ("Correspondence Address (if different)", "우편 주소(다른 경우)", "通訊地址（如不同）")),
        ("part", ("Part B  Details of Application", "B부  신청 내용", "B部  申請詳情")),
        ("check", ("(1) Licence Applied for", "(1) 신청 면허", "(1) 申請的執照"), [("Full Driving Licence", "정식 운전면허", "正式駕駛執照"), ("Driving Instructor's Licence", "운전강사 면허", "駕駛教師執照")]),
        ("check", ("Licence Period", "면허 기간", "執照有效期"), [("10-year", "10년", "10年"), ("3-year", "3년", "3年"), ("1-year (aged 70 or above)", "1년(만 70세 이상)", "1年（70歲或以上）")]),
        ("check", ("(2) Required Service", "(2) 신청 업무", "(2) 所需服務"), [("First Issue", "신규 발급", "首次簽發"), ("Renewal", "갱신", "續期"), ("Addition of new entitlement(s)", "면허 종류 추가", "加簽新的駕駛類別")]),
        ("text", ("Vehicle class code(s) / group code(s) applied for (enter \"A\" beside the code for automatic transmission)", "신청 차종 코드·그룹 코드(자동변속 차량은 코드 옆에 \"A\")", "申請的車輛類別編號／組別編號（如屬自動波車輛，請在編號旁加上「A」）"), "full"),
        ("part", ("Part C  Medical Declaration", "C부  건강 상태 신고", "C部  健康聲明")),
        ("yn", ("Are you suffering from any disease or physical disability which may affect your ability to drive safely?", "안전 운전에 영향을 줄 수 있는 질병이나 신체장애가 있습니까?", "閣下是否患有可能影響安全駕駛能力的疾病或身體傷殘？")),
        ("part", ("Part D  Vehicle Class Codes", "D부  차종 코드", "D部  車輛類別編號")),
        ("table", [("Code", "코드", "編號"), ("Vehicle Class", "차종", "車輛類別")], [
            [("1", "1", "1"), ("Private Car", "승용차", "私家車")], [("2", "2", "2"), ("Light Goods Vehicle", "경화물차", "輕型貨車")],
            [("3", "3", "3"), ("Motor Cycle", "오토바이", "電單車")], [("4", "4", "4"), ("Motor Tricycle", "삼륜 오토바이", "機動三輪車")],
            [("5", "5", "5"), ("Taxi", "택시", "的士")], [("8", "8", "8"), ("Light Bus", "소형 버스", "小型巴士")]]),
        ("part", ("Declaration", "선서", "聲明")),
        ("note", ("I declare that the information given in this application is true and correct.", "본인은 이 신청서의 정보가 사실이며 정확함을 선서합니다.", "本人聲明本申請書所填報的資料均屬真實及正確。")),
        ("sign", [("Signature of Applicant", "신청인 서명", "申請人簽署"), ("Date", "날짜", "日期")]),
    ],
}

FORMS["ir1249"] = {
    "slug": "addresschange", "no": "IR1249 (1/2026)", "dept": "ird", "file": "ir1249.pdf",
    "title": ("Notification of Change of Postal Address", "우편 주소 변경 신고서", "更改郵遞地址通知書"),
    "intro": ("To: The Commissioner of Inland Revenue. You may also login eTAX to update your address.", "수신: 국세청장. eTAX에 로그인하여 주소를 변경할 수도 있습니다.", "致：稅務局局長。你亦可登入「稅務易」更新地址。"),
    "items": [
        ("date", ("New POSTAL Address with effect from", "새 우편 주소 적용일", "新郵遞地址生效日期")),
        ("addr", ("New POSTAL Address", "새 우편 주소", "新郵遞地址")),
        ("note", ("Please amend the POSTAL Address of the file(s) as indicated by a ✓ in the box(es) below:", "아래에 ✓ 표시한 파일의 우편 주소를 변경해 주세요.", "請按下列方格內「✓」號所示，修改有關檔案的郵遞地址："))
        ,
        ("part", ("To be completed by salary earner / property owner / sole proprietor", "급여소득자·부동산 소유자·개인사업자 작성란", "由受薪人士／物業業主／獨資業務東主填寫")),
        ("boxes", ID_NO, 10),
        ("pair", ("Tax Return – Individuals file", "개인 세금 신고서 파일", "個別人士報稅表檔案"), [("Name of Individual", "개인 성명", "個別人士姓名"), ("File No.", "파일 번호", "檔案號碼")]),
        ("pair", ("Property Tax file", "재산세 파일", "物業稅檔案"), [("Location of property", "부동산 소재지", "物業地址"), ("File No.", "파일 번호", "檔案號碼")]),
        ("pair", ("Other Tax file", "기타 세금 파일", "其他稅項檔案"), [("Name of Taxpayer", "납세자 성명", "納稅人姓名"), ("File No.", "파일 번호", "檔案號碼")]),
        ("text", ("Full Name", "성명", "全名"), "half"), ("text", TEL, "half"),
        ("sign", [("Signature (same signature as used in tax returns / past correspondence)", "서명(세금 신고서·기존 서신과 같은 서명)", "簽署（須與報稅表／過往書信所用的簽署相同）"), ("Date", "날짜", "日期")]),
        ("part", ("To be completed by business owner / employer for change of postal address of the company", "사업주·고용주가 법인 우편 주소 변경 시 작성", "由業務東主／僱主就更改公司郵遞地址填寫")),
        ("pair", ("Profits Tax file", "법인이윤세 파일", "利得稅檔案"), [("Name of business / company", "사업체·법인명", "業務／公司名稱"), ("File No.", "파일 번호", "檔案號碼")]),
        ("pair", ("Employer's Return of Remuneration and Pensions file", "고용주 보수·연금 신고 파일", "僱主填報的薪酬及退休金報稅表檔案"), [("Name of business / company", "사업체·법인명", "業務／公司名稱"), ("File No.", "파일 번호", "檔案號碼")]),
        ("text", ("Name of Person signing", "서명인 성명", "簽署人姓名"), "half"), ("text", ("Designation", "직위", "職位"), "half"),
        ("sign", [("Signature", "서명", "簽署"), ("Company chop", "법인 인감", "公司印章"), ("Date", "날짜", "日期")]),
        ("note", ("Attention: Any change in business address should also be reported to the Business Registration Office within 1 month.", "참고: 사업장 주소가 바뀌면 1개월 이내에 사업자등록사무소에도 신고해야 합니다.", "注意：如更改業務地址，亦須在1個月內通知商業登記署。")),
    ],
}

ORDER = ["gf340", "ir76c", "td558", "td557", "ir1249"]

# ----------------------------------------------------------------------------- catalogue
CAT_TITLE = ("Government Form Catalogue", "정부 서식 목록", "政府表格目錄")
CAT_USERS = [("residents", ("For Residents users", "주민용", "居民適用")), ("business", ("For Business & Trade users", "비즈니스·무역용", "工商貿易適用")), ("nonresidents", ("For Non-Residents users", "비거주자용", "非居民適用"))]
CAT_SEARCH = ("Search government forms", "정부 서식 검색", "搜尋政府表格")
CAT_PH = ("Enter keyword(s)", "검색어 입력", "輸入關鍵字")
CAT_HOT = ("Hot Searches:", "인기 검색어:", "熱門搜尋：")
CAT_HOT_WORDS = [("address", "주소", "地址"), ("driving licence", "운전면허", "駕駛執照"), ("employment", "채용", "政府職位"), ("tax", "과세", "稅"), ("vehicle licence", "차량 면허", "車輛牌照")]
CAT_INTRO = ("On this page you can find government forms, guidance notes and related information.", "이 페이지에서 정부 서식, 작성 안내 및 관련 정보를 찾을 수 있습니다.", "你可在本頁找到政府表格、填表須知及相關資料。")
CAT_FORMATS = ("Forms are available in one or more of the following formats:", "서식은 다음 형식 중 하나 이상으로 제공됩니다.", "表格會以下列一種或多種格式提供：")
CAT_FMT = [("Adobe PDF", "Adobe PDF", "Adobe PDF"), ("Online Form", "온라인 서식", "網上表格"), ("Microsoft Word", "Microsoft Word", "Microsoft Word")]
CAT_COMMON = ("Commonly Used Government Forms", "자주 쓰는 정부 서식", "常用政府表格")
CAT_TABS = [("svc", ("Services", "서비스별", "服務")), ("life", ("Life Events", "생활 이벤트별", "生活事件"))]
CAT_NONE = ("No forms found.", "일치하는 서식이 없습니다.", "找不到表格。")
CAT_EMPTY = ("There are no commonly used forms under this category.", "이 분류에는 자주 쓰는 서식이 없습니다.", "此類別沒有常用表格。")
# Services tab: category slug (from the residents tree) -> [(sub-heading, [form codes])]
CAT_SVC = {
    "employment": [(("Job Search", "구직", "求職"), ["gf340"])],
    "taxes": [(("Salaries Tax & Personal Assessment", "근로소득세 및 개인 과세", "薪俸稅及個人入息課稅"), ["ir76c"]), (("General Information", "일반 정보", "一般資料"), ["ir1249"])],
    "transport": [(("Driving Licences, Tests & Permits", "운전면허·시험·허가", "駕駛執照、考試及許可證"), ["td557"]), (("Vehicle Registration, Transfer & Examination", "차량 등록·이전·검사", "車輛登記、轉讓及檢驗"), ["td558"])],
    "housing": [(("Moving Home", "이사", "搬遷"), ["ir1249"])],
}
CAT_LIFE = [
    (("Looking for a Job", "구직", "求職"), ["gf340"]),
    (("Moving Home", "이사", "搬遷"), ["ir1249"]),
    (("Owning and Driving a Vehicle", "차량 소유·운전", "擁有及駕駛車輛"), ["td557", "td558"]),
    (("Paying Tax", "세금 납부", "繳稅"), ["ir76c", "ir1249"]),
]
VIEWER = {"print": ("Print", "인쇄", "列印"), "save": ("Download (Save as PDF)", "내려받기(PDF로 저장)", "下載（另存為PDF）"), "back": ("Back to GovBHG", "정부포털 BHG로 돌아가기", "返回BHG政府一站通"),
          "page": ("Page", "쪽", "頁"), "official": ("For official use only", "관공서 기재란", "此欄由辦事處填寫")}
