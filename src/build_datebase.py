from pathlib import Path

import duckdb


def find_project_root(marker = ".git"):
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if(parent/marker).exists():
            return parent
    raise FileNotFoundError("未找到项目根目录，请确认在项目内运行")

# PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = find_project_root()
PROCESSED = PROJECT_ROOT / "data" / "processed"
DB = PROJECT_ROOT / "data" / "datebase"
CLEAN_PARQUET = PROCESSED/"user_behavior_clean.parquet"
DB_PATH = DB/"user_behavior.duckdb"

def main():
    DB.mkdir(parents=True,exist_ok= True)
    if not CLEAN_PARQUET.exists():
        raise FileNotFoundError(f"清洗后的数据不存在：{CLEAN_PARQUET}")

    # with 会在退出时自动关闭连接，即使抛异常
    with duckdb.connect(str(DB_PATH)) as con:
        con.execute(f"""
            CREATE OR REPLACE TABLE user_behavior AS
            SELECT * FROM read_parquet('{CLEAN_PARQUET}')
        """)
        count = con.sql("SELECT COUNT(*) FROM user_behavior").fetchone()[0]
        print(f"建表完成，共 {count} 行")

if __name__ == "__main__":
    main()