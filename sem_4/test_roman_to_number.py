"""
TDD : turn roman to number test
"""

from roman_to_number import roman_to_number
from roman_to_number import input_user

def test_I_give_1():
    assert roman_to_number('I') == 1

def test_V_give_1():
    assert roman_to_number('V') == 5

def test_II_give_2():
    assert roman_to_number('II') == 2

def test_VI_give_6():
    assert roman_to_number('VI') == 6

def test_IV_give_4():
    assert roman_to_number('IV') == 4

def test_IV_give_9():
    assert roman_to_number('IX') == 9

def test_XIX_give_19():
    assert roman_to_number('XIX') == 19
    
# def test_input_is_roman():
#    roman_sample = ['I', 'II', 'III', 'IV', 'V']
#    assert input_user() in roman_sample