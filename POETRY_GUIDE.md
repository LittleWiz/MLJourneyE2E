---

# 📖 Poetry Setup Guide for `mljourneye2e`

## ✨ Overview
`Poetry` is a modern tool for managing Python dependencies, virtual environments, and packaging—all powered through the `pyproject.toml` file. This guide walks you through the process you followed for setting up your MLOps project with Poetry.

---

## 🧭 Step-by-Step Workflow

### 1️⃣ Install Poetry
Use the official one-liner installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
```bash
pip install poetry
```

Verify installation:

```bash
poetry --version
```

---

### 2️⃣ Initialize the Project
In the project root folder:

```bash
poetry init
```

- Accept default name `mljourneye2e` or customize as needed.
- Follow CLI prompts to specify version, author, and dependencies.

Your resulting `pyproject.toml` (already created) includes metadata and a well-scoped dependency list.

---

### 3️⃣ Add Your Dependencies
You can always add additional libraries later:

```bash
poetry add <package-name>
```

Example:

```bash
poetry add matplotlib scikit-learn
```

For dev dependencies:

```bash
poetry add --group dev black pytest
```

---

### 4️⃣ Install Dependencies
After finalizing your `pyproject.toml`, install everything:

```bash
poetry install
```

This sets up:
- A virtual environment
- A `poetry.lock` file for reproducibility

---

### 5️⃣ Activate Your Environment

Since `poetry shell` is no longer bundled by default in Poetry 2.x, use one of the two options:

#### Option A: Recommended Activation
```bash
poetry env activate
```
This will print the shell command needed to activate the venv manually.  
**On Windows, copy and run the printed command directly in your terminal, for example:**
```bash
C:\Users\user\AppData\Local\pypoetry\Cache\virtualenvs\mljourneye2e-xxxx-py3.12\Scripts\activate.bat
```
After running this, your prompt should change to show your Poetry environment (not `(base)`).

#### Option B: Enable Legacy Shell Plugin
```bash
poetry self add poetry-plugin-shell
poetry shell
```

---

### 6️⃣ Project Files Breakdown

#### `pyproject.toml`
Your configuration includes:
- Python 3.12 support
- Author: "Little Wiz"
- Key dependencies for MLOps (e.g., `mlflow`, `bentoml`, `feast`, `deepchecks`, etc.)
- Build backend powered by `poetry-core`

#### `poetry.lock`
Generated automatically after running `poetry install` or `poetry lock`. Ensures deterministic installs across machines by recording the exact versions of all dependencies and their sub-dependencies.  
If you update your `pyproject.toml` dependencies manually, run:

```bash
poetry lock
```

This will resolve and update the lock file without installing packages.  
To install dependencies as per the lock file, use:

```bash
poetry install
```

---

### 7️⃣ Using Your Poetry Environment as a Jupyter Kernel

To run Jupyter notebooks (e.g., `House_price_main.ipynb`) with your Poetry-managed environment in VS Code:

1. **Install `ipykernel` in your Poetry environment:**

   ```bash
   poetry add ipykernel
   ```

2. **Add your Poetry environment as a Jupyter kernel:**

   ```bash
   poetry run python -m ipykernel install --user --name mljourneye2e --display-name "Python (mljourneye2e)"
   ```

3. **Restart VS Code (recommended).**

4. **Select the correct kernel in your notebook:**
   - Open your `.ipynb` file in VS Code.
   - Click the kernel picker (top right of the notebook interface).
   - Choose **Python (mljourneye2e)** (or the display name you set above).

5. **(Optional) Verify the kernel is correct:**
   In a notebook cell, run:
   ```python
   import sys
   print(sys.executable)
   ```
   The output path should match your Poetry environment path (see `poetry env info --path`).

---

## 🧪 Helpful Commands

| Action                       | Command                                     |
|-----------------------------|---------------------------------------------|
| Add package                 | `poetry add package-name`                  |
| Remove package              | `poetry remove package-name`               |
| Run script in env           | `poetry run python script.py`              |
| View env info               | `poetry env info`                          |
| Update dependencies         | `poetry update`                            |
| Rebuild env from lock       | `poetry install` (after modifying lockfile)|
| Sync env with lockfile      | `poetry sync`                              |
| Check project health        | `poetry check`                             |
| **Update lock file only**   | `poetry lock`                              |

---

## 💡 Tips & Extras

- ✅ Use `poetry build` if you plan to package and publish.
- 🧬 Great for reproducible experiments and CI/CD workflows.
- 📂 Use VS Code? Run `poetry env info --path` to set your interpreter manually.

---

