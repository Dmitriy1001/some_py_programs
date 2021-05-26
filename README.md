For your attention elementary python scripts
-------
are_texts_match

Returns true if the two texts match 70 percent or more.

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
is_password_strong

The function checks if the password meets the requirements.

1. 8 to 20 characters
2. Contains only the following symbols (and at least one symbol from each category):
      - capital letters,
      - lower case,
      - numbers
      - special characters from! @ # $% ^ & *?

-------
look_n_say

The look and say sequence is a sequence in which each number is the result of a "look and say" operation on the previous element.
Considering for example the classical version startin with "1": ["1", "11", "21, "1211", "111221", ...]. You can see that the second element describes
the first as "1(times number)1", the third is "2(times number)1" describing the second, the fourth is "1(times number)2(and)1(times number)1" and so on.

The function takes a starting string (not necessarily the classical "1") and return the nth element of the series.

-------
valid_number_british

In the UK mobile numbers begin with '07' followed by 9 other digits, e.g. '07454876120'.
Sometimes the number is preceded by the country code, the prefix '+44', which replaces the '0' in ‘07’, e.g. '+447454876120'.
And sometimes you will find numbers with dashes in-between digits or on either side, e.g. '+44--745---487-6120' or '-074-54-87-61-20-'. 
As you can see, dashes may be consecutive.

The function checks if the string is a valid UK mobile phone number or not

-------
