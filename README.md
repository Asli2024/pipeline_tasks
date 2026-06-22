# Pipeline Tasks - CI/CD Learning Repository

A simple CI/CD implementation with a Python application, automated testing, and Docker deployment.

##  What's Included

### Task 1: Continuous Integration (CI Pipeline)
Automatically runs tests and linting checks on every push to main branch.

**Workflow:** `.github/workflows/ci-pipeline.yml`

**Steps:**
-  Checkout code
-  Set up Python 3.12
-  Install dependencies (pytest, pylint)
-  Run linting checks
-  Run unit tests

### Task 2: Continuous Deployment (CD Pipeline)
Automatically builds and pushes Docker image to Docker Hub on every push to main.

**Workflow:** `.github/workflows/cd-pipeline.yml`

**Steps:**
-  Checkout code
-  Login to Docker Hub
-  Build Docker image
-  Push to Docker Hub with commit SHA tag

##  Quick Start

### Run Locally

```bash
# Clone repository
git clone https://github.com/Asli2024/pipeline_tasks.git
cd pipeline_tasks

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest test_app.py -v

# Run application
python app.py
# Output: Hello, World!
```

### Build Docker Image

```bash
docker build -t pipeline-app .
docker run pipeline-app
# Output: Hello, World!
```

Note: The CD pipeline tags the image with the commit SHA (e.g., pipeline-app:abc123def456) when pushing to Docker Hub.

### Project Structure

```
pipeline_tasks/
  .github/
    workflows/
      ci-pipeline.yml
      cd-pipeline.yml
  app.py
  test_app.py
  requirements.txt
  Dockerfile
  README.md
```

##  Application

Simple Python application:

```python
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    print(hello())
```

### Tests

```python
def test_hello():
    assert hello() == "Hello, World!"
```

Run tests:
```bash
pytest test_app.py -v
```

Run linting:
```bash
pylint app.py
```

##  Docker

### Build Image
```bash
docker build -t pipeline-app .
```

### Run Container
```bash
docker run pipeline-app
```

### Image Details
- **Base:** Python 3.11-slim
- **Port:** Not exposed (console app)
- **CMD:** Runs `python app.py`

##  GitHub Actions Workflows

### CI Pipeline Workflow

**File:** `.github/workflows/ci-pipeline.yml`

**Trigger:** Push to `main` branch

**What it does:**
- Checks out your code
- Installs Python 3.12
- Installs dependencies from requirements.txt
- Runs pylint linting checks on app.py
- Runs pytest tests
- Passes if all linting and tests succeed

### CD Pipeline Workflow

**File:** `.github/workflows/cd-pipeline.yml`

**Trigger:** Push to `main` branch

**What it does:**
- Checks out your code
- Logs in to Docker Hub
- Builds Docker image
- Pushes to Docker Hub with tag: `username/pipeline-app:commit-sha`

**Permissions:** `contents: read` (only reads repository)

**Required Secrets:**
- `DOCKERHUB_USERNAME` - Your Docker Hub username
- `DOCKERHUB_TOKEN` - Your Docker Hub access token

##  Setup Instructions

### 1. Create Docker Hub Access Token

1. Go to https://hub.docker.com/settings/security
2. Click **"New Access Token"**
3. Name it (e.g., `github-actions`)
4. Choose **Read & Write** permissions
5. Click **"Generate"**
6. Copy the token immediately (it won't appear again)

### 2. Add Secrets to GitHub

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"** twice to add:

   **Secret 1:**
   - Name: `DOCKERHUB_USERNAME`
   - Value: Your Docker Hub username

   **Secret 2:**
   - Name: `DOCKERHUB_TOKEN`
   - Value: The token from step 1

### 3. Push Changes and Watch Pipelines

```bash
git add .
git commit -m "Setup CI/CD"
git push origin main
```

Go to **GitHub Actions** tab to watch the workflows run.

##  How It Works

1. **You push to main** → GitHub detects push event
2. **CI Pipeline runs** → Tests your code, fails if tests don't pass
3. **CD Pipeline runs** → Builds Docker image and pushes to Docker Hub
4. **Your image is published** → Available at `docker.io/your-username/pipeline-app:commit-sha`

##  Pipeline Status

- View workflows: **GitHub → Actions tab**
- View pushed images: **Docker Hub → Your account**
- Run tests locally: `pytest test_app.py -v`

##  Technologies

- **Language:** Python 3.12
- **Testing:** pytest
- **Linting:** pylint
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Registry:** Docker Hub

##  Learn More

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [Docker Hub](https://hub.docker.com/)

##  Features

Automated testing on every push
Code linting checks
Automatic Docker image builds
Push to Docker Hub
Simple Python application
Unit test coverage
GitHub Actions integration  

---

**Repository:** https://github.com/Asli2024/pipeline_tasks
