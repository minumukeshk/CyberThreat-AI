# CyberThreat AI v2: SQL Findings Report

## 1. Dataset Overview
- Total records: 42,220
- BENIGN records: 20,000
- ATTACK records: 22,220
- Traffic categories: 15

## 2. Key SQL Findings

### 1. Attack Activity by Hour
- Highest activity: 10 AM
- Attack count: 7,903

### 2. Top Threat Sources
- Source IP: 172.16.0.1
- Attack records: 21,184
- Unique targets: 2

### 3. Destination Port Analysis
- Port 80: 14,184 attacks
- Port 22: 1,510 attacks
- Port 21: 1,505 attacks
- Port 80 accounts for 63.83% of malicious records.

### 4. Daily Attack Distribution
- Friday: 9,000
- Wednesday: 8,511
- Tuesday: 3,000
- Thursday: 1,709
- Monday: 0

### 5. Hourly Attack Changes
- 10 AM: 7,903 attacks
- 11 AM: 1,810 attacks
- 12 PM: 135 attacks

### 6. Port Risk Classification
Project-defined thresholds:
- High Risk: 1,000 or more attacks
- Medium Risk: 100–999 attacks
- Low Risk: Fewer than 100 attacks

## 3. SQL Concepts Implemented
- GROUP BY and HAVING
- Date functions
- RANK()
- LAG()
- CTE
- Subqueries
- CASE WHEN
- SQL Views

## 4. SQL Views Created
1. vw_daily_attack_summary
2. vw_top_threat_sources
3. vw_port_risk

## 5. Limitations
- Dataset contains laboratory-generated network traffic.
- The sample has a higher proportion of attacks than typical real-world traffic.
- Source IPs are not confirmed real-world attackers.
- Risk thresholds are project-defined.

## 6. Conclusion
SQL analysis identified patterns in attack frequency, source IP activity, destination ports and daily traffic distribution. These findings will support the CyberThreat AI dashboard and machine learning analysis.
