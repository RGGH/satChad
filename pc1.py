import pinecone  # pip install pinecone-client

# connect to pinecone (get API key and env at app.pinecone.io)
pinecone.init(api_key="YOUR_API_KEY", environment="YOUR_ENV")
# create index
pinecone.create_index(
	'youtube-search',
  	dimension=768, metric='cosine'
)
# connect to the new index
index = pinecone.Index('youtube-search')
