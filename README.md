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
# Save results to JSON file
python auth_analyzer.py \
  --log /var/log/auth.log \
  --json-out auth_analysis.json
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--log` | Path to authentication log file (required) |
| `--json-out` | Save results to JSON file |

## Log Format

The tool expects standard Linux authentication logs (auth.log) with entries like:

```
Failed password for invalid user admin from 192.168.1.100
Accepted publickey for user from 192.168.1.50
Failed password for root from 10.0.0.1
```

## Output Format

### Console Output

```json
{
  "top_fail_ips": [
    ["192.168.1.100", 150],
    ["10.0.0.1", 89]
  ],
  "spray_ips": [
    ["192.168.1.100", 5]
  ],
  "success_after_fail": [
    {
      "user": "admin",
      "ip": "192.168.1.100",
      "fails": 45,
      "success": 1
    }
  ]
}
```

## Detected Patterns

### 1. Brute Force Attacks

Identifies IPs with high numbers of failed login attempts:
- **Threshold**: Multiple failed attempts from same IP
- **Severity**: High
- **Action**: Block IP, investigate source

### 2. Credential Spraying

Detects username enumeration attacks:
- **Pattern**: Multiple different usernames from same IP
- **Threshold**: 3+ different users per IP
- **Severity**: Medium-High
- **Action**: Monitor IP, implement rate limiting

### 3. Success After Failure

Identifies successful logins after multiple failures:
- **Pattern**: Successful login after failed attempts
- **Severity**: High (potential compromised account)
- **Action**: Investigate account, force password reset

## Examples

### Example 1: Basic Analysis

```bash
# Analyze auth log
python auth_analyzer.py --log /var/log/auth.log
```

### Example 2: Save Report

```bash
# Save analysis to JSON
python auth_analyzer.py \
  --log /var/log/auth.log \
  --json-out security_report.json
```

## Use Cases

- **Security Monitoring**: Detect attacks in real-time
- **Incident Response**: Analyze authentication logs
- **Threat Detection**: Identify suspicious patterns
- **Educational Purposes**: Learn about authentication attacks

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security analysis and educational purposes only.

- Only analyze logs you own or have explicit written authorization to analyze
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

**Remember**: Only analyze logs you own or have explicit authorization to analyze!
