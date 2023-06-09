import json
from pprint import pprint
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm.notebook import tqdm
from qdrant_client import QdrantClient

model = SentenceTransformer('all-MiniLM-L6-v2', device="cpu") # device="cpu" if you don't have a GPU
vs = model.get_sentence_embedding_dimension()

# ------ Qdrant ---------------

client = QdrantClient(url="http://127.0.0.1:6333")
from qdrant_client.models import Distance, VectorParams

client.recreate_collection(
    collection_name="youtube-search",
    vectors_config=VectorParams(size=vs, distance=Distance.COSINE),
)

print("successfully created collection")

# ----------------------------------------------------

df = pd.read_json("data/mC43pZkpTec/parsed_subtitles.txt", lines=True)
print(df[:4])
print("dataframe loaded\n")

vectors = model.encode([
    row.text
    for row in df.itertuples()
], show_progress_bar=True)

print(vectors.shape)

np.save('startup_vectors.npy', vectors, allow_pickle=False)

fd = open("data/mC43pZkpTec/parsed_subtitles.txt")

# payload is now an iterator over startup data
payload = map(json.loads, fd)

# Load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if you don't want to load all data into RAM
vectors = np.load('./startup_vectors.npy')

# ------------- Upsert to Qdrant ------------------------

client.upload_collection(
    collection_name="youtube-search",
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)