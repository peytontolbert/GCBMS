from .database import Neo4jConnection

class NodeManager:
    def __init__(self):
        self.conn = Neo4jConnection()

    def create_node(self, node_type: str, attributes: dict) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                f"CREATE (n:{node_type} $attributes) RETURN n",
                attributes=attributes
            )
            return result.single()["n"]

    def delete_node(self, node_id: str) -> None:
        with self.conn.get_session() as session:
            session.run("MATCH (n) WHERE n.id = $id DETACH DELETE n", id=node_id)

    def update_node(self, node_id: str, attributes: dict) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                "MATCH (n) WHERE n.id = $id SET n += $attributes RETURN n",
                id=node_id,
                attributes=attributes
            )
            return result.single()["n"]

    def get_node(self, node_id: str) -> dict:
        with self.conn.get_session() as session:
            result = session.run(
                "MATCH (n) WHERE n.id = $id RETURN n",
                id=node_id
            )
            return result.single()["n"]

    def find_nodes(self, filters: dict) -> list:
        with self.conn.get_session() as session:
            query = "MATCH (n) WHERE "
            conditions = []
            for key, value in filters.items():
                conditions.append(f"n.{key} = ${key}")
            query += " AND ".join(conditions) + " RETURN n"
            result = session.run(query, **filters)
            return [record["n"] for record in result]