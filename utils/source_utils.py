from typing import List
import pandas as pd

date_columns = ["IYEAR", "IDAY", "IMONTH", "IDATE", "FMONTH"]
columns_to_drop = [
    "DISPCODE",
    "SEQNO",
    "_PSU",
    "CTELENUM",
    "WEIGHT2",
    "HEIGHT3",
    "RENTHOM1",
    "VETERAN3",
    "CHILDREN",
    "SEATBELT",
    "_CHLDCNT",
    "_RFSEAT2",
    "_RFSEAT3",
    "QSTLANG",
    "QSTVER",
    "USEEQUIP",
    "PERSDOC2",
    "MEDCOST",
    "WTKG3",
    "HTM4",
    "HTIN4",
    "_WT2RAKE",
    "_RAWRAKE",
    "CHECKUP1",
    "_AGE65YR",
    "_AGEG5YR",
    "_BMI5",
    "INCOME2",
    "EDUCA",
    "_LLCPWT",
    "_HCVU651",
    "_STRWT",
    "_LLCPWT",
    "HIVTST6",
    "_RFBMI5",
    "_AIDTST3",
    "SMOKE100",
    "_RFSMOK3",
    "_RFBING5",
]


def get_sample_dataframe(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """90
    Function called to get a sample dataframe from a list of dataframes.
    Args:
        List[dataframes]: A list of pandas dataframes.
    Returns:
        Sample dataframe.
    """

    # Combine all dataframes
    combined_df = pd.concat(dfs, join="inner", ignore_index=True)

    # Drop columns
    combined_df.drop(columns=columns_to_drop, inplace=True)

    # Get columns with high null values
    null_counts = combined_df.isnull().sum()
    null_percentages = null_counts / len(combined_df) * 100
    columns_high_nulls = null_percentages[null_percentages > 20].index.tolist()

    # Filter out columns with high null values
    filtered_df = combined_df.drop(columns=columns_high_nulls)

    # Get sample size
    sample_size = 100000

    # Get counts by year
    counts_by_year = filtered_df["IYEAR"].value_counts()

    # Filter out years with less than sample size
    filtered_years = counts_by_year[counts_by_year >= sample_size]

    # Get sample dataframe with filtered years and sample size
    sample_df = (
        filtered_df[filtered_df["IYEAR"].isin(filtered_years.index)]
        .groupby("IYEAR", group_keys=False)
        .apply(lambda x: x.sample(sample_size))
        .reset_index(drop=True)
    )

    # Create month column
    sample_df["calculated_month"] = sample_df["IMONTH"].apply(convert_date_fields)

    # Create year column
    sample_df["calculated_year"] = sample_df["IYEAR"].apply(convert_date_fields)

    # Drop date columns
    sample_df.drop(columns=date_columns, inplace=True)

    # Return sample dataframe
    return sample_df


def convert_date_fields(string_value) -> int:
    """
    Function called to convert a string date value with byte notation to an integer.
    Args:
        String: A string with byte notation.
    Returns:
        Integer.
    """

    return int(string_value.replace("b'", "").replace("'", "").strip())
