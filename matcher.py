import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
with open('role_data.json','r') as f:
    data=json.load(f)

model=SentenceTransformer('all-mpnet-base-v2')

def get_embedding(text):
    return model.encode(text)

def recommend_roles(resume_text):
    resume_vec=get_embedding(resume_text)
    scores=[]
    for role,profile in data.items():
        score=cosine_similarity([resume_vec],[np.array(profile['embeddings'])])[0][0]
        scores.append([score,role])
    scores.sort(reverse=True)
    return scores[:5]

def match_role(resume_text,role_name):
    resume_vec=get_embedding(resume_text)
    role_vec=np.array(data[role_name]['embeddings'])
    resume_text = re.sub(r'[^\w\s]', '', resume_text)
    resume_set=set(resume_text.lower().split())
    role_set={keyword.lower() for keyword in data[role_name]['keywords']}
    missing_keywords=role_set-resume_set
    score=cosine_similarity([resume_vec],[role_vec])[0][0]
    return score,missing_keywords
