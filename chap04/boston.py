import matplotlib.pyplot as plt
import tensorflow.keras as k
from tensorflow.keras.datasets import boston_housing

(train_X, train_Y), (test_X, test_Y) = boston_housing.load_data()

print(len(train_X), len(test_X))
print(train_X[0])
print(train_Y[0])

x_mean = train_X.mean()
x_std = train_X.std()
train_X -= x_mean
train_X /= x_std
test_X -= x_mean
test_X /= x_std

y_mean = train_Y.mean()
y_std = train_Y.std()
train_Y -= y_mean
train_Y /= y_std
test_Y -= y_mean
test_Y /= y_std

print(train_X[0])
print(train_Y[0])

model = k.Sequential([
    k.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    k.layers.Dense(units=39, activation='relu'),
    k.layers.Dense(units=26, activation='relu'),
    k.layers.Dense(units=1)
])
model.compile(optimizer=k.optimizers.Adam(lr=0.07), loss='mse')
model.summary()

history = model.fit(train_X, train_Y, epochs=100, batch_size=32, validation_split=0.25,
                    callbacks=[k.callbacks.EarlyStopping(patience=10, monitor='val_loss')])
# history = model.fit(train_X, train_Y, epochs=50, batch_size=32, validation_split=0.25)

plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()

model.evaluate(test_X, test_Y)

pred_Y = model.predict(test_X)

plt.figure(figsize=(5, 5))
plt.plot(test_Y, pred_Y, 'b.')
plt.axis([min(test_Y), max(test_Y), min(test_Y), max(test_Y)])

plt.plot([min(test_Y), max(test_Y)], [min(test_Y), max(test_Y)], ls='--', c='.3')
plt.xlabel('test_Y')
plt.ylabel('pred_Y')

plt.show()
