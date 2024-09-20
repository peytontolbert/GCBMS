from .database import Neo4jConnection

class EdgeManager:
    def __init__(self):
        self.conn = Neo4jConnection()

    def create_edge(self, source_node_id: str, target_node_id: str, edge_type: str, attributes: dict) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                f"""
                MATCH (a), (b)
                WHERE a.id = $source_id AND b.id = $target_id
                CREATE (a)-[r:{edge_type} $attributes]->(b)
                RETURN r
                """,
                source_id=source_node_id,
                target_id=target_node_id,
                attributes=attributes
            )
            return result.single()["r"]

    def delete_edge(self, edge_id: str) -> None:
        with self.conn.get_session() as session:
            session.run("MATCH ()-[r]->() WHERE r.id = $id DELETE r", id=edge_id)

    def update_edge(self, edge_id: str, attributes: dict) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                "MATCH ()-[r]->() WHERE r.id = $id SET r += $attributes RETURN r",
                id=edge_id,
                attributes=attributes
            )
            return result.single()["r"]

    def get_edge(self, edge_id: str) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                "MATCH ()-[r]->() WHERE r.id = $id RETURN r",
                id=edge_id
            )
            return result.single()["r"]

    def find_edges(self, filters: dict) -> list:
        with self.conn.get_session() as session:
            query = "MATCH ()-[r]->() WHERE "
            conditions = []
            for key, value in filters.items():
                conditions.append(f"r.{key} = ${key}")
            query += " AND ".join(conditions) + " RETURN r"
            result = session.run(query, **filters)
            return [record["r"] for record in result]