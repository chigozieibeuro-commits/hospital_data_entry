import psycopg2

def connection():
    con=psycopg2.connect(
        host="db",
        postgres_user="postgres",
        postgres_db="health_file",
        postgres_password="password",
        port="5432:5432"
    )

    return con