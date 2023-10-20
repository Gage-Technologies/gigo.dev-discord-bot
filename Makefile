
docker:
	docker build --tag=gigodev/gigo-dev-discord-bot .

docker-push:
	docker push gigodev/gigo-dev-discord-bot
