#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 11

def test_code1():
    assert main.countB("bat") == 1, "error"
    assert main.countB("pool") == 0, "error"
    assert main.countB("bbbbbbbbbb") == 10, "error"

def test_code2():
    assert main.removeLast("shovel") == "shove", "error"
    assert main.removeLast("mask") == "mas", "error"
    assert main.removeLast("knights") == "knight", "error"

def test_code3():
    assert main.sumBetweenOdd(5, 13) == 27, "error"
    assert main.sumBetweenOdd(0, 10) == 25, "error"
    assert main.sumBetweenOdd(0, 0) == 0, "error"

def test_code4():
    assert main.firstLast("alpha") == True, "error"
    assert main.firstLast("ringworm") == False, "error"
    assert main.firstLast("enrage") == True, "error"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
