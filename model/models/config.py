batch_size = 32
num_gpus = 0
num_workers= 4

learning_rate= 0.0002,
adam_b1= 0.8,
adam_b2= 0.99,
lr_decay= 0.999,
seed= 1234,

upsample_rates= [8,8,2,2],
upsample_kernel_sizes= [16,16,4,4],
upsample_initial_channel= 512,
resblock_kernel_sizes= [3,7,11],
resblock_dilation_sizes= [[1,3,5], [1,3,5], [1,3,5]],
resblock_initial_channel= 256,

lst =[]