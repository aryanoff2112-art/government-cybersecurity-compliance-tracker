# Security Model

## CIA Triad

### Confidentiality
Only authorized users should access sensitive information.

Examples:
- Role-based access
- Multi-factor authentication
- Encryption
- Data classification

### Integrity
Information should remain accurate and protected from unauthorized modification.

Examples:
- Audit logs
- Approval workflows
- Change management
- Integrity monitoring

### Availability
Authorized users should be able to access services when required.

Examples:
- Backups
- Disaster recovery
- Redundancy
- Incident response

## Privacy

Data protection should consider:
- Purpose of collection
- Data minimization
- Access control
- Retention
- Secure disposal
- Accountability

## Risk Management

The prototype uses:

`Risk Score = Likelihood × Impact`

Likelihood and impact are represented on a 1–5 scale in the sample data.

## Important Limitation

This project does not implement real authentication, encryption, production audit logging or real government integrations. It is a learning prototype and must not be deployed with real citizen or government data without a complete security assessment and appropriate controls.
