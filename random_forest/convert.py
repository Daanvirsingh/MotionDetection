import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model("/home/daanvir/gg/project/SRM_project/random_forest/NMI/saved_model.pbtxt.index")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)