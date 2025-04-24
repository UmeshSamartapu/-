import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))
print("GPUs:", tf.config.list_physical_devices('GPU'))


# import tensorflow as tf
# import time

# # Set up GPU test
# with tf.device('/GPU:0'):
#     a = tf.random.normal([10000, 10000])
#     b = tf.random.normal([10000, 10000])
#     start = time.time()
#     c = tf.matmul(a, b)
#     print("Time taken on GPU:", time.time() - start)
