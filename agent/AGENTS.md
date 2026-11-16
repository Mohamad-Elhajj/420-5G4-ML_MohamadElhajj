# AGENTS.md

## Portée

Ce dossier contient uniquement l'application C++ `bibliotheque`. Les notebooks Python des dossiers parents `apprentissage/` et `analyse_image/` ne concernent pas ce périmètre. Conserver les textes affichés, messages et commentaires en français.

## Compiler et exécuter

Depuis `agent/` :

```bash
cmake -S . -B build
cmake --build build -j
./build/bibliotheque -d data
```

- Toujours fournir `-d` ou `--data-dir` : sans cette option, les chemins de fichiers sont vides et la sauvegarde échoue.
- Le répertoire passé à `-d` doit contenir `books.txt` et `users.txt`.
- L'application est interactive et terminal-only. Le choix `0` sauvegarde puis quitte ; le choix `13` crée des fichiers `.backup`.
- Pour un test sans modifier les données suivies, copier `data/` dans un répertoire temporaire et lancer avec `-d <temporaire>`.
- Il n'y a ni tests, ni linter, ni CI. Vérifier une modification par la compilation, puis par une exécution avec des données temporaires.

## Build

- `CMakeLists.txt` globbe `*.cpp` : relancer CMake après ajout ou suppression d'un fichier source.
- Le projet exige CMake >= 3.21 et compile en C++17 avec `-Wall -Wextra -Wpedantic`.
- Le binaire produit est `build/bibliotheque` ; `build/*` est ignoré par `agent/.gitignore`.
- Le devcontainer `agent/.devcontainer` installe CMake 3.22.2. Son montage X11 est inutile pour cette application en terminal.

## Format des données

Les champs sont séparés sans échappement ; ne pas introduire le séparateur dans une valeur.

- `books.txt` : `titre|auteur|isbn|1-ou-0|idEmprunteur`
- `users.txt` : `nom|id|isbn1,isbn2`

Les données sont chargées au démarrage et sauvegardées uniquement via le menu `12` ou à la sortie avec `0`.
