#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code définit une classe qui fait des opérations arithmétiques avec des complexes
"""


class SimpleComplexCalculator:
    """simple classe model, SimpleCalculator class"""

    def __init__(self):
        """constructeur de la classe"""

    # Fonction somme
    def sum_complex(self, complex_1, complex_2):
        """On récupère les deux attributs de l'objet et on
        effectue la somme complexe"""
        if (
                isinstance(complex_1[0], int)
                and isinstance(complex_2[0], int)
                and isinstance(complex_1[1], int)
                and isinstance(complex_2[1], int)
        ):
            return [
                complex_1[0] + complex_2[0],
                complex_1[1] + complex_2[1],
            ]
        return "ERROR"
            

    # Fonction soustraction
    def substract_complex(self, complex_1, complex_2):
        """On récupère les deux attributs de l'objet et on
        effectue la soustraction complexe"""
        if (
                isinstance(complex_1[0], int)
                and isinstance(complex_2[0], int)
                and isinstance(complex_1[1], int)
                and isinstance(complex_2[1], int)
        ):
            return [
                complex_1[0] - complex_2[0],
                complex_1[1] - complex_2[1],
            ]
        return "ERROR"

    # Fonction multiplier
    def multiply_complex(self, complex_1, complex_2):
        """On récupère les deux attributs de l'objet et on
        effectue la multiplication complexe"""
        if (
                isinstance(complex_1[0], int)
                and isinstance(complex_2[0], int)
                and isinstance(complex_1[1], int)
                and isinstance(complex_2[1], int)
        ):
            return [
                complex_1[0] * complex_2[0]
                - complex_1[1] * complex_2[1],
                complex_1[0] * complex_2[1]
                + complex_1[1] * complex_2[0],
            ]
        return "ERROR"

    # Fonction diviser
    def divide_complex(self, complex_1, complex_2):
        """On récupère les deux attributs de l'objet et
        on effectue la division complexe"""
        if (
                isinstance(complex_1[0], int)
                and isinstance(complex_2[0], int)
                and isinstance(complex_1[1], int)
                and isinstance(complex_2[1], int)
        ):
            if (
                complex_1[0] != 0
                and complex_2[0] != 0
                and complex_1[1] != 0
                and complex_2[1] != 0
            ):  # verification qu'aucun des attributs n'est nul
                real = (
                    complex_1[0] * complex_2[0]
                    + complex_1[1] * complex_2[1]
                ) / (complex_2[0] ** 2 + complex_2[1] ** 2)
                imag = (
                    complex_1[1] * complex_2[0]
                    - complex_1[0] * complex_2[1]
                ) / (complex_2[0] ** 2 + complex_2[1] ** 2)
                return [real, imag]
            return "vous avez essayé de diviser par zéro"
        return "ERROR"
