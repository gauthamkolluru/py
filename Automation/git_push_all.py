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

def find_modified_repos(dir_list):
    for directory in dir_list:
        dir_contents = os.listdir(os.path.join(set_root_dir(),directory))
        for content in dir_contents:
            
    return ""


print(find_local_repos(set_root_dir()))
