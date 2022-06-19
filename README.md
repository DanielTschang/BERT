# 基於Bert 的 sentence similarity Model
Tensorflow版本 : 1.15
Numpy請安裝1.19.0以下

## 經過10萬筆 3個epoch的訓練
- eval_accuracy = 0.8487
- eval_loss = 0.7586791

## Data format
```
sentence_1,sentence_2,label
```
例
```
戴資穎拿冠軍啦！,戴資穎得第一名！,1
```
lable 1為同義句,0為非同義句

## 如何Train
1. 到config.py的Config中將self.do_train改成True

2. 將Bert Model(本repo使用Bert-wwm-ext [link](https://github.com/ymcui/Chinese-BERT-wwm) )放到model資料夾中

3. Train
```
python3 run_similarity.py
```
## Train完後
到config.py的Config終將self.do_train改成False, self.do_predict改成True可以測試
若要架起localhost則安裝flask(pip install flask)
```python
python3 server.py
```
port預設為5000

## Call API
GET method
```
127.0.0.1:5000/similarity?sen1=戴資穎拿冠軍啦！&sen2=戴資穎得第一名！
```
會回傳json
```
{
  "score":"0.99932754"
}
```

