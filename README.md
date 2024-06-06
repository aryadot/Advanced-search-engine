# Warehouse and Retail Sales Data Engineering Project

This project demonstrates an end-to-end data engineering pipeline that extracts data from a CSV file, transforms it, and loads it into a PostgreSQL database using a star schema design. The processed data is then visualized using Metabase.

## Project Structure
![dashboard1.PNG](assets/architecture.PNG)

## Tech Stack

- Docker
- Python (Pandas, SQLAlchemy, logging)
- PostgreSQL
- Metabase

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Dorianteffo/etl_pipeline_docker_metabase.git
   ```

2. Navigate to the project directory:
   ```
   cd etl_pipeline_docker_metabase
   ```

3. Start the Docker containers:
   ```
   docker-compose up --build -d
   ```

4. Connect to the PostgreSQL database:
   ```
   docker exec -ti warehouse psql postgres://dorian:1412@localhost:5432/retail_sales
   ```

5. Create the necessary schemas by running the SQL script in the `sql` directory:
   ```sql
   CREATE SCHEMA landing_area;
   CREATE SCHEMA staging_area;
   ```

6. Run the Python scripts to load data into the landing area and transform it into the staging area:
   ```
   python pipeline/to_landing.py
   python pipeline/to_staging.py
   ```

7. Access the Metabase dashboard at `http://localhost:3000`.

## Data Pipeline

1. **Data Loading**: The `pipeline/to_landing.py` script reads the CSV file from the `dataset` directory and loads it into the `landing_area` schema of the PostgreSQL database using SQLAlchemy and Pandas.

2. **Data Transformation**: The `pipeline/to_staging.py` script reads the data from the `landing_area` schema, applies data cleaning and transformation logic, and builds fact and dimension tables based on the star schema design.

3. **Data Loading to Staging**: The transformed tables are loaded into the `staging_area` schema for visualization purposes.

4. **Data Visualization**: Metabase is used to connect to the PostgreSQL database and create a dashboard to visualize the data stored in the `staging_area` schema.

## Dataset

The dataset used in this project is sourced from https://catalog.data.gov/dataset/warehouse-and-retail-sales.

## Dashboard

The Metabase dashboard can be accessed at `http://localhost:3000` after following the setup instructions.

![dashboard1.PNG](assets/metabase_dashboard_1.PNG)
![dashboard2.PNG](assets/metabase_dashboard_2.PNG)


Feel free to explore the code and adapt it to your own data engineering projects!


