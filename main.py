from src.models.yolo_model import YOLOModel
from src.drone.mavlink import DroneController

def main():
    model = YOLOModel()
    print("✅ 模型加载完成")
    drone = DroneController()
    print("✅ 无人机系统启动完成")

if __name__ == "__main__":
    main()