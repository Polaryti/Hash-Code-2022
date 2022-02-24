def output_process(solution, file):
    with open(file.replace('in', 'out'), 'w') as f:
        f.write(str(len(solution)) + '\n')
        for project, people in solution.items():
            f.write(project + '\n')
            for person in list(people):
                if person == "":
                    print('mal')
                f.write(str(person) + " ")
            f.write('\n')
