# Tutorial for regular expressions in python

# Symbols

#   .	Matches any single character except newline
#   ^	Anchors a match at the start of a string
#   $	Anchors a match at the end of a string
#   *	Matches zero or more repetitions
#   +	Matches one or more repetitions
#   ?	Matches zero or one repetition
#   {}	Matches an explicitly specified number of repetitions
#   []	Specifies a character class
#	examples: [0-9] - any number between 0 and 9
#	examples: [a-z] - any letter between a and z
#	examples: [a-zA-Z] - any lower or upper case letter
#   ()	Creates a group
#   |	Matches symbol on the left OR right side

# Reference
# https://realpython.com/regex-python/

import re
from colorama import Fore

txt = "The rain in Spainn"

# tests is regex succeeds on our text
def test(string):
    if(re.search(string, txt)):
        print(Fore.GREEN + "regex {%s} on text '%s' successful" % (string, txt))
    else:
        print(Fore.RED + "regex {%s} on text '%s' unsuccessful" % (string, txt))

# tests is regex succeeds on text argument
def test_custom(string, txt_arg):
    if(re.search(string, txt_arg)):
        print(Fore.GREEN + "regex {%s} on text '%s' successful" % (string, txt_arg))
    else:
        print(Fore.RED + "regex {%s} on text '%s' unsuccessful" % (string, txt_arg))

# examples -- text
test("the")
test("Thd")
test("")
test("the")
 
# examples -- .
test(".")
test("T.e")
test("T..")
test("The.rain.in.Spain")

# examples -- ^
test("^")
test("^T")
test("^t")
test("^a")

# examples -- $
test("$")
test("T$")
test("n$")
test(".$")

# examples -- *
test_custom("foo-*bar", "foobar")
test_custom("foo-*bar", "foo-bar")
test_custom("foo-*bar", "foo--bar")
test_custom("foo-*bar", "foo---------bar")

# examples -- +
test_custom("foo-+bar", "foobar")
test_custom("foo-+bar", "foo-bar")
test_custom("foo-+bar", "foo--bar")
test_custom("foo-+bar", "foo---------bar")

# examples -- ?
test_custom("foo-?bar", "foobar")
test_custom("foo-?bar", "foo-bar")
test_custom("foo-?bar", "foo--bar")
test_custom("foo-?bar", "foo---------bar")

# examples -- []
test_custom("[a-z]", "a")
test_custom("[a-z]", "1")
test_custom("[a-z]", "21432")
test_custom("[a-z]", "kasjdnf")
test_custom("[a-z]", "D")
test_custom("[a-zA-Z]", "D")
test_custom("[a-zA-Z]", "sdSAF")
test_custom("[abc]", "a")
test_custom("[abc]", "s")
test_custom("[az]", "s")
test_custom("[az]", "z")

# examples -- ()
test_custom("(abc)+", "abc")
test_custom("a(bc)+", "abc")
test_custom("a(bc)+", "abcbc")
test_custom("a(bc)+", "ac")
test_custom("a(bc)+", "bc")

# examples -- |
test_custom("(a|c)", "c")
test_custom("(a|c)", "a")
test_custom("(a|c)", "b")
test_custom("(ab|c)", "b")
test_custom("([0-9]|[a-z])", "b")
test_custom("([0-9]|[a-z])", "5")
test_custom("([0-9]|[a-z])", "B")

# examples -- {}
test_custom("a{3}", "B")
test_custom("a{3}", "aaa")
test_custom("a{3}", "a")
test_custom("a{3}", "")
test_custom("(abc){2}", "abc")
test_custom("(abc){2}", "abcab")
test_custom("(abc){2}", "abcabc")
test_custom("a{2,}", "aaa")
test_custom("a{2,}", "aaaaaaa")
test_custom("a{2,3}", "aaa")
test_custom("a{2,3}", "aaaaaaa")
test_custom("a{,3}", "aaaaaaa")
test_custom("a{,3}", "a")
test_custom("a{,3}", "")

##############################################################

# Questions

# 1.
# 
# Create a regex that succeeds on a string if it:
#
# 	a. at least one digit
# 	b. at least one lower case letter
# 	c. a digit or a letter
# 	d. begins with the word 'Cat'
# 	e. contains the word 'the'
# 	e. ends with an n
# 	f. contains either "aiden" or "anton"
# 	g. contains 2 occurrences of "ab"
# 	h. less than 4 occurrences of "abc"
# 	i. between 2 and 5 occurrences of "ab"
# 	j. starts and ends with the letter f

# Testing areas
