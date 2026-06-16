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
    pass