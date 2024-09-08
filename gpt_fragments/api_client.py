import openai



class GPTClient:
    def __init__(self):
        openai.api_key = 'your-api-key-here'

    def generate_summary_and_tags(self, content):
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=f"Resume el siguiente contenido y genera tags:\n\n{content}", #TODO: initial version, remove this when the prompt is ready
            max_tokens=1000
        )
        summary = response['choices']
        tags = ["Api", "Tickets"]
        return summary, tags
