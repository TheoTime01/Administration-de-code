#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code permet de faire des logging des différents fonctions
des packages utilisés
"""
import unittest
import logging
from Package_Calculator.Calculator import SimpleComplexCalculator


class test_sum(unittest.TestCase):
    """Cette classe permet de vérifier le bon fonctionnement de la méthode
    sum_complex de la classe SimpleCalculator"""
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleComplexCalculator()
        self.logger = logging.getLogger("Somme")

    def test_sum_2Tup(self):
        """somme de deux tuples, le résultat doit être [2,7]"""
        resultat = self.calculator.sum_complex([1,5], [1,2])
        self.assertEqual(resultat, [2,7])
        self.logger.warning("somme de deux tuples => OK") 

    def test_sumstr(self):
        """Somme de deux tuples contenant un entier et un caractère, le résultat 
        doit être ERROR"""
        resultat = self.calculator.sum_complex([2,7], ["2",7])
        self.assertEqual(resultat, "ERROR")
        self.logger.warning("somme tuples avec un entier et un caractère =>Erreur=>OK")
    
    def test_sumNeg(self):
        """Somme entre deux tuples contenant un entier positif et un entier négatif:
        le résultat doit être [0,-12]"""
        resultat = self.calculator.sum_complex([-1,-10], [1,-2])
        self.assertEqual(resultat, [0,-12])
        self.logger.warning("somme de deux tuples(entier positif, entier négatif)=>OK")


class test_sub(unittest.TestCase):
    """Cette classe permet de vérifier le bon focntionnement de la méthode
    susbtract de la classe SimpleCalculator"""
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleComplexCalculator()
        self.logger = logging.getLogger("Soustraction")

    def test_sub_2Tup(self):
        """Soustraction de deux tuples, le résultat doit être [0,3]"""
        resultat = self.calculator.substract_complex([1,5], [1,2])
        self.assertEqual(resultat, [0,3])
        self.logger.warning("soustraction de deux tuples => OK")

    def test_subStr(self):
        """Soustraction de deux tuples contenant un entier et un caractère, le résultat 
        doit être ERROR"""
        resultat = self.calculator.substract_complex(["1",5], [1,"2"])
        self.assertEqual(resultat, "ERROR")
        self.logger.warning("soustraction tuples avec un entier et un caractère =>Erreur=>OK")

    def test_sumNeg(self):
        """Soustraction entre deux tuples contenant un entier positif et un entier négatif
        le résultat doit être [2,-7]"""
        resultat = self.calculator.substract_complex([1,-5], [-1,2])
        self.assertEqual(resultat, [2,-7])
        self.logger.warning("soustraction de deux tuples(entier positif, entier négatif)=>OK")



class Testmultiply_complex(unittest.TestCase):

    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleComplexCalculator()
        self.logger = logging.getLogger("Multiplication")

    def test_mult2Tup(self):
        """Multiplication entre deux tuples, le résultat doit être [-9,7]"""
        resultat = self.calculator.multiply_complex([1,5], [1,2])
        self.assertEqual(resultat, [-9,7])
        self.logger.warning("multiplication de deux tuples => OK")

    def test_multStr(self):
        """"Multiplication de deux tuples contenant un entier et un caractère, le résultat
        doit être ERROR"""
        resultat = self.calculator.multiply_complex(["1",5], ["1",2])
        self.assertEqual(resultat, "ERROR")
        self.logger.warning("multiplication tuples avec un entier et un caractère =>Erreur=>OK")

    def test_multNeg(self):
        """Multiplication entre deux tuples contenant un entier positif et un entier négatif,
        le résultat doit être [9,7]"""
        resultat = self.calculator.multiply_complex([1,-5], [-1,2])
        self.assertEqual(resultat, [9,7])
        self.logger.warning("multiplication de deux tuples(entier positif, entier négatif)=>OK")


class testdivide_complex(unittest.TestCase):

    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleComplexCalculator()
        self.logger = logging.getLogger("Division")


    def test_div2Tup(self):
        """Division entre deux entier, on doit obtenir [2.2,0.6]"""
        resultat = self.calculator.divide_complex([1,5], [1,2])
        self.assertEqual(resultat, [2.2,0.6])
        self.logger.warning("division de deux tuples => OK")


    def test_div_Zero(self):
        """Division par 0, nous devons obtenir un message d'erreur"""
        resultat = self.calculator.divide_complex([1,5], [0,0])
        self.assertEqual(resultat, "vous avez essayé de diviser par zéro")
        self.logger.warning("Test division par 0 => OK")

    def test_divNeg(self):
        """Division d'un entre deux tuples contenant un entier positif et un entier négatif, 
        on doit obtenir [-2.2,0.6]"""
        resultat = self.calculator.divide_complex([1,-5], [-1,2])
        self.assertEqual(resultat, [-2.2,0.6])
        self.logger.warning("division de deux tuples(entier positif, entier négatif)=>OK")

    def test_divStr(self):
        """Division de deux tuples contenant un entier et un caractère, le résultat
        doit être ERROR"""
        resultat = self.calculator.divide_complex([1,5], [1,"2"])
        self.assertEqual(resultat, "ERROR")
        self.logger.warning("division tuples avec un entier et un caractère =>Erreur=>OK")



if __name__ == '__main__':
    unittest.main()



