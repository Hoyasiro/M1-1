# 아이 키 성장 기록 × 성장도표 비교 시계열 분석 (M1-1)

> 분석 내용과 결과는 [REPORT.md](REPORT.md)에 정리합니다. (작성 예정)

## 폴더 구조

```
data/child_growth_anon.csv   # 익명화된 성장 기록 (분석 입력)
data/growth_chart_2017.xlsx  # 2017 소아청소년 성장도표 (비교 기준)
prepare_data.py              # 원본 → 익명화 변환 스크립트
requirements.txt             # 라이브러리 버전 고정
```

## 데이터 출처

| 파일 | 출처 | 기간/범위 | 비고 |
|---|---|---|---|
| `child_growth_anon.csv` | 보호자가 직접 기록한 아이(남아) 키·몸무게 기록 | 2017-01 ~ 2026-10, 435행 | 익명화본 |
| `growth_chart_2017.xlsx` | 질병관리청, [2017 소아청소년 성장도표](https://knhanes.kdca.go.kr/knhanes/grtcht/dwnld/measPrg.do) | 0 ~ 227개월, 성별별 LMS·백분위 | 이용 조건 확인 중 |

참고: 국민건강보험공단 [영유아성장도표 LMS 기준](https://www.data.go.kr/data/15133061/fileData.do)(0~84개월, 이용허락범위 제한 없음)은
위 성장도표와 0~84개월 남아 키 M값이 완전히 일치하여 별도로 포함하지 않았다.

## 개인정보 보호

원본 데이터와 생년월일 파일은 미성년자 개인정보 보호를 위해 저장소에서 제외했으며,
분석은 익명화본(`data/child_growth_anon.csv`)부터 재현 가능하다.

익명화 방식: 실제 측정 날짜(`Date`)를 삭제하고 아래 두 컬럼으로 대체했다.
- `days`: 생후 경과 일수
- `month`: 측정 월(1~12)

## 실행 방법

```bash
python -m pip install -r requirements.txt
```
