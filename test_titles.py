import pytest
from titles import get_redirect

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







