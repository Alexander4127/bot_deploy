# BOT-DEPLOY

The main objective is to create CI/CD using docker files and some other instruments.

## Code
- Under complex constructions for updating by commits, I wrote a simple telegram-bot.
- I used `pyyotube` library and API to find top-3 videos by keywords and print some information about them.
- I got the cloud to make a free instance and use it for running my bot.
- Server was taken on two months on December 20, 2021.
- The username is `@MyReallySimpleBot`.

## Docker

As it is known, I need `DockerFile` to create an image. I need the `requirements.txt` to download libraries and choose settings. Then the image will be sent to the server after some tests. The next part is about some features for this goal.

## .yml files
There are several files, I will write about the each one.

1. `main.yml` can be triggered by pushes with tags or pull requests. Like the next one, it uses Github Actions and runs two tests. The first one is to build an image, and the second is to check the code with a linter.
2. `publish.yml` is called after achievement all tests. It updates the image on the [DockerHub](https://hub.docker.com/repository/docker/alexander4127/bot-deploy).
3. `docker-compose.yml` is the most significant file. It is on the server, and I do not need it on Github, but I added it to show the code. It uses [WatchTower](https://containrrr.dev/watchtower/) to collect the updates in the cycle from the DockerHub.

As a result, I can clone the repository, make local changes and push them to Github. After successful tests, my modifications will be added to the bot functionality.
