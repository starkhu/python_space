# Test Op: reduce_sum && reduce_mean && reduce_max && argmax

import tensorflow as tf
from tensorflow import logging

x = [[1, 2], [3, 4], [5, 6]]
x1 = tf.cast(x, tf.float32)

def execute_op(op_func):
    def wrapper(inp):
        op_list = op_func(inp)
        for op in op_list:
            init = tf.global_variables_initializer()
            with tf.Session() as sess:
                sess.run(init)
                out = sess.run(op)
                print(out)
                #print(type(out))
    return wrapper

# Function Desc:
#   a function evaluated on a dimension of tensor
# Parameter Desc:
#   input_tensor: input
#   axis(old version is reduction_indices)
#   keepdims(old version is keep_dims)
@execute_op
def reduce_test(inp):
    y_mean1 = tf.reduce_mean(inp, axis=0, keepdims=True)
    y_mean2 = tf.reduce_mean(inp, axis=1)
    y_sum1 = tf.reduce_sum(inp, axis=1)
    y_sum2 = tf.reduce_sum(inp)
    return [y_mean1, y_mean2, y_sum1, y_sum2]


def getShapeTest(inp):
    x_shape = inp.get_shape()
    print(x_shape)

#Function Desc:
#   return the index number of the maximum value in the vector.
@execute_op
def argmax_test(inp):
    y_arg = tf.argmax(inp, 1)
    return [y_arg]

#input: NHWC, filter:H,W,Cin,Cout. input.C=filter.Cin
@execute_op
def conv_test(inp):
    x1 = tf.ones([10, 10, 1], tf.float32)
    x2 = 2 * tf.ones([10, 10, 1], tf.float32)
    x3 = 3 * tf.ones([10, 10, 1], tf.float32)
    x = tf.concat([x1, x2, x3], axis=2)
    x = tf.reshape(x, [1, 10, 10, 3])
    xx = tf.Variable(tf.random_normal([1, 10, 10, 3]))
    w1 = tf.ones([8, 8, 3, 1], tf.float32)
    w2 = 2 * tf.ones([8, 8, 3, 1], tf.float32)
    w = tf.concat([w1, w2], axis=3)
    #w = tf.ones([8, 8, 3, 2], tf.float32)
    ww = tf.Variable(tf.random_normal([8, 8, 3, 2]))
    y_conv = tf.nn.conv2d(xx, w, strides=[1, 2, 2, 1], padding="VALID", data_format="NHWC")
    return [y_conv]

@execute_op
def subtract_test(inp):
    y_subtract = tf.subtract(inp, 2*inp)
    return [y_subtract]

@execute_op
def collection_test(inp):
    tf.add_to_collection('tf_collection', tf.constant(2.0))
    tf.add_to_collection('tf_collection', tf.constant(3.0))
    y_get_collection = tf.get_collection('tf_collection')
    return [y_get_collection]

@execute_op
def sparse_to_dense_test(inp):
    a = [1, 2, 3]
    y_dense = tf.sparse_to_dense(a, [10], 2)
    return [y_dense]

@execute_op
def stackTest(inp):
    x2 = tf.add(inp, 10)
    y_stack = tf.stack([x1, x2], axis=0)
    y1_stack = tf.stack([x1, x2], axis=1)
    return [inp, x2, y_stack, y1_stack]

@execute_op
def unstackTest(inp):
    y_unstack = tf.unstack(inp, axis=0)
    return [y_unstack]

@execute_op
def assignTest(inp):
    var = tf.Variable(tf.constant(0.0), dtype=tf.float32)
    y_assign = tf.assign(var, 10)
    return [y_assign]

def op_test():
    #set the threshhold for what messages will be logged : DEBUG, INFO, WARN, ERROR, FATAL
    logging.set_verbosity(tf.logging.INFO)
    #getShapeTest(x1)
    #reduce_test(x1)
    #argmax_test(x1)
    #conv_test(x1)
    #subtract_test(x1)
    #collection_test(x1)
    #sparse_to_dense_test(x1)
    #loadGraphTest()
    #stackTest(x1)
    #unstackTest(x1)
    assignTest(x1)


if __name__  ==  '__main__':
    op_test()
