#!/usr/bin/env sh


echo "v0.0.01 init $(basename $(PWD)) microservice"

echo "v0.0.02 create domain, model and view; init alembic for db migrations management; create err.py, unit_of_work.py"

echo "v0.0.03 create repository(model_kwargs): domain"

echo "v0.0.04 create service(repository.domain): view"

echo "v0.0.05 create controller(service.view): endpoint"

echo "v0.0.06 create web.app.api(controller): api"


# ========================================================================
# VERSION_git_tag_________________________________________________________
# ========================================================================
git add . 
git commit -m "v0.0.01 init $(basename $(PWD)) microservice"


# git the hash of that commit with $(git rev-parse --short HEAD)
_TARGET_COMMIT_HASH='32cd40d'


# go back to the target commit and create a tag
_TAG_NAME='v0.0.01'
git checkout "${_TARGET_COMMIT_HASH}"


# create tag
git tag ${_TAG_NAME} -m "$(git rev-parse --short HEAD) $(date) $(git log -1 --pretty=%B)"


# display tag comment: eg (v0.0.01    32cd40d  Fri Jul 12 21:00:58 MDT 2024  v0.0.01 init multi_language_strings microservice)
git tag -n1 v0.0.01


