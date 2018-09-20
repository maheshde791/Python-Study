#!usr/bin/python
def test(v):
    # Test for None.
    # ... Print -1 for length if None.
    if v is not None:
        print(len(v))
    else:
        print(-1)

# Use None argument.
test(None)

# Use string argument.
test("hello")