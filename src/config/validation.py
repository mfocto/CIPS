from typing import Tuple, Optional

"""
config 변경 요청에 대한 유효성 검사
"""

def validate_config (cfg) -> Tuple[bool, Optional[str]]:

    # 1. 블러 유효성 검사
    if cfg.enable_blur:
        if cfg.blur_ksize <= 0 :
            return False, 'invalid config: enable_blur 가 true 일 때 blur_size는 0보다 커야 합니다.'
        if cfg.blur_ksize % 2 == 0:
            # 가우시안 블러 => 중심 픽셀 중심으로 계산
            # 커널크기가 홀수여야 중심을 계산 가능
            return False, 'invalid config : blur_size 값은 홀수여야 합니다.'

    # 2. ROI 유효성 검사
    enable_roi = cfg.enable_roi
    if enable_roi:
        if cfg.roi_x < 0 or cfg.roi_y < 0:
            return False, 'invalid config: ROI 옵션 사용할 경우 roi_x와 roi_y 값은 양수여야 합니다.'
        if cfg.roi_w <= 0 or cfg.roi_h <= 0:
            return False, 'invalid config: ROI 옵션 사용 시 roi_w와 roi_h 값은 0보다 커야 합니다.'

    # 3.Resize 유효성 검사
    enable_resize = cfg.enable_resize
    if enable_resize:
        if cfg.resize_width <= 0 or cfg.resize_height <= 0:
            return False, 'invalid config: Resize 사용 시 resize_w, resize_h 값은 0보다 커야 합니다.'

    return True, None