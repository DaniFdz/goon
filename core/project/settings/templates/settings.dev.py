DEBUG = True
SECRET_KEY = "django-insecure-3)gqd#y5inj052qqcsdt%_*$+ol-xc1onl4^071v=2=_lr587)"

LOGGING["formatters"]["colored"] = {  # type: ignore # noqa: F821
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["cooking_core"]["level"] = "DEBUG"  # type: ignore # noqa: F821
LOGGING["handlers"]["console"]["level"] = "DEBUG"  # type: ignore # noqa: F821
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore # noqa: F821
