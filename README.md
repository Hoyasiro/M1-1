# 아이 키 성장 기록 × 성장도표 비교 시계열 분석 (M1-1)

> 분석 내용과 결과는 [REPORT.md](REPORT.md)에 정리합니다. (작성 예정)

## 폴더 구조

```
data/child_growth_anon.csv   # 익명화된 성장 기록 (분석 입력)
prepare_data.py              # 원본 → 익명화 변환 스크립트
requirements.txt             # 라이브러리 버전 고정
```

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
