import a.conftest
import a.b.conftest
import b.conftest

import a.test_same
import a.b.test_same
import b.test_same

from pathlib import Path

print(str(Path('a/test_same.py')), end=' ')
a.test_same.test_same(a.conftest.fixture_a.__wrapped__())
print('.')

print(str(Path('a/b/test_same.py')), end=' ')
a.b.test_same.test_same(a.conftest.fixture_a.__wrapped__(), a.b.conftest.fixture_a_b.__wrapped__())
print('.')

print(str(Path('b/test_same.py')), end=' ')
b.test_same.test_same(b.conftest.fixture_b.__wrapped__())
print('.')
