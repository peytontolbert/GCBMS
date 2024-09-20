from abc import ABC, abstractmethod
from typing import List
from ast import AST

class ParserInterface(ABC):
    
    @abstractmethod
    def parse_file(self, file_path: str) -> AST:
        """Parses a single file and returns its Abstract Syntax Tree (AST)."""
        pass
    
    @abstractmethod
    def parse_directory(self, directory_path: str) -> List[AST]:
        """Recursively parses all files within a directory and returns their ASTs."""
        pass