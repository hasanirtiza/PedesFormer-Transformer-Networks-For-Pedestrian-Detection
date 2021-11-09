checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
load_from = './pretrained_models/cascade_mask_rcnn_swin_base_patch4_window7.pth'
#load_from = './work_dirs/crowdhuman_pre_ecp_ft/epoch_23.pth'
#load_from = './work_dirs/ecp_base_3x_coco_pre/epoch_31.pth'
#load_from = './work_dirs/wp_only/epoch_15.pth'
#load_from = './work_dirs/cp_ft_wp_pre_ecp_ft/epoch_1.pth'
resume_from = None
workflow = [('train', 1)]
work_dir = './work_dirs/cp_dummy_train'








