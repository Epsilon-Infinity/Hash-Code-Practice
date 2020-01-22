import util
from copy import deepcopy
from collections import defaultdict

def solver(paticipants, pizas):
    pizas_key = defaultdict(list)
    for i, v in enumerate(pizas):
      pizas_key[v].append(i)
    acc = [[], 0]
    print('File loaded :: size of piza : %s, paticipants : %d ' % (len(pizas), paticipants))
    def solve(pizs):
        s = sum(pizs)
        if s <= paticipants:
            if s > acc[1]:
              acc[1] = s
              acc[0] = pizs
              print('Found :', s)
            return
        for j in range(len(pizs)):
            solve(pizs[0:j] + pizs[j+1:])
            if acc[1] == paticipants:
                break
    solve(pizas)
    print('************** Solution *************')
    return [pizas_key[v].pop(0) for v in acc[0]]

if __name__=="__main__":
    util.solve_files('input', solver)