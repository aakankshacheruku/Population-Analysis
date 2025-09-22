# Population Analysis

Combine public-style population data, compute year-over-year growth, and produce a simple table and plot. I started small so the project runs fast and is easy to review.

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
make quickstart
```

Outputs will appear in `reports/tables/` and `reports/figures/`.

## What I learned
- Keep calculations simple and NA-safe first, then iterate.
- Make small, testable steps and produce artifacts (CSV/PNG) every run.
- Write down decisions so future changes are easier to review.

## Decisions & next steps
- Start with a small sample so the pipeline is easy to run.
- Growth % tells the story better than raw counts. I plan to add more countries and a population pyramid next.
- Roadmap: expand data, add better metrics, and tighten tests as I go.

## Preview
After `make quickstart`, you should see a CSV table and one PNG in `reports/`.
