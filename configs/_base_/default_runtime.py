# checkpoint saving
checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
#load_from = '../../input/resnest50-pretrained-weight/resnest50_converted-1ebf0afe.pth'     #####
#load_from = 'resnest50_converted-1ebf0afe.pth'     #####
load_from = None
resume_from = None
workflow = [('train', 1)]
