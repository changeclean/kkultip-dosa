"""꿀팁도사 출생연도별 띠 운세. 오락용 창작 콘텐츠이며 예측 서비스가 아닙니다."""
from datetime import timedelta

MESSAGES = {
 "총운": [
  "해야 할 일을 하나씩 정리하고 작은 성취부터 확인해 보세요. 다른 사람과 속도를 비교할 필요는 없습니다.",
  "익숙한 일에서도 놓친 부분이 없는지 살펴보세요. 차분하게 점검하는 태도가 어울립니다.",
  "주변의 이야기를 듣되 자신에게 중요한 기준을 생각해 보세요. 종이에 적으면 마음을 정리하기 쉽습니다.",
  "새로운 계획은 한꺼번에 시작하지 않아도 됩니다. 가장 손쉬운 첫 단계부터 해보세요.",
  "일정이 바뀌더라도 잠깐 여유를 두고 우선순위를 다시 정해 보세요. 유연함도 좋은 선택입니다.",
  "미뤄 둔 약속이나 일을 돌아보세요. 작은 실천이 다음 행동을 이어가는 계기가 될 수 있습니다."
 ],
 "재물운": [
  "충동구매보다 꼭 필요한 지출을 먼저 따져보세요. 예산표를 살펴보기에 좋은 기회입니다.",
  "할인율에만 마음을 빼앗기지 말고 사용 빈도를 생각해 보세요. 구매 조건을 비교하는 것도 좋습니다.",
  "구독 서비스나 자동이체 내역을 점검해 보세요. 잊고 있던 작은 지출을 찾을 수 있습니다.",
  "큰돈을 움직일 계획이라면 관련 조건과 위험을 직접 확인하세요. 운세를 투자 판단에 활용하지 마세요.",
  "지출을 하루만 기록해 봐도 소비 습관을 발견할 수 있습니다. 실천 가능한 작은 목표를 세워보세요.",
  "누군가와 돈을 주고받는 약속이 있다면 금액과 일정을 명확하게 남기세요. 친분과 금전 관리는 별개입니다."
 ],
 "애정운": [
  "소중한 사람에게 먼저 안부를 건네 보세요. 꾸밈없는 한마디가 대화를 시작하는 데 도움이 됩니다.",
  "상대방이 내 마음을 당연히 알 거라고 생각하지 마세요. 원하는 바를 다정하게 표현해 보세요.",
  "다른 의견이 나와도 바로 답을 정하려 하지 말고 이유를 들어보세요. 서로를 이해하는 시간이 될 수 있습니다.",
  "혼자만의 시간이 필요하다면 부드럽게 이야기해 보세요. 서로의 경계를 존중하는 것도 관계의 일부입니다.",
  "고마웠던 일을 구체적으로 떠올려 보세요. 작은 감사 표현이 평범한 하루를 따뜻하게 만듭니다.",
  "새로운 만남을 급하게 판단하기보다 함께 있을 때 편안한지 살펴보세요. 관계의 속도는 사람마다 다릅니다."
 ],
 "건강운": [
  "오래 앉아 있었다면 가볍게 자세를 바꾸고 잠시 움직여 보세요. 무리하지 않는 습관이 중요합니다.",
  "잠과 휴식 시간이 일정한지 돌아보세요. 피곤한 날에는 할 일을 조금 덜어내는 것도 방법입니다.",
  "바쁘더라도 식사와 물 마시는 시간을 챙겨 보세요. 몸의 신호를 무시하지 않는 것이 좋습니다.",
  "화면을 오래 봤다면 눈과 어깨를 잠깐 쉬게 해주세요. 짧은 휴식도 일상에 넣어 보세요.",
  "운동 계획은 자신의 체력에 맞게 조절해 보세요. 갑작스럽게 무리할 필요는 없습니다.",
  "건강에 관한 걱정은 운세로 판단하지 마세요. 불편한 증상이 있으면 필요한 진료를 받으세요."
 ],
 "직장·사업운": [
  "업무나 약속의 범위와 마감일을 다시 확인해 보세요. 사전 조율이 불필요한 일을 줄일 수 있습니다.",
  "새로운 제안을 받았다면 장점과 부담을 함께 적어 보세요. 실제 조건을 비교한 판단이 중요합니다.",
  "협력할 일이 있다면 서로 기대하는 결과를 먼저 확인해 보세요. 짧은 대화가 오해를 줄여 줍니다.",
  "반복되는 일에서 작은 개선점을 찾아보세요. 큰 변화보다 꾸준한 정리가 도움이 될 수 있습니다.",
  "해야 할 일을 긴급도와 중요도로 나눠 보세요. 우선순위가 뚜렷하면 집중하기 쉬워집니다.",
  "진행한 일의 성과를 간단히 기록해 보세요. 다음 계획을 세울 때 유용한 참고가 됩니다."
 ]
}
YOUNG = {
 "총운": ["작은 도전 하나를 골라 시작해 보세요. 잘하는 것보다 꾸준히 해보는 과정도 중요해요.","친구와 생각이 달라도 차분히 이야기해 보세요. 서로의 입장을 알게 될 수 있어요.","하루에 해낸 일을 떠올려 보세요. 사소한 성취도 소중합니다."],
 "재물운": ["용돈을 어떻게 쓸지 미리 적어 보세요. 갖고 싶은 것과 필요한 것을 구분해 볼 수 있어요.","돈을 쓰기 전에 비슷한 물건이 있는지 살펴보세요. 작은 절약 습관을 만들 수 있어요.","저축하고 싶은 목표를 정해 보세요. 금액보다 계획을 지키는 연습이 중요해요."],
 "애정운": ["가족이나 친구에게 고마운 마음을 표현해 보세요. 함께 웃는 시간도 소중해요.","서로 좋아하는 놀이가 달라도 존중해 보세요. 새로운 공통점을 찾을 수 있어요.","친구의 이야기를 잘 들어보세요. 자신의 기분도 편안하게 말해 보면 좋아요."],
 "건강운": ["놀고 공부하는 사이에 쉬는 시간을 챙겨 보세요. 몸이 피곤하면 보호자에게 이야기해요.","잠자는 시간을 일정하게 정해 보세요. 활동과 휴식의 균형이 중요해요.","화면을 오래 봤다면 잠깐 멀리 바라보세요. 가벼운 놀이로 몸을 움직여도 좋아요."],
 "직장·사업운": ["공부에서 모르는 부분은 질문해 보세요. 질문하는 것도 배우는 과정이에요.","해야 할 숙제를 작은 순서로 나눠보세요. 하나를 끝내고 다음 것을 시작해요.","새로운 취미를 배우며 실수해도 괜찮아요. 천천히 익히는 시간을 가져 보세요."]
}
STAGES = [
 (17,"학교생활과 친구 관계, 새로운 배움에서 즐거운 순간을 찾아보세요."),
 (29,"진로와 관계, 새로운 경험 사이에서 자신의 속도를 지켜보세요."),
 (44,"일과 개인 시간, 가까운 사람과의 약속을 균형 있게 정리해 보세요."),
 (59,"맡은 역할이 많더라도 자신을 돌보는 시간을 남겨 두세요."),
 (200,"경험에서 얻은 지혜를 활용하되 새로운 의견에도 마음을 열어 보세요.")
]

