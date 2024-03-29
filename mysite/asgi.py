import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path
from mysite.wsgi import *

django_asgi_app = get_asgi_application()

from digitaltwin.consumers import CounterConsumer, CarConsumer

application = ProtocolTypeRouter(
    {
        # Django's ASGI application to handle traditional HTTP requests
        "http": django_asgi_app,
        # WebSocket handler
        "websocket": OriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        path("ws/counter/", CounterConsumer.as_asgi()),
                        path("ws/car/", CarConsumer.as_asgi()),
                    ]
                )
            ),
            ["*"],
        ),
    }
)
