#!/usr/bin/env python
"""
Een script waarbij je om input vraagt achter een willekeurig woord en waarbij het script
het woord achterstevoren weergeeft.
"""


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"

#vraagt om de getallen in te geven
word = input('Enter word: ')
reversed=''.join(reversed(word))
print(reversed)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
