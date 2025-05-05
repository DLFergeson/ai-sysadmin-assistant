"""
Entry point for AI Assistant. Selects CLI or GUI mode.
"""

import argparse
from modes.cli_mode import run_cli
from modes.gui_mode import run_gui

def main():
    """Main function to launch CLI or GUI based on user input."""
    parser = argparse.ArgumentParser(description="AI Assistant for System Admins and Network Engineers")
    parser.add_argument('--mode', choices=['cli', 'gui'], default='cli', help='Run mode: cli or gui')
    args = parser.parse_args()

    if args.mode == 'cli':
        run_cli()
    else:
        run_gui()

if __name__ == '__main__':
    main()
