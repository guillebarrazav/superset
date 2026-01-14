import os

# =========================
# METADATA DATABASE (OBLIGATORIO)
# =========================
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
if not SQLALCHEMY_DATABASE_URI:
    raise RuntimeError(
        "SQLALCHEMY_DATABASE_URI is required. "
        "Superset will not start without a metadata database."
    )

# =========================
# SECURITY
# =========================
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SUPERSET_SECRET_KEY is required")

# =========================
# REDIS (ACA SIDECAR)
# =========================
REDIS_HOST = "localhost"
REDIS_PORT = "6379"

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_qa_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_URL": f"redis://{REDIS_HOST}:{REDIS_PORT}/0",
}

DATA_CACHE_CONFIG = CACHE_CONFIG
FILTER_STATE_CACHE_CONFIG = CACHE_CONFIG
EXPLORE_FORM_DATA_CACHE_CONFIG = CACHE_CONFIG

ROW_LIMIT = 5000
SUPERSET_WEBSERVER_TIMEOUT = 120

# =========================
# BRANDING
# =========================

THEME_DEFAULT = {
    "token": {
        "brandLogoUrl": "/static/assets/images/gfn-logo.png",
        "brandIconMaxWidth": 150,
        "brandLogoHeight": "28px",
        "brandLogoMargin": "10px 0","brandLogoAlt": "GeForce NOW Digevo",
        "brandLogoHref": "/",
        "colorPrimary": "#76B900",
        "fontFamily": "Inter, Helvetica, Arial",
    },
    "algorithm": "default",
}

THEME_DARK = {
    "token": {
        "brandLogoUrl": "/static/assets/images/gfn-logo-dark.png",
        "brandIconMaxWidth": 150,
        "brandLogoHeight": "28px",
        "brandLogoMargin": "10px 0",
        "brandLogoAlt": "GeForce NOW Digevo",
        "brandLogoHref": "/",
        "brandAppName": "GeForce NOW Digevo Analytics Platform",
        "colorPrimary": "#76B900",
        "fontFamily": "Inter, Helvetica, Arial",
    },
    "algorithm": "dark",
}

ENVIRONMENT_TAG_CONFIG = {
    "variable": "FLASK_ENV",
    "values": {
        "qa": {
            "color": "#f59e0b",
            "text": "QA",
        },
        "production": {
            "color": "#dc2626",
            "text": "PROD",
        },
    },
}

APP_NAME = "GeForce NOW Digevo Analytics Platform - v1.0.0 - QA"