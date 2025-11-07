# PA3: 안전한 Python 빌트인 래퍼 에이전트

Python의 내장 함수(built-in functions)를 안전하게 래핑(wrapping)하여, LLM과 같은 외부 에이전트가 제한된 환경에서 코드를 실행하고 질의에 응답할 수 있도록 돕는 예제 프로젝트입니다.

## 주요 아이디어

- **안전한 래핑**: `wrapped_builtins.py` 파일은 `print()`, `len()` 등 표준 Python 내장 함수를 `w_` 접두사가 붙은 함수(예: `w_print`, `w_len`)로 감쌉니다. 데코레이터를 사용해 원본 함수의 시그니처를 보존하므로, 에이전트가 함수를 쉽게 이해하고 사용할 수 있습니다.
- **제한된 환경**: `pa3_initial.py`의 `ChatAgent`는 `tools` 매개변수로 전달된 함수들만 도구로 사용할 수 있습니다. 이를 통해 `eval`이나 `exec`처럼 위험할 수 있는 함수는 제외하고, 허용된 기능만 선택적으로 노출할 수 있습니다.

## 파일 구조

- `pa3_initial.py`: `ChatAgent`를 초기화하고 실행하는 메인 스크립트입니다.
- `wrapped_builtins.py`: 내장 함수를 래핑하고, 에이전트에 제공할 함수 목록(`wrapped_builtins`)을 관리합니다.
- `README.md`: 프로젝트 설명서입니다.
- `.gitignore`: Git에서 추적하지 않을 파일 목록입니다.

## 요구사항

- Python 3.8 이상
- `python-dotenv`: `.env` 파일에서 환경 변수를 불러올 때 사용합니다.
- `openai`: OpenAI API와 상호작용합니다.
- `agent-framework`: Microsoft의 AI 에이전트 프레임워크입니다. [공식 GitHub](https://github.com/microsoft/agent-framework)에서 더 많은 정보를 확인할 수 있습니다.

**의존성 설치 (가상환경 권장):**
```bash
# Python 가상환경 생성 및 활성화
python3 -m venv .venv
source .venv/bin/activate

# requirements.txt 파일로부터 의존성 설치
# 참고: agent-framework는 사전 출시(pre-release) 버전 설치가 필요할 수 있습니다.
pip install -r requirements.txt --pre
```

## 설정

프로젝트 실행을 위해 OpenAI API 정보가 필요합니다. 루트 디렉터리에 `.env` 파일을 생성하고 아래와 같이 환경 변수를 설정하세요.

```env
# .env 파일 예시
OPENAI_MODEL_NAME="gpt-4o"
OPENAI_API_KEY="sk-..."
OPENAI_ENDPOINT="https://api.openai.com/v1"
```

## 사용법

환경 변수 설정이 완료되었다면, 터미널에서 아래 방법으로 에이전트를 실행할 수 있습니다.

**1. 인자로 직접 쿼리 전달**
```bash
python pa3_initial.py "1 + 1"
```

**2. 대화형 모드로 실행**
```bash
python pa3_initial.py
# Query: 0.043 - 0.001
```

**3. 파이프(`|`)로 입력 전달**
```bash
echo "2 * 3" | python pa3_initial.py
```

`pa3_initial.py`는 `ChatAgent`를 생성하고 `run()` 함수를 호출하여 질의를 처리합니다. 결과는 `Response:`와 함께 표준 출력으로 표시됩니다.

## 확장 방법

`wrapped_builtins`에 새로운 함수를 추가하려면:

1.  `wrapped_builtins.py` 파일에 `@wrap_builtin` 데코레이터를 사용해 새 `w_<name>` 함수를 정의합니다.
2.  생성한 함수를 `wrapped_builtins` 리스트에 추가합니다.
3.  `pa3_initial.py`에서 `tools` 매개변수로 해당 함수명을 전달하거나, 리스트 전체를 넘겨주도록 수정합니다.

> **⚠️ 보안 경고**
> `eval`, `exec`과 같이 임의의 코드를 실행할 수 있는 함수를 에이전트에 노출하는 것은 심각한 보안 위험을 초래할 수 있습니다. 현재 코드에는 `w_eval`이 포함되어 있으니, 실제 운영 환경에서는 반드시 비활성화하거나 신중하게 사용해야 합니다.

## 저자

Byeongki Jeong

## 라이선스

This project is licensed under the MIT License.

**MIT License**

Copyright (c) 2025 Byeongki Jeong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

