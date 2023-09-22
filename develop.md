## Update procedure

1. Increase the version of pyprojyect.toml
2. create docs
3. build & publish
4. `git commit` and push

## create docs

```bash
pdoc --html --output-dir=docs src/check-library  --force
mv docs/check-library/* docs/
rm -r docs/check-library
```

## test

```bash
python src/che/che.py -v
```

build and publish

```bash
rye build
rye publish
```
