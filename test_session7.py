import pytest
import random
import string
import session7
import os
import inspect
import re

CHECK_FOR_FUNCT_IMPL = [
   
    'create_deck_cards_normal_function',
    'create_deck_cards_single_expression',
    'play_poker_game'


    ]

README_CONTENT_CHECK_FOR = [
    'vals',
    'create_deck_cards_normal_function',
    'create_deck_cards_single_expression',
    'Royal Flush',
    'Straight Flush',
    'Four Of A Kind',
    'Full House',
    'Flush',
    'Straight',
    'Three Of A Kind',
    'Two Pair',
    'One Pair',
    'suits',
]

# Tests related to readme
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Readme is not formatted properly"

# --------------------------------------------------------------------------------------
# Tests related Contents in session 4 file


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_implemented():
    code_lines = inspect.getsource(session7)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            print(c)
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL == True, 'You forgot to implement all functions! Try again!'
