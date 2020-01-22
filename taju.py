import os
import util
from copy import deepcopy

def solver(paticipants, pizas):
    pizas_key = {v:i for i, v in enumerate(pizas)}
    acc = [[], 0]
    print('File loaded :: %s, %d ' % (len(pizas), paticipants))
    def solve(piza_idx, pizs):
        s = sum(pizs)
        if s <= paticipants:
            if s > acc[1]:
              acc[1] = s
              acc[0] = piza_idx
              print('Found %s'%s)
            return
        for j in range(len(pizs)):
            copy_index = deepcopy(piza_idx)
            copy_index.append(pizas_key[pizs[j]])
            solve(copy_index, pizs[0:j] + pizs[j+1:])
            if acc[1] == paticipants:
                break
    result = []
    solve([], pizas)
    for i in range(len(pizas)):
      if i not in set(acc[0]):
        result.append(i)
    return result

if __name__=="__main__":
    util.solve_files('input', solver)