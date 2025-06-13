import ...
from ...

@pytest.fixture
...
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize([?], testcases)
...
    assert solution.isMatch(s, p) == expected

"""
@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch() == 
"""
