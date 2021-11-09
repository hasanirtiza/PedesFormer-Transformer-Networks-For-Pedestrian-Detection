export CUDA_VISIBLE_DEVICES=9


#python tools/test_cityperson_swin.py ./work_dirs/cp_base_3x_coco_pre/cascade_mask_rcnn_swin_base_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco.py ./work_dirs/crowdhuman_pre_ecp_pre_cp_ft/epoch_ 1 340 --out res.json 




python tools/test_cityperson_swin.py ../Swin-Transformer-Object-Detection/work_dirs/cp_base_3x_coco_pre/cascade_mask_rcnn_swin_base_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco.py ../Swin-Transformer-Object-Detection/work_dirs/cp_base_3x_coco_pre/epoch_ 9 340 --out res.json






