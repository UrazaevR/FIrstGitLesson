def say_hello(name):
    print(f'Hello, {name}!')


def goodbye_world():
    print('Bye bye')
    return 'Bye bye'


if __name__ == '__main__':
    say_hello(input())
    goodbye_world()