# find-random-number

A faire :
- Problème : le nom de l'utilisateur n'apparaît pas quand on clique sur suivant
    malgré que je set le nom après l'avoir émis à travers un signal et get avec une fonction
    Résolution : dans la fonction get j'update le label pour être sûr de l'avoir en 
    même temps.
- Problème : le nombre ne s'envoie pas quand j'appuie sur valider.
    Résolution : LE worker n'existait pas car il n'était pas un attribut de main_window
    et donc n'existait pas tout le long de l'existence de main_window.py.