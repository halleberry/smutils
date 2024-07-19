# microsvc


1. [v0.1 mission's input, data and output, as well as, setup and versioning (git)](#v01-missions-input-data-and-output-as-well-as-setup-and-versioning--git-)

2. [v0.2 oas's version, info, paths, servers and components' schemas](#v02-oass-version-info-paths-servers-and-components-schemas)

3. [v0.3 model, domain, view, unit_of_work and errs](#v03-model-domain-view-unitofwork-and-errs)

4. [v0.4 repository, service, controller and web.app:api](#v04-repository-service-controller-and-webapp--api)

5. [v0.5 security & deployment](#v05-security--deployment)

6. [v1.0 release](#v10-release)





## v0.1 mission's input, data and output, as well as, setup and versioning (git)


Create directory, readme, .gitignore, setup, requirements and entrypoint then setup virtualenv and git.


- [create readme with mission's input, data and output](https://github.com/halleberry/smutils/blob/main/microsvc_README.md)

- [create .gitignore](https://github.com/halleberry/smutils/blob/main/.gitignore)

- [create setup.py](https://github.com/halleberry/smutils/blob/main/microsvc_setup.py)

- [create requirements](https://github.com/halleberry/smutils/blob/main/microsvc_requirements.txt)

- [create entrypoint](https://github.com/halleberry/smutils/blob/main/microsvc__main__.py)

- setup virtualenv: `$ deactivate && pipenv --rm && pipenv --python 3.9.17 && pipenv shell `

- setup git: `$ git init`

- save changes: `$ git add . &&  git commit -m "v0.1 init $(basename $(PWD)) microservice" `

- create version tag: `$ git tag v0.1 -m "$(git rev-parse --short HEAD) $(date) $(git log -1 --pretty=%B)" `


## v0.2 oas's version, info, paths, servers and components' schemas





## v0.3 model, domain, view, unit_of_work and errs

## v0.4 repository, service, controller and web.app:api

## v0.5 security & deployment

## v1.0 release












