import argparse
import os
from core.system_audit import run_system_audit
from core.service_audit import run_service_audit
from core.config_audit import run_config_audit
from core.risk_engine import calculate_risk
from utils.report_utils import generate_report

def main():
    parser = argparse.ArgumentParser(
        description="HARDEN-SEC - Linux Security Hardening Audit"
    )
    parser.add_argument("--format", choices=["txt", "json", "html"], default="txt")
    parser.add_argument("--mode", choices=["REAL", "DRY"], default="REAL")
    args = parser.parse_args()

    print(f"[+] Starting security audit in {args.mode} mode\n")

    if os.geteuid() != 0:
        print("[!] Warning: Running without root may cause incomplete results\n")

    findings = []

    print("[*] Analyzing system permissions and users...")
    sys_findings = run_system_audit()
    findings += sys_findings
    print(f"[*] System audit completed ({len(sys_findings)} findings)\n")

    print("[*] Analyzing active services...")
    svc_findings = run_service_audit()
    findings += svc_findings
    print(f"[*] Services audit completed ({len(svc_findings)} findings)\n")

    print("[*] Analyzing critical configurations...")
    cfg_findings = run_config_audit()
    findings += cfg_findings
    print(f"[*] Configuration audit completed ({len(cfg_findings)} findings)\n")

    score, level, summary = calculate_risk(findings)
    generate_report(findings, score, level, summary, args.format)

    print("[+] Audit finished")
    print(f"[+] Security score: {score}/100")
    print(f"[+] Risk level: {level}")
    print(f"[+] Summary: {summary}")


if __name__ == "__main__":
    main()
