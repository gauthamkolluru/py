import os
import sys
import subprocess


class GitPullPush:
    def set_root_dir(self):
        if sys.platform == 'win32':
            return f'C:\\Users\\{os.environ["USERNAME"]}\\Documents'
        return f'/home/{os.environ["USER"]}/Documents/'


    def find_local_repos(self):
        self.root_dir = self.set_root_dir()
        return [directory for directory in os.listdir(self.root_dir) if os.path.exists(
            os.path.join(os.path.join(self.root_dir, directory), '.git'))]

    def git_pull_all(self):
        self.dir_list = self.find_local_repos()
        for directory in self.dir_list:
            subprocess.run(['git','pull'], cwd=os.path.join(self.set_root_dir(), directory), shell=True)
        return "ok"

    def find_modified_repos(self):
        self.dir_list = self.find_local_repos()
        for directory in self.dir_list:
            for content in os.listdir(os.path.join(self.set_root_dir(),directory)):
                print(content)
            break
        return ""


if __name__ == "__main__":
    git_obj = GitPullPush()
    # git_obj.git_pull_all()
    git_obj.find_modified_repos()