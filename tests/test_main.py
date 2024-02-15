from unittest import TestCase
import pytest

import tasks
# TASK 1


class TextUniqueMentors(TestCase):
    def test_string_equality(self):
        expected = ('Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, '
                    'Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, '
                    'Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, '
                    'Эдгар, Юрий')
        result = tasks.unique_mentors()
        self.assertEqual(result, expected)

    def test_duration_equality(self):
        expected = ('Самый короткий курс(ы): Fullstack-разработчик на Python - 12 месяца(ев)',
                    'Самый длинный курс(ы): Java-разработчик с нуля, Frontend-разработчик с нуля - 20 месяца(ев)')
        result = tasks.longest_and_shortest_duration()
        self.assertEqual(result, expected)


def test_map_courses_by_duration():
    expected = 'Fullstack-разработчик на Python - 12 месяцев'
    result = tasks.map_courses_by_duration()
    assert result == expected


# TASK 2
def test_api_yandex():
    expected = 201
    result = tasks.create_folder('test_folder', "")
    assert result == expected


def test_create_folder_already_exists():
    expected = 409
    result = tasks.create_folder('test_folder', "")
    assert result == expected


def test_not_authorized():
    expected = 401
    result = tasks.create_folder('test_folder', '')
    assert result == expected
