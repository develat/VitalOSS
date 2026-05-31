import argparse
import sys
from rich.console import Console
from scanner import RepositoryScanner
from reporter import generate_visual_report

console = Console()

def main():
    parser = argparse.ArgumentParser(
        description="VitalOSS: Automated auditing tool for open-source project health and sustainability."
    )
    parser.add_argument(
        "--repo",
        type=str,
        required=True,
        help="Target GitHub repository in the format 'username/repo-name' (e.g., 'pallets/flask')"
    )

    args = parser.parse_args()
    repo_path = args.repo

    # Basic validation
    if "/" not in repo_path:
        console.print("[bold red]Error:[/bold red] Repository format must be 'owner/repo_name'.")
        sys.exit(1)

    console.print(f"[*] Initializing VitalOSS scanner for [bold cyan]{repo_path}[/bold cyan]...")
    
    # Run the scanner with a rich loading status indicator
    with console.status(f"[bold green]Scanning '{repo_path}' data from GitHub API...", spinner="dots"):
        scanner = RepositoryScanner(repo_path)
        raw_data = scanner.scan()

    # Generate the terminal visual report
    generate_visual_report(raw_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Scan interrupted by user. Exiting...[/bold yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]An unexpected error occurred:[/bold red] {str(e)}")
        sys.exit(1)
