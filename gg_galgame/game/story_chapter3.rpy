## 第三章：爬山与山顶

label chapter3_start:

    scene bg school_gate with dissolve
    pause 0.5

    "周六早上，阳光明媚。"
    "班级组织了爬山活动。"

    show bs normal at char_left with dissolve
    show gg casual normal at char_right_large with dissolve

    "拨鼠穿着运动装，活力满满。"
    "GG穿着简单的T恤和牛仔裤，很清爽。"

    bs "出发出发！今天一定要爬到山顶！"

    show gg casual tsundere at char_right_large

    ww "……你每次都这么说，每次都半途而废。"

    bs "这次不一样！有[player_name]在，我一定行！"

    show zm normal at char_center with dissolve

    zm "兄弟，左右护法啊。"

    hide zm with dissolve

    scene bg hiking with dissolve

    "山路比我想象中要陡。"

    show bs normal at char_left with dissolve

    bs "[player_name]，你累不累？要不要休息一下？"

    mc "我没事，你呢？"

    bs "我体力很好的！你别小看我！"

    show gg casual normal at char_right_large with dissolve

    "GG走在另一边，步伐稳健。"
    "她没说话，但偶尔会看我一眼。"

    "突然，拨鼠脚下一滑——"

    show bs surprised at char_left

    bs "啊——！"

    "同一瞬间，GG在另一边也滑了一下。"

    show gg casual surprised at char_right_large

    "两个人都需要帮忙，但我只能先去一个。"

    menu:
        "先扶拨鼠":
            $ change_mouse_affection(5, "先扶拨鼠")
            $ change_gg_affection(-2, "忽略GG")
            jump ch3_help_mouse_first

        "先扶GG":
            $ change_gg_affection(5, "先扶GG")
            $ change_mouse_affection(-2, "忽略拨鼠")
            jump ch3_help_gg_first

label ch3_help_mouse_first:

    mc "小心！"

    "我冲过去扶住了拨鼠。"

    show bs shy at char_left

    bs "谢、谢谢……"

    "她的脸红了。"

    "另一边，GG自己站稳了。"

    show gg casual think at char_right_large

    "她看了我一眼，没说话，转身继续往上走。"

    mc "GG，你没事吧？"

    ww "……我没事。不用你管。"

    show bs sad at char_left

    "拨鼠看了看GG的背影，表情有些复杂。"

    jump ch3_after_slip

label ch3_help_gg_first:

    mc "GG！"

    "我冲过去扶住了GG。"

    show gg casual shy at char_right_large

    ww "我、我自己可以！"

    "她挣脱了，但没有真的用力。"

    "另一边，拨鼠自己站稳了。"

    show bs normal at char_left

    bs "没事没事！我皮糙肉厚的！"

    "她笑着说，但我注意到她揉了揉脚踝。"

    mc "拨鼠，你的脚——"

    show bs shy at char_left

    bs "真的没事啦！快走快走！"

    jump ch3_after_slip

label ch3_after_slip:

    show bs sad at char_left

    "拨鼠看着这一幕，表情有一瞬间暗了一下。"
    "但她很快又笑了起来。"

    show bs normal at char_left

    bs "快走快走！山顶见！"

    hide bs with dissolve
    hide gg with dissolve

    scene bg mountaintop with dissolve

    "终于到了山顶。"
    "视野一下子开阔起来。"
    "远处的城市在阳光下闪闪发光。"

    show gg casual normal at char_center with dissolve

    "GG站在山顶的石头上，风吹起她的头发。"

    ww "好漂亮……"

    mc "嗯，确实很漂亮。"

    show gg casual tsundere at char_center

    ww "……我说的是风景。"

    mc "我也是说风景啊。"

    show gg casual shy at char_center

    ww "哼。"

    "她别过脸，但我看到她嘴角微微上扬了。"

    "拨鼠也爬上来了，气喘吁吁。"

    show bs normal at char_left with dissolve

    bs "累、累死我了……你们倒是爬得快……"

    "大家坐在山顶休息，吹着风。"

    bs "来来来，拍张合照！"

    "拨鼠掏出手机，招呼大家一起。"

    bs "[player_name]，你站谁旁边？"

    menu:
        "站在GG旁边":
            $ change_gg_affection(3, "合照站GG旁边")
            $ change_mouse_affection(-1, "合照不选拨鼠")
            jump ch3_photo_gg

        "站在拨鼠旁边":
            $ change_mouse_affection(3, "合照站拨鼠旁边")
            $ change_gg_affection(-1, "合照不选GG")
            jump ch3_photo_mouse

