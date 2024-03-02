# scripts/run_migrations.py

from alembic.config import Config
from alembic import command

def run_migrations():
    # Load Alembic configuration from the provided config file
    alembic_cfg = Config("alembic.ini")  # Path to your Alembic config file
    
    # Run the migrations to the latest version
    command.upgrade(alembic_cfg, "head")

    print("Running migrations...")

# Call the function to execute migrations when this script is run directly
if __name__ == "__main__":
    run_migrations()
