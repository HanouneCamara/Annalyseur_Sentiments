from textblob import TextBlob
import nltk

nltk.download('punkt_tab')


# Boucle pour demander une saisie utilisateur
while True:
    texte = input("Saisissez un texte pour analyser le sentiment (ou tapez 'exit' pour quitter) : ")
    
    if texte.lower() == 'exit':
        print("Au revoir!")
        break
    # Créer un objet TextBlob avec le texte saisi
    blob = TextBlob(texte)
    
    # Analyse de sentiment
    sentiment = blob.sentiment.polarity  # Donne un score de -1 (négatif) à 1 (positif)
 
     # Affichage du résultat
    if sentiment > 0:
        print("Sentiment positif")
    elif sentiment < 0:
        print("Sentiment négatif")
    else:
        print("Sentiment neutre")