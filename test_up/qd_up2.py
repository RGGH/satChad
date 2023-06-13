from qdrant_client.http.models import PointStruct
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

client = QdrantClient("localhost", port=6333)

operation_info = client.upsert(
    collection_name="test_collection",
    wait=True,
    points=[
        PointStruct(id=4, vector=[0.05, 0.51, 0.76, 0.74], payload={"city": "Paris"}),
        PointStruct(id=5, vector=[0.19, 0.41, 0.75, 0.11], payload={"city": ["Rome", "London"]}),
        PointStruct(id=6, vector=[0.36, 0.75, 0.47, 0.94], payload={"city": ["Berlin", "Moscow"]}),
    ]
)

from qdrant_client.http.models import UpdateStatus
print(operation_info.status)
