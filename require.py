import textwrap
import inspect
import sys

runtime = inspect.currentframe

IDENTIFIER = 'CONTENT__'

def python_require(module, runtime):
    # Get content in module
    with open(module, 'r') as f:
        data = f.read()
        data = textwrap.dedent(data)
    
    # Search globals for file content that's actually being run.
    if IDENTIFIER in runtime.f_globals:
        read = runtime.f_globals[IDENTIFIER]
    else:
        # Set the content to the default if it doesn;t exist yet.
        with open(runtime.f_globals['__file__'], 'r') as f:
            read = f.read()

    # Add the module code to the following code.
    post = data + '\n' + '\n'.join(
        read.splitlines()[runtime.f_lineno:]
    )
    
    # Modify the global variable so the next iteration f this function has access to it.
    runtime.f_globals[IDENTIFIER] = post
    
    # Execute the module code and the flowwing code.
    exec(post, runtime.f_globals)

    # Stop before executing the following code twice.
    sys.exit()