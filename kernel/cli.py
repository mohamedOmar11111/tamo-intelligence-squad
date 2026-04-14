import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich import box

console = Console()

def get_header():
    ascii_logo = """
 ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗
 ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
    INTELLIGENCE SQUAD v1.0.0
    """
    return Panel(
        Text(ascii_logo, style="bold cyan", justify="center"),
        style="cyan",
        box=box.DOUBLE
    )

def get_session_info():
    table = Table(box=None, show_header=False, padding=(0, 2))
    table.add_row(Text("MODEL", style="dim"), Text("anthropic/claude-3-5-sonnet", style="bold white"))
    table.add_row(Text("DIRECTORY", style="dim"), Text(os.getcwd(), style="bold white"))
    table.add_row(Text("SYSTEM", style="dim"), Text("ONYX_KERNEL_STABLE", style="bold green"))
    table.add_row(Text("LATENCY", style="dim"), Text("120ms", style="bold yellow"))
    return Panel(table, title="[bold white]Session Status[/]", border_style="dim")

def get_workflow_menu():
    table = Table(box=None, show_header=False, padding=(0, 2))
    table.add_row(Text("/recon", style="bold cyan"), Text("Deep Market Intelligence & Gap Analysis", style="dim"))
    table.add_row(Text("/ghost", style="bold cyan"), Text("Semantic Sovereignty & G.E.O Audit", style="dim"))
    table.add_row(Text("/vampire", style="bold cyan"), Text("Ad Strategy Extraction & Counter-Strike", style="dim"))
    table.add_row(Text("/forge", style="bold cyan"), Text("30-Day Nuclear Content Engineering", style="dim"))
    table.add_row(Text("/audit", style="bold cyan"), Text("Brand Voice & Compliance Verification", style="dim"))
    return Panel(table, title="[bold white]Command Protocols[/]", border_style="dim")
from kernel.mission_architect import MissionArchitect

console = Console()

def main_loop():
    console.clear()
    console.print(get_header())

    layout = Layout()
    layout.split_row(
        Layout(get_session_info(), name="left", ratio=1),
        Layout(get_workflow_menu(), name="right", ratio=2)
    )

    console.print(layout)
    console.print("\n[bold cyan]>[/] [white]Ready for mission input...[/]")

    # Simulation for demonstration
    cmd = console.input("[bold cyan]ONYX[/] @ [white]mission_control[/] > ")
    if cmd.startswith("/recon"):
        console.print("[dim]> initiating_recon_squad: sentinel_active[/]")
        console.print("[dim]> crawling_competitor_data...[/]")

        # Mock mission output
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        architect = MissionArchitect(project_root)

        target = cmd.split(" ")[1] if len(cmd.split(" ")) > 1 else "unknown_target"
        report_path = architect.generate_report(
            "The Scout (Recon Squad)", 
            target, 
            "### Competitor Audit\nFound 3 major vulnerabilities in pricing strategy.\n## Market Gap\nHigh demand for AI-integrated automation in localized sectors."
        )

        console.print(f"\n[bold green]✔[/] MISSION COMPLETE.")
        console.print(f"[bold white]REPORT GENERATED:[/] [cyan]{report_path}[/]")
def export_screenshot():
    # Use a separate console with a fixed width for the screenshot
    export_console = Console(width=120, record=True)
    export_console.print(get_header())
    
    layout = Layout()
    layout.split_row(
        Layout(get_session_info(), name="left", ratio=1),
        Layout(get_workflow_menu(), name="right", ratio=2)
    )
    
    export_console.print(layout)
    export_console.print("\n[bold cyan]>[/] [white]Ready for mission input...[/]")
    
    # Path relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(project_root, "assets")
    
    os.makedirs(assets_dir, exist_ok=True)
    screenshot_path = os.path.join(assets_dir, "terminal_preview.svg")
    
    export_console.save_svg(screenshot_path, title="Onyx Intelligence Squad")
    console.print(f"[bold green]✔[/] Screenshot exported to [bold]{screenshot_path}[/]")

if __name__ == "__main__":
    if "--screenshot" in sys.argv:
        export_screenshot()
    else:
        main_loop()
