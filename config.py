from sqlalchemy import create_engine, text
import os



DB_URI = "mariadb+mariadbconnector://root:chethan123@localhost:3307/frappe"
#DB_URI = "oracle+cx_oracle://sys:chethan123@localhost:1521/XE?mode=SYSDBA"

# Azure OpenAI Configuration
config = {
    'api-version': '2024-05-01-preview',
    'openai-endpoint': "https://fabee-v2-chat.openai.azure.com/",
    'llm-deployment-name': "azure/gpt-4o",
    'api-key': ""
}

if not config['api-key']:
    raise ValueError("AZURE_OPENAI_API_KEY is missing! Set it in environment variables.")

def get_mariadb_tables():
    """Fetch all tables for the connected MariaDB schema."""
    engine = create_engine(DB_URI)
    with engine.connect() as conn:
        result = conn.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]
    return tables

TABLES = get_mariadb_tables()
