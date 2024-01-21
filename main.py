'''
Addition Rule. To add the probabliity of two events, we add their individual 
probabilities and subtract the proability of their intersection
(This is accounted for in their individual probabilities))
You do not have to worry about the probability of the intersection if 
they are mutually excusive because that probability is 0
'''

def prob_a_or_b(a,b,all_possible_outcomes):
  prob_a = len(a)/len(all_possible_outcomes)

  prob_b = len(b)/len(all_possible_outcomes)

  inter = a.intersection(b)

  prob_inter = len(inter)/len(all_possible_outcomes)

  return prob_a + prob_b - prob_inter


# Dependent events
def prob_a_and_b_dependent(a, b, all_possible_outcomes):
  prob_a = len(a) / len(all_possible_outcomes)
  prob_b = len(b) / len(all_possible_outcomes)
  prob_a_and_b_dependent = prob_a * prob_b * len(a.intersection(b)) / len(all_possible_outcomes)
  return prob_a_and_b_dependent

# Independent events
def prob_a_and_b_independent(a, b, all_possible_outcomes):
  prob_a = len(a) / len(all_possible_outcomes)
  prob_b = len(b) / len(all_possible_outcomes)
  prob_a_and_b_independent = prob_a * prob_b
  return prob_a_and_b_independent