# monitoring-app-ia

## Description
Ce projet est une application de monitoring pour un modèle de régression linéaire utilisant le dataset California Housing. L'application permet de surveiller les dérives de données et les performances du modèle.

## Prérequis
- Docker
- Docker Compose

## Installation
1. Clonez le dépôt :
    ```sh
    git clone <git@github.com:Jakimpact/monitoring-app-ia.git>
    cd monitoring-app-ia
    ```

2. Construisez et démarrez les services Docker :
    ```sh
    docker-compose up --build
    ```

## Utilisation
### API
L'API est définie dans le fichier main.py. Elle permet de faire des prédictions avec le modèle entraîné.

### Monitoring
Les notebooks model.ipynb et monitoring_ml.ipynb contiennent le code pour entraîner le modèle et surveiller les dérives de données.

1. Exécutez le notebook [model.ipynb](http://_vscodecontentref_/7) pour entraîner le modèle et exporter les datasets de référence et de dérive.
2. Exécutez le notebook [monitoring_ml.ipynb](http://_vscodecontentref_/8) pour générer les rapports de dérive de données avec Evidently.

### Grafana
Grafana est configuré pour afficher les tableaux de bord de monitoring. Les fichiers de configuration se trouvent dans le dossier grafana.

### Prometheus
Prometheus est configuré pour collecter les métriques. Le fichier de configuration se trouve dans prometheus.yml.

## Dépendances
Les dépendances Python sont listées dans les fichiers [requirements.txt](http://_vscodecontentref_/9) :
- [requirements.txt](http://_vscodecontentref_/10)
- [requirements.txt](http://_vscodecontentref_/11)