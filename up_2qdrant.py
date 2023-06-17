import json
from pprint import pprint
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm.notebook import tqdm

from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus
from qdrant_client.models import PointStruct
from qdrant_client.models import Distance, VectorParams

model = SentenceTransformer('all-MiniLM-L6-v2', device="cpu") # device="cpu" if you don't have a GPU
vs = model.get_sentence_embedding_dimension()


client = QdrantClient(url="http://127.0.0.1:6333")
coll_name="youtube-search2"
print(f"collection = {coll_name}")

client.recreate_collection(
    collection_name="youtube-search2",
    vectors_config=VectorParams(size=vs, distance=Distance.COSINE),
)

collection_info = client.get_collection(collection_name="youtube-search2")
print(f"current vector count = ", collection_info.vectors_count)
# ----------------------------------------------------
fname = "data/eRvBj7j24B0/parsed_subtitles.txt"

df = pd.read_json(fname, lines=True)
print(df[:4])
print("dataframe loaded\n")

vectors = model.encode([
    row.text
    for row in df.itertuples()
], show_progress_bar=True)

print(vectors.shape)

np.save('startup_vectors.npy', vectors, allow_pickle=False)

fd = open(fname)

# payload is now an iterator over startup data
payload = map(json.loads,fd)
payload = [item for item in payload]
from pprint import pprint
print((payload[0]))


# Load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if you don't want to load all data into RAM
vectors = np.load('./startup_vectors.npy')

# ------------- Upsert to Qdrant ------------------------
index = list(range(len(df)))

client.upsert(
    collection_name=coll_name,
    points=[
        PointStruct(
            id=collection_info.vectors_count + idx,
            vector=vector.tolist(),
            payload=payload[idx]
        )
        for idx, vector in enumerate(vectors)
    ]
)
collection_info = client.get_collection(collection_name=coll_name)
print(f"new vector count = after upsert ", collection_info.vectors_count)
print("Done")

