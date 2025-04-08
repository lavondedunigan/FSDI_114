{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c81765b-ddef-497f-a038-98bbe4fd4ff6",
   "metadata": {},
   "outputs": [],
   "source": [
    "Problem 1\n",
    "\n",
    "## Anagram Chech\n",
    "Create a function, `anagram _check`, that receives two arguments of type string and determines if these are anagrams of each other (criteria below), `True` if these are anagrams of each other, `False` otherwise.\n",
    "\n",
    "##Criteria\n",
    "Two strings are anagrams of each other if, and only if, all the criteria below are met:\n",
    "1. They must use contain the same amount of letters. \n",
    "2. They must use the same letters the same amount of times.\n",
    "\n",
    "## Examples\n",
    "\n",
    "heart and earth\n",
    "cars and scars\n",
    "rats and star\n",
    "\n",
    "## Note\n",
    "The three examples above are just examples, there may be other strings (many) that meet the criteria above.

# Psuedocode version

# define function "anagram_check" with params string1 and string2:
    string1 = string2 without spaces in lower case
    string2 = string2 without spaces in lower case
    if the length if string1 is not equal to the length of string2:
        return False
    otherwise:
        d1 = new dictionary
        d2 = new dictionary
        for each "number" in the range from 0 to the length of string1:
        if the character at position "number" in string1 is not in d1:
            add that character to d1 as a key, and set its value to 1      # indicating we've seen this character once
        otherwise:
            add 1 to the value associated with this character in d1         # indicating we've seen this character more than once
        if the character at position "number" in string2 is not in d2:
            add that character to d2 as a key, and set its value to 1      # indicating we've seen this character once
    otherwise:
            add 1 to the value associated with this character in d2         # indicating we've seen this character once     
    if d1 == d2
        return True
    otherwise:
        return False


   ]
 s1 = 'heart'
> s2 = catsi'>> s3 =ratsid>>> def is_anagram(s1, s2
...     if s1.lower() == s2.lower
...        return Fe
...     return sorted(s1.lower()) == sorted(s2.low) s1(Falses
   True
>>> is_anagraFalse 
Falsescars2'   dvivii'
>>> is_anaTruess23
Fastar>>     = 'evivi'
>>> is
print(anagramSolution3('rats', 'star'))
anagram(s1, s2)

  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
