# AllenNLP-Benchmark

## Build Docker Image for AllenNLP 1.0.0

```sh
cd allennlp-1.0.0
docker build -t allennlp-1.0.0 .
```

## Run Docker Container for AllenNLP 1.0.0

```sh
cd allennlp-1.0.0
docker run -it -v `pwd`:/workspace/ allennlp-1.0.0:latest bash
cd workspace
```

## Run Coreference Resolution model

```sh
cd workspace
python coreference-resolution.py
```

## Build Docker Image for AllenNLP 1.4.0

```sh
cd allennlp-1.4.0
docker build -t allennlp-1.4.0 .
```

## Run Docker Container for AllenNLP 1.4.0

```sh
cd allennlp-1.4.0
docker run -it -v `pwd`:/workspace/ allennlp-1.4.0:latest bash
cd workspace
```

## Run Named Entity Recongnition model

```sh
cd workspace
python ner.py
```

## Run Semantic Role Labelling model

```sh
cd workspace
python semantic-role-labelling.py
```