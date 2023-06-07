
import json
from pprint import pprint

from sentence_transformers import SentenceTransformer

retriever = SentenceTransformer('flax-sentence-embeddings/all_datasets_v3_mpnet-base')
retriever

# ------ Pinecone ---------------
import pinecone  # pip install pinecone-client
import os

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

# connect to pinecone (get API key and env at app.pinecone.io)
pinecone.init(api_key=PINECONE_API_KEY, environment="us-west4-gcp")

# Run once to create Pinecone Vector DB
# # create index
# pinecone.create_index(
# 	'youtube-search',
#   	dimension=768, metric='cosine'
# )

# connect to the new index
index = pinecone.Index('youtube-search')
# ----------------------------------------------------

# ytt = [json.loads(line) for line in open('data/Onzd5QxKaGQ/parsed_subtitles.txt', 'r')]
    
# print(f"\nlength of ytt= {len(ytt)}\n\n")

# from tqdm.auto import tqdm

# docs = []  # this will store IDs, embeddings, and metadata

# batch_size = 64

# for i in tqdm(range(0, len(ytt), batch_size)):
#     i_end = min(i+batch_size, len(ytt))
#     # extract batch from YT transactions data
#     batch = ytt[i:i_end]
    
#     # encode batch of text
#     embeds = retriever.encode([i['text'] for i in batch]).tolist()
    
#     # each snippet needs a unique ID
#     # we will merge video ID and start_seconds for this
#     ids = [i['video_id']+str(i['start_second']) for i in batch]

#     # # create metadata records
#     meta = [{
#         'video_id': x['video_id'],
#         'title': x['title'],
#         'text': x['text'],
#         'start_second': x['start_second'],
#         'end_second': x['end_second'],
#         'url': x['url'],
#         'thumbnail': x['thumbnail']
#     } for x in batch]
    

#     # # # create list of (IDs, vectors, metadata) to upsert
#     to_upsert = list(zip(ids, embeds, meta))
#     # # # add to pinecone
#     index.upsert(vectors=to_upsert)
    
# QUERY -------------------------------------------------- 
    
query = "what is fair value accounting?"

xq = retriever.encode([query]).tolist()

xc = index.query(xq, top_k=5,
                 include_metadata=True)

print(xc)



