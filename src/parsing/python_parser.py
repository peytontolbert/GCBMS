import ast
from typing import List
from .parser_interface import ParserInterface

class PythonParser(ParserInterface):
    
    def parse_file(self, file_path: str) -> ast.AST:
        with open(file_path, 'r') as file:
            content = file.read()
        return ast.parse(content, filename=file_path)
    
    def parse_directory(self, directory_path: str) -> List[ast.AST]:
        asts = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    asts.append(self.parse_file(file_path))
        return asts