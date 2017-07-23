import os, sys
import time
start = time.time()
import tensorflow as tf
import image_slicer
from io import BytesIO
import random

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# change this as you see fit
# image_path = sys.argv[1]

# Read in the image_data
# Loads label file, strips off carriage return
# label_lines = [line.rstrip() for line
#                    in tf.gfile.GFile("retrained_labels.txt")]
label_lines = []
label_lines.append("not track")
label_lines.append("turtle track")
# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
start = time.time()
#files = ["testing/small.jpg","testing/tire.jpg","testing/tire2.jpg","testing/test.jpg","testing/test3.jpg","testing/sand.jpg"]
files = ["testing/tt.jpg"]
tiles = image_slicer.slice(files[0],32)
print(tiles)
smple = random.sample(range(1,32),5)
found = 0
with tf.Session() as sess:
    for t in smple:
        i = tiles[t]
        imageBuf = BytesIO()
        image = i.image
        image.save(imageBuf, format="JPEG")
        image = imageBuf.getvalue()
    #    print(imageBuf.name)
        start_temp = time.time()
        #image_data = tf.gfile.FastGFile(i, 'rb').read()
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            #print(human_string,score)
            #if(human_string == "turtle track" and score > 0.5):
            if(score > 0.5):
                print("start")
                print(human_string,score)
                print(t)
                print(tiles[t])
                print("end")
            # found =1

            #print('%s (score = %.5f)' % (human_string, score))
            #print()
        if(found == 1):
            break
        print(time.time()-start_temp)
print(time.time()-start)
