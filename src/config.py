from pathlib import Path


def find_project_root(marker = ".git"):
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if(parent/marker).exists():
            return parent
    raise FileNotFoundError("未找到项目根目录，请确认在项目内运行")

PROJECT_ROOT = find_project_root()

# 数据目录
DATA_DIR = PROJECT_ROOT/"data"
RAW_DIR = DATA_DIR/"raw"
PARQUET_DIR = DATA_DIR/"parquet"
PROCESSED_DIR = DATA_DIR/"processed"
DB_DIR = DATA_DIR/"database"

# 文件路径
RAW_CSV = RAW_DIR/"user_behavior.csv"
RAW_PARQUET = PARQUET_DIR/"user_behavior_raw.parquet"
CLEAN_PARQUET = PROCESSED_DIR/"user_behavior_clean.parquet"
DB_PATH = DB_DIR/"user_behavior.duckdb"

def ensure_dirs():
    """确保所有数据目录存在。"""
    for d in [RAW_DIR, PARQUET_DIR, PROCESSED_DIR, DB_DIR, DATA_DIR]:
        d.mkdir(parents=True, exist_ok=True)

