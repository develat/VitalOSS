import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """VitalOSS Configuration Parameters"""
    
    # GitHub Authentication
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        print("Warning: GITHUB_TOKEN is not set. API rate limits will be restricted.")
    
    # Health Score Weights (Total: 100 points)
    SCORE_WEIGHTS = {
        "has_license": 20,           # Points for having a valid OSS license
        "has_readme": 15,            # Points for having a README
        "readme_quality": 15,        # Points based on README content quality/length
        "recent_activity": 25,       # Points for commits/releases within the last 30 days
        "issue_responsiveness": 25   # Points for quick issue triage/resolution
    }
    
    # Thresholds
    ACTIVITY_DAYS_THRESHOLD = 30        # What counts as "recent"
    ISSUE_RESPONSE_DAYS_THRESHOLD = 7   # What counts as a "responsive" issue resolution
