# Build Instructions

Configure the environment

```bash
conda create -n et-engine-docs-python-core python=3.11.9
conda activate et-engine-docs-python-core
pip install -r requirements-docs.txt
```

# Build

```bash
make clean
make html
```
