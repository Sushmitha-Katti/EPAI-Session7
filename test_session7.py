import pytest
import random
import string
import session7
import os
import inspect
import re
import string
import math

CHECK_FOR_FUNCT_IMPL = [
   
    'fiboacci_number_check',
    'add_numbers',
    'strip_vowel',
    'relu',
    'sigmoid',
    'shift_characters',
    'swear_word_check',
    'add_even_numbers_using_list',
    'biggest_printable_ascii_character',
    'add_every_third_number',
    'number_plates',
    'number_plates_arguments_accept',



    ]

README_CONTENT_CHECK_FOR = [
    'fiboacci_number_check',
    'add_numbers',
    'strip_vowel',
    'relu',
    'sigmoid',
    'shift_characters',
    'swear_word_check',
    'add_even_numbers_using_list',
    'biggest_printable_ascii_character',
    'add_every_third_number',
    'number_plates',
    'number_plates_arguments_accept',
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

def test_fibonacci_series():
    fib_num = (1,3,8,13,55)
    for i in fib_num:
        assert session7.fiboacci_number_check(i) == True, "Fibonacci implementation is not correct"

def test_add_numbers():
    a = [random.randint(1,30) for _ in range(5)]
    b = [random.randint(1,30) for _ in range(5)]
    c = []
    for  i,j in zip(a,b):
        
            if(i%2==0 and j%2!=0):
                c.append(i+j)
    result =  session7.add_numbers(a,b)
    assert result == c, "Add numbers is improper"


def test_strip_vowel():
    inpt = "".join([random.choice(string.ascii_letters) for _ in range(5)])
    vowels = ['a', 'e', 'i', 'o','u']
    result = ""
    for i in inpt:
        if(i not in vowels):
            result = result+i
    assert result == session7.strip_vowel(inpt), "Function implementation has a problem"


    

def test_relu():
    a = [random.randint(-10,10) for _ in range(5)]
    result = []
    for i in a:
        if(i<0):
            result.append(0)
        else:
            result.append(i)
    assert result == session7.relu(a), "Function implementation has a problem"
def test_sigmoid():
    a = [random.randint(-10,10) for _ in range(5)]
    result = []
    for i in a:
        result.append(1 / (1 + math.exp(-i)))
    assert result == session7.sigmoid(a), "Function implementation has a problem"

def test_shift_characters():
    inpt = ['xyz', 'abc']
    result = ['cde', 'fgh']
    for i in range(2):
        assert result[i] == session7.shift_characters(inpt[i]), "Shifting is Wrong!!"


def test_swear_words():
    paragraph = "The chair in the corner where it had been for over 25 years. The only difference was there was someone actually sitting in it. How long had it been since someone had done that? Ten years or more he imagined. Yet there was no denying the presence in the chair now."
    assert False == session7.swear_word_check(paragraph), "There are no swear words exist!!!"


def number_plates_arguments_accept():
    with pytest.raises(TypeError):
        session7.number_plates_partial("DA", 4444), "Partial Function is not working properly!!"
    

