## 🚀 블로그 게시물 자동 업데이트

### Blog
![blog_sample.png](docs%2Fblog_sample.png)
### Github
![github_sample.png](docs%2Fgithub_sample.png)
## ❗️개발 목적
- 블로그 게시물을 올리면 github에도 연동 될 수 있도록 하고 싶었습니다.

## 📜 작동 구조
![작동 구조.png](docs%2F%EC%9E%91%EB%8F%99%20%EA%B5%AC%EC%A1%B0.png)

## 🔦 기 능
- 매일 2시 15분에 github action 실행
- Blog에 새로운 게시물이 없다면 종료
- 새로운 게시물이 있다면, github 메인 화면의 Readme를 다루는 repo의 브랜치 생성,img폴더 삭제
- 새로운 Readme를 만들 문자열 생성
- README.md 파일 업데이트
- 브랜치 병합

## 🛠️ 개선 사항
- 조금 더 배운 후에 파이썬스럽게 고쳐보고 싶습니다.
- 나의 블로그가 아니더라도, 클래스명만 주어지면 동작하는 코드를 만들어 보고 싶습니다.