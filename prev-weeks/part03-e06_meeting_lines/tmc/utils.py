import importlib
import sys

def load(pkg, method, err=None):

    if not err:
        err = '{0}.{1} does not exist!'.format(pkg, method)

    def fail(*args, **kwargs):
        raise AssertionError(err)

    try:
        return getattr(importlib.import_module(pkg), method)
    except Exception:
        return fail

def get_out():
    return sys.stdout.getvalue().strip()

def get_err():
    return sys.stderr.getvalue().strip()

def any_contains(needle, haystack):
    any(map(lambda x: needle in x, haystack))



def patch_name(m, d):
    import importlib
    parts=d.split(".")
    try:
        getattr(importlib.import_module(m), parts[-1])
#        p='src.mystery_data.LinearRegression'
        p=".".join([m, parts[-1]])
    except ModuleNotFoundError:
        raise
    except AttributeError:
        if len(parts) == 1:
            raise
        try:
            getattr(importlib.import_module(m), parts[-2])
#            p='src.mystery_data.linear_model.LinearRegression'
            p=".".join([m] + parts[-2:])
        except AttributeError:
            if len(parts) == 2:
                raise
#            p='src.mystery_data.sklearn.linear_model.LinearRegression'
            getattr(importlib.import_module(m), parts[-3])
            p=".".join([m] + parts[-3:])
    return p
