import os
import sys
import subprocess


class GitPullPush:
    def set_root_dir(self):
        if sys.platform == 'win32':
            return f'C:\\Users\\{os.environ["USERNAME"]}\\Documents'
        return f'/home/{os.environ["USER"]}/Documents/'


    def find_local_repos(self, root_dir):
        return [directory for directory in os.listdir(root_dir) if os.path.exists(
            os.path.join(os.path.join(root_dir, directory), '.git'))]

    def git_pull_all(self, dir_list):
        for directory in dir_list:
            subprocess.run(['cd', os.path.join(self.set_root_dir(), directory)], shell=True)
            subprocess.run(['git','pull'], shell=True)
        return "ok"

    def find_modified_repos(self, dir_list):
        for directory in dir_list:
            for content in os.listdir(os.path.join(self.set_root_dir(),directory)):
                pass
        return ""


if __name__ == "__main__":
    git_obj = GitPullPush()
    git_obj.git_pull_all(git_obj.find_local_repos(git_obj.set_root_dir()))