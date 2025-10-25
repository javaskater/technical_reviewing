# Running composer from the Host
* [From the docs](https://github.com/dunglas/symfony-docker/blob/main/README.md)
* The remote compose command installing the orm vendor dependency, also modifies the docker - compose file to add the Mysql image ...
> The Docker configuration of this repository is extensible thanks to Flex recipes. By default, the recipe installs PostgreSQL
```bash
docker compose exec php composer req symfony/orm-pack # symfony/orm-pack includes a recipe
```