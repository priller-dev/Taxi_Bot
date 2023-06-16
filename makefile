push:
	git add .
	git commit -m $(msg)
	git push -u origin2 main


setup:
	pip install -r requirements.txt