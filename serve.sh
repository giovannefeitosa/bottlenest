function goServe() {
  local HERE=$(cd $(dirname $0); pwd)
  cd $HERE
  export PYTHONPATH="$PYTHONPATH:$HERE/src"
  
  flask --app examples.helloworld.main:bootstrap run
}

( goServe )
