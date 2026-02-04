import sqlite3
import pandas as pd
import os

from log import log_progress
from extract import extract_from_csv, extract_from_json, extract_from_xml
from transform import transform
from load import load_to_csv, load_to_db
from db import run_query


def main():
    # --------------------------------------------------
    # Project base directory (ETL_Lab_1/)
    # --------------------------------------------------
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Paths configuration
    log_file = os.path.join(BASE_DIR, "logs", "log_file.txt")
    data_path = os.path.join(BASE_DIR, "data", "raw")
    target_file = os.path.join(
        BASE_DIR, "data", "transformed", "transformed_data.csv"
    )

    # Database configuration (as requested in the lab)
    db_path = os.path.join(BASE_DIR, "etl_database.db")
    table_name = "vehicles"

    # Ensure required folders exist
    os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "data", "transformed"), exist_ok=True)

    # Connect to database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)

    # --------------------------------------------------
    # 1. Start ETL Process
    # --------------------------------------------------
    log_progress("ETL Job Started", log_file)

    # --------------------------------------------------
    # 2. Extract Phase
    # --------------------------------------------------
    log_progress("Extract phase Started", log_file)

    df_csv = extract_from_csv(data_path)
    df_json = extract_from_json(data_path)
    df_xml = extract_from_xml(data_path)

    extracted_data = pd.concat(
        [df_csv, df_json, df_xml], ignore_index=True
    )
    log_progress("Data extraction complete", log_file)

    # --------------------------------------------------
    # 3. Transform Phase
    # --------------------------------------------------
    log_progress("Transform phase Started", log_file)
    transformed_data = transform(extracted_data)
    log_progress("Data transformation complete", log_file)

    # --------------------------------------------------
    # 4. Load Phase
    # --------------------------------------------------
    load_to_csv(transformed_data, target_file)
    log_progress("Data saved to CSV", log_file)

    load_to_db(transformed_data, conn, table_name)
    log_progress("Data loaded to Database", log_file)

    # --------------------------------------------------
    # 5. Query Phase (Task 4)
    # --------------------------------------------------
    log_progress("Running queries", log_file)

    while True:
        print("\n--- Query Menu ---")
        print("1. Show vehicles manufactured after 2015")
        print("2. Count vehicles by fuel type")
        print("3. Show average price of vehicles")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            query_statement = f"""
            SELECT car_model, year_of_manufacture, price
            FROM {table_name}
            WHERE year_of_manufacture > 2015
            """
            run_query(query_statement, conn)

        elif choice == "2":
            query_statement = f"""
            SELECT fuel, COUNT(*) AS count
            FROM {table_name}
            GROUP BY fuel
            """
            run_query(query_statement, conn)

        elif choice == "3":
            query_statement = f"""
            SELECT ROUND(AVG(price), 2) AS average_price
            FROM {table_name}
            """
            run_query(query_statement, conn)

        elif choice == "4":
            print("Exiting query menu...")
            break

        else:
            print("Invalid choice, please try again.")

    # Close connection
    conn.close()
    log_progress("ETL Job Ended", log_file)


if __name__ == "__main__":
    main()
