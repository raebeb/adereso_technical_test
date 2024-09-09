from gpt_fragments.fragment_processor import FragmentProcessor

def main():
    processor = FragmentProcessor()
    processor.process_fragments('data/adereso_cda.jsonl', 'output/processed_output.jsonl')

if __name__ == "__main__":
    main()
