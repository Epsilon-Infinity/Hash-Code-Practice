def read_input(file):

    inp = open(f"input/{file}.in")
    M, N = list(map(int, inp.readline().rstrip().split()))
    P = map(int, inp.readline().rstrip().split())

    return M, P


def generate_output(file, sums):
    
    K = len(sums)
    P = " ".join([str(s) for s in sums.keys()])
    out = open(f"output/{file}.out","w+")
    
    out.write(f"{K}\n")
    out.write(f"{P}\n")


def small_ended(M, P):
    
    sums = {}
    tot = 0
    
    for i, z in enumerate(P):
        
        if tot+z > M:
            break
        
        tot += z
        
        sums[i] = z
    
    return sums


def big_ended(M, P):
    
    P = list(P)
    lp = len(P)
    sums = {}
    tot = 0
    
    for i, z in enumerate(reversed(P)):
        
        if tot+z > M:
            break
        
        tot += z
        
        sums[lp-i-1] = z
    
    return sums
        
        

def points(sums):
    
    print(sum(sums.values()))


def solve(file):
    M, P = read_input(file)
    sums = small_ended(M, P)
    generate_output(file, sums)


def test():

    file = 'a_example'
    M, P = read_input(file)
    s = small_ended(M,P)
    b = big_ended(M,P)
    points(s)
    points(b)


test()