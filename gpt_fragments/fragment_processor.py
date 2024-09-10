from gpt_fragments.api_client import GPTClient
from gpt_fragments.utils import read_jsonl, write_jsonl, get_article_context
from tqdm import tqdm
import concurrent.futures

class FragmentProcessor:
    """
    A class representing a fragment processor.

    Attributes:
        gpt_client (:obj:`GPTClient`): The GPT client used for generating summaries and tags.
    """    
    def __init__(self):
        """
        Initialize a GPTClient object.

        This function initializes an instance of the GPTClient class and assigns it to the self.gpt_client attribute.

        Args:
            None

        Returns:
            None
        """        
        self.gpt_client = GPTClient()

    def process_fragments(self, input_file: str, output_file: str) -> None:
        """
        Process the fragments from an input file and generate related fragments.

        Args:
            input_file (str): The file path to the input JSONL file.
            output_file (str): The file path to write the output JSONL file.

        Returns:
            None

        Raises:
            IOError: If there is an issue with reading or writing the files.
        """
        fragments = []
        articles = list(read_jsonl(input_file))

        article_list = [article for article in articles if article['type'] == 'article']
        total_articles = len(article_list)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.generate_fragment, article): article for article in article_list}

            for future in tqdm(concurrent.futures.as_completed(futures), total=total_articles):
                try:
                    fragment = future.result()
                    fragments.append(fragment)
                except Exception as e:
                    print(f"Error procesando un fragmento: {e}")

        for fragment in fragments:
            fragment['related_fragments'] = self.find_related_fragments(fragment, fragments)

        write_jsonl(output_file, fragments)

    def generate_fragment(self, article: dict) -> dict:
        """
        Generate a fragment of content for an article.

        Args:
            self: The instance of the class.
            article (dict): A dictionary containing information about the article, including 'url' and 'text'.

        Returns:
            dict: A dictionary containing the generated fragment with 'title', 'content', 'summary', 'tags', 'original_reference', and 'related_fragments'.
        """        
        prompt = get_article_context(article['url'], self.gpt_client)
        title, summary, tags = self.gpt_client.generate_summary_and_tags(article['text'], prompt)

        return {
            'title': title,
            'content': article['text'],
            'summary': summary,
            'tags': tags,
            'original_reference': article['url'],
            'related_fragments': []
        }

    def find_related_fragments(self, fragment: dict, all_fragments: list) -> list:
        """
        Find related fragments based on tags.

        Args:
            fragment (dict): The fragment to find related fragments for.
            all_fragments (list): A list of all fragments to search for related fragments.

        Returns:
            list: A list of titles of related fragments.
        """        
        related = []
        for other_fragment in all_fragments:
            if other_fragment != fragment:
                if any(tag in fragment['tags'] for tag in other_fragment['tags']):
                    related.append(other_fragment['title'])
        return related
