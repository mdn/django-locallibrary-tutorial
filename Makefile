run:
	@echo "Running docker compose locally..."
	docker-compose up -d

stop:
	@echo "Stopping local environment..."
	docker-compose stop

clean:
	@echo "Removing containers..."
	docker-compose stop
	docker-compose rm

migrations:
	@echo "Building migrations..."
	python manage.py makemigrations

migrate:
	@echo "Running migrations..."
	python manage.py migrate

collectstatic:
	@echo "Collecting static files..."
	python manage.py collectstatic

fixtures:
	@echo "Loading fixtures..."
	python manage.py loaddata fixtures/*.json