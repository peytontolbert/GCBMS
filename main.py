from src.database.database import GraphDatabase
from src.agent.llm_agent import LLMAgent
from src.ui.server import start_web_server

def main():
    graph_db = GraphDatabase()
    llm_agent = LLMAgent(graph_db)
    start_web_server(graph_db, llm_agent)

if __name__ == "__main__":
    main()