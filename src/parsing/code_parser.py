import os
from typing import List
from .python_parser import PythonParser
from .javascript_parser import JavaScriptParser
from .java_parser import JavaParser
from .dependency_analyzer import DependencyAnalyzer
from .documentation_extractor import DocumentationExtractor

class CodeParser:
    
    def __init__(self):
        self.parsers = {
            'Python': PythonParser(),
            'JavaScript': JavaScriptParser(),
            'Java': JavaParser()
        }
        self.dependency_analyzer = DependencyAnalyzer()
        self.documentation_extractor = DocumentationExtractor()
    
    def parse_file(self, file_path: str, language: str):
        parser = self.parsers.get(language)
        if not parser:
            raise ValueError(f"Unsupported language: {language}")
        ast_tree = parser.parse_file(file_path)
        imports = self.dependency_analyzer.analyze_imports(ast_tree)
        function_calls = self.dependency_analyzer.analyze_function_calls(ast_tree)
        inheritances = self.dependency_analyzer.analyze_class_inheritance(ast_tree)
        docstrings = self.documentation_extractor.extract_docstrings(ast_tree)
        comments = self.documentation_extractor.extract_comments(ast_tree)
        return {
            'imports': imports,
            'function_calls': function_calls,
            'inheritances': inheritances,
            'docstrings': docstrings,
            'comments': comments
        }
    
    def parse_directory(self, directory_path: str, language: str):
        parser = self.parsers.get(language)
        if not parser:
            raise ValueError(f"Unsupported language: {language}")
        ast_trees = parser.parse_directory(directory_path)
        results = []
        for ast_tree in ast_trees:
            imports = self.dependency_analyzer.analyze_imports(ast_tree)
            function_calls = self.dependency_analyzer.analyze_function_calls(ast_tree)
            inheritances = self.dependency_analyzer.analyze_class_inheritance(ast_tree)
            docstrings = self.documentation_extractor.extract_docstrings(ast_tree)
            comments = self.documentation_extractor.extract_comments(ast_tree)
            results.append({
                'imports': imports,
                'function_calls': function_calls,
                'inheritances': inheritances,
                'docstrings': docstrings,
                'comments': comments
            })
        return results