# LetMeRollForYou
Dice rolling simulator with Python and Django framework

## Setup
In order to acces random.org API app needs secutity token. 

Token might be provided by manulally setting up enviroment variable `RANDOM_TOKEN=random-api-key` or (better solution) by creating `.env` file in project main folder:

```
# .env:
RANDOM_TOKEN=random-api-key
```

## Tests
To run tests type:
```
coverage run .\manage.py test
```
For report follow with:
```
coverage html
```
