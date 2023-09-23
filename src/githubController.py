from github import Auth, Github
import os
from datetime import datetime
import requests
import re


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

def new_post_checker(repo,pars_datas):
    readme = repo.get_readme()
    readme_text = readme.decoded_content.decode('utf-8')
    date_pattern = r'\d{4}\.\s\d+\.\s\d+\.'
    dates = re.findall(date_pattern, readme_text)
    github_date = datetime.strptime(dates[0], '%Y. %m. %d.')
    blog_date = datetime.strptime(pars_datas[0][0], '%Y. %m. %d.')
    if github_date < blog_date:
        return True
    else:
        return False


def delete_files(repo,new_branch_name):
    """
    :param repo: github repo
    :param new_branch_name: new_branch_name
    :return:
    """
    try:
        for content in repo.get_contents('img', ref=new_branch_name):
            repo.delete_file(
                content.path,
                f"{datetime.now().strftime('%Y%m%d')}",
                content.sha,
                branch=new_branch_name
            )
        print(f"{new_branch_name}_delete")
    except:
        print(f"{new_branch_name}가 이미 삭제되었습니다.")

def create_img_files(repo,img_name,img_content,new_branch_name):
    try:
        repo.create_file(
            path=f'img/{img_name}.png',
            message=f"Add img file {img_name} upload",
            content=img_content,
            branch=new_branch_name
        )
    except:
        print(f"이미 {img_name}파일이 생성되었습니다.")

def final_readme_update(repo,readme_txt,new_branch_name):
    readme = repo.get_readme(ref=new_branch_name)
    try:
        repo.update_file(
            path=readme.path,
            message="Update README",
            content=readme_txt,
            sha=readme.sha,
            branch=new_branch_name
        )
    except:
        print("readme_update 오류 발생")

def repo_merge(repo,base_branch_name,new_branch_name):
    # main 브랜치로 이동하여 새 브랜치를 병합합니다.
    repo.merge(base_branch_name,new_branch_name,'merge_complete')



