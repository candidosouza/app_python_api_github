class MarkdownGenerator:
    
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'**ID:** {repo.id} **Name:** {repo.name} **Stars:** {repo.stars}\n' for repo in repos)
        
        return f'## Repos \n\n{items}'
