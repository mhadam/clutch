CMD_ARGUMENTS ?= $(cmd)

.PHONY: shell help build rebuild service login test clean prune unit integration

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

unit:
	docker build -f docker/clutch.df -t clutch-test .
	docker run --rm --entrypoint "/bin/sh" clutch-test -c "mypy .; pytest tests/unit"

integration:
	docker build -f docker/clutch.df -t clutch-test .
	docker run --rm --entrypoint "/bin/sh" clutch-test -c "mypy .; pytest tests/unit"

end-to-end:
	docker-compose -f ./docker/docker-compose.yml up -d --force-recreate --no-deps --build testbed transmission
	docker-compose -f ./docker/docker-compose.yml run --rm start_dependencies
	docker-compose -f ./docker/docker-compose.yml run --rm testbed sh -c "mypy .; pytest tests/endtoend"

test-shell:
	docker-compose -f ./docker/docker-compose.yml run testbed --entrypoint "/bin/sh"

transmission-shell:
	docker-compose -f ./docker/docker-compose.yml run transmission --entrypoint "/bin/sh"

clean-containers:
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)
