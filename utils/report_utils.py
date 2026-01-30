import os
import json
from datetime import datetime

def generate_report(findings, score, level, summary, fmt="txt"):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add more professional details
    report_data = {
        "audit_date": timestamp,
        "security_score": score,
        "risk_level": level,
        "summary": summary,
        "total_findings": len(findings),
        "findings": findings,
        "recommendations": generate_recommendations(summary, score)
    }

    if fmt == "json":
        with open("reports/report.json", "w") as f:
            json.dump(report_data, f, indent=4)

    elif fmt == "html":
        with open("reports/report.html", "w") as f:
            f.write(f"<h1>HARDEN-SEC Security Audit Report</h1>")
            f.write(f"<p>Date: {timestamp}</p>")
            f.write(f"<p>Score: {score}/100</p>")
            f.write(f"<p>Risk Level: {level}</p>")
            f.write("<h2>Summary of Findings</h2><ul>")
            for sev, count in summary.items():
                f.write(f"<li>{sev}: {count}</li>")
            f.write("</ul><h2>Details</h2><ul>")
            for fnd in findings:
                f.write(f"<li>[{fnd['severity']}] {fnd['message']}</li>")
            f.write("</ul><h2>Recommendations</h2><ul>")
            for rec in report_data["recommendations"]:
                f.write(f"<li>{rec}</li>")
            f.write("</ul>")

    else:  # txt
        with open("reports/report.txt", "w") as f:
            f.write("HARDEN-SEC Security Audit Report\n")
            f.write("="*50 + "\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"Score: {score}/100\n")
            f.write(f"Risk Level: {level}\n")
            f.write(f"Summary: {summary}\n")
            f.write(f"Total Findings: {len(findings)}\n\n")
            f.write("Findings:\n")
            for fnd in findings:
                f.write(f"[{fnd['severity']}] {fnd['message']}\n")
            f.write("\nRecommendations:\n")
            for rec in report_data["recommendations"]:
                f.write(f"- {rec}\n")


def generate_recommendations(summary, score):
    recs = []
    if summary["CRITICAL"] > 0:
        recs.append("Immediately address CRITICAL findings.")
    if summary["HIGH"] > 0:
        recs.append("Harden exposed services and high-risk configurations.")
    if summary["MEDIUM"] > 0:
        recs.append("Review medium-risk items.")
    if score < 60:
        recs.append("Review overall server security policy.")
    return recs
