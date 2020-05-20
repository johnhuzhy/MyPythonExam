# coding:utf-8
import json
import pprint


def fun10_15():
    """
    JSON⇒シークエンス
    """
    # dict
    json_str = '{"name":"John", "age":32}'
    student = json.loads(json_str)
    print(type(student), '⇒', student)
    print(f"{student['name']} is {student['age']} years old.")
    # list
    arry_str = '[{"name":"John", "age":32, "male": true},{"name":"Stella", "age":26, "male": false}]'
    students = json.loads(arry_str)
    print(type(students), '⇒', students)
    for sts in students:
        if sts['male']:
            print(f"{sts['name']} (he)is {sts['age']} years old.")
        else:
            print(f"{sts['name']} (she)is {sts['age']} years old.")
    # from file
    sample = None
    with open('./prop/sample_data.json') as file:
        sample = json.load(file)
    print(type(sample))
    for key in sample.keys():
        if type(sample[key]) == list:
            print(f"{key} is ↓↓↓LIST↓↓↓")
            pprint.pprint(sample[key])
        else:
            print(f"{key} is {sample[key]}.")


def fun10_16():
    """
    シークエンス⇒JSON
    """
    student = [{'name': 'John', 'age': 32, 'male': True},
               {'name': 'Stella', 'age': 26, 'male': False}]
    json_str = json.dumps(student)
    print(type(json_str), '⇒', json_str)


if __name__ == "__main__":
    fun10_15()
    fun10_16()
