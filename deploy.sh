# 파일이 바뀌었을 때만 커밋
if git diff --quiet && git diff --cached --quiet; then
  echo "Nothing to commit."
else
  echo "Enter commit message: "
  read msg
  git add .
  git commit -m "$msg"
  git push
fi
