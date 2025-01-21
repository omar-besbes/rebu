.PHONY: install-all run-all

install-all:
	@echo "Setting up driver-assignment virtual environment..."
	cd driver-assignment; \
	python3 -m venv venv; \
	./venv/bin/pip install -r requirements.txt
	@echo "Setting up trip-management virtual environment..."
	cd trip-management; \
	python3 -m venv venv
	@echo "Installing dependencies for invoice-generation..."
	cd invoice-generation; \
	npm i
	@echo "Installing dependencies for route-optimization..."
	cd route-optimization; \
	go mod tidy

run-all:
	@echo "Running driver-assignment..."
	cd driver-assignment; \
	./venv/bin/python main.py & echo $$! > driver-assignment.pid
	@echo "Running invoice-generation..."
	cd invoice-generation; \
	node app.js & echo $$! > invoice-generation.pid
	@echo "Running route-optimization..."
	cd route-optimization; \
	go run main.go & echo $$! > route-optimization.pid
	@echo "Running trip-management..."
	cd trip-management; \
	./venv/bin/python main.py & echo $$! > trip-management.pid
	@echo "All applications started in the background

kill-all:
	rm **/*.pid
	for port in 9000 9001 9002 9003; do fuser -k "$$port"/tcp; done
	@echo "All applications killed in the background


