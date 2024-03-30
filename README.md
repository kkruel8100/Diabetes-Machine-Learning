## Diabetes-Machine-Learning

To Do

1. Add additional libraries
2. Verify structure
3. Add steps

#### Programs/Libraries

Python, Pandas

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

If you are recreating source step, then you must have .env file with AWS links.
If not skip to Step 3.

Step 2:

Run source.ipynb
Result: datasets/sample_dataset.csv created

If you are recreating clean data set, then continue to Step 3.
If not skip to Step 4.

Step 3:

Run sample.ipynb
Result: datasets/cleaned_data.csv created

Step 4:

Run modeling.ipynb

#### Resources

##### Datasets

Behavioral Risk Factor Surveillance System
Public health surveys of people from 2011-2015
https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system

Acknowledgements:
This dataset was released by the CDC (Centers for Disease Control and Prevention)

License:
[CCO: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
