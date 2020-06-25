import check50
# TODO: remove!
import check50.runner


def get_checks(module):
    attrs = [getattr(module, attr) for attr in dir(module)]
    # This is an awful hack. Better way to identify a check dynamically?
    return [check for check in attrs if hasattr(check, "_check_dependency")]

def import_checks(module, prefix=""):
    checks = get_checks(module)

    for check in checks:
        old_name = check.__name__
        new_name = prefix + old_name

        # Rename check
        check.__name__ = new_name

        # Rename in the runner
        index = check50.runner._check_names.index(old_name)
        check50.runner._check_names[index] = new_name

        # Import check in current module
        globals()[new_name] = check

        # This is another awful hack
        # The original function name, instead of the decorated one, is used to create check_results
        # and this is directly used in the dependency graph.
        # Should fix!!!
        for cell in check.__closure__:
            if callable(cell.cell_contents):
                cell.cell_contents.__name__ = new_name
                break


hello = check50.import_checks("../hello")
import_checks(hello, prefix="hello_")

greedy = check50.import_checks("../greedy")
import_checks(greedy, prefix="greedy_")

mario = check50.import_checks("../mario")
import_checks(mario, prefix="mario_")

vigenere = check50.import_checks("../vigenere")
import_checks(vigenere, prefix="vigenere_")
