## Diabetes-Machine-Learning

#### Contributors

- Duran, Chris
- Kruel, Kimberly
- McClure, Mistie
- McDaniel, Geoff

#### Question

Can survey results predict whether a person has diabetes?

#### Synopsis

The CDC estimates that 20% of individuals living with diabetes are unaware of their condition. The objective is to determine the effectiveness of various modeling techniques in accurately predicting a binary diagnosis of diabetes, based on a 21-feature dataset representing key health indicators. These indicators include general physical health, financial circumstances, and educational background. A pipeline has been developed to fit (7) models to the data and utilize hyperparameter tuning for the top three performing models based on accuracy. Based upon the scoring of the models, the dataset is confirmed to be well structured, consisting of features with equivalent impact in determining whether a patient has diabetes or not. All models performed with a test accuracy of ~86%. The best performing tuned model was the XGBoost Tree Classifier, with a test set accuracy score of 86.7%. A low recall score of 0.16 communicates that some further hypertuning is necessary on the XGBoost Classifier in order to limit the potential of wrongly diagnosing a patient with diabetes that doesn't have diabetes. An important use of these models would be to deploy within doctor's offices as a way to navigate pertinent questions relating to those risk factors associated with a diabetes diagnosis. An application could also be deployed for common use, in which a user potentially concerned with a risk of diabetes can appropriately evaluate said risk.

#### Installs

A list of required libraries located here: (utils/package-list.txt)

#### Program Structure

    └───root
        └───datasets
            │   2015_formats.json
            |   cleaned_dataset.csv
            │   codebook15_llcp.pdf
            |   diabetes_012_health_indicators_BRFSS2015.csv
            |   diabetes_binary_5050split_health_indicators_BRFSS2015.csv
            |   diabetes_binary_health_indicators_BRFSS2015.csv
            └───sample_dataset.csv
        └───utils
            │   pipeline.py
            │   sample_cleaning_utils.py
            └───source_utils.py
        │   .env
        │   .gitignore
        │   main.ipynb
        |   modeling.ipynb
        |   pipeline.ipynb
        |   plotting.ipynb
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
