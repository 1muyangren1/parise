import cv2
from ultralytics import YOLO

# 加载模型
model = YOLO("yolov8n.pt")

# 用绝对路径，避免找不到图片
image_path = r"C:\Users\muyangren\Documents\GitHub\parise\test.png"

# 读取图片
img = cv2.imread(image_path)

# 推理
results = model(img)
annotated_img = results[0].plot()

# 显示结果
cv2.imshow("识别结果", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果
cv2.imwrite("result.png", annotated_img)
print("✅ 识别完成！结果已保存为 result.png")