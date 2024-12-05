import mysql.connector


def save_to_sql(**kwargs):
    ti = kwargs["ti"]
    data = ti.xcom_pull(task_ids="scrape")

    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "",
    }

    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO breaking_news (author, published_at, text) VALUES (%s, %s, %s)",
        (data["author"], data["published_at"], data["text"]),
    )
    conn.commit()

    cur.close()
    conn.close()
