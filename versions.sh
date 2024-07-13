#!/usr/bin/env sh


echo "v0.0.01 init microservice $(basename $(PWD))"

echo "v0.0.02 create domain, model and view & init alembic for db migrations management."

echo "v0.0.03 create repository(model_kwargs): domain"

echo "v0.0.04 create service(repository.domain): view"

echo "v0.0.05 create controller(service.view): endpoint"

echo "v0.0.06 create web.app.api(controller): api"
