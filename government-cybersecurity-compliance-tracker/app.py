import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

BASE = Path(__file__).parent
DATA = BASE / "data"

st.set_page_config(
    page_title="Government Cybersecurity Compliance Tracker",
    page_icon="🔐",
    layout="wide",
)

def load_json(filename):
    with open(DATA / filename, "r", encoding="utf-8") as f:
        return json.load(f)

departments = pd.DataFrame(load_json("departments.json"))
controls = pd.DataFrame(load_json("controls.json"))
risks = pd.DataFrame(load_json("risks.json"))
incidents = pd.DataFrame(load_json("incidents.json"))
programs = pd.DataFrame(load_json("programs.json"))
budget = pd.DataFrame(load_json("budget.json"))

risks["risk_score"] = risks["likelihood"] * risks["impact"]
budget["remaining"] = budget["allocated"] - budget["spent"]
budget["utilization_pct"] = (budget["spent"] / budget["allocated"] * 100).round(1)

st.title("🔐 Government Cybersecurity & Data Protection Compliance Tracker")
st.caption("Academic prototype for a Cybersecurity & Data Protection Internship")

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Select module",
        [
            "Dashboard",
            "Government Structure",
            "Security Controls",
            "Risk Register",
            "Incident Management",
            "Government Programs",
            "Security Budget",
        ],
    )
    st.divider()
    st.info(
        "Educational prototype only. No real government or citizen data should be entered."
    )

if page == "Dashboard":
    st.subheader("Security Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Departments", len(departments))
    c2.metric("Security Controls", len(controls))
    c3.metric("Open Risks", int((risks["status"] != "Controlled").sum()))
    c4.metric("Incidents", len(incidents))

    left, right = st.columns(2)

    with left:
        status_counts = controls["status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        fig = px.pie(status_counts, names="Status", values="Count", title="Control Status")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        severity = incidents["severity"].value_counts().reset_index()
        severity.columns = ["Severity", "Count"]
        fig = px.bar(severity, x="Severity", y="Count", title="Incident Severity")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Highest Demonstration Risks")
    st.dataframe(
        risks.sort_values("risk_score", ascending=False)[
            ["id", "asset", "threat", "likelihood", "impact", "risk_score", "status"]
        ],
        use_container_width=True,
        hide_index=True,
    )

elif page == "Government Structure":
    st.subheader("Government Organizational Structure")
    st.markdown(
        """
        **Ministry / Department → Divisions / Units → Officers → Operational Staff**

        The prototype uses departments and responsibilities to demonstrate accountability
        and ownership of cybersecurity activities.
        """
    )
    st.dataframe(departments, use_container_width=True, hide_index=True)

    st.subheader("Cybersecurity Responsibility Flow")
    st.code(
        """Department
    ↓
Division / Unit
    ↓
Responsible Officer
    ↓
Security Control / Process
    ↓
Monitoring and Review""",
        language="text",
    )

elif page == "Security Controls":
    st.subheader("Security & Compliance Control Register")

    col1, col2 = st.columns(2)
    with col1:
        status_filter = st.multiselect(
            "Filter by status",
            sorted(controls["status"].unique()),
            default=list(sorted(controls["status"].unique())),
        )
    with col2:
        category_filter = st.multiselect(
            "Filter by category",
            sorted(controls["category"].unique()),
            default=list(sorted(controls["category"].unique())),
        )

    filtered = controls[
        controls["status"].isin(status_filter)
        & controls["category"].isin(category_filter)
    ]
    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.subheader("Control Categories")
    cat = controls["category"].value_counts().reset_index()
    cat.columns = ["Category", "Controls"]
    fig = px.bar(cat, x="Category", y="Controls", title="Controls by Category")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Risk Register":
    st.subheader("Cybersecurity Risk Register")

    st.caption("Demonstration formula: Risk Score = Likelihood × Impact")

    selected = st.slider("Minimum risk score", 1, 25, 1)
    filtered = risks[risks["risk_score"] >= selected].sort_values(
        "risk_score", ascending=False
    )

    st.dataframe(
        filtered[
            [
                "id",
                "asset",
                "threat",
                "likelihood",
                "impact",
                "risk_score",
                "owner",
                "status",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

    fig = px.scatter(
        risks,
        x="likelihood",
        y="impact",
        size="risk_score",
        hover_name="asset",
        text="id",
        title="Likelihood vs Impact",
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "Incident Management":
    st.subheader("Cybersecurity Incident Register")
    st.dataframe(incidents, use_container_width=True, hide_index=True)

    st.subheader("Incident Response Workflow")
    st.code(
        """Detection → Assessment → Classification → Containment
→ Investigation → Recovery → Documentation → Lessons Learned""",
        language="text",
    )

elif page == "Government Programs":
    st.subheader("Government Programs & Security Requirements")
    st.dataframe(programs, use_container_width=True, hide_index=True)

    st.info(
        "Digital government programs should consider security and privacy requirements "
        "during planning, procurement, implementation and monitoring."
    )

elif page == "Security Budget":
    st.subheader("Cybersecurity Budget & Financial Management")

    total_allocated = budget["allocated"].sum()
    total_spent = budget["spent"].sum()
    total_remaining = budget["remaining"].sum()
    utilization = total_spent / total_allocated * 100

    c1, c2, c3 = st.columns(3)
    c1.metric("Allocated", f"₹{total_allocated:,.0f}")
    c2.metric("Spent", f"₹{total_spent:,.0f}")
    c3.metric("Utilization", f"{utilization:.1f}%")

    st.dataframe(budget, use_container_width=True, hide_index=True)

    fig = px.bar(
        budget,
        x="category",
        y=["allocated", "spent"],
        barmode="group",
        title="Allocated vs Spent",
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("Cybersecurity & Data Protection Internship • Government Systems & Procedures • Educational Prototype")
