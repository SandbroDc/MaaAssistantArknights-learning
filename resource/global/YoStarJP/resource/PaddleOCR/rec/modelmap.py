import onnx
model = onnx.load("inference.onnx")
print(onnx.helper.printable_graph(model.graph))