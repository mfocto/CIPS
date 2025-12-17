from generated import vision_pb2

def default_config():
    """
     서버 시작 시 적용할 기본 설정
    """
    return vision_pb2.Config(
        enable_gray=True,
        enable_blur=False,
        blur_ksize=5,
        enable_roi=True,
        enable_resize=False,

        roi_x=0,
        roi_y=0,
        roi_w=0,
        roi_h=0,

        resize_width=0,
        resize_height=0,
    )