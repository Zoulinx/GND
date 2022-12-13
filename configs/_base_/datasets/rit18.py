# dataset settings
dataset_type = 'R18dataset'
data_root = 'data'
crop_size = (512, 512)
train_pipeline = [
    dict(type='LoadTIFImageFromFile'),
    dict(type='LoadTIFAnnotations2C'),
    dict(type='Resize', img_scale=(512, 512)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadTIFImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='RIT-18/sun/clip_sun_index_img',
        ann_dir='RIT-18/sun/clip_sun_label',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='RIT-18/shadow/clip_shadow_index_img',
        ann_dir='RIT-18/shadow/clip_shadow_label',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='RIT-18/shadow/clip_shadow_index_img',
        ann_dir='RIT-18/shadow/clip_shadow_label',
        pipeline=test_pipeline))
