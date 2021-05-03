build-tiny-app:
	docker image build -t tiny-app ./tiny-app

run-tiny-app:
	docker run -p 5000:5000 -d tiny-app

run:
	docker-compose up -d