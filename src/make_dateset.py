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
RAW = PROJECT_ROOT / "data" / "raw"
PARQUET = PROJECT_ROOT / "data" / "parquet"

def main():
    PARQUET.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(RAW / "user_behavior.csv", low_memory=False)
    df.to_parquet(PARQUET / "user_behavior_raw.parquet", index=False)

if __name__ == "__main__":
    main()