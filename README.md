# AdmCo_Partie_RenduFinal

__Ce code provient de mon gitlab[https://gitlab.com/Theo_Time01/admco_partie_rendufinal.git] où les pipelines sont excécutées__

## I. Objectif

L'objectif de ce projet est de créer un calculateur permettant de faire la somme, la différence, le produit et la division de 2 nombres complexes  sous forme de classes et packages, tout en assurant des tests fonctionnels et en ajoutant une intégration continue du projet.

## II. Organisation du projet

Voici l'arborescence simplifiée du projet :

    .
    ├── Package_Calculator
    │   ├── __init__.py
    │   ├── Calculator.py
    │   └── __pycache__
    │  
    ├── Package_Test
    │   ├── test.exo7.py
    │   ├── __init__.py
    │   └── __pycache__
    │
    ├── dist
    │   └── Package_Calculator_Complex-0.0.1.tar.gz  
    │   
    ├── README.md
    ├── requirements.txt
    └── setup.py

Le projet est donc composé des fichiers essentiels (README.md, .git), de fichiers permettant la bonne éxécution du projet (setup.py et requirements.txt), ainsi que deux packages:  

* Le premier est le package Calculator, qui possède un deuxième packages à l'intérieur : Package_Calculator
* Le deuxième est le Package_Test.  

#### Package_Calculator

C'est dans ce package qu'est définie le script Calculator.py qui définit sous forme d'une classe SimpleComplexCalculator des méthodes correspondant aux opérations élémentaires. Ce package apparaît donc comme une librairie qu'il faudra importer afin d'utiliser les méthodes pour calculer.  

#### Package_Test

C'est dans ce Package que sont géré tous les tests sur les méthodes du package Calculator, permettant de tester si les méthodes fonctionnent toujours bien malgré des modifications qu'on pourrait apporter au package Calculator. Les Tests sont gérés dans le script Calculator_test.py qui définit quatre classes (une par opérande), définissant chacune toutes les possibilités et les testants, afin de vérifier que les méthodes définies dans le package calculator fonctionnent dans tous les cas. Les tests sont effectué automatiquement à l'appel du script (soit appel direct soit appel par pytest), grâce au module unittest.  

## III. Importation des packages

Avant de pouvoir utiliser les packages ensembles, il faut importer les packages et leurs contenu, pour cela il existe trois méthodes différentes :

#### 1. PYTHONPATH

La première solution, relativement contraignante mais rapide à mettre en place et de placer le PYTHONPATH à la racine du projet, pour cela il faut ouvrir un terminal et se placer à la racine du projet et entrez la commande suivante :  

    export PYTHONPATH=$PYTHONPATH:'.'

#### 2. SETUP.PY

La deuxième solution est de créer un script python setup.py qui va permettre d'importer un package, pour cela il faut dans ce script indiquer le chemin d'accès à ce Package. Il faudra aussi dans certains cas définir un fichier texte requirements permettant de spécifier certaines versions de modules nécessaires à la bonne réalisation des actions.

    python setup.py sdist

    pytest

si un message d'erreur s'affiche et que le test ne s'effectue pas, alors, il faut créer un environnement virtuel et installer le fichier requirements pour pouvoir éxécuter les tests:

    sudo apt-get install python3-venv

    python3 -m venv tuto_venv

    source ./venv/bin/activate #activation du virtual env

    pip install -r requirements.txt

    python setup.py sdist

    pytest

#### 3. Test Pypi

voir Exercice 9

## IV.  Execution des Tests

Maintenant que les packages sont bien importés et installés, on peut effectuer les tests, pour cela il existe deux possiblités pour éxecutés les tests, le lancement du script Calculator_test.py et pytest.  

#### 1. Calculator_test.py

On peut appeler directement le script, il faut cependant pour cela avoir réglé le PYTHONPATH. Dans un terminal se placer à la racine du projet et entrer la commande :  

    python3 Package_Test/Calculator_test.py

#### 2. Pytest

La seconde méthode est d'entrer la commande `pytest` à la racine du projet. Cette commande va éxecuter tous les scripts python qui possède "test" dans leur nom.

## V. Intégration Continue

Le projet étant enrigstrer sur Gitlab, on peut utiliser toutes les options que le site propose. L'intégration continue fait partie de ces options possibles. Cela consiste à effectuer automatiquement des actions sur le projet à chaque push du projet sur Gitlab. Dans notre cas, trois étapes sont définies à chaque push du projet sur Gitlab:  

* Analyse de la syntaxe des codes.  
* Lancement de la commande Pytest.  
* Archivage disponible au téléchargement du package Calculator.  

Pour effectuer cela, il faut créer un fichier .yml qui définit les étapes à effectuer.  
Une fois un push effectué, on peut suivre dans l'onglet CI/CD / pipeline l'éxecution de l'intégration continue, et ainsi avoir l'information sur chacune des étapes si elles ont bien été effectuées sans difficultées.

## VI. Autres Dépôts du projet

Chaque aspect du projet a été traité indépendemment sous la forme de projets Gitlab indépendants. Pour plus d'information sur un aspect précis vous pouvez lire le README de l'exerice correspondant, les liens :  

* Exercice 1: <https://gitlab.com/tp1_ex1/TP1_ex1>
* Exercice 2  : <https://gitlab.com/Theo_Time01/admco.git>
* Exercice 3  : <https://gitlab.com/Theo_Time01/tp1_ex3>
* Exercice 4  : <https://gitlab.com/Theo_Time01/tp1_ex4>  
* Exercice 5  : <https://gitlab.com/Theo_Time01/tp1_ex5>  
* Exercice 6  : <https://gitlab.com/Theo_Time01/tp1_ex6>  
* Exercice 7  : <https://gitlab.com/Theo_Time01/tp1_ex7>  
* Exercice 8 : <https://gitlab.com/Theo_Time01/tp1_ex8>  
* Exercice 9 : <https://gitlab.com/Theo_Time01/pypi>  
* Exercice 10 : <https://gitlab.com/Theo_Time01/tp1_ex10>  

## VII. Ressources

<https://gitlab.com/fabricejumel/rendufinal_bouyssoux/-/tree/master/>  

PEP8 :  
<https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8>  
<https://python.doctor/page-pep-8-bonnes-pratiques-coder-python-apprendre>  
<https://python.sdv.univ-paris-diderot.fr/15_bonnes_pratiques/>  
<https://about.gitlab.com/handbook/business-ops/data-team/python-style-guide/>  
<https://blog.impulsebyingeniance.io/outils-et-bonnes-pratiques-pour-un-code-python-de-bonne-qualite/>  
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>  

Black : <https://python.doctor/page-black-code-formatter>  

Pylint : <https://realpython.com/python-code-quality/>  

Intégration continue : <https://gitlab.com/js-ci-training/ci-hero-unitarytest-python>  

TestPypi : <https://packaging.python.org/tutorials/packaging-projects/#packaging-your-project>  
