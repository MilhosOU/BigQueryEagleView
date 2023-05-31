import os
import sys
import pandas as pd
from tqdm import tqdm
from termcolor import colored
from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

def main(project_id):

    # Get list of datasets in the project
    datasets = list(client.list_datasets(project_id))
    datasets_list = [dataset.dataset_id for dataset in datasets]

    print(colored('Total number of datasets: ', 'blue'), len(datasets_list))

    # Create a DataFrame to store all the results
    all_results = pd.DataFrame()

    # Loop through each dataset (schema)
    for dataset_name in tqdm(datasets_list, desc = 'Processing datasets', ncols = 100):
        print(colored('Processing dataset: ', 'green'), dataset_name)
        
        # Define the query
        query = f"""
        SELECT *
        FROM `{project_id}`.{dataset_name}.INFORMATION_SCHEMA.TABLES AS I
        LEFT JOIN `{project_id}`.{dataset_name}.__TABLES__ AS T ON I.TABLE_NAME = T.table_id
        LEFT JOIN `{project_id}`.{dataset_name}.__TABLES_SUMMARY__ AS S ON I.TABLE_NAME = S.table_id
        """

        # Run the query
        query_job = client.query(query)

        # Convert the results to a pandas DataFrame
        results = query_job.to_dataframe()

        # Append the results to the all_results DataFrame
        all_results = pd.concat([all_results, results])

    print(colored('Writing results to CSV file...', 'yellow'))

    # Write the all_results DataFrame to a CSV file
    all_results.to_csv('bigquery_results.csv', index=False)
    print(colored('CSV file written successfully.', 'green'))


if __name__ == '__main__':
    project_id = sys.argv[1]
    main(project_id)
