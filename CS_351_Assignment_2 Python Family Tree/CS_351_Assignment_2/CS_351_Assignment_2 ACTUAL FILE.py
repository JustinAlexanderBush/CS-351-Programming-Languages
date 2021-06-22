#This program will have different relationships between parents, children, siblings, aunts, uncles and grandparents
from kanren import run, eq, membero, var, conde, Relation, facts

x = var()

parent = Relation()
brother = Relation()
sister = Relation()
aunt = Relation()
uncle = Relation()
cousin = Relation()
grandparent = Relation()

facts(parent, ("Michael", "Justin"),
              ("Michael", "Mike Jr."),
              ("Frank Sr.", "Michael"),
              ("Frank Sr.", "Frank Jr."), 
              ("Frank Sr.", "Regina"),
              ("Frank Sr.", "Tony"),
              ("Tony", "Kimbery"),
              ("Tony", "Deanna"),
              ("Tony", "Little Tony"),
              ("Regina", "Ryan"),
              ("Regina", "Courtney"),
                                        )

facts(brother,  ("Justin", "Mike Jr."),
                ("Michael", "Frank Jr."),
                ("Michael", "Tony"),
                                    )

facts(sister, ("Regina", "Michael"),
              ("Regina", "Frank Jr."),
              ("Regina", "Tony"),
                                     )

facts(aunt, ("Regina", "Justin"),
            ("Regina", "Mike Jr."),
                                    )

facts(uncle, ("Tony", "Justin"),
             ("Tony", "Mike Jr."),
             ("Frank Jr.", "Justin"),
             ("Frank Jr.", "Mike Jr."),
                                    )

facts(cousin, ("Justin", "Ryan"),
              ("Justin", "Courtney"),
              ("Justin", "Kimberly"),
              ("Justin", "Deanna"),
              ("Justin", "Little Tony"),
                                        )

facts(grandparent, ("Frank Sr.", "Justin"),
                   ("Frank Sr.", "Mike Jr."),
                                               )

#print the parent of "Justin"
print ( run(1, x, parent(x, "Justin")) )         

#the two children of Michael
print ( run(2, x, parent("Michael", x)) )

#the two brothers of Michael
print ( run(2, x, brother("Michael", x)) )

#the sister of Frank Jr.
print ( run(1, x, sister(x, "Frank Jr.")) )

#the grandparent of Mike Jr.
print ( run(1, x, grandparent(x, "Mike Jr.")) )

#the cousins of Justin
print ( run(2, x, parent("Michael", x)) )

#the children of Grandpa Frank Sr.
print ( run(4, x, parent("Frank Sr.", x)) )

#the cousins of Justin
print ( run(5, x, cousin("Justin", x)) )