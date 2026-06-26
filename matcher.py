from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from roles import role_profiles

model=SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text)

def recommend_roles(resume_text):
    resume_vec=get_embedding(resume_text)
    scores=[]
    for role,keywords in role_profiles.items():
        role_vec=get_embedding(keywords)
        score=cosine_similarity([resume_vec],[role_vec])[0][0]
        scores.append([score,role])
    scores.sort(reverse=True)
    return scores[:5]

def match_role(resume_text,role_name):
    resume_vec=get_embedding(resume_text)
    role_vec=get_embedding(role_profiles[role_name])
    resume_set=set(resume_text.lower().split())
    role_set=set(role_profiles[role_name].lower().split())
    missing_keywords=role_set-resume_set
    score=cosine_similarity([resume_vec],[role_vec])[0][0]
    return score,missing_keywords
