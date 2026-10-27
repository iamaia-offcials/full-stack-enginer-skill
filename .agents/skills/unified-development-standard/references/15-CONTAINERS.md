# 15. Containers, Docker/Podman, PaaS, and deployment

Apply container-specific rules only when the project uses containers; evaluate hosting against requirements first.

- `[CTR-001] SHOULD` For a justified single-VPS container deployment, assess Compose or Quadlet and whether a control panel is useful. Compare managed/static/serverless hosting first; the standard does not require containers.
- `[CTR-002] MUST` Use a supported base image, multi-stage/minimal runtime, non-root where feasible, no embedded secrets, minimum capabilities, a read-only filesystem where feasible, and correct health/signal handling.
- `[CTR-003] MUST` Expose only necessary public ports through one HTTPS reverse proxy. Keep databases/Redis/queues off the public internet by default; separate networks and volumes.
- `[CTR-004] MUST` Keep declarative Compose/Quadlet definitions in Git and environment configuration/secrets separate. `latest` cannot be the sole deployment reference.
- `[CTR-005] MUST` Keep persistent data outside replaceable containers and include it in off-host backup/restore plans. Image rollback is not database rollback.
- `[CTR-006] MUST` Record deployment commit/digest, applied migrations, environment changes, and smoke results. Automatic deployment does not prove service health.
- `[CTR-007] MUST` Configure graceful shutdown, resource limits, restart policy, stdout/stderr logging, timeouts, and readiness for the actual service.
- `[CTR-008] SHOULD` Podman rootless + Quadlet is a valid pilot. First verify persistent volumes, UID mapping, systemd lingering, networking, restart/reboot, health, backup, and rollback. `podman compose` uses an external provider; do not assume complete Docker Compose equivalence.
- `[CTR-009] MUST` Do not run independent Coolify webhooks, Actions SSH-CD, and Watchtower/auto-update for the same application. Coordinate one owner of host ingress ports 80/443.
- `[CTR-010] SHOULD` Introduce infrastructure as code (OpenTofu/Ansible, etc.) as needs grow, with a verified recovery plan. Simple products do not require Kubernetes/Swarm.
- `[CTR-011] MUST` Secure SSH keys and firewall rules, grant minimal service permissions, apply timely security updates, separate environment secrets, and restrict Docker socket access.

## Trade-offs
| Approach | Strengths | Constraints | Suitable context |
|---|---|---|---|
| Docker + Compose | Mature workflow, PaaS ecosystem, simple single host | Daemon/socket and permissions require care | Justified container deployment on one VPS |
| Podman + Quadlet | Daemonless, rootless-first, systemd | Compose is not fully native; panel compatibility | Standalone Linux service, rootless pilot |
| Coolify / Dokploy | UI, deployment, environment/domain management | Extra control layer and rollout constraints | Several projects on a VPS |
| Kubernetes | Orchestration at scale | High operational complexity | Proven large-scale infrastructure needs |

## Release strategy
A single instance may have brief downtime. When zero/near-zero downtime is required, test blue-green/rolling updates in the selected deployment mechanism. Use expand/backfill/contract migrations. Plan routing and certificates before changing reverse proxies.

For task-specific patterns and examples, read the relevant section of [practical formulas](../guides/PRACTICAL-FORMULAS.md).
