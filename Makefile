.PHONY: builder

builder:
	docker build -f Dockerfile_builder -t xnaveira/rostollador_builder .

test:
	docker build -f Dockerfile_test -t xnaveira/rostollador_test .

rostollador: builder
	docker build -t xnaveira/rostollador .
