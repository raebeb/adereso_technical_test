import unittest
import os
import json
from gpt_fragments.fragment_processor import FragmentProcessor


class TestFragmentProcessor(unittest.TestCase):

    def setUp(self):
        self.input_file = 'tests/test_input.jsonl'
        self.output_file = 'tests/test_output.jsonl'

        test_data = [
            {"type": "article", "url": "https://example.com/article1", "text": "Este es el contenido del artículo 1."},
            {"type": "article", "url": "https://example.com/article2", "text": "Este es el contenido del artículo 2."}
        ]

        with open(self.input_file, 'w') as f:
            for item in test_data:
                f.write(json.dumps(item) + "\n")


    def test_process_fragments(self):
        processor = FragmentProcessor()
        processor.process_fragments(self.input_file, self.output_file)

        self.assertTrue(os.path.exists(self.output_file), "El archivo de salida no se creó correctamente.")

        with open(self.output_file, 'r') as f:
            output_data = [json.loads(line) for line in f]

        self.assertEqual(len(output_data), 2, "La cantidad de fragmentos generados no es correcta.")
        self.assertIn('title', output_data[0], "El fragmento no contiene un título.")
        self.assertIn('summary', output_data[0], "El fragmento no contiene un resumen.")
        self.assertIn('tags', output_data[0], "El fragmento no contiene etiquetas.")

    def test_generate_fragment(self):
        processor = FragmentProcessor()
        article = {"type": "article", "url": "https://example.com/article1",
                   "text": "Este es el contenido del artículo 1."}

        fragment = processor.generate_fragment(article)

        self.assertIn('title', fragment, "El fragmento generado no contiene un título.")
        self.assertIn('summary', fragment, "El fragmento generado no contiene un resumen.")
        self.assertIn('tags', fragment, "El fragmento generado no contiene etiquetas.")
        self.assertEqual(fragment['original_reference'], article['url'],
                         "La referencia al artículo original es incorrecta.")

    def test_related_fragments(self):
        processor = FragmentProcessor()

        fragments = [
            {"title": "Fragmento 1", "tags": ["API", "Tickets"], "content": "Contenido 1"},
            {"title": "Fragmento 2", "tags": ["API", "Integración"], "content": "Contenido 2"},
            {"title": "Fragmento 3", "tags": ["CRM", "Integración"], "content": "Contenido 3"}
        ]

        related = processor.find_related_fragments(fragments[0], fragments)

        self.assertIn("Fragmento 2", related, "El fragmento relacionado no se identificó correctamente.")
        self.assertNotIn("Fragmento 3", related, "El fragmento no relacionado fue identificado incorrectamente.")


if __name__ == '__main__':
    unittest.main()
