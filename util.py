import os


def read_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        m, n = list(map(int, lines[0].strip().split()))
        l =  list(map(int, lines[1].strip().split()))
        return m, n, l

def solve_files(dir, solver):
    result_dir = os.path.join(dir,"..","result")
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    for file in os.listdir(dir):
        print("Solving file :",file)
        m, n, l = read_file(os.path.join(dir, file))
        s = solver(m,l)
        with open(os.path.join(result_dir,file+'.sol'), "w") as solution:
            solution.write(str(len(s))+"\n")
            solution.write(" ".join([str(i) for i in s]))
