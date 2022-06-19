# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from .run_similarity import BertSim
from datetime import datetime

BertModel = BertSim()
BertModel.set_predict_mode()

app = Flask(__name__)

@app.route('/similarity', methods=['GET'])
def similarity():
	start = datetime.now()
	sentence1 = request.args.get('sen1')
	sentence2 = request.args.get('sen2')
	score = BertModel.predict(sentence1,sentence2)
	score = score[0][1]
	print("[similarity][api]score :",score)
	end = datetime.now()
	duration = end-start
	print("[similarity][api]predict duration : {second:.4f} seconds".format(second=duration.total_seconds()))
	return jsonify({'score': str(score)})
app.run()