# Cintainerize my ML model

Remember: in case you change the Pipfile: recreate requirements.txt via `pipenv requirements >> requirements.txt`

Use this as a submodule in your repo that defines the model (modelrepo).

```
modelrepo
│   ├── containerize/
│   ├── containerizeconfig.yaml
│   ├── other stuff from the modelrepo
```

The containerizeconfig.yaml makes sure the containerize subrepo knows what model to use.


