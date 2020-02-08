# -*- coding: utf-8 -*-
from streamparse import Bolt, TicklessBatchingBolt, BatchingBolt


class ExampleStatelessBolt(Bolt):
    """Exemple de bolt sans état ni fenêtre.

    Étend la classe Bolt, attention à ne pas surcharger la méthode __init__(self).
    Le code d'initialisation est à placer dans initialize(self,strom_conf,context).
    """

    # Schéma de sortie du Bolt, ici un seul attribut appelé json
    outputs = ["json"]

    def initialize(self, strom_conf, context):
        """Initialise le bolt.

        Effectue le travail fait habituellement dans le constructeur.
        """
        self.str_to_append = "\n"

    def process(self, tup):
        """Traite un tuple."""
        value1 = tup.values[0]  # valeur de la première colonne du tuple
        result1 = value1 + self.str_to_append  # Histoire de faire un calcul
        # Émettre un nouveau tuple dont le contenu est donnée par la liste [result1]:
        self.emit([result1], anchors=[tup])


class ExampleStatelessWindowedBolt(TicklessBatchingBolt):
    """Bolt utilisant une fenêtre.

    Ce type de bolt accumule les tuples et déclenche un calcul à intervalles réguliers (15 secondes)).

    Dans cet exemple, le bolt calcule le nombre de messages de la fenêtre.
    """

    outputs = ["count"]
    secs_between_batches = 15  # Taille de la fenêtre en secondes

    def initialize(self, strom_conf, context):
        """Initialise le bolt.

        Effectue le travail fait habituellement dans le constructeur.
        """
        pass

    def process_batch(self, key, tuples):
        """Traite les tuples de la fenêtre.

        Attention, c'est cette méthode qu'il faut changer pour un bolt avec fenêtrage."""
        # Histoire de faire un calcul, ici le nombre de tuples dans la fenêtre:
        result = len(tuples)
        self.emit([result])


class ExampleStatefulBolt(Bolt):
    """Bolt conservant un état. 
    
    streamparse étant assez limité, cet état sera perdu en cas de redémarrage du bolt.
    
    Dans cet exemple, le bolt calcule les valeurs maximales et minimales du premier composant des tuples reçus.
    """

    outputs = ["min", "max"]

    def initialize(self, strom_conf, context):
        """Initialise le bolt.

        Effectue le travail fait habituellement dans le constructeur.
        """
        self.mini = None
        self.maxi = None

    def process(self, tup):
        """Traite un tuple."""
        tupval = tup.value[0]
        if self.mini is None or self.mini > tupval:
            self.mini = tupval
        if self.maxi is None or self.maxi < tupval:
            self.maxi = tupval
        self.emit([self.mini, self.maxi])


class ExampleStatefulWindowedBolt(TicklessBatchingBolt):
    """Bolt utilisant une fenêtre.

    Ce type de bolt accumule les tuples et déclenche un calcul à intervalles réguliers tout en conservant un état.
    streamparse étant assez limité, cet état sera perdu en cas de redémarrage du bolt.

    Dans cet exemple, le bolt calcul le nombre maximal de messages dans une fenêtre.
    """

    outputs = ["maxcount"]
    secs_between_batches = 15  # Taille de la fenêtre en secondes

    def initialize(self, strom_conf, context):
        """Initialise le bolt.

        Effectue le travail fait habituellement dans le constructeur.
        """
        self.maxcount = None

    def process_batch(self, key, tuples):
        """Traite les tuples de la fenêtre.

        Attention, c'est cette méthode qu'il faut changer pour un bolt avec fenêtrage."""
        # Histoire de faire un calcul, ici le nombre de tuples dans la fenêtre:
        count = len(tuples)
        if self.maxcount is None or self.maxcount < count:
            self.maxcount = count
        self.emit([self.maxcount])
