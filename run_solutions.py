from collections import Mapping
import os
from six import string_types
import sys
import yaml

# set the base dir path
DIR = os.path.abspath(os.path.dirname(__file__))


def get_test_dirs():
    # get the list of directories to run tests on
    #  if provided on the command line
    if len(sys.argv) > 2:
        return [
            d for d in sys.argv[2].split(',')
            if '-' in d and len(d.split('-')) == 2
        ]
    # else get all of em
    else:
        return [
            os.path.join(DIR, d) for d in os.listdir(DIR)
            if os.path.isdir(os.path.join(DIR, d))
            and '-' in d
            and len(d.split('-')) == 2
        ]


def get_readme_path():
    # set README location
    # if commandline arg is docker
    if len(sys.argv) > 1 and sys.argv[1] == 'docker':
        return '/tmp/repo/README.md'
    # else local
    else:
        return os.path.join(DIR, 'README.md')


def get_config():
    # load the runtime config
    p = os.path.join(DIR, 'run_config.yaml')
    with open(p) as f:
        c = yaml.safe_load(f)

    if c:
        return c
    else:
        raise Exception('Issue loading config')


def get_solution(s=None):
    if s is None:
        s = CONFIG.get('solution', {}).get('value', '')
    t = CONFIG.get('solution', {}).get('type', 'string')

    if t == 'int':
        return int(s)
    elif t == 'float':
        return float(s)
    elif t == 'boolean':
        return bool(s)
    else:
        return str(s)


# Set contants
TEST_DIRS = get_test_dirs()
README = get_readme_path()
CONFIG = get_config()
SOLUTION = get_solution()
SOLUTION_FIELD = CONFIG.get('leaderboard', {}).get('solutionField', 'Solution')
RANKING_FIELD = CONFIG.get('leaderboard', {}).get('rankingField', 'Time')
FIELDS = CONFIG.get('leaderboard', {}).get('fields', [])
OOPS_FIELDS = CONFIG.get('oops', {}).get('fields', [])


def build_test(d):
    if os.path.isfile(os.path.join(d, 'build.sh')):
        os.system('cd {} && bash build.sh'.format(d))


def run_test(d):
    test_out = os.popen('cd {} && bash run.sh'.format(d)).read()
    print('    {}'.format(test_out))
    return test_out


def transform_results(results):
    fields = CONFIG.get('leaderboard', {}).get('fields', [])
    temp_results = []
    for r in results:
        temp = {}
        for i, val in enumerate(r.replace('\n', '').split(',')):
            temp[fields[i]] = val.strip()
            if fields[i] == SOLUTION_FIELD:
                temp[SOLUTION_FIELD] = get_solution(temp[SOLUTION_FIELD])
            if fields[i] == RANKING_FIELD:
                temp[RANKING_FIELD] = float(temp[RANKING_FIELD])
        temp_results.append(temp)

    correct = [r for r in temp_results if r[SOLUTION_FIELD] == SOLUTION]
    incorrect = [r for r in temp_results if r[SOLUTION_FIELD] != SOLUTION]
    if correct:
        avg = sum(c[RANKING_FIELD] for c in correct) / len(correct)
        correct = correct[0]
        correct[RANKING_FIELD] = avg

    if incorrect:
        solutions = ','.join([i[SOLUTION_FIELD] for i in incorrect])
        incorrect = incorrect[0]
        incorrect[SOLUTION_FIELD] = solutions

    return correct, incorrect


def get_test_results(d):
    print('Building {}...'.format(d))
    build_test(d)
    results = []
    print('Running {}...'.format(d))
    for _ in range(CONFIG.get('testCount', 1)):
        results.append(run_test(d))

    return transform_results(results)


def get_readme():
    if os.path.isfile(README):
        with open(README) as f:
            readme = f.read()

        if readme:
            return readme

    raise Exception('No README file found at path: {}'.format(README))


def write_readme(readme):
    if os.path.isfile(README):
        with open(README, 'w') as f:
            f.write(readme)
    else:
        raise Exception('No README file found at path: {}'.format(README))


def strip_current_results(readme):
    leader = readme.find('### Leaderboard')
    oops = readme.find('### Oops')
    if leader:
        return readme[:leader]
    elif oops:
        return readme[:oops]

    return readme


def data_to_md_table(data, ordered_fields, title=None, sort_field=None):
    if not sort_field:
        sort_field = ordered_fields[0]

    # Transform data into table records
    # If data is a map, make it a list of maps
    if isinstance(data, Mapping):
        data = [data]

    # Data is a string, assume CSV in order. Go ahead and md-ify it
    if isinstance(data, string_types):
        data = ' | '.join(data.split(','))
    # else data is a list of dicts.
    else:
        if not ordered_fields:
            ordered_fields = sorted(list(data[0].keys()))

        data = '\n'.join([' | '.join([str(d.get(f)) for f in ordered_fields])
                         for d in sorted(
                             data, key=lambda k: k.get(sort_field))])

    # add header and divider
    header = ' | '.join(ordered_fields) + '\n'
    div = ' | '.join(['---' for _ in range(len(ordered_fields))]) + '\n'

    out = header + div + data + '\n\n'
    if title:
        if not title.endswith('\n\n'):
            title += '\n\n'

        out = title + out

    return out


def update_readme(correct, incorrect):
    readme = get_readme()
    readme = strip_current_results(readme)

    if correct:
        readme += data_to_md_table(correct, FIELDS, title='### Leaderboard',
                                   sort_field=RANKING_FIELD)

    if incorrect:
        readme += data_to_md_table(incorrect, OOPS_FIELDS, title='### Oops')

    write_readme(readme)


if __name__ == '__main__':
    correct_results = []
    incorrect_results = []
    for d in TEST_DIRS:
        correct, incorrect = get_test_results(d)
        if correct:
            correct_results.append(correct)
        if incorrect:
            incorrect_results.append(incorrect)

    print('Updating README.md...')
    update_readme(correct_results, incorrect_results)
    print('Done')
