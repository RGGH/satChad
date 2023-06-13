from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

client = QdrantClient("localhost", port=6333)
client.recreate_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=4, distance=Distance.DOT),
)

collection_info = client.get_collection(collection_name="test_collection")

from pprint import pprint
pprint(collection_info)
