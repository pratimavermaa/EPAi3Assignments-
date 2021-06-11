import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import time
import part1
import part2

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_part2_readme_exists():
    """ A. failure_message: Found README.md file
        B. Once you write this test, it needs to print the filures_message for failing this test.
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_part2_readme_300_words():
    """ A. failures_message: Make your README.md file interesting! Add atleast 300 words
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"


def test_part2_readme_proper_description():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_part2_readme_file_for_more_than_10_hashes():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_part2_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
        A.  failures_message_1: Your script contains misplaced indentations
            failures_message_2: Your code indentation does not follow PEP8 guidelines
        B. Once you write this test, it needs to print the failures_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_part1_function_name_had_cap_letter():
    """ A. failures_message: You have used Capital letter(s) in your function names
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_generate_deck_using_Normal_func():
    assert part1.genrate_deck(suits,value) == ['2spades', '3spades', '4spades', '5spades', '6spades', '7spades', '8spades', 
    '9spades', '10spades', 'jackspades', 'queenspades', 'kingspades', 'acespades', '2clubs', '3clubs', '4clubs', '5clubs', '6clubs', '7clubs', '8clubs', '9clubs', '10clubs', 'jackclubs', 'queenclubs', 'kingclubs', 'aceclubs', '2hearts', '3hearts', '4hearts', '5hearts', '6hearts', '7hearts', '8hearts', '9hearts', '10hearts', 'jackhearts', 'queenhearts', 'kinghearts', 'acehearts', '2diamonds', '3diamonds', '4diamonds', '5diamonds', '6diamonds', '7diamonds', '8diamonds', 
    '9diamonds', '10diamonds', 'jackdiamonds', 'queendiamonds', 'kingdiamonds', 'acediamonds'], 'Deck is not generated properly'


def test_generate_deck_lambda_map_zip():
    assert part1.generate_deck_using_lambda_map_zip(suits,value) == ['2spades', '3clubs', '4hearts', '5diamonds', '6spades',
     '7clubs', '8hearts', '9diamonds', '10spades', 'jackclubs', 'queenhearts', 'kingdiamonds', 'acespades', '2clubs', '3hearts', '4diamonds', '5spades', '6clubs', '7hearts', '8diamonds', '9spades', '10clubs', 'jackhearts', 'queendiamonds', 'kingspades', 'aceclubs', '2hearts', '3diamonds', '4spades', '5clubs', '6hearts', '7diamonds', '8spades', '9clubs', '10hearts', 'jackdiamonds', 'queenspades', 'kingclubs', 'acehearts', '2diamonds', '3spades', '4clubs', '5hearts', '6diamonds', '7spades',
     '8clubs', '9hearts', '10diamonds', 'jackspades', 'queenclubs', 'kinghearts', 'acediamonds'], 'Deck is not generated properly'
     
def test_fib_check():
    assert part2.fib_check(55) == True, "functionality not working as expected"

def test_even_odd():
    assert part2.even_odd([2,4,6,9,10,22,33], [12,4,7,16,15,25,26]) == [13, 25, 47], "functionality not working as expected"

def test_strip_vowel_str():
    assert part2.strip_vowel_str('python') == 'pythn', "functionality not working as expected"

def test_relu_activation():
    assert part2.relu_activation(-3, -2, -1, 0, 1, 2, 3.5]) == [0, 0, 0, 0, 1, 2, 3.5], "functionality not working as expected"

def test_sigmoid_activation():
    assert part2.sigmoid_activation([-3, -2, -1, 0, 1, 2, 3.5]) == [0.05, 0.12, 0.27, 0.5, 0.73, 0.88, 0.97], "functionality not working as expected"

def test_shift_5_char():
    assert part2.shift_5_char('abcde') == 'fghij', "functionality not working as expected"
    
def test_profane_filter():
    assert part2.test_profane_filter('Fuck') == True, "functionality not working as expected"

def test_add_even_num():
    assert part2.add_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30, "functionality not working as expected"

def test_big_char_str():
    assert part2.big_char_str('Welcome') == 'o', "functionality not working as expected"

def test_add_third_num():
    assert part2.add_third_num([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18, "functionality not working as expected"

def test_num_plate():
    assert part2.num_plate() != ['KA29QD1029', 'KA22IU3699', 'KA88VT3796', 'KA77VK7525', 'KA26NC7952', 'KA62IB6018', 'KA84IH9472', 'KA69UT6490',
                                 'KA98PP3681', 'KA42QI1845', 'KA27ID7921', 'KA46JT4251', 'KA96BW1429', 'KA47HT8486', 'KA50BN1069'], "functionality not working as expected"

