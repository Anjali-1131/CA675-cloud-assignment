import json

with open('top10spamusers.json','r') as f:
    data = json.load(f)

data_model = {}
for obj in data:
    reviewerID = obj.get('reviewerID')
    if reviewerID in data_model:
        data_model[reviewerID]+=[obj.get('reviewText')]
    else:
        data_model[reviewerID]=[]

for k,v in data_model.items():
    comment = ' '.join(v)
    with open(k+'.txt','w') as f:
        f.write(comment)