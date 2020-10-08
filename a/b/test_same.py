print(f"\n{'-' * 60}\nimported {__file__}\nspec: {__spec__}\n\n")

def test_same(fixture_a, fixture_a_b):
    import sys
    from pprint import pp
    pp('\n')
    pp({k: v for k, v in sys.modules.items() if 'test_' in k or 'conftest' in k})
    assert fixture_a == 'a'
    assert fixture_a_b == 'a_b'
