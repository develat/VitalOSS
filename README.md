# VitalOSS

VitalOSS is an automated auditing tool designed to evaluate the health and sustainability of open-source projects. By analyzing GitHub repositories, it generates a comprehensive "Health Score" based on key maintainability indicators.

## The Problem
Open-source software (OSS) powers the modern web, but maintainer burnout and project abandonment remain critical issues. Sustainability in OSS is often difficult to measure at a glance. Developers and organizations need a reliable way to assess whether a project is actively maintained, welcoming to contributors, and legally safe to use before integrating it into their stacks.

## How it works
VitalOSS scans a target GitHub repository and calculates a Health Score by evaluating structural and behavioral metrics:
- **License Presence:** Ensures the project has a clear and valid open-source license.
- **README Quality:** Checks for essential documentation (installation, usage, contribution guidelines).
- **Recent Activity:** Analyzes commit frequency, recent releases, and overall project momentum.
- **Issue Responsiveness:** Measures how quickly maintainers respond to and resolve issues.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/vitaloss.git

# Navigate into the project directory
cd vitaloss

# Install dependencies
npm install

# Run the auditor
npm start
```

## Roadmap
- [x] Initial GitHub repository structural analysis (License, README).
- [ ] Implement activity and issue response tracking.
- [ ] **AI Semantic Analysis:** Integrate GPT-4o for deep semantic analysis of issue threads and PR discussions to gauge community tone and maintainer workload.
- [ ] Developer dashboard with historical health trends.
