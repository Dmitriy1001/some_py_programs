For your attention elementary python scripts
-------
OOP

Code examples using OOP

-------
are_texts_match

Returns true if the two texts match 70 percent or more.

-------
cryptography

Simple popular ciphers

-------
passwords

Contains password generators/validators

-------
IPv4_validator

Verifys the validity of IPv4 addresses.

-------
birding_codes

In the world of birding there are four-letter codes for the common names of birds. These codes are created by some simple rules:

    If the bird's name has only one word, the code takes the first four letters of that word.
    If the name is made up of two words, the code takes the first two letters of each word.
    If the name is made up of three words, the code is created by taking the first letter from the first two words and the first two letters from the third word.
    If the name is four words long, the code uses the first letter from all the words.

The function  takes an array of strings of common bird names from North America, and create the codes for those names.

-------
braces_status

The function checks the braces status in a string, and return True if all braces are properly closed, or False otherwise. Available types of brackets: (), [], {}.

Without using regex

-------
converts_all_cases

Changes current case to a given case.

-------

coordinates_validator

Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative. Coordinates can only contain digits, or one of the following symbols (including space after comma) __ -, . __

There should be no space between the minus "-" sign and the digit after it.

-------
is_password_strong

The function checks if the password meets the requirements.

1. 8 to 20 characters
2. Contains only the following symbols (and at least one symbol from each category):
      - capital letters,
      - lower case,
      - numbers
      - special characters from! @ # $% ^ & *?

-------
life_number

Accepts a date of birth (as a string) in the following format: "yyyy-mm-dd". The function returns a one digit integer between 1 and 9 which represents the Life Path Number of the given date of birth.

-------
look_n_say

The look and say sequence is a sequence in which each number is the result of a "look and say" operation on the previous element.
Considering for example the classical version startin with "1": ["1", "11", "21, "1211", "111221", ...]. You can see that the second element describes
the first as "1(times number)1", the third is "2(times number)1" describing the second, the fourth is "1(times number)2(and)1(times number)1" and so on.

The function takes a starting string (not necessarily the classical "1") and return the nth element of the series.

-------
numeric_template_formatter

The template might consist of other numbers, special characters or the like: replaces only alphabetical characters (both lower- and uppercase);
if the given or default string representing the number is shorter than the template, just repeats it to fill all the spaces.

-------
string_incrementer

If the string already ends with a number, the number be incremented by 1.
If the string does not end with a number, the number 1  be appended to the new string.
If the number has leading zeros the amount of digits  be considered.

-------
valid_number_british

In the UK mobile numbers begin with '07' followed by 9 other digits, e.g. '07454876120'.
Sometimes the number is preceded by the country code, the prefix '+44', which replaces the '0' in ‘07’, e.g. '+447454876120'.
And sometimes you will find numbers with dashes in-between digits or on either side, e.g. '+44--745---487-6120' or '-074-54-87-61-20-'. 
As you can see, dashes may be consecutive.

The function checks if the string is a valid UK mobile phone number or not

-------
vowel_shifting

The function shifts the vowels by "n" positions to the right.
(if n is negative - to the left)
"Position" means the vowel's position if taken as one item in a list of all vowels within the string.
A shift by 1 would mean, that every vowel shifts to the place of the next vowel.

Shifting over the edges of the text should continue at the other edge.
