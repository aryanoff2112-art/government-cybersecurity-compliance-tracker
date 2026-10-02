# Project Report

## 1. Introduction

Government departments increasingly depend on digital systems for administration and public services. These systems process official records, personal information, financial information and operational data.

This project demonstrates a simplified dashboard for managing cybersecurity, data protection, compliance and administrative information within a hypothetical government environment.

## 2. Problem Statement

Government organizations need visibility into security controls, risks, incidents, budgets and responsibilities. When information is spread across separate spreadsheets or documents, it can become difficult to identify ownership, pending controls and high-priority risks.

The proposed application provides a single educational dashboard for this information.

## 3. Objectives

- Model a government organizational hierarchy.
- Track administrative and cybersecurity responsibilities.
- Maintain a simplified compliance register.
- Track security risks and incidents.
- Monitor cybersecurity-related budget utilization.
- Record government programs and their security requirements.
- Demonstrate inter-departmental coordination.

## 4. Methodology

The project uses JSON files as a lightweight data layer. Streamlit provides the user interface, while Pandas processes tabular data and Plotly provides visualizations.

The dashboard calculates risk scores using:

`Risk Score = Likelihood × Impact`

Scores are used to prioritize demonstration data; they are not an official government risk rating.

## 5. Security Model

The application demonstrates the following concepts:

- Least privilege
- Role-based access
- Data classification
- Auditability
- Incident management
- Risk-based prioritization
- Backup and recovery
- Security awareness
- Third-party risk management

## 6. Expected Outcome

The project demonstrates how administrative and cybersecurity information can be organized into one management view. It is intended for academic learning and portfolio demonstration.
