#2. Définissez la classe Product avec ses attributs cost, price, et marque dans la méthode init.
#3. Définissez la classe Meubles en tant que sous-classe de la classe Product, en utilisant le mot-clé "class Meubles(Product):".
#4. Définissez la méthode init de la classe Meubles en appelant la méthode init de la classe parent avec le super().init(cost, price, marque).
#5. Ajoutez les attributs spécifiques à la classe Meubles, tels que les matériaux, la couleur et les dimensions.
#6. Répétez les étapes 3 à 5 pour les classes Canape, Chaise et Table.
#7. Vous pouvez maintenant utiliser ces classes pour créer des instances de meubles spécifiques dans votre programme principal.

class Product:
    def__init__(self,cost,price,marque):
        self.cost = cost
        self.price = price
        self.marque = marque

class Meubles(Product):
    def__init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Canape(Product):
    def__init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Chaise(Product):
    def__init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions


class Table(Product):
    def__init__(self,cost,price,marque,matériaux,couleur,dimensions):
        super().__init__(cost,price,marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions