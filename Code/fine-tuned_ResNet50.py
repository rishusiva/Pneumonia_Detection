from ResNet50 import *

resnet_model.trainable = True

print("Number of layers in the base model: ", len(resnet_model.layers))

# Fine-tune from this layer onwards
fine_tune_at = 100

# Freeze all the layers before the `fine_tune_at` layer
for layer in resnet_model.layers[:fine_tune_at]:
  layer.trainable = False

model2.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])

print(model2.summary())

fine_tune_epochs = 10
epochs_on_raw_model = 30

total_epochs =  epochs_on_raw_model + fine_tune_epochs

history_fine =model2.fit(train,epochs=total_epochs, 
                    validation_data=validation,
                    steps_per_epoch=100,
                    callbacks=[early_stopping,lr],
                    batch_size=32)

train_score = model2.evaluate(train)

print("Train Loss: ", train_score[0])
print("Train Accuracy: ", train_score[1])

test_score = model2.evaluate(test)
print("\nTest loss: ", test_score[0])
print("Test Accuracy: ", test_score[1])

