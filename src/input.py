file = 'data/a_an_example.in.txt'

people = {}
projects = {}


def sort_dict_by_sub_value_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1]['score'])


if __name__ == "__main__":
    with open(file, 'r') as f:
        c, p = f.readline().split()
        for pearson in range(int(c)):
            name, n_skills = f.readline().split()
            if name not in people:
                people[name] = []
            for skill in range(int(n_skills)):
                people[name].append(f.readline().strip().split())
        for project in range(int(p)):
            name, days, score, best, roles = f.readline().strip().split()
            if name not in projects:
                projects[name] = {
                    'name': name,
                    'days': int(days),
                    'score': int(score),
                    'best': int(best),
                    'roles': []
                }

            for role in range(int(roles)):
                projects[name]['roles'].append(f.readline().strip().split())

    projects = sort_dict_by_sub_value_dict(projects)
    print(people)
    print(projects)
