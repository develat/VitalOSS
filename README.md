# VitalOSS

VitalOSS is an automated auditing tool designed to evaluate the health and sustainability of open-source projects. By analyzing GitHub repositories, it generates a comprehensive "Health Score" based on key maintainability indicators.

## The Problem
Open-source software (OSS) powers modern infrastructure, yet maintainer burnout and project abandonment remain critical risks to software supply chains. Sustainability in OSS is difficult to measure objectively at a glance. Developers and organizations need a reliable, automated framework to assess whether a project is actively maintained, welcoming to stakeholders, and legally compliant before integrating it into production environments.

## How It Works
VitalOSS connects directly to the GitHub API to scan target repositories and compute a structured Health Score by evaluating core structural and behavioral dimensions:
- **License Compliance:** Verification of valid, standard open-source licenses to prevent legal exposure.
- **Documentation Quality:** Heuristic analysis of essential files (including README, CONTRIBUTING, and CODE_OF_CONDUCT).
- **Project Activity Dynamics:** Commit frequency, release intervals, and continuous integration vitality checked against customizable time windows.
- **Maintenance Responsiveness:** Closed-to-open issue ratios and duration metrics mapping the velocity of maintainer triage and community support.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/vitaloss.git

# Navigate into the project directory
cd vitaloss

# Install required Python dependencies
pip install -r requirements.txt

# Execute a health scan
python main.py --repo usernames/repo-name
```

## Roadmap
- [x] Baseline repository structural analysis (License, README verification).
- [x] Scriptable Command-Line Interface and visual terminal reporting engines.
- [ ] Implement robust activity intervals and issue triage tracking mechanisms.
- [ ] **AI Semantic Analysis:** Integrate OpenAI Codex endpoints to perform semantic parsing of issue threads and PR discussions, assessing developer sentiment trends and accurate workload telemetry.
- [ ] Web-based central telemetry dashboard showing historical health score trajectories.
