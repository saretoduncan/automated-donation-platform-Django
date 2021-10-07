serve: 
	python3 manage.py runserver

commit:
	git add .
	git commit -m "made changes"
	git push 

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
