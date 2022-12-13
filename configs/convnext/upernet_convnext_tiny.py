_base_ = [
    '../_base_/models/upernet_convnext.py', '../_base_/datasets/rit18.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
crop_size = (512, 512)
num_classes = 8
model = dict(
    backbone=dict(
        in_channels=6,
        type='mmcls.ConvNeXt',
        arch='tiny',
        out_indices=[0, 1, 2, 3],
        drop_path_rate=0.4,
        layer_scale_init_value=1.0,
        gap_before_final_norm=False),
    decode_head=dict(
        in_channels=[96, 192, 384, 768],
        num_classes=num_classes,
    ),
    auxiliary_head=dict(in_channels=384, num_classes=num_classes),
    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(341, 341)),
)

optimizer = dict(
    constructor='LearningRateDecayOptimizerConstructor',
    _delete_=True,
    type='AdamW',
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg={
        'decay_rate': 0.9,
        'decay_type': 'stage_wise',
        'num_layers': 6
    })

lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=2)
# fp16 settings
optimizer_config = dict(type='Fp16OptimizerHook', loss_scale='dynamic')
# fp16 placeholder
fp16 = dict()
