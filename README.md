# Containerize my ML model

Remember: in case you change the Pipfile: recreate requirements.txt via `pipenv requirements >> requirements.txt` (We want to use just pip in the container)
Use this as a submodule in your repo that defines the model (modelrepo).

```
modelrepo
│   ├── containerize_my_ml/
│   ├── containerizeconfig.yaml
│   ├── other stuff from the modelrepo
```

The containerizeconfig.yaml makes sure the containerize subrepo knows what model to use.

# Build container locally:

Execute this from the modelrepo, not from the containerize_my_ml folder
```
docker build -f containerize_my_ml/Dockerfile -t nameofmyimage .  
docker run -it nameofmyimage
```
