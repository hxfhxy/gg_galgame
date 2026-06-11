## 第五章：校庆风波

label chapter5_start:

    scene bg classroom with dissolve
    pause 0.5

    "校庆前一天，大家都在忙着准备。"

    show gg school normal at char_left with dissolve
    show bs normal at char_right with dissolve

    "GG作为班长负责统筹，拨鼠负责舞蹈排练。"
    "两个人都很忙，但偶尔会在走廊里碰到。"

    bs "GG！舞台那边的灯调好了吗？"

    ww "调好了。你的舞蹈练得怎么样？"

    bs "没问题！明天一定惊艳全场！"

    show gg school tsundere at char_left

    ww "……希望如此。"

    "她们的对话很自然，但我能感觉到空气中有一丝紧张。"

    "这时候，两个人同时看向了我。"

    bs "[player_name]！帮我对一下舞蹈动作吧！"

    ww "[player_name]，合唱还需要排练一遍。"

    "两个人都等着我做选择。"

    menu:
        "帮拨鼠对舞蹈动作":
            $ change_mouse_affection(5, "帮拨鼠排练")
            $ change_gg_affection(-2, "选拨鼠")
            jump ch5_help_mouse

        "帮GG排练合唱":
            $ change_gg_affection(5, "帮GG排练")
            $ change_mouse_affection(-2, "选GG")
            jump ch5_help_gg

        "你们两个自己商量":
            $ change_gg_affection(1, "中立")
            $ change_mouse_affection(1, "中立")
            jump ch5_help_both

label ch5_help_mouse:

    hide gg with dissolve
    show bs normal at char_center with dissolve

    "我帮拨鼠对舞蹈动作。"
    "她跳得很好，只是有些细节需要调整。"

    bs "这个动作对不对？"

    mc "手臂再抬高一点。"

    bs "这样？"

    mc "嗯，完美。"

    show bs shy at char_center

    bs "嘿嘿，有你看着我就放心了。"

    hide bs with dissolve

    jump ch5_festival_prep_end

label ch5_help_gg:

    hide bs with dissolve
    show gg school normal at char_center with dissolve

    "我帮GG排练合唱。"
    "她的声音很好听，但高音部分有点紧张。"

    mc "别紧张，深呼吸。"

    show gg school shy at char_center

    ww "我才不紧张……"

    "但她确实唱得更好了。"

    hide gg with dissolve

    jump ch5_festival_prep_end

label ch5_help_both:

    hide gg with dissolve
    hide bs with dissolve

    "两个人都有点不满，但还是各自去忙了。"

    jump ch5_festival_prep_end

label ch5_festival_prep_end:

    scene bg corridor with dissolve

    "傍晚，我在走廊里遇到了GG。"

    show gg school think at char_center with dissolve

    ww "[player_name]。"

    mc "怎么了？"

    ww "明天……你会来看合唱吧？"

    mc "当然。"

    show gg school tsundere at char_center

    ww "……随便你。来不来都无所谓。"

    "她转身走了。但我注意到，她问完之后脚步明显轻快了。"

    hide gg with dissolve

    scene bg festival_stage with dissolve
    pause 0.5

    "校庆当天，文艺汇演正式开始。"

    show gg school normal at char_center with dissolve

    "我们班的合唱节目排在第五个。"
    "站在舞台上，灯光打在身上，台下坐满了人。"

    mc "（小声）别紧张，就像排练时那样就好。"

    show gg school shy at char_center

    ww "（小声）我才不紧张……"

    "音乐响起，我们一起开口。"
    "她的声音很清澈，和我想象中一样好听。"
    "一曲终了，台下响起了热烈的掌声。"

    show gg school normal at char_center

    ww "……今天表现得还行。"

    mc "你唱得很好听。"

    show gg school tsundere at char_center

    ww "哼，这种事不用你说。"

    "但她嘴角微微上扬。"

    hide gg with dissolve

    "下一个节目，是拨鼠的舞蹈。"

    show bs normal at char_center with dissolve

    "她穿着亮闪闪的演出服，活力四射。"
    "音乐响起，她跳了起来。"
    "动作干净利落，笑容灿烂得像太阳。"
    "台下响起了热烈的欢呼。"

    "表演结束后，她跑下台，直奔我这边。"

    show bs shy at char_center

    bs "你看到了吗？你看到了吗？"

    mc "看到了，你太厉害了。"

    bs "真的？"

    mc "真的。全场最耀眼的就是你。"

    "她脸红了，但笑得很开心。"

    hide bs with dissolve

    "就在这时候，一个男生走了过来。"

    show jc normal at char_left with dissolve

    jc "gg，今天的演出很棒，我想请你——"

    "不知道什么时候，GG出现在我旁边。"
    "她下意识地抓住了我的手臂。"

    show gg school tsundere at char_right

    ww "不用了，我已经有约了。"

    jc "……这位是？"

    menu:
        "我是她的人":
            $ change_gg_affection(8, "大胆表态")
            jump ch5_bold

        "我是她的朋友":
            $ change_gg_affection(-3, "只说是朋友")
            jump ch5_friend

        "沉默，让她自己说":
            $ change_gg_affection(3, "沉默等待")
            jump ch5_silent

label ch5_bold:

    mc "我是她的人。"

    show gg school shy at char_right

    ww "你、你在说什么啊！"

    show jc sad at char_left

    jc "……原来如此。打扰了。"

    hide jc with dissolve

    show gg school tsundere at char_right

    ww "你……你怎么能乱说！"

    mc "可是你刚才不是抓住我了吗？"

    show gg school shy at char_right

    ww "那、那是……条件反射！"

    jump ch5_festival_end

label ch5_friend:

    mc "我是她的朋友。"

    show gg school sad at char_right

    "GG的手松开了，表情变得有些失落。"

    ww "……对，只是朋友。"

    jc "那gg，你愿意——"

    ww "我说了不用了！"

    hide jc with dissolve

    "她转身跑开了。"

    jump ch5_festival_end

label ch5_silent:

    mc "……"

    ww "他是……"

    show gg school think at char_right

    ww "他是我很重要的人。"

    show jc disappointed at char_left

    jc "……好吧，我明白了。"

    hide jc with dissolve

    show gg school tsundere at char_right

    ww "别误会！我只是不想被他纠缠！"

    jump ch5_festival_end

label ch5_festival_end:

    hide gg with dissolve

    "校庆结束了。"
    "我在操场上看到了拨鼠。"
    "她正在收拾舞台道具，一个人搬着箱子。"

    show bs normal at char_center with dissolve

    mc "我来帮你。"

    show bs shy at char_center

    bs "谢谢！"

    "我们一边收拾一边聊天。"

    bs "今天真开心。"
    bs "你看了我的表演，还帮GG解了围。"

    mc "你都看到了？"

    show bs normal at char_center

    bs "当然看到了。"
    bs "[player_name]，你对GG……是不是有特别的感情？"

    mc "我……"

    bs "没关系的，你不用回答。"
    bs "我只是想让你知道……"
    bs "不管你选谁，我都希望你幸福。"

    "她笑了，但眼里有一丝我看不懂的情绪。"

    hide bs with dissolve

    scene bg black with fade
    pause 1.0

    "校庆结束了。"
    "但我的心，还没有做出选择。"
    "明天……我必须想清楚。"

    $ chapter = 5
    jump chapter6
