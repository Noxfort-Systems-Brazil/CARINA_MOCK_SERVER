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
# File: src/infrastructure/composite_logger.py
# Author: Gabriel Moraes
# Date: October 2026

from typing import Any, List
from src.core.interfaces import ILogger

class CompositeLogger(ILogger):
    """
    CompositeLogger applies the Composite Pattern to allow broadcasting
    logs to multiple ILogger implementations simultaneously.
    """
    def __init__(self, loggers: List[ILogger]):
        self._loggers = loggers

    def info(self, message: str, **kwargs: Any) -> None:
        for logger in self._loggers:
            logger.info(message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        for logger in self._loggers:
            logger.warning(message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        for logger in self._loggers:
            logger.error(message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        for logger in self._loggers:
            logger.debug(message, **kwargs)
