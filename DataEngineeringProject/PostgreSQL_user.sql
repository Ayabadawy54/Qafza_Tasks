-- Create the ETL user/role with the password 'ETLProject'
CREATE ROLE etl WITH LOGIN PASSWORD 'ETLProject';

-- Grant CONNECT permission on the ETLData database
GRANT CONNECT ON DATABASE "ETLData" TO etl;

-- Grant permissions on all tables in the public schema
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO etl;

-- Optionally, if you want to allow the ETL role to automatically access tables created in the future
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO etl;

-- Grant CREATE privileges on the public schema
GRANT CREATE ON SCHEMA public TO etl;

-- Optionally, grant USAGE privileges if not already granted
GRANT USAGE ON SCHEMA public TO etl;


-- Allow the etl role to automatically have permissions on tables created in the public schema
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO etl;

-- Optionally, allow etl to manage future sequences
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT USAGE, SELECT ON SEQUENCES TO etl;

SELECT * FROM "stg_Department";

