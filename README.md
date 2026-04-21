🚗 Autonomous AI Car Simulation using Deep Learning
A complete end-to-end self-driving car simulation built using Computer Vision + Deep Learning, where an AI model learns to drive autonomously by observing a simulated environment.

📌 Project Overview
This project simulates a self-driving car system where:

A virtual car navigates a road with obstacles
Training data is generated automatically
A CNN model learns steering behavior
The trained model drives the car in real-time
👉 This mimics real-world autonomous driving pipelines at a simplified level.

🎯 Why I Built This
To understand how self-driving systems work
To implement a full ML pipeline (data → training → inference)
To combine simulation + deep learning
To build a real-time AI system from scratch
⚙️ Tech Stack
Python
Pygame (Simulation)
OpenCV (Image processing)
TensorFlow / Keras (Deep Learning)
NumPy
🧠 System Architecture
Simulation → Data Collection → Dataset (X, y)
            ↓
        CNN Training
            ↓
      Trained Model (.h5)
            ↓
     Real-Time AI Driving
🗂️ Project Structure
car_game/
│
├── collect_data.py     # Data generation using simulation
├── train_model.py      # CNN model training
├── run_ai_car.py       # AI driving using trained model
├── check_data.py       # Dataset analysis
│
├── data/
│   ├── X.npy           # Images (features)
│   └── y.npy           # Steering labels
│
├── model.h5            # Trained model
├── .gitattributes      # Git LFS config
├── .gitignore
└── README.md
🔄 Workflow (End-to-End)
1️⃣ Data Collection (collect_data.py)
Simulation built using Pygame

Car moves automatically with obstacle avoidance logic

Frames captured from screen

Labels generated:

-1 → Left
0 → Straight
1 → Right
Key Optimization:
Captures frame every 5 iterations → reduces redundancy
frame_count += 1
if frame_count % 5 == 0:
📌 Data saved as:

X.npy → images
y.npy → labels
2️⃣ Dataset Analysis (check_data.py)
Used to verify dataset balance:

np.sum(y == -1)
np.sum(y == 1)
np.sum(y == 0)
Ensures model doesn't become biased.

3️⃣ Model Training (train_model.py)
Steps:
Load dataset
Shuffle data
Normalize input
Train CNN
Model Architecture:
Conv2D (24 filters)
Conv2D (36 filters)
Conv2D (48 filters) ✅ improvement
Dense layers
model.add(Conv2D(24,(5,5), activation='relu'))
model.add(Conv2D(36,(5,5), activation='relu'))
model.add(Conv2D(48,(3,3), activation='relu'))
Loss function:

loss = 'mse'
📌 Output:

Continuous steering value
4️⃣ AI Driving (run_ai_car.py)
Key Features:
🔹 Look-Ahead Vision
img = screen[200:600]
→ Model sees upcoming road

🔹 Prediction
prediction = model.predict(img)
🔹 Decision Thresholds
< -0.2 → Left
> 0.2 → Right
🔹 Safety Override (VERY IMPORTANT)
If obstacle too close:

Ignore AI
Perform emergency dodge
🔹 Movement Smoothing
if move == 0:
    move = last_move
👉 Prevents jittery movement

▶️ How to Run
Step 1: Install Dependencies
pip install numpy pygame opencv-python tensorflow scikit-learn
Step 2: Generate Data
python collect_data.py
Step 3: Train Model
python train_model.py
Step 4: Run AI Car
python run_ai_car.py
Step 5: Check Dataset (Optional)
python check_data.py
📦 Large File Handling
This project uses Git LFS for:

.npy
.h5
Clone with:

git lfs pull
🚀 Key Features
Real-time AI decision making
Automatic dataset generation
Custom CNN model
Collision avoidance system
Smooth driving control
⚠️ Challenges Faced
Large dataset handling (Git LFS required)
Model instability due to imbalance
Real-time prediction latency
Noise in training data
🔮 Future Improvements
Reinforcement Learning (DQN / PPO)
Better lane detection
Multi-car simulation
Web-based visualization
⭐ Support
If you like this project:

⭐ Star the repo
🍴 Fork it
💡 Contribute
