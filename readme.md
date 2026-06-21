This project is a two-tier Notes application built with Flask and PostgreSQL,
containerized using Docker and deployed to AWS EC2 via a fully automated CI/CD pipeline
using GitHub Actions. 
The workflow starts when code is pushed to the dev branch, 
which triggers the dev pipeline — it runs tests using pytest, 
builds a Docker image and pushes it to DockerHub, 
then SSHes into the Dev EC2 instance and pulls the latest image and starts 
the containers using docker-compose. 
Once verified on dev, a pull request is raised from dev to main, 
which triggers the prod pipeline following the same steps but deploying to the Prod EC2 instance.
The application runs as two containers — Flask (web) on port 5000 and PostgreSQL (db) on port 5432
— connected via an internal Docker network, with Postgres never exposed to the outside world.
Environment variables including database credentials are managed via a .env file on each EC2 
instance and GitHub Secrets are used for DockerHub credentials and SSH access, ensuring
no sensitive data is committed 
to the repository.

