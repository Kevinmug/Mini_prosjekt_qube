# Quanser Qube Servo 2 – ROS2 Mini Project

This project implements a ROS2-based system for modeling, visualizing, and controlling a **Quanser Qube Servo 2**.

---

## Packages

### `qube_description`

Contains the URDF/Xacro model of the Qube.

**Features:**

* Visualized in RViz2
* Includes:

    * Base
    * Rotor (disk)
    * Angle indicator

**Run:**

```bash
ros2 launch qube_description view_qube.launch.py
```

---

### `qube_bringup`

Launches the full system.

**Starts:**

* `robot_state_publisher`
* RViz
*  Controller and hardware interfaces

---

### `pid_controll`

PID controller for the Qube.

**Topics:**

* Subscribes to: `measured_angle`
* Publishes to: `voltage`

**Parameters:**

* `p`
* `i`
* `d`
* `reference`

**Run with parameters:**

```bash
ros2 launch pid_controll controller.launch.py p:=2.0 i:=0.1 d:=0.5 reference:=1.57
```

---

### `qube_controller`

Basic controller node (template / extension point).

---

### `joint_state_publisher_gui`

Used for simulation of joint movement in RViz.

**Run:**

```bash
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

---

## Build Instructions

```bash
cd C:\pixi_ws
pixi shell
call ros2-windows\local_setup.bat
colcon build --base-paths src
call install\local_setup.bat
```

---

## Visualization

Start Qube model:

```bash
ros2 launch qube_description view_qube.launch.py
```

Start joint GUI:

```bash
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

Move the slider to see the disk rotate in RViz.

---

## Notes

* Hardware driver (`qube_driver`) may not work locally without proper device setup
* Simulation is done using `joint_state_publisher_gui`
