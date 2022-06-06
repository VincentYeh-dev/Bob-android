"""Run inference with a YOLOv5 model on images, videos, directories, streams

Usage:
    $ python path/to/object_detect.py --source path/to/img.jpg --weights yolov5s.pt --img 640
"""
from Bob.visual.detector.concrete.face_detect_deepface import FaceDetector
from Bob.visual.detector.concrete.object_detect_yolov5 import ObjectDetector
from Bob.visual.monitor.concrete.crt_camera import CameraMonitor
from constants import CommandControlListener
from device_config import getSerialBluetooth


print("Monitor start")
try:
    camera_monitor = CameraMonitor(0)
    camera_monitor.registerDetector(FaceDetector(1), False)
    camera_monitor.registerDetector(ObjectDetector(2, conf=0.4), False)
    package_device = getSerialBluetooth()
    package_device.setListener(CommandControlListener(package_device,camera_monitor))
    package_device.start()
except (KeyboardInterrupt, SystemExit):
    print("Interrupted!!")
