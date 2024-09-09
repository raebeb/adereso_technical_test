from os import environ
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = Path('enviroment/.env')
load_dotenv(dotenv_path)

OPENAI_TOKEN = environ.get('OPENAI_TOKEN')

class GPTClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_TOKEN)

    def generate_summary_and_tags(self, content):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Resume el siguiente contenido y genera tags:."},
                {"role": "user", "content": content},
            ],
            max_tokens=1000,
        )
        summary = response.choices[0].message.content
        # print(f"Summary: {summary}")
        tags = ["Api", "Tickets"]
        return summary, tags