label ch3_photo_gg:

    show gg casual tsundere at char_center

    ww "为什么要他站我旁边？"

    bs "因为你们俩最般配啊！"

    show gg casual angry at char_center

    ww "拨鼠！！！"

    "咔嚓——"

    jump ch3_photo_end

label ch3_photo_mouse:

    show bs shy at char_left

    bs "嘿嘿，好近~"

    show gg casual think at char_right_large

    "GG站在另一边，表情淡淡的。"

    "咔嚓——"

    jump ch3_photo_end

label ch3_photo_end:

    bs "哇！你们在拍偶像剧吗？好浪漫！"

    show gg casual angry at char_center

    ww "才没有！"

    "大家坐在山顶休息，吃着带来的零食。"
    "气氛很轻松，笑声不断。"

    show zm normal at char_right with dissolve

    zm "来来来，拍张合照！"

    hide zm with dissolve

    bs "[player_name]，你站GG旁边！"

    show gg casual tsundere at char_center

    ww "为什么要他站我旁边？"

    bs "因为你们俩最般配啊！"

    show gg casual angry at char_center

    ww "拨鼠！！！"

    "咔嚓——"

    scene bg mountaintop with dissolve
    show gg casual shy at char_center with dissolve

    "拍完照后，其他人开始下山了。"
    "GG却还站在原地，看着远方。"

    mc "不走吗？"

    ww "……再看一会儿。"

    "我站在她旁边，也看着远方。"

    ww "[player_name]。"

    mc "嗯？"

    show gg casual think at char_center

    ww "你真的……一点都不记得了吗？"

    mc "你又问这个。到底是什——"

    ww "算了。"
    ww "不记得也好。"
    ww "反正都是小时候的事了。"

    "她转身准备下山。"

    mc "GG。"

    "她停下脚步。"

    mc "虽然我不记得了，但是……"
    mc "如果你想告诉我，我随时愿意听。"

    show gg casual shy at char_center

    "她沉默了一会儿。"

    ww "……以后再说吧。"

    "她快步走下山去。"

    hide gg with dissolve

    scene bg dorm_area with dissolve

    "下山后，天色渐晚。"
    "我们经过宿舍楼下。"

    show bs normal at char_center with dissolve

    bs "[player_name]，今天爬山累不累？"

    mc "还好。你呢？你滑了那一下没事吧？"

    show bs shy at char_center

    bs "没事没事！有你扶我嘛。"

    "她笑得很开心。"

    bs "对了，下周有校庆，你期待吗？"

    mc "校庆？"

    bs "对啊！有文艺汇演，还有各种摊位。"
    bs "GG是班长，要负责我们班的节目。"
    bs "你去帮忙的话，她一定会很高兴的！"

    mc "你怎么知道？"

    show bs normal at char_center

    bs "因为我了解她啊！别看她嘴硬，其实心里想什么我都猜得到。"

    mc "（拨鼠……她真的很善解人意。）"

    hide bs with dissolve

    scene bg black with fade
    pause 1.0

    "GG……她好像在等我记起什么。"
    "拨鼠……她的笑容，总能让人放松下来。"
    "校庆就要到了。"

    $ chapter = 3
    jump chapter4
