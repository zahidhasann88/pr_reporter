class ReportGenerator:
    def __init__(self, github_client):
        self.github_client = github_client

    def generate_summary(self, pr_details):
        summary = {
            'title': pr_details['title'],
            'author': pr_details['user']['login'],
            'created_at': pr_details['created_at'],
            'merge_status': 'Merged' if pr_details.get('merged', False) else 'Not Merged',
            'comments': pr_details.get('comments', 0),
            'additions': pr_details.get('additions', 0),
            'deletions': pr_details.get('deletions', 0),
        }
        return summary

    def generate_report(self):
        pull_requests = self.github_client.get_pull_requests()
        report = []
        for pr in pull_requests:
            pr_details = self.github_client.get_pull_request_details(pr['number'])
            report.append(self.generate_summary(pr_details))
        return report
