# TryStack



A little micro-service to run isolated tasks. i used fastapi and mysql for implement mvc behavior.

for run this app run this command on trystack directory:
```
uvicorn app.trystack:app --reload
```

## Dependencies: 
mysql used for storing user's data. you can run mysql on docker with this command:
```
docker run -d --name  mysql  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=trystack mysql:8
```

## Contributions:
All contributions are welcomed. Help us to enrich this repository.

## Copyright:
Copyright & copy; 2022 Amir Mortezaee <amir.mortezaee1@gmail.com>
