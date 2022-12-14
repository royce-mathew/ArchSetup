import os
import subprocess
from pathlib import Path


class CommandManager:
    def __init__(self): # Constructor
        self.file_path = Path(__file__).parent.absolute() # Get Path of the running directory
        self.home_dir = os.path.expanduser('~') # Expand on the home directory


    def run_commands(self, command_list: list[str]):
        for command in command_list:
            subprocess.run(command.split(), cwd=self.file_path)


    def rewrite_setup(self): # Rewrites current directory config with os config
        setup_commands: list[str] = [
            f'cp -r nvim {self.home_dir}/.config/nvim/',
            f'cp .bashrc {self.home_dir}/',
            'fisher install IlanCosman/tide@v5',
        ]
        self.run_commands(setup_commands)


    def fresh_install(self): # Fresh Install all relevant packages 
        fresh_commands: list[str] = [
            'sudo pacman -Syu',
            'sudo pacman -S neovim',
            'sudo pacman -S fish',
            'curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher',
        ]

        self.run_commands(fresh_commands)


    def pull_data(self):
        pull_commands: list[str] = [
            f'cp {self.home_dir}/.bashrc .',
            f'cp -r {self.home_dir}/.config/nvim .',
        ]
        CommandManager.run_commands(pull_commands)



def main():
    print("*Welcome to Arch Setup*\n\nOptions:")
    print("1. Full Install")
    print("1. Package Install")
    print("2. Rewrite Packages")
    print("3. Pull Packages Locally")
    print("4. Exit")

    # os.chdir(file_path)

    s: str = str(input("Selected Option (4): "))
    cmd = CommandManager();

    match s:
        case '0':
            cmd.fresh_install()
            cmd.rewrite_setup()
        case '1': # Fresh Install Packages
            cmd.fresh_install()
        case '2': # Rewrite Entire Setup
            cmd.rewrite_setup()
        case '3':
            cmd.pull_data() # Pull local files / directories 
        case _: # Default
            print("Exited Program")
            return
            


if __name__ == "__main__":
    try:
        main();
    except KeyboardInterrupt:
        print("Exited")
        pass