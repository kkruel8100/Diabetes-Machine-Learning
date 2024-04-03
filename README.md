## Diabetes-Machine-Learning

#### Question

Can survey results predict whether a person has diabetes?

To Do

1. Add additional libraries
2. Verify structure
3. Add steps

#### Programs/Libraries

Python, Pandas, MatPlotLib

#### Installs

#### Program Structure

    └───root
        └───datasets
            │   2015_formats.json
            │   codebook15_llcp.pdf
            └───sample_dataset.csv
        └───utils
            │   pipeline.py
            │   sample_cleaning_utils.py
            └───source_utils.py
        │   .env
        │   .gitignore
        │   main.ipynb
        │   README.md
        │   sample.ipynb
        └───source.ipynb

#### Program Details

_Source_

The source data is health surveys from people from 2011-2015. Due to the size of the datasets and the scope of the surveys, it was necessary to filter the original datasets to focus on diabetes and reduce the sample size to 100000 for each year.

The source.ipynb and source_utils.py gather the original datasets and filters the information creating the sample_dataset.csv. It is not necessary to run source.ipynb.

AWS is used to store the original datasets. To run the panels in source.ipynb, the environment variables must be set up in .env. The AWS storage will be deleted after the project has been completed.

Step 1:

Clone the repository.

Step 2:

Run main.ipynb

_Note:_ Main notebook has two panels that are commented out. Neither panel needs to be ran to run the notebook. The output is part of the repo.

- To run panel for source, you must have a .env file with links to AWS resources. The output for source is available in datasets/sample_dataset.csv. Comment in the %run ... line.

- To run panel for sample, comment in the %run ... line. The output for sample is available in datasets/cleaned_dataset.

- Due to findings from the cleaned_dataset, all pipelines - modelings and plotting used the datasets/diabetes_binary_health_indicators_BRFSS2015

#### Methodology

Original approach: Combine and clean source data from CDC for years 2011-2015 and concatenate on shared features. After reviewing results, determination made that survey information was inconsistent across 5 years to achieve meaningful results.

_Note:_ modeling.ipynb file was used to review correlations and columns from the cleaned_dataset (all 5 years) and the 2015 dataset.

Modified approach: Use data sourced from the CDC for year 2015.

#### Resources

##### Datasets

Behavioral Risk Factor Surveillance System
Public health surveys of people from 2011-2015
https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system

Acknowledgements:
This dataset was released by the CDC (Centers for Disease Control and Prevention)

License:
[CCO: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

Diabetes Health Indicators Dataset
https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

Acknowledgements:
See the above Behavioral Risk Factor Surveillance System
Public health surveys of people from 2015

License:
[CCO: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
