# SEA
## Overview

This Python script is designed to process and analyze event logs provided in a CSV format. It converts the CSV data into a JSON list, creates various statistical summaries, and visualizes data through plots saved in PDF and Excel formats. The script handles tasks like data cleaning, transformation, grouping, and visualization to provide insights into event logs such as the frequency of events by type, source IP, destination host/port, and the geographical location of source IPs.

### Features

- CSV to JSON Conversion: Transforms CSV log data into a JSON list for easier manipulation.
- Data Analysis and Summarization: Generates statistical summaries grouped by source IP and destination host/port.
- Excel Reporting: Saves detailed events and summaries into an Excel file with multiple sheets for comprehensive analysis.
- Data Visualization: Creates visual representations of data and saves them into a PDF file, including plots for events by object type, source IP, country, and the top targets of attacks.

### Requirements

- Python 3.x
- pandas
- matplotlib
- xlsxwriter

Ensure all dependencies are installed using pip:

    pip install pandas matplotlib xlsxwriter

## Usage

Prepare your CSV file with event logs. The expected delimiter between values in the CSV file is a semicolon (;). Execute the script from the command line, providing the path to your CSV file as an argument:
    
    python3 run.py path_to_your_file.csv

## Output

The script will create an 'data' directory if it doesn't exist.
Inside the 'data' directory, you'll find two files:

- events.xlsx: An Excel file containing detailed events, group summaries by source IP, and other statistical summaries.
- stats.pdf: A PDF file with visualized data plots.

## Note

This script assumes that the input CSV file contains specific columns such as time, src.ip, dst.host, dst.ip, dst.port, and object.type. Adjustments might be needed based on the actual structure of your CSV file.
