```markdown
# 无人机视觉定位系统

基于 树莓派4B + 摄像头 + OpenCV 实现的无人机视觉导航、目标检测与定位控制

## 项目介绍

本项目用于无人机自主视觉导航开发，包含：
- 摄像头实时图像采集
- 视觉目标识别与跟踪
- ArUco 码精准定位
- 光流估计（单目 / Mavlink）
- 支持 C++ 高性能运行 + Python 快速验证

## 项目结构

```
UAV-Vision-Project/
├── README.md              # 项目说明
├── .gitignore             # Git 忽略文件
├── requirements.txt       # Python 依赖
├── src/                   # 主源码目录（C++ 核心算法）
├── scripts/               # Python 测试 / 辅助脚本
└── docs/                  # 说明文档
```

## 环境依赖

### C++ 依赖
- OpenCV 4.x (C++)
- C++11 及以上
- CMake / Make

### Python 依赖
- Python 3.8+
- opencv-python
- torch
- ultralytics
- numpy

## 安装 Python 依赖

```bash
pip install -r requirements.txt
```

## C++ 编译与运行

```bash
mkdir build
cd build
cmake ..
make -j4
./drone_vision
```

## Python 演示运行

```bash
# 运行摄像头实时检测
python src/inference/video_demo.py --source 0
```

## 功能说明

- 摄像头视频流读取与显示
- 目标识别与跟踪
- ArUco 码精准定位
- 无人机定点悬停控制
- 视觉避障基础框架

## 硬件平台

- 树莓派 4B
- 树莓派 V2 摄像头
- 开源飞控（Pixhawk / PX4 / APM）
```
