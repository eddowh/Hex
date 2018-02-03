# -*- coding: utf-8 -*-

import argparse
import os.path

HERE = os.path.dirname(os.path.abspath(__file__))

class HexArtCLI(object):

    acceptable_output_extensions = ['.ps']

    arguments = [
        {
            'name': 'input_hex_filepath',
            'help_text': '',
        },
        {
            'name': 'input_png_filepath',
            'help_text': '',
        },
    ]

    optional_arguments = [
        {
            'flag': '-o',
            'name': '--output',
            'help_text': '',
            'required': True,
            'default': '',
        },
    ]

    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._add_arguments()
        self._args = None

    @property
    def args(self):
        return self._args

    def _add_arguments(self):
        # required arguments
        for arg in self.arguments:
            self._parser.add_argument(arg['name'], help=arg['help_text'])
        # optional arguments
        for arg in self.optional_arguments:
            self._parser.add_argument(arg['flag'], arg['name'], help=arg['help_text'], required=arg['required'], default=arg['default'])

    def run(self):
        self._parse_and_validate_args()

    def _parse_and_validate_args(self):
        self._args = self._parser.parse_args()
        input_hex_filepath = os.path.join(HERE, self.args.input_hex_filepath) if not os.path.isabs(args.input_hex_filepath) else args.input_hex_filepath
        input_png_filepath = os.path.join(HERE, self.args.input_png_filepath) if not os.path.isabs(args.input_png_filepath) else args.input_png_filepath

        # check if output is postscript
        output_filepath = self.args.output
        is_valid_output_filepath = False
        for ext in self.acceptable_output_extensions:
            if output_filepath.endswith(ext):
                is_valid_output_filepath = True
                break
        if not is_valid_output_filepath:
            raise Exception

def main():
    hex_art_cli = HexArtCLI()
    hex_art_cli.run()

if __name__ == '__main__':
    main()
