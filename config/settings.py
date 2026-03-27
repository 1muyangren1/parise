# ==============================================
# Parise 无人机视觉项目全局配置文件
# ==============================================

# ---------------------------
# 1. 模型相关配置
# ---------------------------
MODEL = {
    # YOLO 模型路径（支持本地路径或 ultralytics 内置模型名）
    "YOLO_MODEL_PATH": "yolov8n.pt",
    # 推理置信度阈值（低于此值的检测结果会被过滤）
    "CONF_THRESHOLD": 0.5,
    # IOU 阈值（NMS 非极大值抑制）
    "IOU_THRESHOLD": 0.45,
    # 推理设备："cpu" / "cuda" / "mps"
    "DEVICE": "cpu",
}

# ---------------------------
# 2. 视觉输入配置（摄像头/图片）
# ---------------------------
VISION = {
    # 摄像头 ID（0 为默认摄像头）
    "CAMERA_ID": 0,
    # 视频流分辨率
    "FRAME_WIDTH": 640,
    "FRAME_HEIGHT": 480,
    # 帧率
    "FPS": 30,
    # ArUco 码配置
    "ARUCO": {
        "DICT": "DICT_4X4_50",  # ArUco 字典类型
        "MARKER_SIZE": 0.1,    # 物理尺寸（米），用于位姿解算
    },
    # 相机内参（后续可替换为实际标定结果）
    "CAMERA_MATRIX": [
        [600, 0, 320],
        [0, 600, 240],
        [0, 0, 1]
    ],
    "DIST_COEFFS": [0, 0, 0, 0, 0],  # 畸变系数
}

# ---------------------------
# 3. 无人机飞控通信配置
# ---------------------------
DRONE = {
    # 连接方式："serial"（串口）/ "udp"（仿真）
    "CONNECTION_TYPE": "serial",
    # 串口配置（Windows 为 COMx，Linux 为 /dev/ttyUSBx）
    "SERIAL_PORT": "COM3",
    "BAUD_RATE": 57600,
    # UDP 配置（用于 SITL 仿真）
    "UDP_IP": "127.0.0.1",
    "UDP_PORT": 14550,
    # 飞行参数
    "TAKEOFF_ALTITUDE": 1.0,  # 起飞高度（米）
    "HOVER_ALTITUDE": 1.2,    # 悬停高度（米）
}

# ---------------------------
# 4. 日志与输出配置
# ---------------------------
LOGGING = {
    "LOG_LEVEL": "INFO",  # DEBUG / INFO / WARNING / ERROR
    "LOG_FILE": "logs/drone_vision.log",
    # 是否保存推理结果图片/视频
    "SAVE_OUTPUT": False,
    "OUTPUT_DIR": "output/",
}

# ---------------------------
# 5. 控制策略配置
# ---------------------------
CONTROL = {
    # 目标跟随模式："aruco" / "yolo"
    "FOLLOW_MODE": "aruco",
    # 位置控制 PID 参数
    "PID": {
        "KP": 0.5,
        "KI": 0.1,
        "KD": 0.2,
    },
    # 安全限制
    "MAX_SPEED": 2.0,        # 最大水平速度（m/s）
    "MAX_CLIMB_RATE": 1.0,   # 最大升降速度（m/s）
}