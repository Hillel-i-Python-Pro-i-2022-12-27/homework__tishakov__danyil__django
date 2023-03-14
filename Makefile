.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-config-i-homework && \
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose up --build

.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down

.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: init-config-i-homework
# Init configs for homework
init-config-i-homework:
	@cp docker-compose.override.homework.yml docker-compose.override.yml

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python manage.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: migrations
#Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
#Migrate
migrate:
	@python manage.py migrate

.PHONY: django-i-generator-contact-i-100
#Cenerate 100 contact(name, number)
django-i-generator-contact-i-100:
	@python manage.py command_to_generate_contacts --amount 100

.PHONY: createsuperuser
#Migrate
superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py creates
	uperuser --user admin --email admin@gmail.com --no-input