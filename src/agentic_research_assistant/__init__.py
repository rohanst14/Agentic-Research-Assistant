import re
from dataclasses import dataclass
@dataclass(frozen=True)
class Evidence:
    source: str
    passage: str
    overlap: int
def retrieve(question,corpus):
    q=set(re.findall(r'\w+',question.lower())); out=[]
    for source,text in corpus.items():
        overlap=len(q & set(re.findall(r'\w+',text.lower())))
        if overlap: out.append(Evidence(source,text,overlap))
    return sorted(out,key=lambda e:(-e.overlap,e.source))
def audit(evidence,corpus):
    return [e for e in evidence if e.source in corpus and e.passage in corpus[e.source]]
def run(question,corpus,limit=3):
    if limit<1: raise ValueError('limit must be positive')
    verified=audit(retrieve(question,corpus)[:limit],corpus)
    return {'question':question,'findings':[{'source':e.source,'quote':e.passage} for e in verified],'trace':['retrieve','audit','synthesize'],'status':'evidence_found' if verified else 'insufficient_evidence'}
