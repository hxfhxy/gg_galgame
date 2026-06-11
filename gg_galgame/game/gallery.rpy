## CG 图鉴系统

init python:
    ## CG 列表定义
    cg_list = [
        {"id": "cg_cover", "name": "封面", "image": "images/cg/gg_cover.png", "condition": "开始游戏"},
        {"id": "cg_base", "name": "初次相遇", "image": "images/cg/gg_base.jpg", "condition": "第一章完成"},
        {"id": "cg_festival", "name": "校庆时光", "image": "images/cg/gg_cover.png", "condition": "第四章完成"},
        {"id": "cg_mountain", "name": "飞天树之约", "image": "images/cg/gg_cover.png", "condition": "第三章完成"},
        {"id": "cg_confession", "name": "真心话", "image": "images/cg/gg_cover.png", "condition": "第五章完成"},
        {"id": "cg_gg_true_end", "name": "GG TRUE END", "image": "images/cg/gg_cover.png", "condition": "达成GG TRUE END"},
        {"id": "cg_gg_normal_end", "name": "GG NORMAL END", "image": "images/cg/gg_cover.png", "condition": "达成GG NORMAL END"},
        {"id": "cg_mouse_true_end", "name": "拨鼠 TRUE END", "image": "images/cg/gg_cover.png", "condition": "达成拨鼠 TRUE END"},
        {"id": "cg_mouse_normal_end", "name": "拨鼠 NORMAL END", "image": "images/cg/gg_cover.png", "condition": "达成拨鼠 NORMAL END"},
        {"id": "cg_bad_end", "name": "BAD END", "image": "images/cg/gg_cover.png", "condition": "达成BAD END"},
    ]

screen gallery_screen():
    tag menu
    use game_menu(_("CG 图鉴"), scroll="viewport"):
        style_prefix "gallery"
        vbox:
            spacing 20
            label "CG 图鉴" xalign 0.5
            null height 20
            grid 5 2:
                spacing 20
                xalign 0.5
                for cg in cg_list:
                    if cg["id"] in cg_unlocked and cg_unlocked[cg["id"]]:
                        button:
                            action Show("cg_view", cg_image=cg["image"])
                            has vbox
                            add cg["image"]:
                                size (280, 158)
                                fit "contain"
                                xalign 0.5
                            text cg["name"] xalign 0.5 size 18
                    else:
                        button:
                            action NullAction()
                            has vbox
                            add Solid("#333"):
                                size (280, 158)
                                xalign 0.5
                            text "???" xalign 0.5 size 18
                            text cg["condition"] xalign 0.5 size 14 color "#666"

screen cg_view(cg_image):
    modal True
    zorder 200
    add cg_image:
        size (1920, 1080)
        fit "contain"
        xalign 0.5
        yalign 0.5
    key "game_menu" action Hide("cg_view")
    textbutton "返回" action Hide("cg_view"):
        xalign 0.95
        yalign 0.05

style gallery_label is gui_label
style gallery_label_text is gui_label_text
style gallery_button is gui_button
style gallery_button_text is gui_button_text
