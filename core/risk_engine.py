SEVERITY_WEIGHTS = {
    "CRITICAL": 30,
    "HIGH": 20,
    "MEDIUM": 10,
    "LOW": 5
}

def calculate_risk(findings):
    score = 100
    summary = {k: 0 for k in SEVERITY_WEIGHTS}

    for f in findings:
        sev = f["severity"]
        summary[sev] += 1
        score -= SEVERITY_WEIGHTS[sev]

    score = max(score, 0)
    level = "LOW" if score >= 85 else "MEDIUM" if score >= 60 else "HIGH"

    return score, level, summary
