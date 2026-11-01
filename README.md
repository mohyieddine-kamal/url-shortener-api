# 🔗 URL Shortener API

API REST de raccourcissement d'URLs : génère un code court unique pour n'importe quelle URL, gère la redirection automatique, et suit le nombre de clics par lien.

**🔗 Démo en ligne :** https://url-shortener-api-9fj8.onrender.com/docs

## 🚀 Points forts

- Génération de code court unique (collision gérée automatiquement)
- Redirection HTTP native (307) vers l'URL d'origine
- Suivi du nombre de clics par lien
- Séparation claire entre routes protégées (création, stats) et route publique (redirection)
- API sécurisée par clé API (`X-API-Key`) sur les endpoints sensibles
- Testé automatiquement, conteneurisé, déployé en production

## 🛠️ Stack

FastAPI · PostgreSQL · SQLAlchemy · Pydantic · Pytest · Docker · Render

## 📡 Endpoints

| Méthode | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/health` | Non | Statut de l'API |
| POST | `/shorten` | Oui | Crée un lien raccourci |
| GET | `/{code}` | Non | Redirige vers l'URL d'origine |
| GET | `/stats/{code}` | Oui | Statistiques d'un lien (clics, date, URL d'origine) |

```bash
curl -X POST "https://url-shortener-api-9fj8.onrender.com/shorten" \
  -H "x-api-key: VOTRE_CLE_API" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://example.com/un-tres-long-lien"}'
```

```json
{
  "short_code": "O4VsrZ",
  "original_url": "https://example.com/un-tres-long-lien",
  "click_count": 0,
  "created_at": "2026-11-01T22:54:33.013102"
}
```

## ⚙️ Démarrage rapide

```bash
git clone https://github.com/mohyieddine-kamal/url-shortener-api.git
cd url-shortener-api
pip install -r requirements.txt
# .env : DATABASE_URL, API_KEY
uvicorn main:app --reload
```

Ou avec Docker, sans rien installer :
```bash
docker compose up --build
```

## ✅ Tests

```bash
python3 -m pytest
```

## 🔮 Améliorations futures

Statistiques avancées (clics par jour, géolocalisation), expiration automatique des liens, interface web pour gérer ses liens sans passer par l'API.
