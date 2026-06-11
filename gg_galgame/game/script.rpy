## 二中之恋 - 双女主版（7章扩充版）

label start:

    $ player_name = renpy.input("请输入你的名字（留空使用默认名「杨哥」）：", default="杨哥", length=20)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "杨哥"

    $ gg_affection = 0
    $ mouse_affection = 0
    $ route = ""
    $ chapter = 0

    scene bg black with fade
    pause 1.0

    "新学期的第一天，阳光透过车窗洒在脸上。"
    "我——[player_name]，因为父母工作调动，转学来到了二中。"
    "说实话，对新学校没什么期待。"
    "毕竟，适应新环境这件事，我向来不太擅长。"

    scene bg school_gate with dissolve
    pause 0.5

    "校门比我想象中气派。"
    "门口三三两两的学生走过，有说有笑。"
    "我深吸一口气，迈步走了进去。"

    jump chapter1

label chapter1:
    $ chapter = 1
    jump chapter1_start

label chapter2:
    $ chapter = 2
    jump chapter2_start

label chapter3:
    $ chapter = 3
    jump chapter3_start

label chapter4:
    $ chapter = 4
    jump chapter4_start

label chapter5:
    $ chapter = 5
    jump chapter5_start

label chapter6:
    $ chapter = 6
    if gg_affection > mouse_affection + 3:
        $ route = "gg"
        jump chapter6_gg_route
    elif mouse_affection > gg_affection + 3:
        $ route = "mouse"
        jump chapter6_mouse_route
    else:
        jump chapter6_neutral

label chapter7:
    $ chapter = 7
    if route == "gg":
        jump chapter7_gg_start
    elif route == "mouse":
        jump chapter7_mouse_start
    else:
        jump bad_ending

label gg_true_ending:
    $ unlock_ending("gg_true_end")
    $ unlock_cg("cg_gg_true_end")
    scene bg black with fade
    pause 2.0
    "—— GG TRUE END ——"
    "「小时候的约定，终于实现了。」"
    "「以后的每一天，我都陪你走。」"
    jump ending_gallery_show

label gg_normal_ending:
    $ unlock_ending("gg_normal_end")
    $ unlock_cg("cg_gg_normal_end")
    scene bg black with fade
    pause 2.0
    "—— GG NORMAL END ——"
    "「朋友以上，恋人未满。」"
    "「但也许，这就是最好的距离。」"
    jump ending_gallery_show

label mouse_true_ending:
    $ unlock_ending("mouse_true_end")
    $ unlock_cg("cg_mouse_true_end")
    scene bg black with fade
    pause 2.0
    "—— 拨鼠 TRUE END ——"
    "「阳光下的约定，温暖了整个青春。」"
    "「你的笑容，是我最好的答案。」"
    jump ending_gallery_show

label mouse_normal_ending:
    $ unlock_ending("mouse_normal_end")
    $ unlock_cg("cg_mouse_normal_end")
    scene bg black with fade
    pause 2.0
    "—— 拨鼠 NORMAL END ——"
    "「温暖的距离，刚刚好。」"
    "「也许有一天，我们会更近一步。」"
    jump ending_gallery_show
