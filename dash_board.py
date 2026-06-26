import streamlit as st
import pandas as pd

from validator import run_all_checks
from quality_score import calculate_quality_score, get_quality_status
from database import get_scan_history, save_scan_result

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Data Quality Monitoring",
    layout="wide"
)

st.title("📊 Automated Data Quality Monitoring System")

# ----------------------------
# Upload Dataset
# ----------------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df_uploaded = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(
        df_uploaded.head(),
        use_container_width=True
    )

    if st.button("Analyze Dataset"):

        # Run Validation
        results = run_all_checks(df_uploaded)
        st.write(results)

        # Calculate Quality Score
        score = calculate_quality_score(results, df_uploaded)

        status = get_quality_status(score)

        # Save into Database
        save_scan_result(
            score,
            status,
            results
        )

        st.success("Dataset analyzed successfully!")

        st.subheader("Analysis Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Quality Score",
                score
            )

        with col2:

            if status == "Excellent":
                st.success(status)

            elif status == "Good":
                st.info(status)

            elif status == "Warning":
                st.warning(status)

            else:
                st.error(status)

        st.subheader("Validation Summary")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Missing Values",
                results["missing_values"]["issue_count"]
            )

        with c2:
            st.metric(
                "Duplicates",
                results["duplicates"]["issue_count"]
            )

        with c3:
            st.metric(
                "Outliers",
                results["outliers"]["issue_count"]
            )

        with c4:
            st.metric(
                "Schema Issues",
                results["schema"]["issue_count"]
            )

        st.subheader("Detailed Validation Output")

        st.json(results)

# ----------------------------
# Historical Dashboard
# ----------------------------

history = get_scan_history()

if len(history) > 0:

    latest_scan = history.iloc[0]

    st.divider()

    st.header("📈 Historical Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Latest Quality Score",
            latest_scan["quality_score"]
        )

    with col2:

        status = latest_scan["quality_status"]

        if status == "Excellent":
            st.success(status)

        elif status == "Good":
            st.info(status)

        elif status == "Warning":
            st.warning(status)

        else:
            st.error(status)

    with col3:
        st.metric(
            "Total Scans",
            len(history)
        )

    st.subheader("Latest Validation Counts")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Missing",
            latest_scan["missing_count"]
        )

    with c2:
        st.metric(
            "Duplicates",
            latest_scan["duplicate_count"]
        )

    with c3:
        st.metric(
            "Outliers",
            latest_scan["outlier_count"]
        )

    with c4:
        st.metric(
            "Schema",
            latest_scan["schema_issue_count"]
        )

    st.subheader("Quality Score Trend")

    trend_df = history[
        ["scan_time", "quality_score"]
    ]

    st.line_chart(
        trend_df.set_index("scan_time")
    )

    st.subheader("Historical Scan Records")

    st.dataframe(
        history,
        use_container_width=True
    )

else:

    st.info("No historical scans found.")