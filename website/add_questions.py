import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from quiz.models import Question, Choice

questions_data = [
    {
        "text": "Quel est l'outil DevOps principalement utilisé pour la gestion du code source et le versioning ? 💻📂",
        "choices": [
            {"text": "Docker 🐳", "is_correct": False},
            {"text": "Jenkins 🛠️", "is_correct": False},
            {"text": "Git 💻", "is_correct": True},
            {"text": "Kubernetes ☸️", "is_correct": False},
        ],
    },
    {
        "text": "Lequel de ces outils est un système d'automatisation de l'intégration et de la livraison continues (CI/CD) ? 🔄⚙️",
        "choices": [
            {"text": "Docker 🐳", "is_correct": False},
            {"text": "Jenkins 🛠️", "is_correct": True},
            {"text": "Git 💻", "is_correct": False},
            {"text": "Kubernetes ☸️", "is_correct": False},
        ],
    },
    {
        "text": "Quel outil DevOps est utilisé pour la conteneurisation d'applications ? 🏗️🐳",
        "choices": [
            {"text": "Docker 🐳", "is_correct": True},
            {"text": "Jenkins 🛠️", "is_correct": False},
            {"text": "Git 💻", "is_correct": False},
            {"text": "Kubernetes ☸️", "is_correct": False},
        ],
    },
    {
        "text": "Lequel de ces outils est une plateforme d'orchestration de conteneurs ? 🔄🛠️",
        "choices": [
            {"text": "Ansible 🔧", "is_correct": False},
            {"text": "Terraform 🛠️", "is_correct": False},
            {"text": "Kubernetes ☸️", "is_correct": True},
            {"text": "Nagios ⚙️", "is_correct": False},
        ],
    },
    {
        "text": "Quelle commande permet de voir les logs d’un conteneur Docker ? 📜🐳",
        "choices": [
            {"text": "docker logs <container_id> 🐳", "is_correct": True},
            {"text": "docker show logs <container_id> 📄", "is_correct": False},
            {"text": "docker history <container_id> ⏳", "is_correct": False},
            {"text": "docker inspect <container_id> 🔍", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce que l'Infrastructure as Code (IaC) ? 📜💻",
        "choices": [
            {"text": "La gestion manuelle de l'infrastructure 🛠️", "is_correct": False},
            {"text": "L'utilisation de code pour gérer et provisionner l'infrastructure 💻", "is_correct": True},
            {"text": "La surveillance des performances des applications 📊", "is_correct": False},
            {"text": "L'automatisation des tests unitaires 🧪", "is_correct": False},
        ],
    },
    {
        "text": "Quel outil peut être utilisé pour l'IaC avec AWS ? ☁️🛠️",
        "choices": [
            {"text": "Ansible 🔧", "is_correct": True},
            {"text": "Docker 🐳", "is_correct": False},
            {"text": "Jenkins 🛠️", "is_correct": False},
            {"text": "Git 💻", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce que le Continuous Integration (CI) ? 🔄💻",
        "choices": [
            {"text": "Le déploiement continu en production 🚀", "is_correct": False},
            {"text": "L'intégration fréquente du code des développeurs dans un dépôt partagé 💻", "is_correct": True},
            {"text": "La gestion de la configuration de l'infrastructure 🛠️", "is_correct": False},
            {"text": "La surveillance des performances des applications 📊", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce que le Continuous Delivery (CD) ? 📦🚚",
        "choices": [
            {"text": "La livraison continue de nouvelles fonctionnalités aux utilisateurs 🎉", "is_correct": True},
            {"text": "L'intégration continue du code 🔄", "is_correct": False},
            {"text": "La gestion de la configuration 🔧", "is_correct": False},
            {"text": "La surveillance des logs 📜", "is_correct": False},
        ],
    },
    {
        "text": "Quelle est la différence entre Continuous Delivery et Continuous Deployment ? 🚀🔁",
        "choices": [
            {"text": "Il n'y a pas de différence ❌", "is_correct": False},
            {"text": "Le Continuous Delivery implique une approbation manuelle avant le déploiement en production, tandis que le Continuous Deployment est entièrement automatisé 🤖", "is_correct": True},
            {"text": "Le Continuous Delivery est plus rapide que le Continuous Deployment ⚡", "is_correct": False},
            {"text": "Le Continuous Deployment est une étape du Continuous Delivery 🔄", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce que Git stash ? 🗂️💻",
        "choices": [
            {"text": "Une commande pour supprimer un commit ❌", "is_correct": False},
            {"text": "Une commande pour enregistrer temporairement des modifications non commitées ⏸️", "is_correct": True},
            {"text": "Une plateforme de gestion de code source 💻", "is_correct": False},
            {"text": "Un outil de déploiement 🚀", "is_correct": False},
        ],
    },
    {
        "text": "Quelle commande Git permet de cloner un dépôt distant ? 📂🔄",
        "choices": [
            {"text": "git clone 🧑‍💻", "is_correct": True},
            {"text": "git copy 📋", "is_correct": False},
            {"text": "git download ⬇️", "is_correct": False},
            {"text": "git fetch 🔄", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce qu'un merge conflict dans Git ? ⚔️📝",
        "choices": [
            {"text": "Une erreur lors du commit ❌", "is_correct": False},
            {"text": "Un problème lorsque deux branches modifient les mêmes lignes d'un fichier ✍️", "is_correct": True},
            {"text": "Un type de branche Git 🌲", "is_correct": False},
            {"text": "Une commande pour fusionner des branches 🔀", "is_correct": False},
        ],
    },
    {
        "text": "Quel outil est souvent utilisé pour l'automatisation des tests ? 🧪🔧",
        "choices": [
            {"text": "Selenium 🔧", "is_correct": True},
            {"text": "Docker 🐳", "is_correct": False},
            {"text": "Jenkins 🛠️", "is_correct": False},
            {"text": "Git 💻", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce que le monitoring continu ? 👀📊",
        "choices": [
            {"text": "La surveillance ponctuelle des applications ⏰", "is_correct": False},
            {"text": "La surveillance constante des applications et de l'infrastructure 🔄", "is_correct": True},
            {"text": "L'automatisation des tests 🧪", "is_correct": False},
            {"text": "La gestion des déploiements 🚚", "is_correct": False},
        ],
    },
    {
        "text": "Quel est l'avantage principal de l'utilisation de conteneurs (comme Docker) ? 🐳💨",
        "choices": [
            {"text": "Ils sont plus lents que les machines virtuelles 🐌", "is_correct": False},
            {"text": "Ils permettent d'isoler les applications et de les rendre portables 🛠️🌍", "is_correct": True},
            {"text": "Ils nécessitent beaucoup de ressources système ⚙️", "is_correct": False},
            {"text": "Ils ne sont pas compatibles avec le cloud ☁️", "is_correct": False},
        ],
    },
    {
        "text": "Qu'est-ce que Kubernetes ? ☸️🔧",
        "choices": [
            {"text": "Un outil de gestion de code source 💻", "is_correct": False},
            {"text": "Une plateforme d'orchestration de conteneurs 🛠️", "is_correct": True},
            {"text": "Un outil d'automatisation de tests 🧪", "is_correct": False},
            {"text": "Un système d'intégration continue 🔄", "is_correct": False},
        ],
    },
]

for q in questions_data:
    question = Question.objects.create(text=q["text"])
    for choice in q["choices"]:
        Choice.objects.create(question=question, text=choice["text"], is_correct=choice["is_correct"])

print("✅ 20 Questions DevOps ajoutées avec succès !")
