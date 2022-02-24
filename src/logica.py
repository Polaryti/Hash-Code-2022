from input import input_process
from output import output_process



def skill_possible(project_skills, pearson_skills):
    for project_skill, skill_score in project_skills.items():
        for pearson_skill_, score in pearson_skills.items():
            if project_skill == pearson_skill_ and skill_score <= score:
                return project_skill
    return False

def is_possible(project, people, schedule, day, duration):
    workers = [0] * len(list(project['roles'].keys()))
    for p, skills in people.items():
        if schedule[p][day] == 0:
            sk = skill_possible(project['roles'], skills[0])
            if not sk:
                pass
            else:
                workers[list(project['roles'].keys()).index(sk)] = p
                del project['roles'][sk]
                for i in range(duration):
                    schedule[p][day + i] = 1
        if project['roles'] == {} and 0 not in workers:
            return workers
    return False              

if __name__ == "__main__":
    schedule = {}
    solution = {}
    file = 'data/f_find_great_mentors.in.txt'

    people, projects = input_process(file)
    for p in list(people.keys()):
        schedule[p] = [0] * 500000
    
    day = 0
    for _, pro in projects.items():
        duration = int(pro['days'])
        res = is_possible(pro, people, schedule, day, duration)

        if res is not False:
            solution[pro['name']] = res

        day += duration

        
    output_process(solution, file)

