# instantEDA

## Overview

The EDA Report Generator automates the process of generating a detailed
Exploratory Data Analysis (EDA) report for any given CSV dataset. This
tool leverages the `ydata_profiling` library to provide key insights
about the dataset, such as summary statistics, data distributions,
missing value analysis, and more, in an interactive HTML format.

The project currently includes a sample dataset (`nissan-dataset1.csv`)
to demonstrate its functionality, but it is designed to work with any
CSV dataset.

## Features

-   **Automated EDA Report**: Generate an in-depth report on any CSV
    dataset using `ydata_profiling`.
-   **CSV Upload**: Simply upload your own CSV file to get a customized
    EDA report.
-   **HTML Output**: The generated report is saved as an interactive
    HTML file.
-   **Data Profiling**: Includes a variety of analysis such as data
    types, correlations, distributions, missing values, and more.

## Requirements

The following libraries are required to run the project:

-   `ydata-profiling==4.12.2`
-   `pandas==2.2.3`

To install the dependencies, use the `requirements.txt` file:

``` bash
pip install -r requirements.txt
```

### `requirements.txt`

    ydata-profiling==4.12.2
    pandas==2.2.3

## Usage

1.  **Prepare your CSV file**: Place your CSV dataset (e.g.,
    `nissan-dataset1.csv`) in the project directory. The project
    currently includes a sample file, but you can upload any dataset in
    CSV format.

2.  **Generate the EDA Report**: Run the script to generate an EDA
    report for the dataset:

    ``` bash
    python generate_report.py
    ```

3.  **View the Report**: Once the script completes, the output will be
    saved as an HTML file (`nissan.html` by default). You can open this
    file in any web browser to explore the data insights.

4.  **Customizing for Your Dataset**: To use a different dataset,
    replace the sample `nissan-dataset1.csv` with your own CSV file in
    the Python script.

## Sample Output

The generated HTML report includes the following sections:

-   **Overview**: Basic information about the dataset (number of rows,
    columns, etc.).
-   **Data Types**: Distribution of data types across columns.
-   **Missing Value Analysis**: Summary of missing values in the
    dataset.
-   **Correlations**: Visualization and statistics about column
    correlations.
-   **Visualizations**: Distribution charts, histograms, and other
    visual insights.

## License

This project is licensed under the MIT License - see the LICENSE file
for details.
