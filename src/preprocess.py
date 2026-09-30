from pathlib import Path

import pandas as pd


def find_project_root(marker = ".git"):
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if(parent/marker).exists():
            return parent
    raise FileNotFoundError("未找到项目根目录，请确认在项目内运行")

# PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = find_project_root()
PARQUET = PROJECT_ROOT / "data" / "parquet"
PROCESSED = PROJECT_ROOT / "data" / "processed"

def main():
    PROCESSED.mkdir(parents= True, exist_ok=True)
    df = pd.read_parquet(PARQUET/"user_behavior_raw.parquet")
    df.columns = df.columns.str.strip().str.lower()
    df = df.drop(columns=['user_geohash'])
    df = df.dropna(subset=["user_id","item_id"])
    df = df.drop_duplicates()
    df = df[df['behavior_type'].isin([1,2,3,4])].copy()
    df['behavior_type'] = df['behavior_type'].map({1:'浏览',2:'收藏',3:'加购',4:'购买'}).astype('category')
    df['time'] = pd.to_datetime(df['time'])
    df.to_parquet(PROCESSED/"user_behavior_clean.parquet",index=False)

if __name__ == "__main__":
    main()