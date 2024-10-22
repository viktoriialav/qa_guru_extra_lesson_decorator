import functools
import re
import types


def make_sentence_from(name: str) -> str:
    return ' '.join(re.split('_+', name)).title()


def step(func):
    @functools.wraps(func)
    def func_with_logging(*args, **kwargs):
        is_method = (
                args
                and isinstance(args[0], object)
                and isinstance(getattr(args[0], func.__name__), types.MethodType)
        )

        args_to_log = args[1:] if is_method else args
        args_and_kwargs_to_log_as_str = [
            *map(str, args_to_log),
            *map(lambda item: f'{item[0]}={item[1]}', kwargs.items())
        ]
        args_and_kwargs_str = (
            (': ' + ', '.join(args_and_kwargs_to_log_as_str))
            if args_and_kwargs_to_log_as_str else ''
        )

        print(
            (f'[{args[0].__class__.__name__}] ' if is_method else '')
            + make_sentence_from(func.__name__)
            + args_and_kwargs_str
        )

        return func(*args, **kwargs)
    return func_with_logging
