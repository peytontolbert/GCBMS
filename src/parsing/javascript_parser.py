import os
from typing import List
from .parser_interface import ParserInterface
import esprima

class JavaScriptParser(ParserInterface):
    
    def parse_file(self, file_path: str):
        with open(file_path, 'r') as file:
            content = file.read()
        return esprima.parseModule(content, comment=True)
    
    def parse_directory(self, directory_path: str) -> List:
        asts = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.js'):
                    file_path = os.path.join(root, file)
                    asts.append(self.parse_file(file_path))
        return asts