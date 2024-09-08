from textblob import TextBlob
from googletrans import Translator

# Initialiser le traducteur
translator = Translator()

# Boucle pour demander une saisie utilisateur
while True:
    texte = input("Saisissez un texte pour analyser le sentiment (ou tapez 'exit' pour quitter) : ")
    
    if texte.lower() == 'exit':
        print("Au revoir!")
        break
    
    try:
        # Traduire le texte en anglais
        traduction = translator.translate(texte, dest='en')
        texte_traduit = traduction.text

        # Analyse de sentiment sur le texte traduit
        blob = TextBlob(texte_traduit)
        sentiment = blob.sentiment.polarity  # Donne un score de -1 (négatif) à 1 (positif)

        # Affichage du résultat
        #print(f"Texte traduit: {texte_traduit}")
        if sentiment > 0:
            print("Sentiment positif")
        elif sentiment < 0:
            print("Sentiment négatif")
        else:
            print("Sentiment neutre")
    except Exception as e:
        print(f"Erreur lors de la traduction ou de l'analyse : {e}")