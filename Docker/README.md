
# Docker

## Utilisation container

lien :
https://www.docker.com/blog/containerized-python-development-part-1/
https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/6211458-lancez-votre-premier-conteneur-en-local

## Initialisation

```
cd Bureau/INFO943/
```

# Lancement container flask
```
docker build -t flaskproj .
docker run -d -p 5000:5000 flaskproj
```
