# master_similarity_scores


## DIDN'T WORK ##
# # # # Above average pairs # # # #         
def above_average(list):
    all_scores = []
    best = {}
    for word1 in list:
        for word2 in list:
            l = word1.lch_similarity(word2)
            all_scores.append(l)
        if l >= statistics.mean(all_scores):
            best.update({(word1, word2): l})
    return best
aa = above_average(konkle_combined)



# # # # Below Average Pairs # # # #
def below_average(list):
    all_scores = []
    best = {}
    for word1 in list:
        for word2 in list:
            l = word1.lch_similarity(word2)
            all_scores.append(l)
        if l < statistics.mean(all_scores):
           best.update({(word1, word2): l})
    return best
ba = below_average(konkle_combined)
