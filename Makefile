build:
	docker build -t python_web_scraping .

serve:
	docker run -v ${PWD}:/local_folder -it --name web_scraping python_web_scraping python3