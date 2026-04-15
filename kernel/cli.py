import os
import sys
import time

# Add project root to sys.path to allow absolute imports
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
if project_root not in sys.path:
    sys.path.append(project_root)

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich import box

# Import TAMO modules
try:
    from kernel.mission_architect import MissionArchitect
    from kernel.mission_runner import MissionRunner
    from kernel.tools import TAMOTools
except ImportError:
    # Fallback for direct execution if the above fails
    from mission_architect import MissionArchitect
    from mission_runner import MissionRunner
    from tools import TAMOTools

console = Console()

def get_header():
    ascii_logo = """
 ████████╗ █████╗ ███╗   ███╗ ██████╗ 
 ╚══██╔══╝██╔══██╗████╗ ████║██╔═══██╗
    ██║   ███████║██╔████╔██║██║   ██║
    ██║   ██╔══██║██║╚██╔╝██║██║   ██║
    ██║   ██║  ██║██║ ╚═╝ ██║╚██████╔╝
    ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ 
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
    table.add_row(Text("SYSTEM", style="dim"), Text("TAMO_KERNEL_STABLE", style="bold green"))
    table.add_row(Text("LATENCY", style="dim"), Text("120ms", style="bold yellow"))
    return Panel(table, title="[bold white]Session Status[/]", border_style="dim")

def get_workflow_menu():
    table = Table(box=None, show_header=False, padding=(0, 2))
    table.add_row(Text("/recon", style="bold cyan"), Text("Market Intelligence Strike & Gap Extraction", style="dim"))
    return Panel(table, title="[bold white]Active Recon Protocol[/]", border_style="dim")

def check_credentials():
    tools = TAMOTools()
    if not tools.exa_key or not tools.firecrawl_key:
        console.print(Panel(
            Text("MISSION DELAYED: API Credentials Missing", style="bold yellow", justify="center"),
            subtitle="[dim]Configuration Required[/]",
            style="yellow"
        ))

        setup = console.input("[bold cyan]?[/] [white]Start automated credential setup? (y/n): [/]").lower()
        if setup == 'y':
            exa = console.input("[bold cyan]>[/] [white]Enter EXA_API_KEY: [/]")
            fire = console.input("[bold cyan]>[/] [white]Enter FIRECRAWL_API_KEY: [/]")

            if exa or fire:
                tools.update_credentials(exa if exa else None, fire if fire else None)
                console.print("[bold green]✔[/] Kernel updated. Initializing squads...\n")
                time.sleep(1)
                return True
        else:
            console.print("[dim]Proceeding in simulation mode (offline)...[/]\n")
            time.sleep(1)
    return False

def main_loop():
    console.clear()
    console.print(get_header())

    # Check for credentials before showing menu
    check_credentials()

    layout = Layout()
    layout.split_row(
        Layout(get_session_info(), name="left", ratio=1),
        Layout(get_workflow_menu(), name="right", ratio=2)
    )

    console.print(layout)
    console.print("\n[bold cyan]>[/] [white]Ready for mission input...[/]")

    # Simulation for demonstration
    cmd = console.input("[bold cyan]TAMO[/] @ [white]mission_control[/] > ")
    if cmd.startswith("/recon"):
        target = cmd.split(" ")[1] if len(cmd.split(" ")) > 1 else "unknown_target"
        console.print(f"\n[bold cyan]MISSION INITIATED:[/] [white]Targeting {target}[/]\n")

        # Execute the mission through agent harmony
        runner = MissionRunner()
        mission_output = runner.run_mission(target)

        # Generate the reports (MD and HTML)
        architect = MissionArchitect(project_root)
        
        md_path, html_path = architect.generate_report(
            "The Scout (Recon Squad)", 
            target, 
            mission_output
        )

        console.print(f"\n[bold green]✔[/] MISSION COMPLETE.")
        console.print(f"[bold white]FEYNMAN REPORT (MD):[/] [cyan]{md_path}[/]")
        console.print(f"[bold white]FINAL NOIR REPORT (HTML):[/] [cyan]{html_path}[/]")

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
    
    assets_dir = os.path.join(project_root, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    screenshot_path = os.path.join(assets_dir, "terminal_preview.svg")
    
    export_console.save_svg(screenshot_path, title="TAMO Intelligence Squad")
    console.print(f"[bold green]✔[/] Screenshot exported to [bold]{screenshot_path}[/]")

if __name__ == "__main__":
    if "--screenshot" in sys.argv:
        export_screenshot()
    else:
        main_loop()
