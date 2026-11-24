# EQUIFLOW – API CONTRACT

## 1. Project Overview

EQUIFLOW is an AI-powered fair resource distribution platform that helps distribute limited resources among disaster-affected villages based on actual needs, urgency and resource availability.

This document defines the common data formats that all three developers must follow to ensure smooth integration.

## 2. Shared Data Flow

The system follows this sequence:

1. Village information is collected.
2. AI Need Assessment analyzes the village's requirements.
3. Priority scores are generated.
4. Fair Resource Allocation receives village requirements, priority scores and available resources.
5. The allocation algorithm calculates resource distribution.
6. Final results are displayed on the dashboard.

## 3. Common JSON Data Structures

### A. Village Information – Input

**Purpose:** Contains basic information about each affected village.

**Used by:** All three modules.

```json
{
  "village_id": "V001",
  "village_name": "Village A",
  "population": 5000,
  "affected_population": 3500,
  "severity": 5,
  "medical_urgency": 4,
  "required_resources": {
    "food_packets": 3000,
    "water_liters": 5000,
    "medical_kits": 500
  }
}
```

### B. AI Need Assessment – Output

**Purpose:** Determines the urgency and priority of each village.

**Responsible module:** AI Need Assessment.

```json
{
  "village_id": "V001",
  "priority_score": 92,
  "priority_level": "Critical",
  "reason": "High affected population and urgent medical needs"
}
```

Priority levels:
- 80–100: Critical
- 60–79: High
- 40–59: Medium
- 0–39: Low

### C. Resource Availability – Input

**Purpose:** Specifies the total resources available for distribution.

**Responsible module:** Resource Management / Allocation.

```json
{
  "available_resources": {
    "food_packets": 5000,
    "water_liters": 8000,
    "medical_kits": 700
  }
}
```

### D. Fair Resource Allocation – Output

**Purpose:** Shows how many resources each village receives and how much demand remains unmet.

**Responsible module:** Fair Resource Allocation.

```json
{
  "village_id": "V001",
  "allocated_resources": {
    "food_packets": 2000,
    "water_liters": 3000,
    "medical_kits": 300
  },
  "unmet_resources": {
    "food_packets": 1000,
    "water_liters": 2000,
    "medical_kits": 200
  }
}
```

## 4. Module Responsibilities

### Module 1 – Frontend
- Collect village information.
- Display village requirements.
- Display available resources.
- Show priority scores.
- Display allocation results and analytics.

### Module 2 – AI Need Assessment
- Analyze affected population.
- Evaluate emergency severity.
- Assess medical urgency and resource shortages.
- Calculate priority scores.
- Generate explanations for priority decisions.

### Module 3 – Fair Resource Allocation
- Receive village requirements and priority scores.
- Consider available resources.
- Allocate resources based on needs and urgency.
- Prevent allocation beyond available stock.
- Calculate unmet demand.
- Compare equal distribution with need-based distribution.

## 5. Important Technical Rules

1. All modules must use the exact JSON field names defined above.
2. Each village must have a unique village_id.
3. Priority scores must be between 0 and 100.
4. Priority scores must be calculated using a transparent and consistent formula.
5. Final resource quantities must be calculated using deterministic optimization logic.
6. Total allocated resources must never exceed available resources.
7. Allocated quantities must never exceed the actual requirements.
8. Unmet demand = Required quantity − Allocated quantity.
9. All APIs must return valid JSON responses.
10. Invalid or missing input data must be handled properly.

## 6. Integration Sequence

Village Information → AI Need Assessment → Priority Scores → Fair Resource Allocation → Allocation Results → Dashboard.

## 7. Sample Test Scenario

Five villages are affected by floods.

Available resources:
- Food packets: 5,000
- Water: 8,000 litres
- Medical kits: 700

The system must:
- Assess the urgency of all five villages.
- Generate priority scores.
- Calculate resource allocations.
- Identify remaining shortages.
- Explain why resources were distributed in that manner.

**Expected outcome:** A transparent, need-based resource allocation recommendation that respects available stock and village requirements.

## 8. Integration Agreement

All developers must follow this API contract while implementing their individual modules.

Any changes to JSON field names, API request formats or response formats must be discussed and agreed upon by all team members before implementation.
