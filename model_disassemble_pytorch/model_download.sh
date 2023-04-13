SRC_MODEL_PATH="./src/src_models"
mkdir $SRC_MODEL_PATH
wget -P $SRC_MODEL_PATH https://download.pytorch.org/models/resnet18-5c106cde.pth
wget -P $SRC_MODEL_PATH https://download.pytorch.org/models/resnet34-333f7ec4.pth
wget -P $SRC_MODEL_PATH https://download.pytorch.org/models/resnet50-19c8e357.pth
wget -P $SRC_MODEL_PATH https://download.pytorch.org/models/resnet101-5d3b4d8f.pth
wget -P $SRC_MODEL_PATH https://download.pytorch.org/models/resnet152-b121ed2d.pth