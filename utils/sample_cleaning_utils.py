import pandas as pd

columns_to_drop = [
    "_STSTR",
    "ASTHMA3",
    "_LTASTH1",
    "_CASTHM1",
    "HAVARTH3",
    "DRNKANY5",
    "DROCDY3_",
]
columns_to_excl_bad_value_conversion = [
    "calculated_month",
    "calculated_year",
    "_STATE",
    "PHYSHLTH",
    "MENTHLTH",
]
bad_data_values = [".D", ".R", 7, 9, ".", 99, 77, 900]
columns_with_number_of_days = ["PHYSHLTH", "MENTHLTH"]
column_alcohol = "ALCDAY5"
columns_calendar = ["calculated_month", "calculated_year"]


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function called to clean a dataframe.
    Args:
        List[dataframes]: A pandas dataframes.
    Returns:
        Cleaned dataframe.
    """

    # Copy dataframe
    cleaned_df = df.copy()

    # Drop columns
    cleaned_df.drop(columns=columns_to_drop, inplace=True)

    # Replace null values with -1 in all columns
    cleaned_df = cleaned_df.fillna(-1)

    # Convert bad data values
    all_columns = cleaned_df.columns.tolist()

    filtered_columns = [
        column
        for column in all_columns
        if column not in columns_to_excl_bad_value_conversion
    ]

    for column in filtered_columns:
        cleaned_df[column] = cleaned_df[column].replace(bad_data_values, -1)

    # Transform columns with number of days
    for column in columns_with_number_of_days:
        cleaned_df[column + "_30_day_range"] = cleaned_df[column].apply(
            map_to_day_range
        )
        cleaned_df.drop(columns=column, inplace=True)

    # Transform columns with alcohol
    cleaned_df[column_alcohol + "_last_30_days"] = cleaned_df[column_alcohol].apply(
        transform_column_alcohol
    )
    cleaned_df.drop(columns=column_alcohol, inplace=True)

    # Create datatime column with last day of the month
    cleaned_df["month_year_datetime"] = pd.to_datetime(
        df["calculated_year"].astype(str) + "-" + df["calculated_month"].astype(str),
        format="%Y-%m",
    ) + pd.offsets.MonthEnd(0)
    cleaned_df.drop(columns=columns_calendar, inplace=True)

    # Return Cleaned Dataframe
    return cleaned_df


def map_to_day_range(value):
    """
    Function called to tranform a value from day to range.
    Args:
        Float.
    Returns:
        Float
    """
    if value > 0 and value <= 10:
        return 1
    elif value > 10 and value <= 20:
        return 2
    elif value > 20 and value <= 30:
        return 3
    elif value == 77 or value == 99:
        return -1
    else:
        return value


def transform_column_alcohol(value):
    """
    Function called to consolidate values.
    Args:
        Float
    Returns:
        Float
    """
    if value in [777, 999]:
        return -1
    elif value == 888:
        return 2
    elif value > 100 and value < 300:
        return 1
    else:
        return value
