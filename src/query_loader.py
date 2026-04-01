from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = BASE_DIR / "sql" / "queries"


def load_query(query_name):

    query_path = SQL_DIR / f"{query_name}.sql"

    with open(query_path, "r") as file:
        query = file.read()

    return query