# Python Automatically moving files

## 설치
- python3 설치 [python3 설치](https://www.python.org/downloads/)
- vscode 설치 [vscode 설치](https://code.visualstudio.com/download)
- watchdog 설치 [watchdog 설치](https://python-watchdog.readthedocs.io/en/stable/)


## v1.0.0
해당 파이썬 스크립트의 로직입니다. 
watchdog 은 미리 인스톨을 해야합니다. 

- [x] 옮기고 싶은 위치에 Image, video 폴더를 만들어줍니다. 
- [x] 먼저 다운로드 폴더에 있는 모든 파일들을 읽어봅시다.
- [x] 모든 파일중에 폴더를 제외한 문서들을 파악합니다.
- [x] 파악된 문서들 중 그림/문서/pdf 등 을 확인합니다.
- [x] 확인된 문서의 이름을 변경합니다.
- [x] 변경된 문서를 각각의 폴더에 이동시켜줍니다.
- [x] 해당 작업은 다운로드 폴더에 변화가 있을 때 마다 자동으로 작동합니다.
- [ ] 백그라운드에서 작업해서 항상 돌아갑니다.