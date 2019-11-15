import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

msg = tf.constant('TensorFlow 2.0 Hello World')
tf.print(msg)