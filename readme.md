# 🚀 Parcours de Graphes : Implémentations Optimisées de DFS et BFS

Ce projet contient mes implémentations en Python des deux algorithmes fondamentaux de parcours de graphes : le **DFS (Depth-First Search)** et le **BFS (Breadth-First Search)**.

L'objectif était de maîtriser ces concepts clés de l'algorithmique, de comprendre la gestion de la mémoire (récursion vs file) et d'appliquer de bonnes pratiques de structuration de code.

---

## 📌 Fonctionnalités & Optimisations

### 1. DFS (Depth-First Search) avec Élagage

- **Concept :** Exploration en profondeur d'abord en utilisant la **récursion** et le **backtracking** (retour en arrière).
- **Optimisation (Pruning) :** Ajout d'une condition d'élagage. Dès que le chemin actuel devient plus long ou égal au meilleur chemin déjà trouvé, l'algorithme arrête d'explorer cette branche inutilement.
- **Cas d'usage :** Recherche exhaustive de tous les chemins possibles.

### 2. BFS (Breadth-First Search) pour le Chemin le Plus Court

- **Concept :** Exploration en largeur (niveau par niveau) en utilisant une file double (`collections.deque`).
- **Optimisation :** Utilisation d'un `set()` pour le suivi des nœuds visités afin de garantir des vérifications instantanées en $O(1)$.
- **Cas d'usage :** Garantie de trouver le chemin le plus court (en nombre d'arêtes) dès la première intersection avec la cible.

---

## 📂 Structure du Projet

Pour respecter le principe de responsabilité unique, le code a été modularisé :

- `DFS.py` : Contient l'algorithme DFS et sa logique de backtracking.
- `BFS.py` : Contient l'algorithme BFS et sa logique de file d'attente.
- `utils.py` : Regroupe les fonctions secondaires (construction du graphe de test, formatage du texte et affichage dynamique).
- `graph.py` : Définition de la classe Graphe et de ses méthodes (ajout de nœuds, d'arêtes et récupération des voisins).

---

## 🧠 Ce que j'ai appris

- **Maîtrise de la récursion :** Compréhension fine de la pile d'appels (_call stack_) et de la portée des variables avec le mot-clé `nonlocal` en Python.
- **Structures de données avancées :** Utilisation de `deque` pour optimiser le coût du `popleft()` en $O(1)$ à la place d'une liste classique en $O(N)$.
- **Refactoring & Clean Code :** Extraction des fonctions utilitaires pour rendre les fichiers principaux hautement lisibles et réutilisables.
