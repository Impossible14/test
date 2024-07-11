import json


def update_values(tests, values_dict):
    if isinstance(tests, list):
        for test in tests:
            update_values(test, values_dict)
    elif isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]
        if 'values' in tests:
            update_values(tests['values'], values_dict)


def main():
    a = open('values.json', 'r')
    values = json.load(a)
    b = open('tests.json', 'r')
    tests = json.load(b)

    values_dict = {value['id']: value['value'] for value in values['values']}

    if 'tests' in tests:
        update_values(tests['tests'], values_dict)

    rep = open('report.json', 'w')
    json.dump(tests, rep, indent=2)


if __name__ == '__main__':
    main()
