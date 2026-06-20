from config import (
    EXCELLENT_THRESHOLD,
    GOOD_THRESHOLD,
    WARNING_THRESHOLD
)


def calculate_quality_score(validation_results, df):
    
    total_rows = len(df)

    total_cells = df.shape[0] * df.shape[1]

    missing_count = validation_results[
        "missing_values"
    ]["issue_count"]

    duplicate_count = validation_results[
        "duplicates"
    ]["issue_count"]

    outlier_count = validation_results[
        "outliers"
    ]["issue_count"]

    missing_rate = (
        missing_count / total_cells
    ) * 100

    duplicate_rate = (
        duplicate_count / total_rows
    ) * 100

    outlier_rate = (
        outlier_count / total_rows
    ) * 100

    score = (
        100
        - missing_rate
        - duplicate_rate
        - outlier_rate
    )

    if score < 0:
        score = 0

    return round(score, 2)

    pass


def get_quality_status(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"

    elif score >= GOOD_THRESHOLD:
        return "Good"

    elif score >= WARNING_THRESHOLD:
        return "Warning"

    else:
        return "Critical"
    pass



