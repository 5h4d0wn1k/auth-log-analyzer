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

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Only analyze logs you own or have explicit authorization to analyze!
