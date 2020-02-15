CMD_ARGUMENTS ?= $(cmd)

.PHONY: shell help build rebuild service login test clean prune

shell:
ifeq ($(CMD_ARGUMENTS),)
	# no command is given, default to shell
	docker-compose -p clutch run --rm testbed sh
else
	# run the command
	docker-compose -p clutch run --rm testbed sh -c "$(CMD_ARGUMENTS)"
endif

rebuild:
	# force a rebuild by passing --no-cache
	docker-compose build --no-cache testbed

service:
	# run as a (background) service
	docker-compose -p $(PROJECT_NAME)_$(HOST_UID) up -d $(SERVICE_TARGET)

login: service
	# run as a service and attach to it
	docker exec -it $(PROJECT_NAME)_$(HOST_UID) sh

build:
	# only build the container. Note, docker does this also if you apply other targets.
	docker-compose -f docker/docker-compose.yml build testbed

clean:
	# remove created images
	@docker-compose -p clutch down --remove-orphans --rmi all 2>/dev/null \
	&& echo 'Image(s) for clutch removed.' \
	|| echo 'Image(s) for clutch already removed.'

prune:
	# clean all that is not actively used
	docker system prune -af

format:
	black .

unit-build:
	docker build -f docker/clutch.df -t clutch-test .

unit:
	docker build -f docker/clutch.df -t clutch-test .
	docker run --rm --entrypoint "/bin/sh" clutch-test -c "mypy . || pytest"
	# here it is useful to add your own customised tests
#	docker-compose -f docker/docker-compose.yml -p clutch run --rm testbed sh -c '\
#		echo "pwd:`pwd`" && pytest && ls tests && echo "Docker runs!"' \
#	&& echo success

integration:
    docker-compose up --build
