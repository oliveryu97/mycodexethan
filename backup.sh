#!/bin/bash
# Simple backup script

BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

echo "📦 Creating backup..."
tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" . 2>/dev/null
echo "✅ Backup saved: backup_$DATE.tar.gz"

# Keep only last 5 backups
ls -t "$BACKUP_DIR"/backup_*.tar.gz | tail -n +6 | xargs -r rm
echo "🧹 Cleaned old backups"
