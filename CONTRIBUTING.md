# Contributing to VitalOSS

First off, thank you for considering contributing to VitalOSS! It's people like you who make open-source software sustainable, safe, and welcoming.

## Our Goal
VitalOSS aims to provide developers with a clear, automated "Health Score" for any GitHub repository, directly addressing the critical issues of maintainer burnout and project abandonment in the OSS ecosystem.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/your-username/vitaloss.git
   cd vitaloss
   ```
3. **Set up your environment:**
   We highly recommend using a Python virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
4. **Configure your GitHub Token:**
   Run `cp .env.example .env` and populate `GITHUB_TOKEN` with your personal access token. This is required to heavily increase your GitHub API rate limits during development and scanning.

## Where We Need Help

While all contributions, refactors, and cleanups are completely welcome, we are actively looking for architecture help in two major areas:

### 1. Improving the Health Metrics Engine
Currently, our `RepositoryScanner` in `scanner.py` evaluates basic structural signals (licenses, standard metric files) and raw activity (commit dates, issue ratios). We want to refine the scoring algorithm by introducing:
*   **Code Quality Signals:** Checking for Linters, test coverage artifacts, and CI/CD pipeline status (e.g., GitHub Actions presence).
*   **Community Health Indicators:** Identifying "good first issue" labels and responsiveness to first-time contributors.
*   **Dependency Analysis:** Automating simple checks for outdated or deeply vulnerable core dependencies.

### 2. AI Sentiment Analysis Integration
We are preparing the project for review by integrating the OpenAI API (GPT-4o) to semantically analyze issue threads and PR discussions.
*   Check the `get_ai_summary` function inside `reporter.py`.
*   We need robust, well-engineered prompts that can read an issue thread and accurately classify the community tone (toxic, collaborative, abandoned) and the maintainer workload levels, without hallucinating.

## Pull Request Process

1. Create a new branch for your feature (`git checkout -b feature/amazing-new-metric`).
2. Ensure your code follows PEP 8 formatting guidelines. Clean, readable code is a strict requirement.
3. Update the `README.md` if you are adding new dependencies to `requirements.txt` or changing the command-line interface in `main.py`.
4. Submit your PR with a clear description of the specific problem solved or the new health metric added.

## Code of Conduct
Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. Let's build a healthier open-source ecosystem together!
