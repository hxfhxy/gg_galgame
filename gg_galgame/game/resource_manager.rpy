## 资源管理器 - 处理图片缩放和适配

## 16:9 适配变换
transform bg_fit:
    size (1920, 1080)
    fit "cover"

## 角色立绘适配变换
transform char_center:
    xalign 0.5
    yalign 1.0
    zoom 1.1

transform char_left:
    xalign 0.2
    yalign 1.0
    zoom 1.0

transform char_right:
    xalign 0.8
    yalign 1.0
    zoom 1.0

transform char_right_large:
    xalign 0.75
    yalign 1.0
    zoom 1.3

## CG 适配
transform cg_full:
    size (1920, 1080)
    fit "cover"
    xalign 0.5
    yalign 0.5

## 淡入淡出效果
transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0

transform fade_out:
    alpha 1.0
    linear 0.5 alpha 0.0

## 轻微震动效果
transform shake:
    xoffset 0
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset 0

## 镜头停顿
transform pause_zoom:
    zoom 1.0
    linear 2.0 zoom 1.05
    linear 2.0 zoom 1.0

## 闪白效果
transform flash_white:
    alpha 0.0
    linear 0.1 alpha 1.0
    pause 0.2
    linear 0.3 alpha 0.0
