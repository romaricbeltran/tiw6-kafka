Kafka :
 - Il met un listener sur 1 fichier précis, on considère que c'est le fichier de base qu'on va récupérer par le script Python
   - On met le listener 1 fois, donc le nom du fichier ne doit pas changer ?
   - Le fichier doit être remplacé ou bien le contenu remplacé seulement ?
 - Il envoi a storm les changements dans le fichier
   - Est ce qu'il peut faire un traitement dessus ? Lucas avait parler de script python 
   - Est ce qu'il envoi juste les nouveau changement ou bien tous le fichier générer ? 
 - Envoi de la ligne au format JSON ? (je dois préciser le format d'entrer et de sortie de kafka sur storm)

Storm :
 - Il traite 1 ligne par 1 ligne car kafka envoi 1 ligne à chaque fois
 - Faire un traitement qui se fait ligne par ligne, en incrémentale
 - Output sur kafka de la ligne traité, on peut faire de multiple output, dont un output vers un nouveau storm via kafka (on utilisera ça pour la classification, le storm qui fera la classification pourra stocker des données dasn des variables (statefull), pas besoin de lire un fichier contenant le résultat précédent)
 