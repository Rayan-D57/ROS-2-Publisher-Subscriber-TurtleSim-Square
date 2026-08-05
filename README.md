# ROS 2 Communication and TurtleSim Control

## Overview

This project consists of two tasks completed using ROS 2 Humble and Python.

The first task demonstrates communication between two ROS 2 nodes using the Publisher/Subscriber architecture, where one node continuously publishes a text message while another node receives and displays it.

The second task demonstrates controlling the TurtleSim robot by publishing velocity commands. The turtle moves forward and performs accurate 90-degree turns to successfully draw a square.

---

# Task 1 - Publisher & Subscriber

## Objective

The objective of this task is to understand the basic communication mechanism in ROS 2 using topics.

A Publisher node sends data to a topic, while a Subscriber node listens to the same topic and receives the published data.

---

## How Publisher & Subscriber Work

1. Create a Publisher node.
2. Create a Subscriber node.
3. Select a common topic for communication.
4. The Publisher continuously sends a text message.
5. The Subscriber receives and displays the same message.
6. The communication continues until the program is stopped.

---

## Running the Publisher

First, source the ROS 2 environment.
source /opt/ros/humble/setup.bash

Move to the project folder.
cd ~/turtle_scripts

Run the Publisher node.
python3 talker.py

The Publisher continuously sends the following message:
Engineer Rayan

---

## Running the Subscriber

Open another terminal.

Source ROS 2 again.
source /opt/ros/humble/setup.bash

Move to the project folder.
cd ~/turtle_scripts

Run the Subscriber.
python3 listener.py

The Subscriber receives the published message and displays it on the terminal.


---

## Subscriber Output

<img width="1919" height="1017" alt="Screenshot 2026-08-05 125441" src="https://github.com/user-attachments/assets/31522a0e-285d-4d79-bcfa-d87d6158a7d6" />


---

# Task 2 - TurtleSim Square

## Objective

The objective of this task is to control the TurtleSim robot using ROS 2.

The node publishes velocity commands to move the turtle forward and rotate it precisely until a complete square is drawn.

---

## How the Program Works

The program performs the following steps:

1. Initializes the ROS 2 node.
2. Creates a Publisher to send movement commands.
3. Creates a Subscriber to read the turtle's current position and orientation.
4. Waits until the turtle's position becomes available.
5. Adjusts the turtle's initial orientation.
6. Moves the turtle forward by a fixed distance.
7. Rotates the turtle exactly 90 degrees.
8. Repeats the process four times.
9. Stops the turtle after completing the square.

---

## Running TurtleSim

### 1. Source ROS 2
source /opt/ros/humble/setup.bash

### 2. Open the project folder
cd ~/turtle_scripts

### 3. Run TurtleSim
ros2 run turtlesim turtlesim_node

### 4. Run the square program
python3 turtle_square.py

The turtle automatically starts moving and draws a square.

---

## TurtleSim Terminal

<img width="1466" height="741" alt="Screenshot 2026-08-05 175856" src="https://github.com/user-attachments/assets/5ec8f3e9-b655-4125-959d-e839c773bc51" />

---

## TurtleSim Terminal 

<img width="1463" height="750" alt="Screenshot 2026-08-05 173306" src="https://github.com/user-attachments/assets/2356a1cc-c77c-4b8f-a135-d96bb66bd457" />

---

## TurtleSim Output

<img width="1254" height="1254" alt="photo_2026-08-05_20-39-05" src="https://github.com/user-attachments/assets/2a7f167b-d37f-486d-989e-30c6c8992f48" />

---

# Topics Used

| Topic | Description |
|---------|-------------|
| /chatter | Communication between Publisher and Subscriber |
| /turtle1/cmd_vel | Sends movement commands to the turtle |
| /turtle1/pose | Provides the turtle's current position and orientation |

---

# Technologies Used

- ROS 2 Humble
- Python 3
- TurtleSim
- geometry_msgs
- turtlesim
- std_msgs

---

# Learning Outcomes

- Understanding ROS 2 node architecture.
- Creating Publisher and Subscriber nodes.
- Learning how topics transfer data between nodes.
- Controlling TurtleSim using velocity commands.
- Reading the turtle's position and orientation.
- Drawing geometric shapes using ROS 2.



















