from pipeline import filter_people
import pytest

def test_filter_people_min_age():
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 19},
        {"name": "Charlie", "age": 34}
    ]
    result = filter_people(people, min_age=21)
    assert len(result) == 2
    assert {"name": "Alice", "age": 25} in result
    assert {"name": "Charlie", "age": 34} in result

def test_filter_people_min_age_2():
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 19},
        {"name": "Charlie", "age": 34}
    ]
    result = filter_people(people, min_age=21)
    assert len(result) == 2
    assert {"name": "Alice", "age": 25} in result
    assert {"name": "Charlie", "age": 34} in result

# def test_filter_fails_on_wrong_age():
#     people = [
#         {"name": "TestUser", "age": 18}
#     ]
#     result = filter_people(people, min_age=21)
#     assert len(result) == 1  # ← This will fail, result will be empty!

def test_filter_fails_on_missing_age():
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},  # Missing 'age'
    ]
    result = filter_people(people, min_age=25)
    assert result == [{"name": "Alice", "age": 30}]

