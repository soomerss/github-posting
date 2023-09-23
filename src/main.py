from crawler import *
from githubController import *
from imageEditor import *
from textCreator import *
from datetime import datetime

def image_uploader(repo,img_urls):
    for url in img_urls:
        img_name, resized_image_content = image_edior(url)
        create_img_files(repo,img_name,resized_image_content,new_branch_name)

if __name__ == '__main__':
    # 크롤러 생성 -> blog data 추출
    crawler = BlogCrawler()
    pars_datas = crawler.soup_parser()

    # github 레포 생성
    repo = create_github_repo(repo_name)

    # new_post_checker
    if new_post_checker(repo,pars_datas):
        # github 브랜치 생성
        create_branch(repo,base_branch_name,new_branch_name)
        # github new_branch img 폴더 삭제
        delete_files(repo,new_branch_name)

        # img urls 추출
        img_urls = create_img_url(pars_datas)

        # github img 업로드
        image_uploader(repo,img_urls)

        # readme text 생성
        table_txt = create_table_text(pars_datas)
        readme_txt = create_readme(table_txt)
        # readme_update
        final_readme_update(repo,readme_txt,new_branch_name)

        # branch_merge
        repo_merge(repo,base_branch_name,new_branch_name)
        print("완료 되었습니다.")
    else:
        print("새로운 게시물이 없습니다.")
