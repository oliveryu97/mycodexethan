# mycodexethan

My personal code experiment repository.

## 🛠️ Tools Included

| File | Description |
|------|-------------|
| `weather.py` | CLI weather tool using Open-Meteo free API |
| `todo.py` | Simple TODO list manager |
| `backup.sh` | Bash backup script |

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/oliveryu97/mycodexethan.git
cd mycodexethan

# Weather usage
python weather.py --city "Tokyo" --lat 35.6762 --lon 139.6503

# TODO usage
python todo.py add --task "Learn Python"
python todo.py list
python todo.py done --id 1

# Backup
bash backup.sh
```

## 📍 Weather Tool

Get current weather for any location:
```bash
python weather.py --lat 40.7128 --lon -74.0060 --city "New York"
```
Output: `📍 New York` / `🌤️  22°C, Clear, Wind: 12 km/h`

## ✅ TODO Manager

Simple command-line TODO list:
```bash
python todo.py add --task "Buy milk"
python todo.py list
python todo.py done --id 1
python todo.py rm --id 1
```

## 📦 Backup Script

Creates timestamped tar.gz backups in `~/backups/`:
```bash
bash backup.sh
```

## 🤝 Contributing

Pull requests welcome! Feel free to fork and submit PRs.

## 📄 License

MIT License
