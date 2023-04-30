mkdir worker_func
V=1.0.0
#build worker_func
cd worker_func
faas new func0 --lang python3-onnx 
mv func0.yml stack.yml
faas new func1 --lang python3-onnx --append stack.yml --version $V
faas new func2 --lang python3-onnx --append stack.yml --version $V
faas new func3 --lang python3-onnx --append stack.yml --version $V
faas new func4 --lang python3-onnx --append stack.yml --version $V
faas new func5 --lang python3-onnx --append stack.yml --version $V
cd ..

#build controller
faas new controller --lang python3-slim  --version $V
cd controller
echo request >> requirement.txt
echo numpy >> requirement.txt
