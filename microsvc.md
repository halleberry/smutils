# microsvc


1. [v0.1.0 mission's input, data and output, as well as, setup and versioning (git)](#v010-missions-input-data-and-output-as-well-as-setup-and-versioning--git-)

2. [v0.2.0 oas's version, info, paths, servers and components' schemas](#v020-oass-version-info-paths-servers-and-components-schemas)

3. [v0.3.0 model, domain, view, unit_of_work and errs](#v030-model-domain-view-unitofwork-and-errs)

4. [v0.4.0 repository, service, controller and web.app:api](#v040-repository-service-controller-and-webapp--api)

5. [v0.5.0 security & deployment](#v050-security--deployment)

6. [v1.0.0 release](#v100-release)





## v0.1.0 mission's input, data and output, as well as, setup and versioning (git)

1. [create directory, readme, .gitignore, setup, requirements, entrypoint, virtualenv](#create-directory-readme-gitignore-setup-requirements-entrypoint-virtualenv)
2. [save changes](#save-changes)
3. [create version tag](#create-version-tag)


### create directory, readme, .gitignore, setup, requirements, entrypoint, virtualenv

- [.gitignore](https://github.com/halleberry/smutils/blob/main/.gitignore)

```shell
#!/usr/bin/env sh

git init

```


### save changes & create version tag

```shell
#!/usr/bin/env sh

# save changes
git add . &&  git commit -m "v0.1.0 init $(basename $(PWD)) microservice"

# create version tag
git tag v0.1.0 -m "$(git rev-parse --short HEAD) $(date) $(git log -1 --pretty=%B)"

```


## v0.2.0 oas's version, info, paths, servers and components' schemas



## v0.3.0 model, domain, view, unit_of_work and errs

## v0.4.0 repository, service, controller and web.app:api

## v0.5.0 security & deployment

## v1.0.0 release












