import unittest
from src.report_generator import ReportGenerator
from src.github_client import GitHubClient

class TestReportGenerator(unittest.TestCase):
    def test_generate_summary(self):
        client = GitHubClient()
        generator = ReportGenerator(client)
        pr_details = client.get_pull_request_details(client.get_pull_requests()[0]['number'])
        summary = generator.generate_summary(pr_details)
        self.assertIn('title', summary)
        self.assertIn('author', summary)

if __name__ == '__main__':
    unittest.main()
