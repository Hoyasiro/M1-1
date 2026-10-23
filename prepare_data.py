"""원본 성장 기록을 익명화한다.

실제 날짜(Date)를 지우고, 그 대신 아래 두 컬럼을 만든다.
- days : 생후 경과 일수 (측정일 - 생년월일)
- month: 측정 월(1~12). 계절별 분석용

생년월일은 코드에 적지 않고 birthdate.txt(저장소 제외)에서 읽는다.
실행: python prepare_data.py
"""
import pandas as pd

RAW_PATH = "data/child_growth_raw.xlsx"
ANON_PATH = "data/child_growth_anon.csv"

with open("birthdate.txt", encoding="utf-8") as f:
    birthdate = pd.Timestamp(f.read().strip())

raw = pd.read_excel(RAW_PATH)

anon = raw.copy()
anon["days"] = (anon["Date"] - birthdate).dt.days
anon["month"] = anon["Date"].dt.month
anon = anon.drop(columns=["Date"])

anon.to_csv(ANON_PATH, index=False, encoding="utf-8-sig")
print(anon.shape)
print(anon.columns.tolist())
