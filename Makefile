build:
	@echo "Running docker compose locally..."
	docker-compose build
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
	docker-compose exec -T catalog python manage.py makemigrations

migrate:
	@echo "Running migrations..."
	docker-compose exec -T catalog python manage.py migrate

collectstatic:
	@echo "Collecting static files..."
	docker-compose exec -T catalog python manage.py collectstatic

fixtures:
	@echo "Loading fixtures..."
	docker-compose exec -T catalog sh -c "python manage.py loaddata fixtures/*.json"
