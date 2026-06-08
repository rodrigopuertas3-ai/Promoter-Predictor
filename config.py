import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#------------------------ info ------------------------#
info = '2023'
pretrain_info = ''
seed = 2023
fold = 5

#------------------------ data ------------------------#
data_root = BASE_DIR + '/data/'
wild_data_path = data_root + 'wild_promoter.csv'                # wild promoter data
synthetic_data_path = data_root + 'synthetic_promoter.csv'      # synthetic promoter data
val_ratio = 0.10        # validation set ratio (for synthetic promoter)
test_ratio = 0.10       # test set ratio (for synthetic promoter)
seq_len = 29            # max base promoter size
num_var = 15            # max variation size
mer = 8                 # k-mer for Extended Vision

#------------------------ train ------------------------#
if_test = False         # if test
pretrain = False        # if pretrain
pretrain_root = BASE_DIR + '/pretrain'
pretrain_model_path = pretrain_root + '/model.ckpt'.format(pretrain_info)    # pretrain model
lr = 0.0001             # init learning rate
batch_size = 64         # batch size
num_epoch = 200         # max number of epoch
weight_decay = 5e-6     # L2 regularization
LRstep_size = 15        # StepLR step size
LRcycle_size = 3        # StepLR cycle size
LRgamma = 0.5        # StepLR lr attenuation rate

#------------------------ save ------------------------#
save_root = BASE_DIR + '/save'
log_file = save_root + '/log_{}.txt'.format(info)                       # save log file path
model_path = save_root + '/model_{}.ckpt'.format(info)                  # save model path
signal_file = BASE_DIR + '/signal.txt'                                  # singal file path
save_fig = BASE_DIR + '/output/EVMP-Transformer_{}.pdf'.format(info)    # save train/valid/test figure path


#------------------------ test ------------------------#
if_predict = True                                                              # if predict
predict_data_path = BASE_DIR + '/data/predecir1.csv'                       # predict data
predict_result_path = BASE_DIR + '/output/predict_results_{}.csv'.format(info)  # save predict result path
