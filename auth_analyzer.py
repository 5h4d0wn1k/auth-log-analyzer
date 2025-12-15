"""
Auth log analyzer (lab/demo).
Detects:
- Rapid failures per IP
- Username spraying (many users from one IP)
- Success after multiple failures
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from typing import Dict, List

FAIL_RE = re.compile(r"Failed password for (invalid user )?(?P<user>\\S+) from (?P<ip>\\S+)")
OK_RE = re.compile(r"Accepted \\S+ for (?P<user>\\S+) from (?P<ip>\\S+)")


def parse_lines(lines: List[str]) -> Dict[str, object]:
    fails_per_ip: Counter[str] = Counter()
    fails_per_user_ip: Counter[tuple[str, str]] = Counter()
    user_success_ip: Dict[tuple[str, str], int] = {}
    spray_ips: Counter[str] = Counter()

    for line in lines:
        m_fail = FAIL_RE.search(line)
        if m_fail:
            ip = m_fail.group("ip")
            user = m_fail.group("user")
            fails_per_ip[ip] += 1
            fails_per_user_ip[(user, ip)] += 1
            continue
        m_ok = OK_RE.search(line)
        if m_ok:
            ip = m_ok.group("ip")
            user = m_ok.group("user")
            user_success_ip[(user, ip)] = user_success_ip.get((user, ip), 0) + 1

    for (user, ip), count in fails_per_user_ip.items():
        if count >= 3:
            spray_ips[ip] += 1

    findings = {
        "top_fail_ips": fails_per_ip.most_common(10),
        "spray_ips": spray_ips.most_common(10),
        "success_after_fail": [
            {"user": user, "ip": ip, "fails": fails_per_user_ip.get((user, ip), 0), "success": succ}
            for (user, ip), succ in user_success_ip.items()
            if fails_per_user_ip.get((user, ip), 0) > 0
        ],
    }
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Auth log analyzer (lab/demo).")
    parser.add_argument("--log", required=True, help="auth.log path.")
    parser.add_argument("--json-out", help="Write JSON report.")
    args = parser.parse_args()

    with open(args.log, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    report = parse_lines(lines)
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
