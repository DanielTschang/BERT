# -*- coding: utf-8 -*-
import pathlib
import os


basedir1 = str(pathlib.Path(os.path.abspath(__file__)).parent)
print(basedir1)

class Config():

    def __init__(self):
        # 一些Configurations
        self.bert_config_file = os.path.join(basedir1,'model' ,'bert_config.json')
        # bert vocab 文件
        self.vocab_file = os.path.join(basedir1, 'model','vocab.txt')
        # train/dev/test data dir
        self.data_dir = os.path.join(basedir1, 'data')
        self.predict_file = os.path.join(basedir1, 'data/dev.csv')
        self.test_file = os.path.join(basedir1, 'data/test.csv')
        # output dir
        self.output_dir = os.path.join(basedir1, 'results')
        # pretrained model
        self.init_checkpoint = os.path.join(basedir1, 'model','bert_model.ckpt')
        self.train_checkpoint = os.path.join(basedir1, 'results')

        self.do_lower_case = True
        self.verbose_logging = False
        self.master = None
        self.version_2_with_negative = False
        self.null_score_diff_threshold = 0.0
        self.use_tpu = False
        self.tpu_name = None
        self.tpu_zone = None
        self.gcp_project = None
        self.num_tpu_cores = 8
        self.task_name = 'sim'
        self.gpu_memory_fraction = 0.8

        self.max_seq_length = 128
        self.doc_stride = 128
        self.max_query_length = 64


        self.do_train = False
        self.do_predict = True
        self.batch_size = 8
        self.predict_batch_size = 8
        self.learning_rate = 5e-5
        self.num_train_epochs = 3.0
        self.warmup_proportion = 0.1
        self.save_checkpoints_steps = 1000
        self.iterations_per_loop = 1000
        self.n_best_size = 20
        self.max_answer_length = 30
        self.eval_batch_size = 16
        # self.do_eval = False