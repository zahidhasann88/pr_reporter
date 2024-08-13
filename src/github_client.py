import os
import requests

class GitHubClient:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.base_url = "https://api.github.com"
        self.repo = os.getenv('GITHUB_REPO')

    def get_headers(self):
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_pull_requests(self):
        url = f"{self.base_url}/repos/{self.repo}/pulls"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def get_pull_request_details(self, pr_number):
        url = f"{self.base_url}/repos/{self.repo}/pulls/{pr_number}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()
