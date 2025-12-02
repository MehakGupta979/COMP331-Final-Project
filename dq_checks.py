# dq_checks.py - auto-generated
import pandas as pd
from pathlib import Path

DATA = Path('/mnt/data/Features data set.csv')
OUT = Path('/mnt/data/results')
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)

df['Date_raw'] = df['Date'].astype(str)
df['Date_p1'] = pd.to_datetime(df['Date_raw'], errors='coerce', infer_datetime_format=True, dayfirst=False)
df['Date_p2'] = pd.to_datetime(df['Date_raw'], errors='coerce', infer_datetime_format=True, dayfirst=True)
df['Date_strip'] = df['Date_raw'].str.strip().str.replace(r"[^\d\-/]", "", regex=True)
df['Date_p3'] = pd.to_datetime(df['Date_strip'], errors='coerce', infer_datetime_format=True)

def pick_date(r):
    for c in ['Date_p1','Date_p2','Date_p3']:
        if pd.notnull(r.get(c)):
            return r.get(c)
    return pd.NaT

df['Date_final'] = df.apply(pick_date, axis=1)

df.to_csv(OUT/'data_with_dates_fixed.csv', index=False)
print('Saved data_with_dates_fixed.csv')
