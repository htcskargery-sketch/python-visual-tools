import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"

def list_files():
    table = Table(title="📂 Beautiful Directory Listing", box=box.ROUNDED, header_style="bold magenta")
    
    table.add_column("Type", justify="center")
    table.add_column("Name", style="cyan")
    table.add_column("Size", justify="right", style="green")
    table.add_column("Modified", justify="right", style="blue")

    try:
        items = sorted(os.listdir('.'), key=lambda x: (not os.path.isdir(x), x.lower()))
        for item in items:
            stats = os.stat(item)
            is_dir = os.path.isdir(item)
            icon = "📁" if is_dir else "📄"
            color = "bold yellow" if is_dir else "white"
            size = "-" if is_dir else format_size(stats.st_size)
            mtime = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            table.add_row(icon, f"[{color}]{item}[/]", size, mtime)
        console.print(table)
        console.print(f"\n[bold green]Total items:[/] {len(items)}")
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")

if __name__ == "__main__":
    list_files()
