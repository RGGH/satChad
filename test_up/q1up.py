from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient

# set up client
client = QdrantClient(host="localhost", port=6333)
coll_name="testx2_collection"
collection_info = client.get_collection(collection_name=coll_name)

# get highest index
print(f"current vector count = ", collection_info.vectors_count)

try:
    client.create_collection(
    collection_name=coll_name,
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)
except:
    pass

# upsert additional points
import numpy as np
from qdrant_client.models import PointStruct

vectors = np.random.rand(100, 100)
client.upsert(
    collection_name=coll_name,
    points=[
        PointStruct(
            id=collection_info.vectors_count + idx,
            vector=vector.tolist(),
            payload={"color": "red", "rand_number": idx % 10}
        )
        for idx, vector in enumerate(vectors)
    ]
)

collection_info = client.get_collection(collection_name=coll_name)
print(f"new vector count = after upsert ", collection_info.vectors_count)
