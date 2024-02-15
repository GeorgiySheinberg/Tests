"""
Функции
"""
from main import *
import requests


def unique_mentors():
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor[0:mentor.find(" "):1]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def longest_and_shortest_duration():
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {'title': course, 'mentor': mentor, 'duration': duration}
        courses_list.append(course_dict)
    min_value = min(durations)
    max_value = max(durations)

    maxes = []
    minis = []
    for id_value, value in enumerate(durations):
        if value >= max_value:
            maxes.append(id_value)
        elif value <= min_value:
            minis.append(id_value)

    courses_min = []
    courses_max = []
    for id_ in minis:
        courses_min.append(courses_list[id_]['title'])
    for id_ in maxes:
        courses_max.append(courses_list[id_]['title'])

    return (f'Самый короткий курс(ы): {"".join(courses_min)} - {min_value} месяца(ев)',
            f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_value} месяца(ев)')


def map_courses_by_duration():
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for idx, item in enumerate(courses_list):
        key = courses_list[idx]['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(idx)

    durations_dict = dict(sorted(durations_dict.items()))
    for key, value in durations_dict.items():
        for index in range(len(value)):
            result = courses_list[value[index]]['title']
            return f'{result} - {key} месяцев'


def create_folder(folder_name, ya_token=None):
    cloud_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    ya_params = {
            'path': f"{folder_name}"
        }
    headers = {
            'Authorization': f'OAuth {ya_token}'
        }
    response = requests.put(cloud_url, params=ya_params, headers=headers)
    return response.status_code


print(create_folder('5'))
