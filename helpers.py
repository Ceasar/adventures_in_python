

def assert_raises(e, func, *args):
    """Assert an expression raises a given type of exception."""
    try:
        func(*args)
    except e:
        assert True
    except Exception as g:
        assert False, "Wrong error raised: %s" % g
    else:
        if e is not None:
            assert False, "No error raised."
