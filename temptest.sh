Z_NEXTVERSION="0.0.4"

function goTestIt() {
  local HERE=$(cd $(dirname $0); pwd)
  cd $HERE
  export PYTHONPATH="$PYTHONPATH:$HERE/src"
  #cd ../test-bottlenest
  #pip install bottlenest==$Z_NEXTVERSION 1> /dev/null || exit 1
  #python3 test.py
  # python3 examples/envFile/main.py
  # python3 examples/websocketsServer/main.py
  python3 examples/clitool/main.py
}

( goTestIt )
