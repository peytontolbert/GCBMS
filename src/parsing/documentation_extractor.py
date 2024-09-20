from typing import List
from ast import AST
import esprima
import javalang

class DocumentationExtractor:
    
    def extract_docstrings(self, ast_tree: AST) -> List[str]:
        """Extracts docstrings from Python AST."""
        docstrings = []
        if isinstance(ast_tree, ast.Module):
            docstrings.append(ast_tree.doc)
        for node in ast.walk(ast_tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                docstrings.append(ast.get_docstring(node))
        return [doc for doc in docstrings if doc]
    
    def extract_comments(self, ast_tree: AST) -> List[str]:
        """Extracts comments from JavaScript AST using Esprima."""
        comments = []
        if hasattr(ast_tree, 'comments'):
            for comment in ast_tree.comments:
                comments.append(comment.value)
        return comments
    
    # Methods for Java comments extraction can be added similarly