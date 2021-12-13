import sqlite3

DATASET = [
    ("Tencho", "2018-12-03"),
    ("Bessho", "2018-12-03"),
    ("Emoto", "2020-12-03"),
    ("Gamo", "2020-12-03"),
    ("Funakoshi", "2020-12-03"),
    ("Funakoshi", "2020-12-03"),
    ("Doigaki", "2020-12-03"),
    ("Doigaki", "2020-20-03"),
    ("Chikura", "2020-12-03"),
    ("Akabane", "2020-12-03"),
]


def main():
    conn = sqlite3.connect(":memory:")

    conn.executescript(
        """
        DROP TABLE IF EXISTS foobar;
        CREATE TABLE foobar (
            last_name TEXT TEXT NOT NULL,
            start_day TEXT NOT NULL
        );
        """
    )

    conn.executemany("INSERT INTO foobar VALUES (?, ?)", DATASET)

    query = """
        SELECT last_name,
            start_day,
            COUNT(*) AS num_entries
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10;
    """

    print(conn.execute(query).fetchall())


if __name__ == "__main__":
    main()
