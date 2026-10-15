
foundry_api_key = ""
foundry_endpoint = "https://azure-test-project-12-resource.openai.azure.com/openai/v1"
foundry_model = "gpt-4.1-mini"

storage_base = "file:/Workspace/CAPSTONE_3/uber-taxi-agentic-etl/data"

source_path = f"{storage_base}/ncr_ride_bookings.csv"
base_path = "/Volumes/databricks_workspace_12/default/etl_output"
bronze_path = f"{base_path}/bronze"
silver_path = f"{base_path}/silver"

# Quarantine necessary for Uber ETL
quarantine_path = f"{base_path}/quarantine"

gold_daily_path = f"{base_path}/gold/daily_trip_summary"
gold_location_path = f"{base_path}/gold/location_trip_summary"
gold_payment_path = f"{base_path}/gold/payment_type_trip_summary"

