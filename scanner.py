from github import Github
from github.GithubException import UnknownObjectException
import datetime
from config import Config

class RepositoryScanner:
    def __init__(self, repo_path: str):
        """
        Initialize with the target repository path (e.g., 'owner/repo_name').
        """
        self.repo_path = repo_path
        # Use the token for authentication to increase API limits, otherwise anonymous
        if Config.GITHUB_TOKEN:
            self.g = Github(Config.GITHUB_TOKEN)
        else:
            self.g = Github()

    def scan(self) -> dict:
        """
        Connects to the repository and extracts raw metrics.
        """
        try:
            repo = self.g.get_repo(self.repo_path)
        except Exception as e:
            return {"error": f"Failed to access repository {self.repo_path}. Error: {str(e)}"}

        # 1. Check for critical files in the root directory
        try:
            # Getting root contents to avoid making a request for each individual file
            root_contents = repo.get_contents("")
            file_names = [f.name.lower() for f in root_contents]
        except Exception:
            file_names = []

        critical_files = {
            "LICENSE": any("license" in f for f in file_names),
            "README.md": "readme.md" in file_names,
            "CONTRIBUTING.md": "contributing.md" in file_names,
            "CODE_OF_CONDUCT.md": "code_of_conduct.md" in file_names
        }

        # 2. Get the last commit date
        try:
            # PyGithub pagination handles [0] gracefully
            last_commit = repo.get_commits()[0]
            last_commit_date = last_commit.commit.author.date.isoformat()
        except Exception:
            last_commit_date = None

        # 3. Calculate open vs closed issues
        try:
            open_issues = repo.open_issues_count
            closed_issues = repo.get_issues(state='closed').totalCount
            total_issues = open_issues + closed_issues
            
            if total_issues > 0:
                closed_percentage = round((closed_issues / total_issues) * 100, 2)
            else:
                closed_percentage = 0.0
        except Exception:
            open_issues = 0
            closed_issues = 0
            total_issues = 0
            closed_percentage = 0.0

        # Return the collected raw data
        raw_data = {
            "repository": self.repo_path,
            "critical_files": critical_files,
            "last_commit_date": last_commit_date,
            "issues": {
                "open": open_issues,
                "closed": closed_issues,
                "total": total_issues,
                "closed_percentage": closed_percentage
            }
        }

        return raw_data

# Example usage for testing locally if run directly
if __name__ == "__main__":
    import json
    from rich import print as rprint
    
    scanner = RepositoryScanner("pallets/flask")
    result = scanner.scan()
    rprint(result)
