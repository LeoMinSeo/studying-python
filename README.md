# 번역 채팅 애플리케이션

## 프로젝트 소개

이 프로젝트는 React를 기반으로 한 프론트엔드와 Flask를 기반으로 한 백엔드를 결합하여 실시간 번역 채팅 서비스를 구현한 애플리케이션입니다. 사용자가 입력한 텍스트를 자동으로 언어 감지 후 한국어-영어 또는 영어-한국어 번역을 제공합니다.

## 특징

- 직관적인 채팅 UI/UX를 통한 사용자 친화적 인터페이스
- 자동 언어 감지 기능 (한국어/영어)
- 양방향 번역 지원 (한국어 ↔ 영어)
- 두 가지 번역 방식 지원:
  - Selenium을 활용한 파파고 자동화 방식
  - DeepL API를 활용한 직접 번역 방식
- 실시간 번역 결과 표시
- 로딩 인디케이터로 번역 진행 상태 시각화

## 기술 스택

### 프론트엔드
- React.js
- CSS (반응형 디자인)

### 백엔드
- Flask (Python)
- DeepL API (번역 API)
- Selenium (웹 자동화)

## 구현 방법

이 프로젝트는 두 가지 번역 방식을 모두 구현했으며, 프론트엔드에서 백엔드 API 요청 주소만 변경하면 두 방식을 모두 사용할 수 있습니다.

### 1. 셀레니움을 활용한 웹 자동화 방식
처음에는 호기심으로 Selenium을 이용하여 네이버 파파고 번역 서비스를 자동화했습니다. 웹 브라우저 자동화를 통해 다음 과정을 수행합니다:

1. 네이버 검색창에서 '파파고' 검색
2. 텍스트 입력 필드에 사용자 메시지 입력
3. 언어 감지 후 필요시 언어 전환
4. 번역 결과 추출 및 반환
5. 헤드리스 모드로 브라우저 창 없이 실행 가능

### 2. DeepL API 활용 방법
이후 응답 속도 개선을 위해 DeepL API를 활용한 방식도 구현했습니다. API 키만 설정하면 직접 API를 통한 번역이 가능하며, 셀레니움 방식보다 훨씬 빠른 응답 속도를 제공합니다.

## 설치 및 실행 방법

### 필수 요구사항
- Node.js
- Python 3.6 이상
- Chrome 브라우저 (Selenium용)

### 프론트엔드 설치
```bash
# 프로젝트 클론
git clone https://github.com/yourusername/translation-app.git
cd translation-app

# 의존성 설치
npm install

# 개발 서버 실행
npm start
```

### 백엔드 설치
```bash
# Python 가상 환경 생성 및 활성화 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install flask flask-cors selenium python-dotenv requests

# DeepL API를 사용할 경우 .env 파일 생성
echo "DEEPL_API_KEY=your_api_key_here" > .env

# 서버 실행
python selenium_basic_2.py  # 파파고 기반 번역(Selenium 방식)
# 또는
python deepl.py  # DeepL API 기반 번역
```

### 번역 방식 전환 방법

프론트엔드에서 백엔드 API 요청 주소만 변경하면 두 가지 번역 방식을 모두 사용해볼 수 있습니다:

1. TranslationChat.js 파일에서 fetch 요청 URL을 변경:
   - Selenium 방식: `fetch("http://localhost:5000/datapost", ...)`
   - DeepL API 방식: `fetch("http://localhost:5000/transdata", ...)`

## 프로젝트 구조

```
translation-app/
├── src/
│   ├── TranslationChat.js     # 메인 채팅 컴포넌트
│   ├── TranslationChat.css    # 스타일시트
│   └── index.js               # 앱 진입점
└── PythonProject/
    └── 0228/
        ├── selenium_basic.py     # Selenium 기본 테스트
        ├── selenium_basic_2.py   # 파파고 기반 번역 서버
        └── deepl.py              # DeepL API 기반 번역 서버
```

## 개발 동기

이 프로젝트는 학습 목적으로 개발되었으며, 특히 Selenium을 이용한 웹 자동화에 대한 호기심과 React 프론트엔드 개발에 대한 이해를 높이기 위해 시작되었습니다. 

처음에는 Selenium을 사용하여 네이버 파파고를 자동화하는 방식으로 한국어를 영어로 번역하는 기능만 구현했습니다. 이후 언어 감지 기능을 추가하여 양방향 번역이 가능하도록 확장했으며, 마지막으로는 성능 개선을 위해 DeepL API를 활용한 방식도 구현했습니다.

두 가지 방식 모두 사용할 수 있도록 구현함으로써 웹 자동화와 API 활용의 차이를 비교할 수 있게 되었습니다.

## 향후 계획

- 모바일 애플리케이션으로 개발하여 핸드폰에서 사용할 수 있도록 구현
- React Native 또는 Flutter를 활용하여 크로스 플랫폼 앱으로 전환
- 오프라인에서도 사용 가능한 기능 추가
- 음성 인식을 통한 번역 기능 추가


---

*이 프로젝트는 학습 목적으로 개발되었으며, 개인적인 흥미와 웹 자동화에 대한 탐구를 위해 만들어졌습니다.*
