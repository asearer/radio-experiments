import psycopg2
from alembic import command
from alembic.config import Config

def migrate_database():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='your_database_name',
        user='your_database_user',
        password='your_database_password',
        host='your_database_host',
        port='your_database_port'
    )

    # Run Alembic migrations
    alembic_cfg = Config("alembic.ini")  # Assuming alembic.ini is your Alembic configuration file
    command.upgrade(alembic_cfg, "head")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    migrate_database()
