dict = {
    '0': [
        {'a': 'abc'},
        {'b': 'bbc'}
    ],
    '1': [
        {'a': 'abc'},
        {'b': 'bbc'}
    ]
}

# print(len(dict['0']))

for index in range(1, len(dict['0'])):
    print(dict['0'][index])