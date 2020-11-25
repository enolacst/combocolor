# combocolor
programmation :

Dans la variante simplifiée proposée dans le cadre du projet, le jeu se limite à 2 joueurs possédant chacun 2 couleurs 
(rouge et bleu pour le joueur A, vert et jaune pour le joueur B). De plus, le plateau de jeu est une simple grille composée de 24 zones de 5 cases chacune 
(cf. image ci-dessus). Chaque zone est taggée avec l'un des trois types de labels permettant d'identifier la valeur de la zone pour le décompte final des points : 
 - un label bleu correspond à des points additifs, 
 - un label rouge à des points soustractifs 
 - label vert à des points multiplicatifs. 
 Les scores se calculent par couleur: on effectue le total des points bleus auxquels on retranche le total des points rouges, 
 et on multiplie le résultat obtenu par le total des points verts. 
Le score global de chaque joueur est défini à tout moment comme le produit (et non pas la somme) des scores correspondants à ses deux couleurs. 
C'est évidemment le programme qui doit se charger à chaque tour de jeu, du calcul et de l'affichage de l'évolution des scores.

On fournit une archive ZIP contenant les images de 6 plateaux de jeu différents, ainsi qu'un encodage de ces plateaux sous la forme de 6 fichiers texte, 
permettant d'identifier la nature des labels de score pour chacune des cases. Comme pour le projet précédent, il faudra créer une (ou plusieurs) classe(s) pour le noyau du jeu, 
permettant de modéliser le jeu de manière abstraite, puis une (ou plusieurs) classe(s) pour l'interface graphique qui mettra en oeuvre la visualisation du plateau de jeu et la gestion des actions des deux joueurs. 
Pour le coloriage des zones lors des tours de jeu, le plus simple est d'utiliser la bibliothèque Pillow qui fournit de nombreux algorithmes de traitement d'images, et en particulier, 
une fonction floodfill qui permet de remplir une zone homogène d'une image avec une couleur spécifiée.
