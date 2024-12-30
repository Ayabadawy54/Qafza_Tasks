#import needed libraries
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pyodbc
import pandas as pd
import os

# Get password from environment variable
pwd = os.environ.get('PGPASS')  # 'PGPASS' is the name of the environment variable storing the password

# Ensure the password is set
if not pwd:
    raise ValueError("Password environment variable 'PGPASS' is not set.")

# PostgreSQL user and role
uid = "etl"  # The role for PostgreSQL

# SQL Server details
sql_server_driver = "{ODBC Driver 17 for SQL Server}"  # Make sure the driver is installed
server = "DESKTOP-BVMIMVV"  # Replace with your actual SQL Server name
database = "AdventureWorks2022"  # Replace with your SQL Server database name

# PostgreSQL details
postgres_server = "localhost"  # Replace with your PostgreSQL server name or IP address
postgres_database = "ETLData"  # Replace with your PostgreSQL database name

# Extract data from SQL Server
def extract():
    try:
        # SQL Server connection string
        connection_string = f'DRIVER={sql_server_driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        src_engine = create_engine(connection_url)
        src_conn = src_engine.connect()
        
        # Specify schema-qualified table name
        schema = "HumanResources"
        table_name = "Department"
        full_table_name = f"{schema}.{table_name}"
        
        print(f"Extracting data from table: {full_table_name}")
        
        # Extract data from the schema-qualified table
        df = pd.read_sql_query(f'SELECT * FROM {full_table_name}', src_conn)
        df = transform(df)  # Apply transformations to the extracted data
        load(df, table_name)  # Load the transformed data to PostgreSQL

    except Exception as e:
        print(f"Data extract error: {str(e)}")

# Transform the data (apply any necessary transformations)
def transform(df):
    try:
        # Example transformation 1: Rename columns (if needed)
        df.rename(columns={
            'DepartmentID': 'department_id',
            'Name': 'department_name',
            'GroupName': 'group_name',
            'ModifiedDate': 'modified_date'
        }, inplace=True)
        
        # Example transformation 2: Fill missing values with a default (if needed)
        df.fillna({'department_name': 'Unknown'}, inplace=True)

        # Example transformation 3: Remove duplicates (if needed)
        df.drop_duplicates(inplace=True)

        # Example transformation 4: Data type casting (if needed)
        df['department_id'] = df['department_id'].astype(int)
        
        # More transformations can be added as per business rules
        print("Transformations applied successfully.")
        return df

    except Exception as e:
        print(f"Data transformation error: {str(e)}")
        return df  # Return the original df in case of an error

# Load data to PostgreSQL
def load(df, tbl):
    try:
        rows_imported = 0
        
        # PostgreSQL connection string for 'etl' user
        postgres_url = f'postgresql://{uid}:{pwd}@{postgres_server}:5432/{postgres_database}'
        engine = create_engine(postgres_url)
        
        print(f"Importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}")
        
        # Save df to PostgreSQL as a staging table
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, chunksize=100000)
        
        rows_imported += len(df)
        print("Data imported successfully")
    except Exception as e:
        print(f"Data load error: {str(e)}")

# Execute the ETL process
if __name__ == "__main__":
    extract()
