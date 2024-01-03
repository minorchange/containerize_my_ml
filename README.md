# Containerize my ML model

Remember: in case you change the Pipfile: recreate requirements.txt via `pipenv requirements >> requirements.txt` (We want to use just pip in the container)
Use this as a submodule in your repo that defines the model (modelrepo).

```
modelrepo
│   ├── containerize_my_ml/
│   ├── containerizeconfig.yaml
│   ├── appname.md (optional)
│   ├── other stuff from the modelrepo
```

The containerizeconfig.yaml makes sure the containerize subrepo knows what model to use.

# Build container locally:

Either do `make build_and_run_locally` from the containerize_my_ml folder or execute this from the modelrepo:
```
docker build -f containerize_my_ml/Dockerfile -t nameofmyimage .  
docker run -it nameofmyimage
```

# Create a tarball containing the build image

Either do `make tarball` from the containerize_my_ml folder or call this from the modelrepo:
```
bash containerize_my_ml/create_tarball.sh
```

# Use Tarball

To use this tarball on any machine call:
```
docker load -i INSERT_THE_RESPECTIVE_NAME_HERE.tar.gz
```