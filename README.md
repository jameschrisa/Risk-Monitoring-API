# Security API Suite

This repository contains three powerful API projects designed to enhance cybersecurity measures for industrial control systems, combat phishing attacks, and monitor supplier security. Each API provides unique features to address specific security concerns.

## Table of Contents

1. [ICS Threat Intel API](#ics-threat-intel-api)
2. [Phishing Pattern Recognition (PPR) API](#phishing-pattern-recognition-ppr-api)
3. [Supplier Security Monitor (SSM) API](#supplier-security-monitor-ssm-api)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## ICS Threat Intel API

The ICS Threat Intelligence API provides a standardized interface for collecting, analyzing, and disseminating threat intelligence related to Industrial Control Systems (ICS).

### Key Features

- Data collection from various sources (open-source, closed-source, sensor data, threat feeds)
- Threat analysis and risk assessment
- Integration with ICS security controls
- Compliance with regulatory standards (e.g., NIST, IEC 62443)

### Endpoints

- `/collection`: Collect threat intelligence data
- `/analysis`: Analyze collected data
- `/dissemination`: Share threat intelligence
- `/integration`: Integrate with security controls

## Phishing Pattern Recognition (PPR) API

The PPR API utilizes machine learning to detect and analyze phishing patterns in URLs, emails, and social media posts.

### Key Features

- URL analysis for phishing patterns
- Email content analysis
- Social media post content analysis
- Machine learning-based prediction of phishing likelihood

### Endpoints

- `/analyze_url`: Analyze a URL for phishing patterns
- `/analyze_email`: Analyze email content for phishing patterns
- `/analyze_social_media`: Analyze social media post content for phishing patterns
- `/get_patterns`: Retrieve a list of known phishing patterns

## Supplier Security Monitor (SSM) API

The SSM API enables businesses to track the security posture of their suppliers, ensuring compliance with security standards and identifying potential vulnerabilities.

### Key Features

- Supplier profiling and security scoring
- Vulnerability tracking
- Compliance monitoring
- Alerting and reporting on supplier security issues

### Endpoints

- `/suppliers`: Retrieve a list of all suppliers
- `/supplier/{id}`: Get a supplier's profile and security score
- `/vulnerabilities`: Retrieve a list of vulnerabilities across all suppliers
- `/compliance`: Monitor compliance status for each supplier
- `/alerts`: Receive alerts on supplier security issues

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/security-api-suite.git
   ```

2. Install dependencies:
   ```
   cd security-api-suite
   pip install -r requirements.txt
   ```

3. Configure the APIs according to the individual README files in each project directory.

## Usage

Each API can be run independently or as part of the suite. Refer to the individual project directories for specific usage instructions and examples.

## Contributing

We welcome contributions to improve these APIs. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
