from os import environ
from pathlib import Path
import re

from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = Path('enviroment/.env')
load_dotenv(dotenv_path)

OPENAI_TOKEN = environ.get('OPENAI_TOKEN')

class GPTClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_TOKEN)

    def generate_summary_and_tags(self, content, prompt=None):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": prompt},
                {"role": "user",
                 "content": f"Para el siguiente contenido, quiero que generes una respuesta en este formato específico:\n\n**Título:** [Título del artículo]\n\n**Resumen:** [Resumen del contenido]\n\n**Tags:** [#Tag1 #Tag2 ...]\n\nContenido:\n{content}"},
            ],
            max_tokens=1000,
        )
        response = response.choices[0].message.content
        title = re.search(r'\*\*Título:\*\*(.*?)\n', response).group(1).strip()
        summary = re.search(r'\*\*Resumen:\*\*(.*?)\n\n', response, re.DOTALL).group(1).strip()
        tags = re.search(r'\*\*Tags:\*\*(.*?)$', response, re.DOTALL).group(1).strip().split()

        return title, summary, tags
