function buildAndPublish() {
  rm -rf dist/
  poetry publish --build
}
( buildAndPublish )