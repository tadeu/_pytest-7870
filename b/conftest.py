print(f"\n{'-' * 60}\nimported {__file__}\nspec: {__spec__}\n\n")

import pytest


@pytest.fixture()
def fixture_b():
    return "b"
