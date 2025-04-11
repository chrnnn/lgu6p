# 파일이 바뀌었을 때만 커밋
if git diff --quiet && git diff --cached --quiet; then
  echo "커밋할 변경 사항이 없습니다."
else
  # 커밋 메시지 입력
  read -p "커밋 메시지를 입력하세요: " user_message

  # KST 시간 (UTC+9) 가져오기
  current_time=$(TZ=Asia/Seoul date "+%Y-%m-%d %H:%M:%S")

  # 최종 커밋 메시지
  commit_message="$user_message | $current_time (KST)"

  # Git 명령어 실행
  git add .
  git commit -m "$commit_message"
  git push
fi