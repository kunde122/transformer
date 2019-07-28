import tensorflow as tf

aa=tf.Variable([[1,1,1],[2,3,1]])

cc=tf.Variable([1,2,1])
bb=[10,10,10]
dd=cc*aa+bb
ww=cc[-1:]
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(dd))