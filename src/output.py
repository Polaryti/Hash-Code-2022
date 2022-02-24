o_file = 'data/output/a_an_example.out.txt'

def from_solution_to_output(solution):
    pass


if __name__ == "__main__":
    n_projects = 0
    projects = {}
    with open(o_file, 'w') as f:
        f.write(str(n_projects) + '\n')
        for project, people in projects.items():
            f.write(project + '\n')
            for person in list(people):
                f.write(person + " ")
            f.write('\n')