import pinecone  # pip install pinecone-client
import os

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

# connect to pinecone (get API key and env at app.pinecone.io)
pinecone.init(api_key=PINECONE_API_KEY, environment="us-west4-gcp")
# create index
pinecone.create_index(
	'youtube-search',
  	dimension=768, metric='cosine'
)
# connect to the new index
index = pinecone.Index('youtube-search')
