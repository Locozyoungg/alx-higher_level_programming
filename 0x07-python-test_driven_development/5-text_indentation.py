#!/usr/bin/python3
"""
Module for text indentation.

This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :.

"""

def text_indentation(text):
    """
    Print a text with 2 new lines after each ., ? and : characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []

    for char in text:
        lines.append(char)
        if char in separators:
            lines.append('\n\n')

    result = ''.join(lines).split('\n')

    for line in result:
        print(line.strip())

if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

