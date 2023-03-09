#Fichier python crée en copiant le fichier 01.class_tree_exo.md et le collant dans 03.class_tree et le renommant .py au lieu de .md
'''- Nous allons a présent charger de nouvelles données,
- prenez le temps de lire ATTENTIVEMENT le contenu du nouveau fichier json_data
- En utilisant le code précédemment réalisé, générez un arbre qui en affiche le contenu
- Attention : N'afficher que les Noeuds possédant des sous-classes
- Autrement dit, il ne faut pas inclure les attributs des Produits, mais seulement les catégories de produit.
- Pour ce faire, il ne faut inclure que les noeuds qui ne sont pas terminaux
- Les noeuds sans enfants doivent être skippés.'''

#- voici le Pseudo code pour vous aider à rédiger le code.


# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree

# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
''' la fonction json_dict_from_file() reste inchangée.'''
import os

def json_dict_from_file():
    """
    Cette fonction ouvre et charge les données JSON du fichier
    dans un dictionnaire Python.

    Returns:
        dict: le dictionnaire Python contenant les données JSON du fichier
    """
    # Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    
    # il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)

    return json_dict

##############################################################################################################
# Fonction pour créer un arbre à partir d'un dictionnaire Python
def create_tree_from_dict(json_dict):
   # Créer un nouvel arbre

    tree_ctfd = Tree()
   # Créer le noeud racine pour l'arbre
    tree_ctfd.create_node(tag="Product Classes Hierarchy", identifier="racine")
    parent_node_id = "racine"
    # Parcourir récursivement le dictionnaire Python pour créer les noeuds de l'arbre (fonction ci dessous)
    tree_ctfd = recursive_tree_from_json(tree_ctfd, json_dict, parent_node_id)
   # Retourner l'arbre
    return tree_ctfd
##############################################################################################################
'''def create_tree_from_dict(tree, parent_node_id, parent_dict):'''
"""
    Cette fonction crée un arbre à partir d'un dictionnaire.
    Elle est appelée récursivement pour chaque sous-dictionnaire.

    Args:
        tree (Tree): un objet Tree de la bibliothèque treelib pour représenter l'arbre
        parent_node_id (str): l'identifiant du noeud parent dans l'arbre
        parent_dict (dict): le dictionnaire Python contenant les données à insérer dans l'arbre
    """
"""
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
       # else:
            ## Créer un nouveau noeud pour la feuille courante du dictionnaire
            #leaf_node_id = f"{parent_node_id}.{key}"
            #tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)
"""
###########################################################################################################
# Fonction récursive pour parcourir un dictionnaire Python et créer des noeuds dans un arbre
def recursive_tree_from_json(tree_rtfj, json_dict, parent_node_id):
        for key, value in json_dict.items():
            if isinstance(value, dict):
                if key!="subclasses": #Ajout de condition if
                    new_node_id = f"{parent_node_id}.{key}"
                    tree_rtfj.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
                else:                 #Ajout de condition else
                     new_node_id = parent_node_id                
            
                # Créer récursivement le sous-arbre pour le dictionnaire courant
                tree_rtfj = recursive_tree_from_json(tree_rtfj, value, new_node_id)
        return tree_rtfj
############################################################################################################
   # Pour chaque clé (class_name) et valeur (class_attrs) dans le dictionnaire :
    #    Créer un nouveau noeud pour la clé courante du dictionnaire (nom de la classe)
     #   Ajouter le nouveau noeud en tant que fils du noeud parent

      #  Si "subclasses" est dans les attributs de la classe en cours (soit : valeur(class_attrs))
       #     Appeler récursivement la fonction pour créer les sous-noeuds de ce dictionnaire

############################################################################################################
# Fonction principale
def main():
    #Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict = json_dict_from_file()
    #Créer l'arbre à partir du dictionnaire Python
    my_tree = create_tree_from_dict(json_dict)
    #Afficher l'arbre de classes
    my_tree.show()

# Code principal
if __name__ == '__main__':
    # Appeler la fonction principale
    main()
#############################################################################################################

'''

Output:


Product Classes Hierarchy
└── Product
    └── Biens Consommation
        ├── Articles Menagers
        │   ├── Appareils Electromenagers
        │   │   ├── Lave-linge
        │   │   ├── Lave-vaisselle
        │   │   └── Refrigerateur
        │   ├── Meubles
        │   │   ├── Canape
        │   │   ├── Chaise
        │   │   └── Table
        │   └── Ustensiles Cuisine
        │       ├── Batterie Cuisine
        │       └── Casserole
        └── Habillement
            ├── Casquette
            ├── Chaussures
            └── Vetements
                ├── Haut
                ├── Pantalon
                └── Robe
'''
