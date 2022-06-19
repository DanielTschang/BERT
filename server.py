from flask import Flask,request,jsonify
from run_similarity import BertSim

BertModel = BertSim()
BertModel.set_predict_mode()

app = Flask(__name__)

@app.route('/similarity', methods=['GET'])
def similarity():
	sentence1 = request.args.get('sen1')
	sentence2 = request.args.get('sen2')
	score = BertModel.predict(sentence1,sentence2)
	score = score[0][1]
	print("[similarity][api]score :",score)
	return jsonify({'score': str(score)})

app.run()