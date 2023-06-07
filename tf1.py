from sentence_transformers import SentenceTransformer

retriever = SentenceTransformer('flax-sentence-embeddings/all_datasets_v3_mpnet-base')
retriever