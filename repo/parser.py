from models.repo import Repo


class RepoParser:
    
    @classmethod
    def parse(cls, response):
        output = []
        for i in range(len(response)):
            res = response[i]
            repo = Repo(res["id"], res["name"], res["stargazers_count"])
            output.append(repo)
        return output