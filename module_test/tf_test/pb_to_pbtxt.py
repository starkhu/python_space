import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants

def pbToPbtxt(pb_file):
    graph_def = tf.GraphDef.FromString(open(pb_file, "rb").read())
    with tf.Session() as sess:
        graph = convert_variables_to_constants(sess, graph_def, ['pool_3/_reshape'])
        tf.train.write_graph(graph, "./data_space/", "graph_pb.txt", as_text=True)

if __name__ == "__main__":
    pb_file = "E:/mini_project/audio_classification/Youtube-8M-WILLOW-master/feature_extractor/models/classify_image_graph_def.pb"
    pbToPbtxt(pb_file)
