.PHONY: test run lint

# Run tests with pytest
test:
	pytest --maxfail=1 --disable-warnings -q

# Run FastAPI app with unvicorn
run:
	uvicorn app.main:app --reload

lint:
	flake8 src/app/