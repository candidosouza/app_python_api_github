from github.client import GitHubClient
from repo.parser import RepoParser
from repo.reports_generators import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator
from repo.reports.writer import ReportWriter

from models.member import Member
from models.manager import Menager

if __name__ == '__main__':
    username = 'candidosouza'
    response = GitHubClient().get_repo_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser().parse(response['body'])
        markdown_report = ReportsGenerator().build(MarkdownGenerator, repos)
        html_report = ReportsGenerator().build(HTMLGenerator, repos)
        ReportWriter().write(markdown_report)

        print(markdown_report)
        print(html_report)
    else:
        print(response['body'])

    member = Member('member', 'member@email.com')
    menager = Menager('manager', 'manager@email.com')

    print(member.members())
    print(member.work())
    print(menager.work())
