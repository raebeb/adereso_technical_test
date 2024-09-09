import json
from gpt_fragments.api_client import GPTClient
from gpt_fragments.utils import read_jsonl, write_jsonl, get_article_context
from tqdm import tqdm

class FragmentProcessor:
    def __init__(self):
        self.gpt_client = GPTClient()

    def process_fragments(self, input_file, output_file):
        fragments = []

        articles = list(read_jsonl(input_file))
        total_articles = len(articles)

        for article in tqdm(articles, total=total_articles):
            if article['type'] == 'article':
                fragment = self.generate_fragment(article)
                fragments.append(fragment)

        write_jsonl(output_file, fragments)

    def generate_fragment(self, article):
        prompt = get_article_context(article['url'])
        title, summary, tags = self.gpt_client.generate_summary_and_tags(article['text'], prompt)

        return {
            'title': title,
            'content': article['text'],
            'summary': summary,
            'tags': tags,
            'original_reference': article['url'],
            'related_fragments': [] #TODO: Implement related fragments
        }
