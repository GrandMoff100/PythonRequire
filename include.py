import textwrap
import inspect
import sys

runtime = inspect.currentframe

def python_include(module, runtime):
    with open(module, 'r') as f:
        data = f.read()
        data = textwrap.dedent(data)
    with open(runtime.f_globals['__file__'], 'r') as f:
        post = '\n'.join(f.read().splitlines()[runtime.f_lineno:])

    exec(data + '\n' + post, globals())
    sys.exit()