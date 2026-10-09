# Government Cybersecurity & Data Protection Compliance Tracker

A Python-based academic project developed as part of a **Cybersecurity & Data Protection Internship**.

The project models how a government department can track administrative procedures, cybersecurity controls, data protection requirements, risks, incidents, and inter-departmental responsibilities from a single dashboard.

## Objectives Covered

This project maps directly to the internship topic **Government Systems & Procedures**:

1. **Government organizational structure and hierarchy**
   - Department, division, role and responsibility management.

2. **Administrative procedures and protocols**
   - Procedure tracking, approval status and responsible officers.

3. **Government acts, rules and regulations**
   - Compliance register for laws, policies and security requirements.

4. **Budgeting and financial management**
   - Security budget allocation and expenditure tracking.

5. **Government schemes and programs**
   - Program registry with security/privacy requirements.

6. **Inter-departmental coordination and communication**
   - Department contacts, incident ownership and escalation tracking.

## Cybersecurity Features

- Role-based access concepts
- Data classification
- Security control tracking
- Compliance status monitoring
- Risk register
- Incident register
- Security budget monitoring
- Inter-department coordination
- Dashboard metrics
- JSON-based local data storage
- Exportable report data

## Tech Stack

- Python 3.10+
- Streamlit
- Pandas
- JSON
- Plotly

## Project Structure

```text
government-cybersecurity-compliance-tracker/
│
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
│
├── data/
│   ├── departments.json
│   ├── controls.json
│   ├── risks.json
│   ├── incidents.json
│   ├── programs.json
│   └── budget.json
│
├── docs/
    ├── PROJECT_REPORT.md
    ├── SECURITY_MODEL.md
    └── GOVERNMENT_PROCEDURES.md

```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aryanoff2112-art/government-cybersecurity-compliance-tracker.git
cd government-cybersecurity-compliance-tracker
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in the browser.

## Important Note

This is an **educational prototype**. It does not connect to real government databases, does not process real citizen information, and should not be treated as an official government compliance system.

The laws, rules and controls shown in the prototype are simplified for academic demonstration. Actual government departments must follow the current laws, rules, notifications, security directions and departmental policies applicable to them.

## Suggested GitHub Topics

```text
cybersecurity
data-protection
government-systems
information-security
compliance
risk-management
python
streamlit
privacy
cybersecurity-internship
```
