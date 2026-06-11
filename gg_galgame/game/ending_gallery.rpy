## 结局图鉴系统

init python:
    ending_list = [
        {"id": "gg_true_end", "name": "GG TRUE END - 小时候的约定", "desc": "兑现童年承诺，与GG相爱相守"},
        {"id": "gg_normal_end", "name": "GG NORMAL END - 朋友以上", "desc": "与GG保持默契的距离，等待更好的时机"},
        {"id": "mouse_true_end", "name": "拨鼠 TRUE END - 阳光下的约定", "desc": "与拨鼠在飞天树下，温暖彼此的青春"},
        {"id": "mouse_normal_end", "name": "拨鼠 NORMAL END - 温暖的距离", "desc": "与拨鼠保持温暖的友谊，也许有一天会更近"},
        {"id": "bad_end", "name": "BAD END - 错过", "desc": "错过了两个人，也错过了青春"},
    ]

screen ending_gallery_screen():
    tag menu
    use game_menu(_("结局图鉴"), scroll="viewport"):
        style_prefix "ending"
        vbox:
            spacing 20
            label "结局图鉴" xalign 0.5
            null height 20
            for ending in ending_list:
                if ending["id"] in ending_unlocked and ending_unlocked[ending["id"]]:
                    frame:
                        xsize 800
                        xalign 0.5
                        padding (20, 20, 20, 20)
                        has vbox
                        text ending["name"] size 28 color "#ffffff"
                        null height 10
                        text ending["desc"] size 20 color "#aaaaaa"
                else:
                    frame:
                        xsize 800
                        xalign 0.5
                        padding (20, 20, 20, 20)
                        has vbox
                        text "???" size 28 color "#666666"
                        null height 10
                        text "未解锁" size 20 color "#444444"
            null height 30
            hbox:
                xalign 0.5
                spacing 50
                textbutton "返回标题" action MainMenu() xalign 0.5

style ending_label is gui_label
style ending_label_text is gui_label_text
style ending_frame is gui_frame
style ending_button is gui_button
style ending_button_text is gui_button_text
