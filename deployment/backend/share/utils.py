from functools import wraps
from typing import Callable

DEFAULT_PRECISION = 16


def make_response():
    def decorator(func: Callable):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            data = func(*args, **kwargs)
            return {
                "code": 200,
                "data": recursive_round(data),
            }

        return wrap_func

    return decorator


def recursive_round(data):
    if isinstance(data, tuple):
        result = []
        for item in data:
            result.append(recursive_round(item))
        return tuple(result)
    elif isinstance(data, list):
        result = []
        for item in data:
            result.append(recursive_round(item))
        return result
    elif isinstance(data, dict):
        result = {}
        for key, item in data.items():
            result[key] = recursive_round(item)
        return result
    elif isinstance(data, float):
        if "e" in str(data):
            num_str, exp_str = str(data).split("e")
            num = float(num_str)
            exp = int(exp_str)
            ndigit = max(DEFAULT_PRECISION - len(str(int(abs(num)))), 0)
            return round(num, ndigit) * 10**exp
        else:
            ndigit = max(DEFAULT_PRECISION - len(str(int(abs(data)))), 0)
            return round(data, ndigit)
    else:
        return data
