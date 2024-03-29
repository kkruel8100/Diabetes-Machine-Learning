## Diabetes-Machine-Learning

#### Program Structure

    └───root
        └───datasets
            │   2015_formats.json
            │   codebook15_llcp.pdf
            └───sample_dataset.csv
        └───utils
            │   pipeline.py
            └───source_utils.py
        │   .env
        │   .gitignore
        │   main.ipynb
        │   README.md
        └───source.ipynb

#### Program Details

_Source_

The source data is health surveys from people from 2011-2015. Due to the size of the datasets and the scope of the surveys, it was necessary to filter the original datasets to focus on diabetes and reduce the sample size to 100000 for each year.

The source.ipynb and source_utils.py gather the original datasets and filters the information creating the sample_dataset.csv. It is not necessary to run source.ipynb.

AWS is used to store the original datasets. To run the panels in source.ipynb, the environment variables must be set up in .env. The AWS storage will be deleted after the project has been completed.

Step 1:

Clone the repository.

Step 2:

#### Resources

##### Datasets

Behavioral Risk Factor Surveillance System
Public health surveys of people from 2011-2015
https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system

Acknowledgements:
This dataset was released by the CDC (Centers for Disease Control and Prevention)

License:
[CCO: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
