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
        "brandLogoUrl": "/static/assets/images/logo.png",
        "brandLogoAlt": "GeForce NOW Digevo",
        "brandLogoHref": "/",
        "colorPrimary": "#f59e0b",
        "fontFamily": "Inter, Helvetica, Arial",
    },
    "algorithm": "default",
}

THEME_DARK = {
    "token": {
        "brandLogoUrl": "/static/assets/images/logo.png",
        "brandLogoAlt": "GeForce NOW Digevo",
        "brandLogoHref": "/",
        "colorPrimary": "#f59e0b",
        "fontFamily": "Inter, Helvetica, Arial",
    },
    "algorithm": "dark",
}

ENVIRONMENT_TAG = {
    "label": "QA",
    "color": "#f59e0b",
}

SHOW_ENVIRONMENT_TAG = True

APP_NAME = "GeForce NOW Digevo Analytics - QA"