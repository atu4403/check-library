## create docs

```bash
pdoc --html --output-dir=docs src/check-library  --force
mv docs/check-library/* docs/
rm -r docs/check-library
```

## test

```bash
 python src/check-library/check.py -v
```

build and publish

```bash
rye build
rye publish
```
