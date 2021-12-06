from argparse import ArgumentParser

from app.core import run_anonymization_pipeline


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("source_uri", type=str, help="The source URI")
    args = parser.parse_args()
    run_anonymization_pipeline(args.source_uri)
