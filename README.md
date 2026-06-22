# Pipeline Tasks - CI/CD Learning Repository

A simple CI/CD implementation demonstrating automated testing, building, and deployment workflows.

## 📚 What's Included

### Task 1: Continuous Integration (CI)
- **Linting** - Code quality checks with pylint
- **Unit Tests** - Running pytest with coverage
- **Docker Build** - Building container images
- **Workflow:** `.github/workflows/ci-pipeline.yml`

### Task 2: Continuous Deployment (CD)
- **Build Docker Image** - Create and prepare container
- **Deploy Application** - Run the application
- **Workflow:** `.github/workflows/cd-pipeline.yml`

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Asli2024/pipeline_tasks.git
cd pipeline_tasks

# Run tests locally
pip install -r requirements.txt
pytest -v

# Build Docker image
docker build -t pipeline-app:latest .

# Run application
docker run pipeline-app:latest
```

## 📂 Project Structure

```
pipeline_tasks/
├── .github/workflows/
│   ├── ci-pipeline.yml       # Task 1: CI Pipeline
│   └── cd-pipeline.yml       # Task 2: CD Pipeline
├── cicd/
│   ├── README.md            # Detailed documentation
│   ├── task-1/README.md     # CI details
│   └── task-2/README.md     # CD details
├── app.py                    # Simple Python application
├── test_app.py              # Unit tests
├── requirements.txt          # Dependencies
├── Dockerfile               # Container image
└── README.md               # This file
```

## ⚙️ Application

Simple Python "Hello World" application:

```python
def hello():
    return "Hello, World!"
```

### Testing
```bash
pytest test_app.py -v
```

### Docker
```bash
docker build -t pipeline-app:latest .
docker run pipeline-app:latest
# Output: Hello, World!
```

## 🔄 GitHub Actions Workflows

### CI Pipeline (`.github/workflows/ci-pipeline.yml`)
**Triggers:** Push or Pull Request to `main`

**Jobs:**
1. **test** - Run unit tests with coverage
2. **lint** - Code quality check
3. **docker-build** - Build Docker image
4. **ci-complete** - Summary

### CD Pipeline (`.github/workflows/cd-pipeline.yml`)
**Triggers:** Push to `main` or CI pipeline success

**Jobs:**
1. **build-and-push** - Build Docker image
2. **deploy** - Deploy and run application

## 📖 View Pipeline Results

1. Go to GitHub repository
2. Click **Actions** tab
3. View workflow runs

## 📚 Learn More

- [CI/CD Documentation](./cicd/README.md)
- [Task 1 - CI Details](./cicd/task-1/README.md)
- [Task 2 - CD Details](./cicd/task-2/README.md)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Docker](https://docs.docker.com/)

## ✅ Key Features

✅ Automated testing on every push  
✅ Code quality checks (linting)  
✅ Docker image builds  
✅ Automated deployment  
✅ Coverage reporting  

---

**Repository:** https://github.com/Asli2024/pipeline_tasks
