## Check missing values
def check_missing_values(df):
    """
    Returns:
    {
        "status": "PASS/FAIL",
        "issue_count": int,
        "details": dict
    }
    """
    missing_values = df.isnull().sum() # Counts null values column by column
    missing_dict = missing_values[missing_values>0].to_dict() ## Converts to dict, only columns with missing values remains
    total_missing = sum(missing_dict.values()) # Counts total missing values

# Determining the status to execute
    status = "PASS"
    if total_missing>0:
        status = "FAIL"

# Returning outputs
    return{
        "status": status,
        "issue_count": total_missing,
        "details": missing_dict
    }
    pass


## Check duplicate values
def check_duplicates(df):
    """
    Returns:
    {
        "status": "PASS/FAIL",
        "issue_count": int,
        "details": dict
    }
    """

    duplicate_count = df.duplicated().sum()

    status = "PASS"

    if duplicate_count>0:
        status = "FAIL"

        return {
        "status": status,
        "issue_count": int(duplicate_count),
        "details": {
            "duplicate_rows": int(duplicate_count)
            }
        }
    pass



## Check Outliers
def check_outliers(df):
    """
    Returns:
    {
        "status": "PASS/FAIL",
        "issue_count": int,
        "details": dict
    }
    """

    outlier_details = {}
    total_outliers = 0
    numeric_columns = [
        col
        for col in df.select_dtypes(include = "number").columns
        if not col.endswith("_id")
    ]

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 - (1.5 * iqr)

        outliers = df[
            (df[column] < lower_bound)
            | (df[column] > upper_bound)
        ]

        count = len(outliers)

        if count > 0:
            outlier_details[column] = count
            total_outliers += count
    
    status = "PASS"

    if total_outliers > 0:
        status = "FAIL"

    return{
        "status" : status,
        "issue_count" : total_outliers,
        "details" : outlier_details
    }


    pass



## Checks Schema 
def check_schema(df):
    """
    Returns:
    {
        "status": "PASS/FAIL",
        "issue_count": int,
        "details": dict
    }
    """
    pass



## Runs all validation check
def run_all_checks(df):
    """
    Returns:
    {
        "status": "PASS/FAIL",
        "issue_count": int,
        "details": dict
    }
    """
    results = {
        "Missing Values" : check_missing_values(df),
        "Duplicates" : check_duplicates(df), 
        "Outliers" : check_outliers(df)
    }
    return results
    pass