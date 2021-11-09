dataset_type = 'CocoDataset'
data_root_coco = 'datasets/pedestrian_datasets/COCOPersons/'
data_root_crowdhuman = 'datasets/pedestrian_datasets/CrowdHuman/'
data_root_cityperson = 'datasets/pedestrian_datasets/CityPersons/'
data_root_wider = 'datasets/pedestrian_datasets/Wider_challenge/'
data_root_ecp = 'datasets/pedestrian_datasets/EuroCity/'
data_root_caltech = 'datasets/pedestrian_datasets/Caltech/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(2048, 1024), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2048, 1024),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        ann_file= data_root_cityperson + 'train_cp_new_mmdet.json',
        img_prefix=data_root_cityperson,
        classes = ['person'],
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root_cityperson + 'val_gt_for_mmdetction.json',
        img_prefix=data_root_cityperson + '/leftImg8bit_trainvaltest/leftImg8bit/val_all_in_folder/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root_cityperson + 'val_gt_for_mmdetction.json',
        img_prefix=data_root_cityperson + '/leftImg8bit_trainvaltest/leftImg8bit/val_all_in_folder/',
        pipeline=test_pipeline))
evaluation = dict(interval=750, metric='bbox')
