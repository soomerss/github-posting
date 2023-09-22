from github import Auth, Github
import os
from datetime import datetime
import requests
import base64

repo_name = 'soomerss/soomerss'
base_branch_name = 'main'
new_branch_name = f'{datetime.now().strftime("%Y%m%d")}post'

def create_github_repo(repo_name):
    """
    github Token을 통해 객체 생성
    :return: github repo
    """
    token = os.environ['MY_GITHUB_TOKEN']
    auth = Auth.Token(token)
    g = Github(auth=auth)
    return g.get_repo(repo_name)

def create_branch(repo, base_branch_name, new_branch_name):
    base_branch = repo.get_branch(base_branch_name)
    try:
        repo.create_git_ref(f"refs/heads/{new_branch_name}", base_branch.commit.sha)
        print("branch가 생성 되었습니다.")
    except:
        print("branch가 이미 생성 되었습니다.")

def delete_files(repo,new_branch_name):
    """
    :param g: github Object
    :param new_branch_name: new_branch_name
    :return:
    """
    for content in repo.get_contents('img', ref=new_branch_name):
        repo.delete_file(
            content.path,
            f"{datetime.now().strftime('%Y%m%d')}",
            content.sha,
            branch=new_branch_name
        )
    print(f"{new_branch_name}_delete")

def create_img_files(repo,img_url,new_branch_name):
    content_name = img_url.split('/')[-2]
    res = requests.get(img_url)
    image_content = res.content
    try:
        repo.create_file(
            path=f'img/{content_name}.png',
            message=f"Add img file {content_name} upload",
            content=image_content,
            branch=new_branch_name
        )
    except:
        print("이미 파일이 생성되었습니다.")

def repo_merge(repo,base_branch_name,new_branch_name):
    # main 브랜치로 이동하여 새 브랜치를 병합합니다.
    repo.merge(base_branch_name,new_branch_name,'merge_okay')

if __name__ == "__main__":
    # delete_files(create_github())
    create_img_files(create_github_repo(repo_name),'https://blog.kakaocdn.net/dn/bg5whL/btsvdr67yL5/2NEuVkFdDdzyRP5NtPEViK/img.jpg',new_branch_name)