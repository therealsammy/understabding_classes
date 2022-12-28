def outer_func():
    message = 'HI'

    def inner_func():
        print(message)

    return inner_func()


outer_func()
