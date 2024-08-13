import sys
import os

# Add the 'src' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from github_client import GitHubClient
from report_generator import ReportGenerator

def main():
    client = GitHubClient()
    generator = ReportGenerator(client)
    report = generator.generate_report()

    if not report:
        print("No pull requests found or the report is empty.")
    else:
        for summary in report:
            print(summary)

if __name__ == '__main__':
    main()
