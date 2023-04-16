faas new func0 --lang python3-onnx 
mv func0.yml stack.yml
faas new func1 --lang python3-onnx --append stack.yml
faas new func2 --lang python3-onnx --append stack.yml
faas new func3 --lang python3-onnx --append stack.yml
faas new func4 --lang python3-onnx --append stack.yml
faas new funcrq --lang python3 --append stack.yml