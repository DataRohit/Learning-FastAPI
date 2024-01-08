# **Learning-FastAPI**

## **FastAPI Docker Setup Commands**

**1. Create a New Migration**
```bash
    docker-compose run app alembic revision --autogenerate -m "New Migration"
```

**2. Migrate the Changes to Database**
```bash
    docker-compose run app alembic upgrade head
```

**3. Build the App Container**
```bash
    docker-compose build
```

**4. Start the Docker Container and Images**
```bash
    docker-compose up
```