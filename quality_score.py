from config import (
    EXCELLENT_THRESHOLD,
    GOOD_THRESHOLD,
    WARNING_THRESHOLD
)


def calculate_quality_score(validation_results):
    """
    Calculate the overall data quality score.

    Parameters:
        validation_results (dict)
        Output returned by run_all_checks()

    Returns:
        float
        Quality score between 0 and 100
    """
    pass


def get_quality_status(score):
    """
    Convert score into quality category.

    Parameters:
        score (float)

    Returns:
        str

    Categories:
        Excellent
        Good
        Warning
        Critical
    """
    pass