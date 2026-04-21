import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from sklearn.utils import shuffle

# 1. Load data
X = np.load("data/X.npy")
y = np.load("data/y.npy")

# 2. Shuffle data (IMPORTANT)
X, y = shuffle(X, y)

# 3. Normalize
X = X / 255.0 

# 4. Build model
model = Sequential()

model.add(Conv2D(24,(5,5), activation='relu', input_shape=(66,200,3)))
model.add(Conv2D(36,(5,5), activation='relu'))

# ✅ Improvement: extra layer
model.add(Conv2D(48,(3,3), activation='relu'))

model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(1))

# 5. Compile
model.compile(optimizer='adam', loss='mse')

# 6. Train with validation
model.fit(X, y, epochs=10, validation_split=0.2)

# 7. Save model
model.save("model.h5")

print("Model trained!")