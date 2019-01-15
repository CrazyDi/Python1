import json
import functools

def to_json(func):
    ## фигня, которая нормально именует функцию
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        ## наша функция
        result = func(*args, **kwargs)
        ## возвращаем результат, преобразованный в JSON
        return json.dumps(result)
    return wrapped

