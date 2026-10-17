# CARINA Mock Server - High-Frequency Telemetry & Synapse Protocol Test Harness
# Copyright (C) 2026 Noxfort Systems
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
# File: main.py
# Author: Gabriel Moraes
# Date: October 2026

import sys
import os
import argparse

# Configure path for local package inclusion
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "proto")))

from src.receiver_facade import ReceiverFacade

def parse_args():
    parser = argparse.ArgumentParser(description="CARINA Mock Server - HFT & Telemetria Synapse")
    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Executa o servidor sem a interface gráfica (modo headless)"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    facade = ReceiverFacade()
    facade.run(headless=args.no_gui)

if __name__ == '__main__':
    main()
