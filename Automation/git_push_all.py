import os
import sys
import subprocess


def set_root_dir():
    if sys.platform == 'win32':
        return f'C:\\Users\\{os.environ["USERNAME"]}\\Documents'
    return f'/home/{os.environ["USER"]}/Documents/'


def find_local_repos(root_dir):
    return [directory for directory in os.listdir(root_dir) if os.path.exists(
        os.path.join(os.path.join(root_dir, directory), '.git'))]

def git_pull_all(dir_list):
    for directory in dir_list:
        subprocess.run(['cd', os.path.join(set_root_dir(), directory)], shell=True)
        subprocess.run(['git','pull'], shell=True)
    return "ok"

def find_modified_repos(dir_list):
    for directory in dir_list:
        dir_contents = os.listdir(os.path.join(set_root_dir(),directory))
        for content in dir_contents:
            pass
    return ""


git_pull_all(find_local_repos(set_root_dir()))