def fortune_detail(kind, code, env):
 today=env["TODAY"]
 start=env["WEEK_START"]
 animals=env["ANIMALS"]
 idx=next(i for i,(c,_,_) in enumerate(animals) if c==code)
 _,name,emoji=animals[idx]
 daily=(kind=="today")
 label="오늘의 운세" if daily else "주간운세"
 when=today.strftime("%Y년 %m월 %d일") if daily else f'{start.strftime("%Y년 %m월 %d일")} ~ {(start+timedelta(days=6)).strftime("%m월 %d일")}'
 seed=today.toordinal() if daily else start.toordinal()
 themes=env["DAILY_THEMES"] if daily else env["WEEKLY_THEMES"]
 head,copy=themes[(seed*7+(0 if daily else 4)+idx*5)%len(themes)]
 esc=env["esc"]
 years=[year for year in range(1948,today.year+1) if (year-2020)%12==idx and today.year-year>=3]
 links=''.join(f'<a href="#year-{y}" class="fortune-year-link">{y}년생</a>' for y in reversed(years))
 keys=list(MESSAGES)
 cards=[]
 for year in reversed(years):
  age=today.year-year
  young=age<18
  captions=["총운","용돈·생활운","친구·가족운","생활·활력운","학업·성장운"] if young else keys
  offset=seed+idx*7+year//12
  topics=[]
  for j,key in enumerate(keys):
   source=YOUNG[key] if young else MESSAGES[key]
   msg=source[(offset+j*3)%len(source)]
   topics.append(f'<section class="fortune-topic"><h3>{esc(captions[j])}</h3><p>{esc(msg)}</p></section>')
  stage=next(text for maxage,text in STAGES if age<=maxage)
  cards.append(f'''<section class="fortune-birth-card" id="year-{year}"><div class="fortune-birth-heading"><span aria-hidden="true">{emoji}</span><div><small>{year} BIRTH YEAR</small><h2>{year}년생 {name}</h2></div><a href="#birth-years" class="fortune-back">연도 선택 ↑</a></div><p class="fortune-age-note">{esc(stage)}</p><div class="fortune-topics">{''.join(topics)}</div></section>''')
 other="weekly" if daily else "today"
 intro=f'<div class="fortune-summary"><b>✦ {name} 전체 총운</b><h2>{esc(head)}</h2><p>{esc(copy)}</p></div>'
 body=f'''<div class="container fortune-page fortune-detail-page">{env['breadcrumb']((label,f'/fortune/{kind}/'),(name,None))}<div class="fortune-title"><span class="eyebrow">KKULTIP DOSA · {esc(when)}</span><span class="fortune-glyph">{emoji}</span><h1>{name} {label}</h1><p>{esc(when)}</p></div>{intro}<nav class="fortune-year-nav" id="birth-years" aria-label="출생연도 선택"><h2>몇 년생이신가요?</h2><p>연도를 누르면 해당 상세 해설로 이동합니다.</p><div class="fortune-year-grid">{links}</div></nav>{env['adslot']()}<div class="fortune-birth-list">{''.join(cards)}</div><div class="note-box fortune-disclaimer"><b>🔮 운세 콘텐츠 안내</b><p>재미로 읽는 창작 콘텐츠이며 미래를 예측하지 않습니다. 재물·건강·법률 관련 판단에는 이용하지 마세요. 음력 설이나 입춘 전후 태어난 분은 띠가 다를 수 있습니다.</p></div><div class="fortune-bottom"><a class="btn btn-light" href="/fortune/{kind}/">← 다른 띠 보기</a><a class="btn btn-primary" href="/fortune/{other}/{code}/">{'주간' if daily else '오늘의'} 운세도 보기 →</a></div></div>'''
 result=env["shell"](f'{when} {name} {label} · 출생연도별 운세',f'{when} {name} 출생연도별 총운·재물운·애정운·건강운·직장운 해설',body,kind,f'fortune/{kind}/{code}/',data={'@type':'WebPage'})
 return result.replace('</head>','<link rel="stylesheet" href="/assets/fortune-detail.css"></head>',1)
