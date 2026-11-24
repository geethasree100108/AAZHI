
def assess_village(village):

    # 1. Calculate affected population percentage
    affected_percentage = (
        village.affected_population / village.population
    ) * 100

    affected_score = affected_percentage

    # 2. Convert severity from 1-5 into 0-100
    severity_score = (village.severity / 5) * 100

    # 3. Convert medical urgency from 1-5 into 0-100
    medical_score = (village.medical_urgency / 5) * 100

    # 4. Calculate absolute affected population score
    population_score = min(
        (village.affected_population / 5000) * 100,
        100
    )

    # 5. Calculate weighted priority score
    priority_score = (
        affected_score * 0.35 +
        severity_score * 0.30 +
        medical_score * 0.25 +
        population_score * 0.10
    )

    priority_score = round(priority_score, 2)

    # 6. Assign priority level
    if priority_score >= 80:
        priority_level = "Critical"
    elif priority_score >= 60:
        priority_level = "High"
    elif priority_score >= 40:
        priority_level = "Medium"
    else:
        priority_level = "Low"

    # 7. Generate assessment explanation
    reason = (
        f"{village.village_name} has "
        f"{affected_percentage:.1f}% affected population, "
        f"severity level {village.severity}/5 and "
        f"medical urgency {village.medical_urgency}/5."
    )

    # 8. Return assessment result
    return {
        "village_id": village.village_id,
        "priority_score": priority_score,
        "priority_level": priority_level,
        "reason": reason
    }


def assess_multiple_villages(villages):

    results = []

    for village in villages:
        result = assess_village(village)
        results.append(result)

    return results
