import pytest
from titles import get_redirect
from titles import more_redirects

def test_get_redirect():
    items = ['horse', 'wagon', 'money']
    
    selection_one = 'horse'
    result = get_redirect(items, selection_one)
    assert result == '/woohoo'

    selection_two = 'wagon'
    result = get_redirect(items, selection_two)
    assert result == '/ohdamn'

    selection_three = 'money'
    result = get_redirect(items, selection_three)
    assert result == '/awjeez'

def test_more_redirects():
    aim = ['left', 'right', 'center']

    aim_left = 'left'
    result = more_redirects(aim, aim_left)
    assert result == '/morir'

    aim_right = 'right'
    result = more_redirects(aim, aim_right)
    assert result == '/mierda'

    aim_center = 'center'
    result = more_redirects(aim, aim_center)
    assert result == '/ganar'







