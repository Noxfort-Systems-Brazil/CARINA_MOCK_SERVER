# CARINA Mock Server - High-Frequency Telemetry & Synapse Protocol Test Harness
# SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# File: src/infrastructure/console_logger.py
# Author: Gabriel Moraes
# Date: October 2026

import logging
from typing import Any
from src.core.interfaces import ILogger

class ConsoleLogger(ILogger):
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self._logger = logging.getLogger("MockServer")
        self._logger.setLevel(logging.INFO)

    def _format_message(self, message: str, kwargs: dict) -> str:
        if kwargs:
            extra_info = ", ".join(f"{k}={v}" for k, v in kwargs.items())
            return f"{message} | {extra_info}"
        return message

    def info(self, message: str, **kwargs: Any) -> None:
        self._logger.info(self._format_message(message, kwargs))

    def warning(self, message: str, **kwargs: Any) -> None:
        self._logger.warning(self._format_message(message, kwargs))

    def error(self, message: str, **kwargs: Any) -> None:
        self._logger.error(self._format_message(message, kwargs))

    def debug(self, message: str, **kwargs: Any) -> None:
        self._logger.debug(self._format_message(message, kwargs))
