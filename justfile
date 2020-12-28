format:
	black .

unit:
	docker build -f docker/clutch.df -t clutch-test .
	docker run --rm --entrypoint "/bin/sh" clutch-test -c "mypy .; pytest tests/unit"

end-to-end:
	docker-compose -f ./docker/docker-compose.yml up -d --force-recreate --no-deps --build testbed transmission
	docker-compose -f ./docker/docker-compose.yml run --rm start_dependencies
	docker-compose -f ./docker/docker-compose.yml run --rm testbed sh -c "pytest tests/endtoend"

integration-shell:
	docker-compose -f ./docker/docker-compose.yml up -d --force-recreate --no-deps --build testbed transmission
	docker-compose -f ./docker/docker-compose.yml run --rm start_dependencies
	docker-compose -f ./docker/docker-compose.yml run --rm testbed sh -c "python -i client_setup.py"

clean-containers:
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)

docs:
	sphinx-autogen docs/index.rst -o docs/
