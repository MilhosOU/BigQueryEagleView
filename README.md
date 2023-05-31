# BigQuery Table Metadata Extraction Script

## Overview

This script serves a crucial role in understanding the state of data within a Google Cloud BigQuery project. 
It is designed to systematically explore all the datasets and their associated tables, retrieving key metadata.

Metadata includes but is not limited to:

- Table and schema names
- Creation time
- Last update time
- Row count
- Storage size

The script collates all this information and compiles it into a CSV file. 
This high-level view of your BigQuery data landscape is invaluable for data governance, system optimization, auditing, and other strategic purposes.

## How it works
The script uses the Google Cloud BigQuery client to iterate through each dataset within a given project.
For each dataset, it runs a query to extract the metadata from the `INFORMATION_SCHEMA.TABLES`, `__TABLES__`, and `__TABLES_SUMMARY__ `views. 
All extracted data is then compiled into a pandas DataFrame, which is then exported to a CSV file.

## Usage
Run the script from the command line, passing in your Google Cloud Project ID as an argument. For example:

```bash
python main.py your-project-id
```

Replace `your-project-id` with the ID of your actual Google Cloud project. 
The script will create a CSV file named `bigquery_results.csv` in the same directory, containing metadata for all tables in the project.

## Dependencies
The script requires the following Python packages:

- os
- sys
- pandas
- tqdm
- termcolor
- google.cloud.bigquery

Ensure these are installed in your Python environment before running the script. You can install them with pip:

```bash
pip install pandas tqdm termcolor google-cloud-bigquery
```

## Authorization
Before running the script, ensure that you're authenticated with Google Cloud and have the necessary permissions to access the BigQuery project and datasets.
The script uses your default Google Cloud credentials. If you encounter a DefaultCredentialsError, follow the Google Cloud documentation to authenticate with a service account.
