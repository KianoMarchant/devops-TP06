#!/bin/bash
set -e

echo "Postgres listo. Iniciando app..."
python3 -c "import app; app.init_db()" 2>/dev/null || true
exec "$@"
