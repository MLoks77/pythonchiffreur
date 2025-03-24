{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eec5e157-b1b3-43e7-91a8-6dc7bebc63ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DaG9BIg)y%Zxr\n"
     ]
    }
   ],
   "source": [
    "# on va ici utiliser secret au lieu de random pour des raisons de sécurité.Le module secrets permet de générer \n",
    "# des nombres aléatoires forts au sens de la cryptographie, adaptés à la gestion des mots de passe, \n",
    "# à l'authentification des comptes, à la gestion des jetons de sécurité et des secrets associés.\n",
    "\n",
    "import secrets\n",
    "import string\n",
    "\n",
    "# on va générer un mot de passe de 12 caractères\n",
    "# on va utiliser les lettres majuscules, minuscules, les chiffres et les caractères spéciaux\n",
    "# on va utiliser secrets.choice pour choisir un caractère aléatoire dans les différentes listes de caractères\n",
    "# on va utiliser la fonction join pour concaténer les caractères choisis\n",
    "\n",
    "# on va commencer par définir les différentes listes de caractères\n",
    "\n",
    "majuscules = string.ascii_uppercase\n",
    "minuscules = string.ascii_lowercase\n",
    "chiffres = string.digits\n",
    "speciaux = string.punctuation\n",
    "\n",
    "# on demande la longueur du mot de passe à l'utilisateur\n",
    "# on va utiliser la fonction int pour convertir la chaîne de caractères en entier\n",
    "# il est possible d'enlever x mais n'oubliez pas de changer x par une valeur dans la ligne avec le range()\n",
    "x = int(input(\"Entrez la longueur du mot de passe en chiffres: \"))\n",
    "\n",
    "# on va maintenant générer le mot de passe\n",
    "\n",
    "mot_de_passe = ''.join([secrets.choice(majuscules + minuscules + chiffres + speciaux) for i in range(x)])\n",
    "print(mot_de_passe)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d89a8d61-1a76-415c-9360-cb7e777b0415",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
