num_frames = 17
frame_interval = 3
image_size = (128, 128)

# Define dataset
root = None
data_path = "CSV_PATH"
use_image_transform = False
num_workers = 4

# Define acceleration
dtype = "bf16"
grad_checkpoint = True
plugin = "zero2"
sp_size = 1

# Define Loss
kl_weight = 0.000001
perceptual_weight = 0.1 # TODO: need to change this to 0.1 !!! according to MAGVIT paper

# Define model

model = dict(
    type="VAE_MAGVIT_V2",
    in_out_channels = 3,
    latent_embed_dim = 256,
    filters = 128,
    num_res_blocks = 4,
    channel_multipliers = (1, 2, 2, 4),
    temporal_downsample = (False, True, True),
    num_groups = 32, # for nn.GroupNorm
    kl_embed_dim = 64,
    custom_conv_padding = None,
    activation_fn = 'swish',
    image_size = image_size,
    separate_first_frame_encoding = False,
)

# Others
seed = 42
outputs = "outputs"
wandb = False

# Training
''' NOTE: 
magvit uses about # samples (K) * epochs ~ 2-5 K,  num_frames = 4, reso = 128
==> ours num_frams = 16, reso = 256, so samples (K) * epochs ~ [500 - 1200], 
3-6 epochs for pexel, from pexel observation its correct
'''

epochs = 10
log_every = 1
ckpt_every = 1000
load = None

batch_size = 8
lr = 1e-4
grad_clip = 1.0
