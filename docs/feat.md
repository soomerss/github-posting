## 최종 목표
- github action을 통해 매일 9시에 크롤러 트리거하여 데이터를 수집 및 Repo 업데이트

## 코드의 순차적 흐름
- github action을 통해 main()함수를 실행
- 크롤러를 통해 블로그 크롤링
- github repo Pull하여 branch 생성
- docs에는 기존 img 폴더 삭제 및 사용할 6개의 img파일 업로드
- template에 크롤러 문자열과 img조합하여 최종 .md생성
- github repo에 pr하여 main브랜치에 병합

## 기능
- 데이터 수집 크롤러 [ v ]
- Readme.md 문자열 만들기 [ v ]
- github repo pull 및 branch 생성 [ v ]
- 기존 img폴더 삭제 및 img 업로드 [ v ]
- 최종 .md 생성 [ v ]
- github repo main브랜치 병합 [ v ]
- github action template 작성 [ ]
