from Parenthesis_Checker import parenthesis_checker


def test_parenthesis_checker():
    assert parenthesis_checker("[{([])}]")
    assert parenthesis_checker("")
    assert parenthesis_checker("((([{([])}])))")
    assert not parenthesis_checker("(([{([])}])))")
    assert not parenthesis_checker("((([{([])}]))")
    assert not parenthesis_checker("([)]")
    assert not parenthesis_checker("[(])")

