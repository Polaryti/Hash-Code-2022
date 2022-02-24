people = {}
projects = {}


def sort_dict_by_sub_value_dict(d):
    return dict(sorted(d.items(), key=lambda kv: kv[1]['score']))


def input_process(file):
    people = {}
    projects = {}

    with open(file, 'r') as f:
        c, p = f.readline().split(" ")
        for pearson in range(int(c)):
            name, n_skills = f.readline().split(" ")
            if name not in people:
                people[name] = []
            for skill in range(int(n_skills)):
                skill_name, skill_score = f.readline().split(" ")
                people[name].append({skill_name: int(skill_score)})
        for project in range(int(p)):
            name, days, score, best, roles = f.readline().strip().split(" ")
            if name not in projects:
                projects[name] = {
                    'name': name,
                    'days': int(days),
                    'score': int(score),
                    'best': int(best),
                    'roles': {}
                }

            for role in range(int(roles)):
                role_name, role_score = f.readline().split(" ")
                projects[name]['roles'][role_name] = int(role_score)

    projects = sort_dict_by_sub_value_dict(projects)
    # print(people)
    # print(projects)

    return people, projects
