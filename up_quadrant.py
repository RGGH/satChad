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
coll_name="youtube-search"
print(f"collection = {coll_name}")

collection_info = client.get_collection(collection_name=coll_name)

# get highest index
print(f"current vector count = ", collection_info.vectors_count)

#try:
#    client.create_collection(
#        collection_name=coll_name,
#        vectors_config=VectorParams(size=vs, distance=Distance.COSINE),
#    )
#except:
#    pass
#
# ----------------------------------------------------
import os

# pick the top file from the list to process
with open('saylor-vids.txt', 'r') as fin:
        data = fin.read().splitlines(True)

        upsert_id = (data[0]).strip('\n')

        with open('saylor-vids.txt', 'w') as fout:
                fout.writelines(data[1:])

                print(upsert_id)

# ----------------------------------------------------

fname = f"data/{upsert_id}/parsed_subtitles.txt"

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


# if upsert works - delete data/{upsertfile}/ 
import shutil
shutil.rmtree("data/"+ upsert_id)
print(f"deleted{upsert_id}")


print("Done")

