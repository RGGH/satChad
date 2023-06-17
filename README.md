# Sat Chad

all-MiniLM-L6-v2
This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.

##### https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2#all-minilm-l6-v2


run yt1.py to get transcripts
run up_quadrant to upsert vectors
neural_searcher and service.py need to go into the FastAPI directory (~/python-server) that the front end calls
the index.html is in /var/www/html and the js is inside the js folder

.

├── data

├── saylor-vids.txt

├── up_quadrant.py
└── yt1.py

run yt1 to get transcripts
run up_quadrant to do the upsert
