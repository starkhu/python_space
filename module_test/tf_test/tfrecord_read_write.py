# 参考博客链接：
# https://zhuanlan.zhihu.com/p/27238630
# https://blog.csdn.net/u010223750/article/details/70482498
# https://blog.csdn.net/happyhorizion/article/details/77894055

import tensorflow as tf

def writeToTfrecordFile(image_path, file_out_path):
    image_data = tf.gfile.FastGFile(image_path, "rb").read()
    image_tensor = tf.image.decode_jpeg(image_data)
    image = image_tensor.eval(session=tf.Session())
    image = image.tostring()
    label = 1
    writer = tf.python_io.TFRecordWriter(file_out_path)
    example = tf.train.Example(features=tf.train.Features(feature={
        'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
        'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image]))
    }))
    writer.write(example.SerializeToString())
    writer.close()

#decode_raw: 将原来编码为字符串类型的变量转换成代码中所需的数据类型，image存在tfrecord中的格式为bytes类型
def readFromTfrecordFile(tfrecord_file_path):
    reader = tf.TFRecordReader()
    filename_queue = tf.train.string_input_producer([tfrecord_file_path])
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(serialized_example, features={
        "image": tf.FixedLenFeature([], tf.string),
        "label": tf.FixedLenFeature([], tf.int64)
    })
    image = tf.decode_raw(features['image'], tf.uint8)
    label = tf.cast(features['label'], tf.int32)

    with tf.Session() as sess:
        #sess.run(tf.global_variables_initializer())
        coord = tf.train.Coordinator() #创建一个协调器，管理线程
        threads = tf.train.start_queue_runners(sess=sess, coord=coord) #启动队列
        print(sess.run(label))
        coord.request_stop() #请求线程结束
        coord.join(threads) #等待线程结束


#decode_raw: 将原来编码为字符串类型的变量转换成代码中所需的数据类型，image存在tfrecord中的格式为bytes类型
def readFromTfrecordFile1(tfrecord_file_path):
    reader = tf.TFRecordReader()
    filename_queue = tf.train.string_input_producer([tfrecord_file_path], shuffle=False, num_epochs=1)
    _, serialized_example = reader.read(filename_queue)
    context, features = tf.parse_single_sequence_example(
        serialized_example,
        context_features={"vid": tf.VarLenFeature(dtype=tf.string),
                          "id": tf.FixedLenFeature([], tf.string)},
        sequence_features={
            "rgb": tf.FixedLenSequenceFeature([], dtype=tf.string)}
    )
    print("type of features_vid.values:", type(context["vid"].values))
    vid = context["vid"].values
    id = context["id"]
    print("id shape:", id.shape)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        coord = tf.train.Coordinator() #创建一个协调器，管理线程
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)  # 启动队列
        try:
            while not coord.should_stop():
                print("11:", coord.should_stop())

                print(sess.run(vid))
        except:
            coord.request_stop() #请求线程结束
        finally:
            print("finally")
        coord.join(threads) #等待线程结束


    # with tf.Session() as sess1:
    #     coord1 = tf.train.Coordinator() #创建一个协调器，管理线程
    #     threads1 = tf.train.start_queue_runners(sess=sess1, coord=coord1) #启动队列
    #     print("12:", coord1.should_stop())
    #     print(sess1.run(vid))
    #     coord.request_stop() #请求线程结束
    #     coord.join(threads1) #等待线程结束

if __name__ == "__main__":
    image_path = "./data_space/dog1.jpg"
    file_out_path = "./data_space/dog1.tfrecord"
    #writeToTfrecordFile(image_path, file_out_path)
    #readFromTfrecordFile(file_out_path)

    tfrecord_file = "E:\\mini_project\\audio_classification\\Youtube-8M-WILLOW-master\\mp4\\input_videos.tfrecord"
    readFromTfrecordFile1(tfrecord_file)