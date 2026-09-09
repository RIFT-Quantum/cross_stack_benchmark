# Cross Stack Benchmark

Quantum circuit benchmarking notebook using Qiskit. Implements Bernstein-Vazirani, QFT, QPE, and Quantum Volume random layers on simulated and real IBM backends.

## Local Setup

```bash
# Create virtual environment
uv venv

# Activate
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

## Run Notebook

```bash
jupyter notebook benchmark.ipynb
```

## Docker Compose (recommended)

```bash
docker compose up
```

Notebook available at the URL printed in terminal (with token). Source files mounted as volume — edits persist.

```bash
# Rebuild after changing requirements
docker compose up --build

# Stop
docker compose down
```

## Docker (standalone)

```bash
docker build -t quantum-benchmark .
docker run -p 8888:8888 quantum-benchmark
```

## Formatting

```bash
source .venv/bin/activate
black benchmark.ipynb
```
