import psycopg2
from psycopg2 import sql
import logging

class QueryEngine:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='your_db',
            user='your_user',
            password='your_password',
            host='localhost',
            port='5432'
        )
        self.logger = logging.getLogger(__name__)

    def execute_query(self, query, params=None, fetch_one=False):
        self.logger.debug(f"Executing query: {query} with params: {params}")
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if fetch_one:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            self.connection.commit()
            return result

    def find_shortest_path(self, source_node_id: str, target_node_id: str) -> list:
        with self.conn.get_session() as session:
            result = session.run(
                """
                MATCH (start {id: $source_id}), (end {id: $target_id}),
                p = shortestPath((start)-[*]-(end))
                RETURN p
                """,
                source_id=source_node_id,
                target_id=target_node_id
            )
            return result.single()["p"] if result.single() else None

    def get_subgraph(self, node_ids: list) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                """
                MATCH (n)-[r]->(m)
                WHERE n.id IN $ids AND m.id IN $ids
                RETURN n, r, m
                """,
                ids=node_ids
            )
            nodes = []
            edges = []
            for record in result:
                nodes.append(record["n"])
                nodes.append(record["m"])
                edges.append(record["r"])
            # Remove duplicates
            nodes = list({node.id for node in nodes})
            edges = list({edge.id for edge in edges})
            return {"nodes": nodes, "edges": edges}