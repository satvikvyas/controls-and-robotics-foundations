# Controls and Robotics Foundations

A repository for simulation-based control systems projects. The focus is on implementing mathematical models (ODEs), classical control (PID), and modern control (LQR/State-Space) using Python.

**Current Maintainer:** satvik vyas

---

## Project Status

### 1. Second-Order System Simulation (Completed)

Modeled a standard mass-spring-damper system to analyze the effect of the damping ratio ($\zeta$) on stability and rise time.

* **Source:** `src/secondodsim.py`
* **Results:** Verified that $\zeta = 1.0$ (Critical Damping) provides the optimal balance between speed and stability, while $\zeta < 1.0$ introduces oscillation.
* **Plot:** See [link1](https://github.com/slimyshi/controls-and-robotics-foundations/blob/main/results/Figure_1.png) and [link2](https://github.com/slimyshi/controls-and-robotics-foundations/blob/main/results/Figure_2.png) for the step response analysis respectively.

### 2. PID Control & Trajectory Tracking (Completed)

Modeled a drone system with gravity and drag, with fixed target (10meters) and tracked path (10 + 5sin(t)) and analysed the impact of kp, kd and ki on the system. Added Feedforward prediction to eliminate phase lag during tracking.

### 3. 2D Waypoint Navigation (Completed)

Implemented a dual-PID control system to navigate a drone through a 2D environment across multiple waypoints using dynamic distance thresholds.

* **Results:** System successfully executed path tracking across coordinates [(0,0) -> (0,10) -> (15,10) -> (20,25)] with a 0.1m cornering tolerance.

### 4. State Space Representation (In Progress)
**source** = "src/state_space.py"
Transitioned the physics engine from scalar variables to a state-space matrix formulation ($\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$) to handle multi-variable physics (inertia and drag) simultaneously using NumPy.

---

## Usage

**1. Clone the repository**
```bash
git clone [https://github.com/slimyshi/controls-and-robotics-foundations.git](https://github.com/slimyshi/controls-and-robotics-foundations.git)