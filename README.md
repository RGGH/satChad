# Sat Chad

all-MiniLM-L6-v2
This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.

##### https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2#all-minilm-l6-v2


run yt1.py to get transcripts
run up_quadrant to upsert vectors
neural_searcher and service.py need to go into the FastAPI directory (~/python-server) that the front end calls
the index.html is in /var/www/html and the js is inside the js folder

`.
├── app.py
├── data
├── id_list.txt
├── index.html
├── js
├── lsd.py
├── neural_searcher.py
├── pc1.py
├── qdrant_storage
├── README.md
├── requirements.txt
├── satChad.code-workspace
├── saylor-vids.txt
├── service.py
├── startup_vectors.npy
├── test_qd.py
├── test_up
├── up_pinecone.py
├── up_quadrant.py
└── yt1.py`
