# Full Stack Engineering Skill

[English](../../README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [简体中文](README.zh-CN.md)

**Un estándar de ingeniería portátil para asistentes de IA: reglas de decisión, explicaciones y ejemplos para planificar, desarrollar y mantener software.**

La habilidad principal, `unified-development-standard`, funciona por sí sola. Ayuda al agente a comprender un producto, elegir una pila tecnológica adecuada e implementar el alcance solicitado con las comprobaciones pertinentes. Una corrección de texto debe seguir siendo una corrección de texto, sin convertirse en una auditoría completa.

## Qué abarca

- Visión del producto, reglas de negocio, primera versión/MVP, selección de tecnologías y complejidad.
- Arquitectura, responsabilidad sobre la lógica, backend, API e integraciones.
- Validación, autorización, secretos y aplicación de invariantes de negocio en un entorno de confianza.
- Restricciones de base de datos, transacciones, índices, migraciones y recuperación.
- Frontend, estilos mantenibles, accesibilidad e interfaces adaptables sin imponer una identidad visual.
- Animación de interfaces: selección según el contexto, interrupción e inversión, movimiento reducido, alternativas funcionales y progreso veraz.
- Referencias UX: 39 estudios suministrados, 12 composiciones condicionales y 27 ejemplos de movimiento con secuencias/GIF, seleccionados según la tarea y el modelo real del negocio.
- SEO técnico y planificación de analítica/píxeles antes de conectar servicios.
- Git, CI/CD que tiene en cuenta los costes, contenedores cuando corresponda, versiones y operaciones.
- Documentación viva: actualizar el documento actual de la funcionalidad y distinguir los planes del historial.

Patrón de decisión: **condición → decisión → motivo → ejemplo → verificación**. Validar el formato de un correo electrónico, parametrizar SQL, renderizar de forma segura y autorizar resuelven problemas distintos; una lista de caracteres prohibidos no los sustituye.

## Contexto e idioma

Todas las instrucciones instaladas están en **inglés**. Los agentes deben seguir respondiendo en tu idioma. El punto de entrada dirige a las secciones pertinentes; no exige leer las 30 referencias. Se instala por defecto un núcleo autónomo; los 18 perfiles especializados son opcionales. Las traducciones del README quedan fuera de la habilidad instalada. Las imágenes de movimiento conservan sus textos originales y tienen explicaciones en inglés.

La [guía de referencias](../../.agents/skills/unified-development-standard/guides/UX-REFERENCE-RESEARCH.md) explica la consulta selectiva por CLI y la [galería sin conexión](../../.agents/skills/unified-development-standard/examples/reference-atlas.html). Abre el HTML localmente tras clonar/descargar; GitHub muestra el código fuente. Los diagramas UX son esquemas, no capturas de sitios; las fechas suministradas no indican una verificación nueva. Edita los JSON canónicos y ejecuta `scripts/reference_atlas.py --build-gallery` desde el núcleo para regenerar la galería derivada; `--check-gallery` detecta diferencias.

El inglés puede consumir menos tokens con algunos tokenizadores, pero el ahorro depende del texto y del modelo. La lectura selectiva y la eliminación de duplicaciones también importan. Los [resultados de la revisión](../REVIEW.md) distinguen los tamaños de texto y recuentos de tokens medidos del comportamiento real durante la ejecución.

## Instalación rápida

Requiere **Python 3.10+**, sin dependencias de pip. Usa `py` en Windows o `python3` en Linux/macOS si ese es el comando de tu intérprete. Se necesita Git para clonar; como alternativa, usa **Code → Download ZIP** en GitHub y extrae el archivo.

```bash
git clone https://github.com/iamaia-offcials/full-stack-enginer-skill.git
cd full-stack-enginer-skill
python tooling/install.py --agent codex --scope user
```

El instalador copia archivos locales. No descarga dependencias, accede a cuentas ni modifica `AGENTS.md`, `CLAUDE.md` o `GEMINI.md`.

Para instalar en un proyecto existente:

```bash
python tooling/install.py --agent codex --repo "/path/to/my-project" --dry-run
python tooling/install.py --agent codex --repo "/path/to/my-project"
```

En Windows, usa una ruta como `"C:/dev/my-project"`. El origen y el destino no deben solaparse: no selecciones el propio directorio de esta suite como destino.

## Compatibilidad con agentes

| Herramienta | `--agent` | Directorio del proyecto | Directorio del usuario |
|---|---|---|---|
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude` | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `gemini` | `.gemini/skills/` | `~/.gemini/skills/` |
| Antigravity App / IDE | `antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| Otros agentes compatibles | `generic` o `--target` | Según el agente | Según el agente |

Elige el comando de tu herramienta:

```bash
python tooling/install.py --agent claude --scope user
python tooling/install.py --agent gemini --repo "/path/to/my-project"
python tooling/install.py --agent antigravity --scope user
python tooling/install.py --target "/path/to/another-agent/skills"
```

Evita instalar copias duplicadas en directorios que descubre el mismo agente. Gemini también admite `.agents/skills`, por lo que una instalación compartida de Codex quizá ya sea visible. Consulta la lista de habilidades del agente y pídele explícitamente que use `unified-development-standard`. Actualiza la detección o inicia una sesión nueva si es necesario. Copiar archivos y confirmar que el modelo los utiliza son comprobaciones distintas.

Las rutas se contrastaron con la documentación oficial el 2026-10-27: [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/), [Antigravity](https://antigravity.google/docs/skills). Estas interfaces pueden cambiar; no se afirma haber ejecutado una prueba real en cada plataforma.

### Lovable e interfaces en la nube

En Lovable, usa **Workspace settings → Skills → Add → Import from GitHub** y selecciona la [carpeta de la habilidad principal](https://github.com/iamaia-offcials/full-stack-enginer-skill/tree/main/.agents/skills/unified-development-standard). Según la [documentación de Lovable](https://docs.lovable.dev/features/skills), se requiere acceso de propietario o administrador del espacio de trabajo. Como alternativa, usa **Upload ZIP**.

Genera el archivo portátil:

```bash
python tooling/package.py
```

El resultado es `dist/unified-development-standard.zip`, que contiene el punto de entrada, referencias, guías, ejemplos y licencia. Importa el paquete completo: `SKILL.md` por sí solo no basta. Instalar en Claude Code no instala una habilidad en una cuenta de Claude en la nube; utiliza el método de importación admitido por esa cuenta. Este instalador no administra cuentas en la nube.

Si un agente tiene acceso a archivos pero no admite habilidades de forma nativa, pídele que lea el `SKILL.md` principal y las secciones enlazadas pertinentes. Sin acceso a archivos ni posibilidad de importación, las instrucciones deben proporcionarse en el chat; eso no es una instalación automática. La compatibilidad depende del entorno, no solo del nombre del modelo.

## Pedir a una IA que lo instale

Envía esta solicitud a un agente con acceso al terminal y a los archivos:

> Instala la habilidad de ingeniería de https://github.com/iamaia-offcials/full-stack-enginer-skill.git. Lee su README y su instalador. Elige el directorio de habilidades de esta herramienta y el alcance solicitado; si no se indica, usa el proyecto actual. Haz una simulación y después instala sin cambiar los archivos de instrucciones existentes del proyecto ni sobrescribir modificaciones locales. Verifica el SKILL.md y las referencias instalados e informa por separado de si el agente detecta la habilidad. Si no es posible instalar en el sistema de archivos, usa la importación documentada o explica la limitación concreta.

Para las interfaces en la nube, usa la importación de GitHub/ZIP indicada arriba. Una interfaz de chat no implica por sí sola la disponibilidad de un terminal con Python.

## Perfiles opcionales

El núcleo ya cubre todos los ámbitos. Instala perfiles solo si resultan útiles flujos de trabajo especializados independientes. El instalador siempre incluye el núcleo como dependencia.

```bash
python tooling/install.py --list
python tooling/install.py --agent codex --scope user --skills uds-security,uds-backend
python tooling/install.py --agent codex --scope user --skills all
```

Perfiles: `uds-product-discovery`, `uds-requirements-planning`, `uds-architecture`, `uds-design-system`, `uds-frontend`, `uds-web-development`, `uds-technical-seo`, `uds-backend`, `uds-data`, `uds-mobile-development`, `uds-performance-optimization`, `uds-dependency-upgrades`, `uds-code-review`, `uds-testing`, `uds-security`, `uds-git-cicd`, `uds-operations`, `uds-project-audit`.

## Ejemplos de uso

> Usa unified-development-standard. Planifica un portal de clientes: define la visión del producto y las reglas de negocio, delimita la primera versión, evalúa futuros equipos de personal y pagos, y elige las tecnologías. Explica qué bases están justificadas ahora y qué trabajo puede esperar.

> Usa unified-development-standard. Añade un campo de correo electrónico al CRM existente. Reutiliza su componente y contrato, comprueba la validación del servidor y los permisos, actualiza la documentación actual de la funcionalidad y ejecuta las comprobaciones pertinentes.

## Actualización, recuperación y desinstalación

En tu copia local del repositorio, descarga los cambios y repite la instalación con el mismo agente, alcance y selección de habilidades:

```bash
git pull --ff-only
python tooling/install.py --agent codex --scope user --update --dry-run
python tooling/install.py --agent codex --scope user --update
```

Si instalaste perfiles, incluye la misma selección de `--skills` al actualizar. El instalador registra los hashes de los archivos y se detiene ante modificaciones locales o archivos añadidos. Conserva y concilia esos cambios antes de actualizar. Para adoptar una instalación anterior sin manifiesto, revisa primero sus archivos y después usa explícitamente:

```bash
python tooling/install.py --agent codex --scope user --update --adopt-existing --dry-run
python tooling/install.py --agent codex --scope user --update --adopt-existing
```

`--adopt-existing` sustituye las carpetas de habilidades correspondientes y conserva los archivos anteriores en `.uds-backups/`, junto al directorio `skills/`. No omite la protección de las instalaciones gestionadas que se han modificado. Los fallos normales de sustitución provocan una reversión; tras una interrupción del proceso o un corte eléctrico, recupera desde la copia de seguridad. Antes de una recuperación manual, conserva la carpeta actual y después restaura la copia elegida con el nombre original de la habilidad.

Para desinstalar, elimina únicamente la carpeta instalada de la habilidad seleccionada. Eliminar el núcleo rompe los perfiles que dependen de él. Las habilidades en la nube se deben eliminar mediante su propia configuración. Nunca elimines habilidades ajenas.

Los enlaces simbólicos, las uniones de directorio y las rutas con puntos de reanálisis se rechazan intencionadamente. Si un fallo deja `.uds-install.lock`, asegúrate primero de que no haya ningún instalador en ejecución y elimina únicamente ese archivo de bloqueo.

## Repositorio y validación

```text
README.md                       Descripción principal e instalación en inglés
LICENSE                         MIT
.agents/skills/
  unified-development-standard/ Núcleo, reglas, guías, plantillas y ejemplos
  uds-*/SKILL.md                 Flujos de trabajo especializados opcionales
docs/i18n/                      Traducciones del README público
docs/REVIEW.md                   Evidencias y limitaciones de la revisión actual
tooling/                        Instalador, empaquetado, validación y evaluación
tests/                          Pruebas de regresión del sistema de archivos y paquetes
```

```bash
python tooling/validate_suite.py
python -m unittest discover -s tests -v
python tooling/package.py
```

Estas comprobaciones cubren metadatos, enlaces locales, identificadores de reglas, instalación, protección durante las actualizaciones y portabilidad del archivo. No demuestran un comportamiento correcto en todos los agentes ni la seguridad de una aplicación. Consulta la [revisión](../REVIEW.md) y la [guía de evaluación del comportamiento](../../tooling/EVALUATION_GUIDE.md).

Para contribuir: edita la regla canónica, conserva su identificador e incluye explicaciones y ejemplos útiles, además de un escenario reproducible para los cambios de comportamiento. Actualiza la documentación existente en su ubicación actual. Mantén las traducciones del README alineadas con el inglés; no traduzcas ni dupliques la habilidad instalada para cada idioma.

## Licencia y límites

[MIT](../../LICENSE). Los documentos de terceros enlazados conservan sus propias condiciones. Las referencias a estándares o empresas no implican certificación ni respaldo.

La habilidad no garantiza la seguridad de una aplicación, su posición en buscadores, el cumplimiento legal ni la ausencia de futuras migraciones. Estos aspectos requieren verificación específica para cada proyecto. No concede herramientas, cuentas ni permiso para publicar u operar sistemas de producción.
