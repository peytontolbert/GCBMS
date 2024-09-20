from flask import Flask

def start_web_server(graph_db, llm_agent):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "GBCMS Web UI"

    # Add more routes and logic as needed

    app.run(host='0.0.0.0', port=5000)