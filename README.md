# CHECKDB Tool 🛠️

# Description 📄

Le CHECKDB Tool est un outil de recherche de texte conçu pour parcourir les fichiers .txt dans un répertoire spécifié et rechercher des occurrences d'une chaîne donnée. Il est développé en Python et utilise des commandes

spécifiques au système d'exploitation pour fonctionner sur différentes plateformes (Windows, Linux, MacOS).

# Fonctionnalités ✨

Effacement de l'écran : Nettoie l'écran avant d'afficher de nouvelles informations, en fonction du système d'exploitation.

Affichage de bannière : Affiche une bannière personnalisée avec des options de menu.

Recherche de texte : Permet de rechercher une chaîne de texte spécifique dans tous les fichiers .txt d'un répertoire donné.

Affichage des résultats : Affiche les résultats de la recherche avec les détails du fichier, du numéro de ligne et de la ligne contenant la chaîne recherchée.

# Prérequis 📋

Python 3.x installé

ripgrep installé et accessible via la commande rg

Fonctionnement confirmé sur Windows, Linux, et MacOS

# Installation 🛠️

Clonez le dépôt ou téléchargez les fichiers sources.

Assurez-vous d'avoir Python 3.x installé sur votre machine.

Installez ripgrep en lançans votre terminale en administrateur puis executer cette commande.

windows : 
```
choco install ripgrep
```

macos : 
```
brew install ripgrep
```
Linux : 
```
sudo apt-get install ripgrep
```

# Utilisation 🚀

Ouvrez un terminal ou une invite de commande.

Naviguez jusqu'au répertoire contenant le fichier checkdb.py.

Exécutez le script avec la commande :

python checkdb.py

Le menu principal apparaîtra avec les options suivantes :

[1] SEARCH 🔍 : Pour effectuer une recherche de texte dans les fichiers .txt.

[0] Exit ❌ : Pour quitter l'application.

# Exemple d'utilisation 📚

Sélectionnez l'option [1] SEARCH 🔍.

Entrez la chaîne de recherche lorsque vous y êtes invité.

Entrez le chemin du répertoire contenant les fichiers .txt.

Les résultats s'afficheront à l'écran, indiquant le fichier, le numéro de ligne et la ligne où la chaîne a été trouvée.

# Note 📝

L'outil utilise ripgrep pour effectuer la recherche sur les systèmes d'exploitation supportés. Assurez-vous que ripgrep est disponible et fonctionnel sur votre machine.

# Licence 📝

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer, à condition de conserver la notice de copyright d'origine.

# Auteurs 👥  

Développé par : Himmler / <@1131256234440392817>

Communauté : https://discord.gg/searchhub
