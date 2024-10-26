def breakingRecords(scores):
    min_count=0
    max_count=0
    min_score=scores[0]
    max_score=scores[0]
    
    for i in scores:
        if min_score>i:
            min_score=i
            min_count+=1
        if max_score<i:
            max_score=i
            max_count+=1
    return max_count,min_count

scores=[12,24,10,24]
res=breakingRecords(scores)
print(res)