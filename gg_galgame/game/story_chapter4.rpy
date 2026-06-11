## 第四章：体育馆与飞天树

label chapter4_start:

    scene bg classroom with dissolve
    pause 0.5

    "爬山之后，班上的气氛活跃了不少。"

    show bs normal at char_left with dissolve

    bs "[player_name]！今天体育课打乒乓球吗？"

    mc "你会打？"

    bs "当然！我可是很厉害的！"

    show gg school normal at char_right with dissolve

    ww "……你上次连发球都过不了网。"

    show bs angry at char_left

    bs "GG！你怎么揭我老底！"

    hide bs with dissolve
    hide gg with dissolve

    scene bg gym_entrance with dissolve

    "体育馆门口，几个班的同学都在往里走。"

    show zm normal at char_center with dissolve

    zm "兄弟，乒乓球你会打吗？"

    mc "会一点。"

    zm "那等会儿咱俩打一局。"

    hide zm with dissolve

    scene bg gym_inside with dissolve

    "体育馆里很热闹。"
    "乒乓球场边围了不少人。"

    show bs normal at char_left with dissolve

    bs "[player_name]！来来来，我先跟你打！"

    "拨鼠拿起球拍，架势十足。"
    "但第一个球就打飞了。"

    show bs shy at char_left

    bs "啊……意外意外。"

    mc "（忍住笑）嗯，意外。"

    show gg school normal at char_right with dissolve

    "GG站在旁边看，嘴角微微上扬。"

    ww "我说什么来着。"

    show bs angry at char_left

    bs "GG你来试试啊！"

    show gg school tsundere at char_right

    ww "我不用试，我知道我打得比你好。"

    bs "那你跟[player_name]打一局！"

    show gg school shy at char_right

    ww "我、我才不要……"

    mc "来吧，就一局。"

    show gg school tsundere at char_right

    ww "……那就一局。"

    hide bs with dissolve

    "GG拿起球拍，姿势很标准。"
    "她打得很认真，每一球都全力以赴。"

    "比分咬得很紧。最后一个球，我有机会扣杀——"

    menu:
        "全力以赴，打过去":
            $ change_gg_affection(3, "认真对待GG")
            jump ch4_pingpong_serious

        "故意放水，让她赢":
            $ change_gg_affection(5, "让GG赢")
            $ change_mouse_affection(-1, "偏向GG")
            jump ch4_pingpong_letwin

label ch4_pingpong_serious:

    "我用力扣了过去。球擦着台面飞出。"

    "GG没接到。"

    mc "承让。"

    show gg school tsundere at char_center

    ww "……哼，再来一局。"

    mc "好啊。"

    show gg school shy at char_center

    ww "……下次我不会输。"

    "她嘴上不服输，但眼里闪着光。"

    jump ch4_pingpong_end

label ch4_pingpong_letwin:

    "我轻轻把球打了回去，力度故意小了一点。"

    "GG抓住机会，一个漂亮的扣杀。"

    show gg school shy at char_center

    ww "……承让。"

    mc "你真的很厉害。"

    ww "这种事不用你说。"

    "但她笑得很开心。"

    "旁边的拨鼠小声嘀咕："

    show bs normal at char_left with dissolve

    bs "（小声）你明明可以赢的……"

    hide bs with dissolve

    jump ch4_pingpong_end

label ch4_pingpong_end:

    "但她笑得很开心。"

    hide gg with dissolve

    show jj normal at char_center with dissolve

    jj "嘿嘿嘿~GG刚才笑得好开心啊~"

    hide jj with dissolve

    show zm normal at char_center with dissolve

    zm "兄弟，GG对别人可不会这样。"
    zm "你小子，有戏啊。"

    hide zm with dissolve

    scene bg flying_tree with dissolve

    "放学后，我一个人经过飞天树。"
    "夕阳穿过红色的纸条，洒了一地碎金。"

    show bs normal at char_center with dissolve

    bs "[player_name]！你也在这？"

    mc "嗯，路过。"

    bs "我经常来这里。"
    bs "看着这些愿望纸条，就觉得世界还是很美好的。"

    "她在树下的长椅上坐下，拍了拍旁边的位置。"

    bs "坐啊。"

    "我在她旁边坐下。"

    show bs think at char_center

    bs "[player_name]，我问你一个问题。"

    mc "什么？"

    bs "你觉得……什么样的人，会让人想要一直待在她身边？"

    mc "为什么突然问这个？"

    show bs shy at char_center

    bs "就……随便问问嘛！"

    mc "（她今天好像有点不一样。）"

    mc "嗯……大概是那种，跟她在一起的时候很轻松，很自然的人吧。"

    "拨鼠安静了一会儿。"

    bs "……那你觉得，我是那种人吗？"

    mc "你？"

    show bs sad at char_center

    bs "大家都觉得我每天都很开心，对吧？"
    bs "其实……我也有很多不开心的时候。"
    bs "但我告诉自己，笑一笑，什么都会过去的。"
    bs "直到遇见你……我才觉得，原来不开心的时候，也可以跟人说。"

    menu:
        "以后不开心的时候，可以跟我说":
            $ change_mouse_affection(8, "承诺陪伴")
            jump ch4_promise

        "你不用总是那么坚强":
            $ change_mouse_affection(5, "理解拨鼠")
            jump ch4_understand

label ch4_promise:

    mc "以后不开心的时候，可以跟我说。"

    show bs shy at char_center

    "拨鼠的眼眶红了。她赶紧擦了擦眼睛。"

    bs "你说的哦！不许反悔！"

    "她轻轻打了我手臂一下，但笑容是我见过最真诚的。"

    jump ch4_flying_tree_end

label ch4_understand:

    mc "你不用总是那么坚强。"

    show bs shy at char_center

    "拨鼠安静了一会儿。"

    bs "……谢谢你。"

    "她说得很轻，没有平时的活力。但这样反而更有分量。"

    jump ch4_flying_tree_end

label ch4_flying_tree_end:

    scene bg flying_tree with dissolve

    "风吹过飞天树，红色的纸条沙沙作响。"

    show bs normal at char_center with dissolve

    bs "对了，你知道吗，校庆那天我也有节目。"

    mc "什么节目？"

    bs "舞蹈！我练了好久呢。"
    bs "你一定要来看哦！"

    mc "当然。"

    show bs shy at char_center

    bs "说定了！"

    hide bs with dissolve

    scene bg school_road with dissolve

    "回家的路上，我看到了GG的背影。"
    "她一个人走在前面。"

    show gg school normal at char_center with dissolve

    mc "GG？"

    show gg school think at char_center

    ww "……你今天跟拨鼠一起打乒乓球了？"

    mc "嗯。"

    ww "……哼。"

    "她加快了脚步。"

    mc "GG，等一下——"

    show gg school tsundere at char_center

    ww "不用你管。"

    hide gg with dissolve

    "她走远了。"
    "但我注意到，她的耳朵是红的。"

    show zm normal at char_center with dissolve

    zm "兄弟，GG吃醋了啊。"
    zm "你到底喜欢哪个？"

    mc "我……"

    zm "别犹豫太久。拖得越久，伤得越深。"

    hide zm with dissolve

    scene bg black with fade
    pause 1.0

    "校庆就在后天了。"
    "GG要负责合唱，拨鼠要表演舞蹈。"
    "而我……还没有做出选择。"

    $ chapter = 4
    jump chapter5
