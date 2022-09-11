import datetime
import logging
from typing import ClassVar
from collections.abc import Callable
from .models import SimpleLogger
from datetime import datetime  # noqa: F401
from django.utils import timezone


class SimpleLoggingMiddleware:
    # назввание, для того, что бы понимать какой middleware отработал
    _NAME: ClassVar[str] = "first"

    #     middleware инициализируется только при запуске приложения, а затем он просто вызывается
    def __init__(self, get_response: Callable):
        # функция с помощью которой мы получаем ответ
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request):
        # сообщение, которое выведется
        message = f"[{self._NAME}] {request.path} {request.user.is_authenticated} {request.user}"
        # до отрабатывания view
        self.logger.info(f"[before] {message}")

        # отрабатывает view:
        response = self.get_response(request)

        self.logger.info(f"[after] {message}")

        if SimpleLogger.objects.filter(username=request.user, url=request.path).exists():
            for el in SimpleLogger.objects.filter(username=request.user, url=request.path):
                el.last_visit = datetime.now(tz=timezone.utc)
                el.count_of_visits += 1
                el.save()
        else:
            SimpleLogger.objects.create(
                username=request.user, url=request.path, last_visit=datetime.now(tz=timezone.utc)
            )

        return response
