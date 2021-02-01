# app/__init__.py
from flask import Flask, render_template, request

def create_app():
	app = Flask(__name__)
	#Route de base du site renvoie vers la homepage
	@app.route('/')
	def iot_homepage():
		return render_template('iot_homepage.html', message="")
	#Route de base avec une methode POST renvoie sur la homepage
	@app.route('/', methods=['POST'])
	def iot_homepage_post():
		if request.method == 'POST':
			message=""
			machine = request.form['machine']
			charge = int(request.form['cpu'])
			duree = int(request.form['time'])
			#=========================
			#Traitement des données Singularity
			#===========================
			if(duree!=0):
				message="CPU lancé à "+str(charge)+"% pendant "+str(duree)+" secondes sur la machine "+machine+"."
			else:
				message="Durée nulle, le CPU n'a pas été chargé."

			return render_template('iot_homepage.html', message=message)			
	#Route vers la page iot_containers avec methode GET
	@app.route('/iot_containers/', methods=['GET'])
	def iot_containers():
		if request.method == 'GET':
			res = request.args['machine']
			return render_template('iot_containers.html', machine=res)
		
	return app