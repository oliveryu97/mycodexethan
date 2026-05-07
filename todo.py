#!/usr/bin/env python3
"""Simple TODO list manager with JSON storage."""

import json
import os
import argparse

FILE = "todos.json"

def load_todos():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="TODO Manager")
    parser.add_argument("action", choices=["add", "list", "done", "rm"], help="Action")
    parser.add_argument("--task", help="Task description (for add)")
    parser.add_argument("--id", type=int, help="Task ID (for done/rm)")
    args = parser.parse_args()
    
    todos = load_todos()
    
    if args.action == "add":
        todos.append({"id": len(todos)+1, "task": args.task, "done": False})
        save_todos(todos)
        print(f"✓ Added: {args.task}")
        
    elif args.action == "list":
        print("\n📋 TODO List:")
        for t in todos:
            status = "✓" if t["done"] else "○"
            print(f"  [{t['id']}] {status} {t['task']}")
            
    elif args.action == "done":
        for t in todos:
            if t["id"] == args.id:
                t["done"] = True
                save_todos(todos)
                print(f"✓ Marked done: {t['task']}")
                break
                
    elif args.action == "rm":
        todos = [t for t in todos if t["id"] != args.id]
        save_todos(todos)
        print(f"✓ Removed task {args.id}")

if __name__ == "__main__":
    main()
