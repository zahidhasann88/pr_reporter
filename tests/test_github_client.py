import unittest
from src.github_client import GitHubClient

class TestGitHubClient(unittest.TestCase):
    def test_get_pull_requests(self):
        client = GitHubClient()
        prs = client.get_pull_requests()
        self.assertTrue(len(prs) > 0)

    def test_get_pull_request_details(self):
        client = GitHubClient()
        pr_number = client.get_pull_requests()[0]['number']
        pr_details = client.get_pull_request_details(pr_number)
        self.assertIn('title', pr_details)

if __name__ == '__main__':
    unittest.main()
