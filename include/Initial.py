
import src.Query as Q
# chemin absolu du module complet si il n'est pas dans le même dossier 
# self.aux : chemin absolu du fichier à appeler (sous linux)

class Form:
    def __init__(self,verb):
        self.verb = verb
        self.subject_pronouns = ["I","You","He/She/It","We","You","They"]
        self.ending = ("o","ch","sh","ss","x","z")
        self.past = Q.is_from("past",self.verb)
        self.pp = Q.is_from("pp",self.verb)
        self.check = Q.is_equal_to(self.verb) # check if self.verb is already in irregular_verbs
        self.aux = (
                
           "data/tobe.data",
           "data/tohave.data",
           "data/todo.data",
           "data/topastbe.data",
           " had",
           " did",
           "'ll",
           " won't",
           "'d",
           " wouldn't",
           "'d have",
           " wouldn't have",
           " will",
           " would",
           " would have"
        )
