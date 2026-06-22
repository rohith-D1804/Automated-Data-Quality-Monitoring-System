import streamlit as st
from database import get_scan_history

st.set_page_config(
    page_title="Data Quality Monitoring",
    layout="wide"
)

st.title("📊 Automated Data Quality Monitoring System")

df = get_scan_history()

if len(df) > 0:

    latest_scan = df.iloc[0]

    st.subheader("Latest Scan Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Quality Score",
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

    st.subheader("Validation Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Missing Values",
            latest_scan["missing_count"]
        )

    with col2:
        st.metric(
            "Duplicates",
            latest_scan["duplicate_count"]
        )

    with col3:
        st.metric(
            "Outliers",
            latest_scan["outlier_count"]
        )

    with col4:
        st.metric(
            "Schema Issues",
            latest_scan["schema_issue_count"]
        )

    st.subheader("Quality Score Trend")

    trend_df = df[
        ["scan_time", "quality_score"]
    ]

    st.line_chart(
        trend_df.set_index("scan_time")
    )

    st.subheader("Scan History")

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning(
        "No scan records found."
    )