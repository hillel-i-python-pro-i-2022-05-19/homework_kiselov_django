# Make some initialization steps. For example, copy configs.
init-configs-i-dev:
    # копируем файл docker-compose.override.dev.yml(копия нашего Docker-compose, который не пушится)
    # @ - нужна для того, что бы сама команда, которая выполняется не печаталась
	@cp docker-compose.override.dev.yml docker-compose.override.yml


# Just run
d-run:
    # для создания контейнера и его запуска
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build


# Make all actions needed for run homework from zero.
d-homework-i-run:
# # @ - Полная сборка контейнера(копирование docker-compose(из шаблона) далее создание контейнера и запуск)
	@make init-configs-i-dev && \
	make d-run


# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge

# Follow logs
d-logs-follow:
	@docker-compose logs --follow


# Shutdown previous, run in detached mode, follow logs
d-run-i-extended:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --timeout 0 && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build --detach && \
	make d-logs-follow


# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down


# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --volumes --remove-orphans --rmi local --timeout 0
#

.PHONY: d-homework-i-run d-homework-i-purge d-logs-follow d-run-i-extended d-stop d-purge



# Эта инструкция указывает docker-compose использовать Docker CLI при выполнении сборки. Вы должны увидеть тот же результат сборки,
# но начиная с экспериментального предупреждения.
# COMPOSE_DOCKER_CLI_BUILD=1 docker-compose build
#
#
# Поскольку docker-compose передает свои переменные среды в CLI Docker, мы также можем указать CLI использовать
# BuildKit вместо сборщика по умолчанию. Для этого мы можем выполнить это:

# COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

# По сути DOCKER_BUILDKIT это сборщик, который имеет дополнительные фичи, такие как кеширование, конкурентность и т.д
# ускоряет сборку контейнеров