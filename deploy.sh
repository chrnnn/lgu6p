#!/bin/bash

# 변경 사항이 없으면 종료
if git diff --quiet && git diff --cached --quiet; then
  echo "커밋할 변경 사항이 없습니다."
  exit 0
fi

# 커밋 메시지 입력
read -p "커밋 메시지를 입력하세요: " user_message

# 현재 시간 (KST)
current_time=$(TZ=Asia/Seoul date "+%Y-%m-%d %H:%M:%S")

# 운영체제 및 버전 감지
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        os_type="$NAME $VERSION"
    else
        os_type="Linux (Unknown Version)"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    os_type="macOS $(sw_vers -productVersion)"
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    if command -v systeminfo &> /dev/null; then
        win_version=$(systeminfo | grep -E "^OS Name|^OS Version" | tr '\n' ' ' | sed 's/^.*OS Name: //; s/ OS Version:/ \(/; s/$/\)/')
        os_type="Windows $win_version"
    else
        os_type="Windows (Version Unknown)"
    fi
else
    os_type="Unknown OS"
fi

# 최종 커밋 메시지
commit_message="$user_message | $current_time (KST) | $os_type"

# Git 명령어 실행
git add .
git commit -m "$commit_message"
git push
