from .database import Neo4jConnection

class QueryEngine:
    def __init__(self):
        self.conn = Neo4jConnection()

    def execute_query(self, query_string: str) -> list:
        with self.conn.get_session() as session:
            result = session.run(query_string)
            return [record.data() for record in result]

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