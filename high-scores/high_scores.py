def latest(scores):
    last_added_score = len(scores) - 1
    return scores[last_added_score]


def personal_best(scores):
    scores.sort()
    bigest_score = len(scores) - 1
    return scores[bigest_score]


def personal_top_three(scores):
    # scores.sort()
    # scores[-1]
    # scores[-2]
    # scores[-3]

    # personal_top_three_scores = []
    # personal_top_three_scores.append(scores[len(scores) - 1])
    # personal_top_three_scores.append(scores[len(scores) - 2])
    # personal_top_three_scores.append(scores[len(scores) - 3])
    # return personal_top_three_scores
    
    # scores.sort(reverse=True)
    # for s in range(len(scores)):
    #     current = scores[s]
        
    #     if current > 2:
    #         scores.remove()
    #         print(s)

    # a = b = c = -1

    # for s in scores:
    #     current = s

    #     if current > a:
    #         temp = a
    #         a = current
    #         current = temp

    #     if current > b:
    #         temp = b
    #         b = current
    #         current = temp
        
    #     if current > c:
    #         c = current



    # top_three = [-1, -2, -3]

    # for s in scores:
    #     min_of_three = min(top_three)
        
    #     if s > min_of_three:
    #         top_three.remove(min_of_three)
    #         top_three.append(s)
    
    # return top_three


    # top_three = []

    # for s in scores:
    #     if len(top_three) < 3:
    #         top_three.append(s)
    #     else:    
    #         top_three.append(s)
    #         min_of_four = min(top_three)
    #         top_three.remove(min_of_four)
            
    # return top_three
