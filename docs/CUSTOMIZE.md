# 🔧 Integration & Customization Guide

## Adding Your Own Scripts
1. Drop `.py` or `.ps1` files in `scripts/`
2. Update `script_recommender.py` to recognize new keywords

## Connecting APIs
Edit keys in:
- `integrations/connectwise.py`
- `integrations/itglue.py`
- `integrations/auvik.py`
- `integrations/automate.py`

## Using with Internal Docs
- Upload internal SOPs to `examples/`
- Ingest via CLI/GUI/Web and validate against those steps

## Expanding LLMs
- Swap `sentence-transformers` with your own local model
- Future support for LLaMA/Mistral adapters
