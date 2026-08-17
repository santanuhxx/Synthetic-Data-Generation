# Synthetic Data Mini-Lab

This folder demonstrates three ideas from the workshop slides.

## 1. Statistical generation

```bash
python 00_synthetic_data/statistical_generation.py
```

This samples values from simple distributions. Notice that plausible individual
columns do not guarantee realistic relationships between columns.

## 2. Rule-based generation

```bash
python 00_synthetic_data/rule_based_generation.py
```

This generates profiles while enforcing explicit constraints and also validates
three example records, including an under-21 alcohol rule violation.

## 3. Generative AI

```bash
python 00_synthetic_data/generative_ai_generation.py
```

This is deliberately provider-neutral. It demonstrates the prompt/output contract
without requiring an API key. The important engineering pattern is:

Generative model -> candidate record -> deterministic validation -> accepted/rejected record.
