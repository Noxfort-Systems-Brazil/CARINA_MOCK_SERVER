<!--
SPDX-FileCopyrightText: 2026 Noxfort Systems <gabriel.moraes@noxfortsystems.com>
SPDX-License-Identifier: Apache-2.0
-->

# Security Policy — CARINA MOCK SERVER

## Supported Versions

CARINA MOCK SERVER is actively maintained by Noxfort Systems. Security updates are applied to the latest release branches.

| Version | Supported          |
| ------- | ------------------ |
| v1.1.x  | :white_check_mark: |
| v1.0.x  | :white_check_mark: |
| < 1.0   | :x:                |

---

## Reporting a Vulnerability

**IMPORTANT:** While CARINA MOCK SERVER is a test harness and simulation sink, it interfaces directly with distributed high-frequency traffic control engines (`CARINA_CORE`) and simulation environments. Malformed Protobuf streams, memory corruption in gRPC dispatchers, or deserialization vulnerabilities must be remediated swiftly.

**DO NOT** disclose vulnerabilities publicly on GitHub Issues or discussion boards.

If you discover a potential security vulnerability, please report it privately:
- **Email:** `security@noxfort.com` *(Noxfort Systems Security Team)*
- Include detailed replication steps, proof-of-concept packets/scripts, and system details.

We will acknowledge receipt within 48 hours and coordinate a coordinated disclosure timeline.
