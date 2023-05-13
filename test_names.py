# Names: Emily, Lizandro, Terral
# Brother Eisinger
# CSE 111
# Purpose: Writing and running test functions often help a software developer find mistakes in code. During this assignment, you will write three test functions. Then use pytest to run the test functions and use the output of pytest to help you find and fix errors in some program functions.
from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Emily", "Cordero") == "Cordero; Emily"
    assert make_full_name("Terral","Shrewsbury") == "Shrewsbury; Terral"
    assert make_full_name("Lizandro", "Vivanco") == "Vivanco; Lizandro"

def test_extract_family_name():
    assert extract_family_name("Cordero; Emily") == "Cordero"
    assert extract_family_name("Shrewsbury; Terral") == "Shrewsbury"
    assert extract_family_name("Vivanco; Lizandro") == "Vivanco"
    
def test_extract_given_name():
    assert extract_given_name("Cordero; Emily")== "Emily"
    assert extract_given_name("Shrewsbury; Terral")== "Terral"
    assert extract_given_name("Vivanco; Lizandro")== "Lizandro"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
