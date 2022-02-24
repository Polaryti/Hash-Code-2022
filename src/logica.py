from sqlalchemy import true

from input import input_process
from output import output_process


def skill_possible(project_skills, pearson_skills):
    for project_skill, skill_score in project_skills.items():
        for pearson_skill_, score in pearson_skills.items():
            if project_skill == pearson_skill_ and skill_score <= score:
                return project_skill
    return []


def is_possible(project, people, schedule, day, duration):
    workers = [0] * len(list(project['roles'].keys()))
    for p, skills in people.items():
        if day not in schedule[p]:
            sk = skill_possible(project['roles'], skills[0])
            if sk != []:
                workers[list(project['roles'].keys()).index(sk)] = p
                project['roles'].pop(sk)
                for i in range(duration):
                    schedule[p][day + i] = 1
        if project['roles'] == {} and 0 not in workers and workers != []:
            return workers

    return False


if __name__ == "__main__":
    schedule = {}
    solution = {}
    file = 'data/b_better_start_small.in.txt'

    people, projects = input_process(file)
    for p in list(people.keys()):
        schedule[p] = {}

    first_iteration = True
    to_delete = []
    i = 100
    while first_iteration or i > 0:
        i -= 1
        first_iteration = False
        day = 0
        to_delete = []
        for pro in list(projects.values()):
            if pro['name'] not in to_delete:
                duration = int(pro['days'])
                res = is_possible(pro, people, schedule, day, duration)

                if res is not False:
                    solution[pro['name']] = res
                    to_delete.append(pro['name'])

                day += duration

        for delete in to_delete:
            projects.pop(delete)

    output_process(solution, file)
