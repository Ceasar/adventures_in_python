

def assert_raises(e, func):
    """Assert an expression raises a given type of exception."""
    try:
        func()
    except e:
        assert True
    except Exception as g:
        assert False, "Wrong error raised: %s" % g
    else:
        if e is not None:
            assert False, "No error raised."
