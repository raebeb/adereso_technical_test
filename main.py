from gpt_fragments.fragment_processor import FragmentProcessor

def main():
    """
    Main function to process JSONL fragments from input file and store processed output in a new file.

    The main function initializes a FragmentProcessor object and uses it to process fragments from the input JSONL file.
    The processed output is then saved to a new JSONL file.

    Args:
        None

    Returns:
        None
    """    
    processor = FragmentProcessor()
    processor.process_fragments('data/adereso_cda.jsonl', 'output/processed_output.jsonl')

if __name__ == "__main__":
    main()

