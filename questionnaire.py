import json

# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

# adaptation de la class Question
class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print("  " + self.titre)
        for i in range(len(self.choix)):
            choix_i = self.choix[i]
            print("  ", i+1, "-", choix_i[0])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        choix_utilisateur = self.choix[reponse_int-1]
        if choix_utilisateur[1]:
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, quizz):
        self.quizz = quizz
        self.recup_elements_quizz()
        self.generer_questions()
        print(f"""                  ---- QUIZZ ----  
                Titre: {self.titre}
                Catégorie: {self.categorie}
                Difficulté: {self.difficulte}
                Nombre de questions: {len(self.questions)}
                """)

    
    # metode pour recupérer les elements du fichier json
    def recup_elements_quizz(self):
        data_quizz = open (self.quizz, "r")
        data_json = data_quizz.read()
        data = json.loads(data_json)
        data_quizz.close()
        self.categorie = data["categorie"]
        self.titre = data["titre"]
        self.questions_dict = data["questions"]
        self.difficulte = data["difficulte"]

    # générer des objets Questions
    def generer_questions(self):
        self.questions = []
        for question in self.questions_dict:
            self.questions.append(Question(question["titre"], question["choix"]))

    def lancer(self):
        score = 0
        i = 0
        for question in self.questions:
            i += 1
            print(f"Question: {i}/{len(self.questions)} ")
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score
    

def demander_reponse_numerique(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


def generer_nom_quizz(nom, diff):
    return nom + "_" + diff + ".json"

"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

"""Questionnaire(
    (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()"""

quizz_noms = (
    "animaux_leschats",
    "arts_museedulouvre",
    "bandedessinnee_tintin",
    "cinema_alien",
    "cinema_starwars",
)
quizz_difficultes = ("debutant", "confirme", "expert")

print("""         BIENVENUE
    Améliorez votre culture """)

print("choisisez un quizz")
for i in range(len(quizz_noms)):
    print(f" {i+1} - {quizz_noms[i]}")
quizz_choix = demander_reponse_numerique(1, len(quizz_noms))
quizz_nom = quizz_noms[quizz_choix-1]

print("choisisez une difficulté")
for i in range(len(quizz_difficultes)):
    print(f" {i+1} - {quizz_difficultes[i]}")
quizz_choix_d = demander_reponse_numerique(1, len(quizz_difficultes))
quizz_difficulte = quizz_difficultes[quizz_choix_d-1]

quizz = generer_nom_quizz(quizz_nom, quizz_difficulte)

Questionnaire(quizz).lancer()


