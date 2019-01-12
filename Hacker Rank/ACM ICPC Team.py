import itertools

def combiKnowledge(topic):
    n = len(topic)
    combi = itertools.combinations(range(n),2)
    knowledge_dict = {}
    for c in combi:
        knowledge_dict.update({c:[int(topic[c[0]][i]) or int(topic[c[1]][i]) for i in range(len(topic[0])) if int(topic[c[0]][i]) or int(topic[c[1]][i])]})
    return knowledge_dict

def acmTeam(topic):
    knowledge_dict = combiKnowledge(topic)
    knowledge = {}
    for k,v in knowledge_dict.items():
        if len(v) in knowledge:
            knowledge[len(v)].append(k)
        else:
            knowledge.update({len(v):[k]})
    print(knowledge)

acmTeam(['1100','0011','1010'])