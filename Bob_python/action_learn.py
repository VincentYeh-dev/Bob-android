from Bob.robot.concrete.crt_dynamixel import Dynamixel
from Bob.robot.concrete.crt_robot import DynamixelRobotAdaptor
from Bob.robot.concrete.servo_agent import CSVServoAgent
from Bob.serial_config import getSerialNameByDescription

bot_description = ".*FT232R.*"
agent = CSVServoAgent("servos.csv")
dynamixel = Dynamixel(getSerialNameByDescription(bot_description), 57600)
for servo in agent.getDefinedServos():
    dynamixel.appendServo(servo)

dynamixel.open()
for servo in agent.getDefinedServos():
    dynamixel.enableToque(servo.getId(), False)
print("Enable torque")
input()
for servo in agent.getDefinedServos():
    dynamixel.enableToque(servo.getId(), True)

for servo in agent.getDefinedServos():
    pos = dynamixel.getPresentPosition(servo.getId())
    print(f"ID#{servo.getId()} Position:{pos}")
dynamixel.close()