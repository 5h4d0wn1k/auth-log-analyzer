# Authentication Log Analyzer

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security analysis and educational purposes. Only use on log files you own or have explicit written authorization to analyze.

## Overview

A powerful authentication log analyzer that detects suspicious authentication patterns including brute force attacks, credential spraying, and successful logins after multiple failures. Designed for security monitoring and threat detection.

## Features

- **Brute Force Detection**: Identifies rapid failed login attempts per IP
- **Credential Spraying Detection**: Detects username enumeration attacks
- **Success After Failure**: Identifies successful logins after multiple failures
- **Top Attackers**: Lists top IPs with failed attempts
- **JSON Output**: Machine-readable results for automation

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/auth-log-analyzer.git
cd auth-log-analyzer

# No installation needed!
python auth_analyzer.py --help
```

## Usage

### Basic Usage

```bash
# Analyze authentication log
python auth_analyzer.py --log /var/log/auth.log
```

### Save Results

```bash
# Save analysis to JSON file
python auth_analyzer.py \
  --log /var/log/auth.log \
  --json-out analysis.json
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--log` | Path to authentication log file (required) |
| `--json-out` | Save results to JSON file | stdout |

## Log Format

The tool expects standard authentication log format (e.g., `/var/log/auth.log`):

```
Failed password for invalid user admin from 192.168.1.100
Failed password for user root from 192.168.1.100
Accepted publickey for user admin from 192.168.1.50
```

## Output Format

### Console Output

```json
{
  "top_fail_ips": [
    ["192.168.1.100", 150],
    ["10.0.0.50", 75]
  ],
  "spray_ips": [
    ["192.168.1.100", 5]
  ],
  "success_after_fail": [
    {
      "user": "admin",
      "ip": "192.168.1.100",
      "fails": 10,
      "success": 1
    }
  ]
}
```

## Detections

### Brute Force Attacks

Identifies IPs with high numbers of failed login attempts:
- **Threshold**: Configurable (default: top 10 IPs)
- **Indicators**: Multiple failed attempts from same IP

### Credential Spraying

Detects username enumeration attacks:
- **Pattern**: Multiple users attempted from same IP
- **Threshold**: 3+ users per IP

### Success After Failure

Identifies successful logins after multiple failures:
- **Risk**: Compromised credentials
- **Action**: Review and investigate

## Examples

### Example 1: Basic Analysis

```bash
# Analyze authentication log
python auth_analyzer.py \
  --log /var/log/auth.log \
  --json-out auth_analysis.json
```

### Example 2: Security Monitoring

```bash
# Regular monitoring
python auth_analyzer.py \
  --log /var/log/auth.log \
  --json-out daily_analysis.json
```

## Use Cases

- **Security Monitoring**: Detect brute force and spraying attacks
- **Threat Detection**: Identify suspicious authentication patterns
- **Incident Response**: Analyze authentication logs during incidents
- **Educational Purposes**: Learn about log analysis techniques

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security analysis and educational purposes only.

- Only analyze log files you own or have explicit written authorization to analyze
- Respect privacy and data protection regulations
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Only analyze log files you own or have explicit authorization to analyze!
