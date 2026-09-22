> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# Auth Log Analyzer

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/auth-log-analyzer)](https://github.com/5h4d0wn1k/auth-log-analyzer)
[![issues](https://img.shields.io/github/issues/5h4d0wn1k/auth-log-analyzer)](https://github.com/5h4d0wn1k/auth-log-analyzer)

Authentication log analyzer for security monitoring and intrusion detection, in
Python with zero dependencies: detects brute force attempts, credential
spraying, and successful logins after repeated failures from standard Linux
auth logs, and emits machine-readable JSON reports.

## Why

Every SSH or web login endpoint produces `auth.log` data that hides attack
signals in noise. This tool turns those logs into ranked, actionable findings
with nothing but the Python standard library: which IPs are hammering failed
passwords (brute force), which IPs are rotating many usernames (credential
spraying), and which accounts succeeded after a string of failures (a probable
compromise). It is ideal for blue-team monitoring, incident response triage,
and education on how authentication attacks look in real log lines.

## Features

- **Brute force detection** — ranks the top IPs by `Failed password` count
  (`top_fail_ips`).
- **Credential spraying detection** — flags IPs that reuse passwords across 3+
  distinct usernames (`spray_ips`).
- **Success-after-failure** — reports user/IP pairs that logged in successfully
  only after prior failed attempts, a classic account-compromise signal.
- **Regex-based parsing** — handles standard `Failed password for` /
  `Accepted ... for` auth.log line patterns with support for `invalid user`.
- **JSON output** — `--json-out` writes a structured report for ingestion into
  dashboards, SIEMs, or downstream automation.
- **Zero dependencies** — Python 3.8+ standard library only; nothing to install.

## Quickstart

### Prerequisites

- Python 3.8+ (no external packages).

### Analyze a log

```bash
python auth_analyzer.py --log /var/log/auth.log
```

### Save a JSON report

```bash
python auth_analyzer.py --log /var/log/auth.log --json-out auth_analysis.json
```

## Examples

Sample log lines the parser understands:

```
Failed password for invalid user admin from 192.168.1.100
Accepted publickey for user from 192.168.1.50
Failed password for root from 10.0.0.1
```

Example report:

```json
{
  "top_fail_ips": [["192.168.1.100", 150]],
  "spray_ips": [["192.168.1.100", 5]],
  "success_after_fail": [
    {"user": "admin", "ip": "192.168.1.100", "fails": 45, "success": 1}
  ]
}
```

## Documentation

- [ETHICS.md](ETHICS.md) — ethical use pledge
- [SCOPE.md](SCOPE.md) — authorized testing scope
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution guidelines
- [CHANGELOG.md](CHANGELOG.md) — version history

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep the tool standard-library-only and
add regression tests for any new log-line pattern.

## License

MIT — see [LICENSE](LICENSE).

**Remember**: only analyze logs you own or have explicit authorization to
analyze.