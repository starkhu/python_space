import tensorflow as tf


def loadGraphTest():
    pb_path = "E:\\mini_project\\audio_classification\Youtube-8M-WILLOW-master\\feature_extractor\\models\\classify_image_graph_def.pb"
    graph_def = tf.GraphDef.FromString(open(pb_path, "rb").read())
    print(type(graph_def))

if __name__ == "__main__":
    loadGraphTest()
