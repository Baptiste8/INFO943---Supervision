Le site Web est lancé via le micro framework FLASK.
Pour l'installer correctement, suivez les étapes suivantes:
-Ouvrir l'invite de commande
-Se placer dans le dossier où l'on veut sauvegarder le site (ex: "flask_project")
-Vérifier que la version 3 de python est installé (sinon l'installer):
	$ python3
-Créer un environnement virtuel (flask_project/env) :
	$ python3 -m venv env
-Activer l'environnement :
	$ source env/bin/activate
-Installer FLASK :
	$ pip install Flask
-Copier le dossier "app" dans le dossier projet (flask_project/app)
-Lancer l'application depuis le dossier "flask_project":
	$ export FLASK_APP=app
	$ FLASK_ENV=development
	$ flask run

Attention, le serveur est lancé en mode développeur !
Vous pouvez naviguer sur le site en vous randant à l'adresse indiqué : "Running on http://ip_adress"
Probablement : http://127.0.0.1:5000/