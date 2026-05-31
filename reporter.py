from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def get_ai_summary(raw_data: dict) -> str:
    """
    Placeholder for AI sentiment analysis.
    
    # TODO: Integrate OpenAI API (e.g., GPT-4o) here to perform deep semantic 
    # analysis on the repository's issue threads and PR discussions. 
    # This will gauge community tone, maintainer workload, and overall 
    # interaction sentiment to refine the Health Score.
    """
    return "[AI Analysis Pending Credits]"

def generate_visual_report(raw_data: dict):
    """
    Generates a professional visual report in the terminal using rich.
    """
    if "error" in raw_data:
        console.print(Panel(f"[bold red]Error:[/bold red] {raw_data['error']}", title="VitalOSS Audit Failed"))
        return

    repo_name = raw_data.get("repository", "Unknown Repository")
    
    console.print(f"\n[bold blue]VitalOSS Audit Report for:[/bold blue] [bold white]{repo_name}[/bold white]\n")

    # Critical Files Table
    files_table = Table(title="Critical Files Verification", show_header=True, header_style="bold magenta")
    files_table.add_column("File", style="cyan", width=25)
    files_table.add_column("Status", justify="center", width=15)

    files_data = raw_data.get("critical_files", {})
    for file_name, present in files_data.items():
        status = "[bold green]✓ Found[/bold green]" if present else "[bold red]✗ Missing[/bold red]"
        files_table.add_row(file_name, status)
        
    console.print(files_table)
    console.print()

    # Activity & Issues Table
    activity_table = Table(title="Activity & Issues Overview", show_header=True, header_style="bold magenta")
    activity_table.add_column("Metric", style="cyan", width=25)
    activity_table.add_column("Value", justify="right", style="white", width=15)

    last_commit = raw_data.get("last_commit_date", "Unknown")
    if last_commit and last_commit != "Unknown":
        last_commit = last_commit[:10]  # Just show the date part YYYY-MM-DD

    issues_data = raw_data.get("issues", {})
    open_issues = str(issues_data.get("open", 0))
    closed_issues = str(issues_data.get("closed", 0))
    closed_percentage = f"{issues_data.get('closed_percentage', 0.0)}%"

    activity_table.add_row("Last Commit Date", last_commit)
    activity_table.add_row("Open Issues", open_issues)
    activity_table.add_row("Closed Issues", closed_issues)
    
    # Color code the resolution rate for better visuals
    cp_val = issues_data.get('closed_percentage', 0.0)
    cp_color = "green" if cp_val >= 70 else ("yellow" if cp_val >= 40 else "red")
    activity_table.add_row("Issue Resolution Rate", f"[bold {cp_color}]{closed_percentage}[/bold {cp_color}]")

    console.print(activity_table)
    console.print()

    # AI Summary Panel
    ai_summary_text = get_ai_summary(raw_data)
    console.print(Panel(ai_summary_text, title="AI Sentiment Analysis", border_style="bold yellow", expand=False))
    console.print()

# Example usage for testing locally if run directly
if __name__ == "__main__":
    from scanner import RepositoryScanner
    scanner = RepositoryScanner("pallets/flask")
    result = scanner.scan()
    generate_visual_report(result)
