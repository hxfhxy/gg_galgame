## 第六章：路线分歧

## ==================== GG 路线 ====================

label chapter6_gg_route:

    scene bg quiet_corner with dissolve
    pause 0.5

    "校庆后的第二天，我在安静角落找到了GG。"
    "她正靠在墙上，手里拿着一张旧照片。"

    show gg school normal at char_center with dissolve

    mc "GG。"

    show gg school think at char_center

    ww "……你怎么来了。"

    mc "我有话想跟你说。"

    "她在旁边坐下，我也坐了下来。"
    "安静了一会儿，她开口了。"

    show gg school sad at char_center

    ww "小时候，我认识一个男孩。"
    ww "他说过会保护我，会一直陪着我。"
    ww "但是后来……他搬家了，再也没有回来。"

    mc "……"

    ww "从那以后，我就不再相信别人说的话了。"
    ww "因为承诺这种东西，太容易被打破了。"

    menu:
        "我想起来了":
            $ change_gg_affection(5, "记起承诺")
            jump ch6_gg_remember

        "我还是想不起来":
            $ change_gg_affection(-2, "没想起来")
            jump ch6_gg_forget

label ch6_gg_remember:

    mc "GG……我想起来了。"
    mc "小时候，我们是邻居。你总是跟在我后面，叫我'小哥哥'。"
    mc "有一次你被别的小孩欺负，我帮你赶走了他们。"
    mc "我答应过你，会一直保护你。"

    show gg school shy at char_center

    ww "你真的想起来了？"

    mc "嗯。对不起，让你等了这么久。"

    ww "……笨蛋，你让我等了十年。"

    "她眼眶红了，但嘴角是笑的。"

    jump ch6_gg_end

label ch6_gg_forget:

    mc "我……还是想不起来。对不起。"

    show gg school sad at char_center

    ww "……算了。不记得也好。"

    "她转身走了。"

    jump ch6_gg_end

label ch6_gg_end:

    hide gg with dissolve

    scene bg school_road with dissolve

    "回家的路上，我看到了拨鼠的背影。"
    "她走得很快，好像在赶什么。"

    show bs normal at char_center with dissolve

    bs "[player_name]！"

    mc "拨鼠？"

    show bs think at char_center

    bs "你最近……好像跟GG走得很近呢。"

    mc "嗯……"

    bs "挺好的，GG她需要有人陪。"

    "她笑了，但笑容里有一丝苦涩。"

    show bs shy at char_center

    bs "没事啦！我先走了！"

    hide bs with dissolve

    "她跑开了。"
    "她的背影，看起来没有平时那么快乐。"

    scene bg black with fade
    pause 1.0

    "GG……我终于想起了小时候的事。"
    "但拨鼠……她的笑容一直在我脑海里。"
    "明天，就是最后一天了。"

    $ chapter = 6
    jump chapter7

## ==================== 拨鼠 路线 ====================

label chapter6_mouse_route:

    scene bg flying_tree with dissolve
    pause 0.5

    "校庆后的第二天，拨鼠约我在飞天树下见面。"
    "夕阳把红色的纸条染成了金色。"

    show bs normal at char_center with dissolve

    bs "[player_name]，你来了。"

    mc "嗯。"

    show bs think at char_center

    bs "我……我想跟你说件事。"

    "她今天不像平时那么活泼，反而有些紧张。"

    bs "从你转学来的第一天起，我就……"
    bs "不，太突然了。让我再想想。"

    show bs shy at char_center

    bs "下次！下次我一定说！"

    "她笑了，但笑声里带着紧张。"

    scene bg quiet_corner with dissolve
    show bs normal at char_center with dissolve

    "我们在安静角落坐了下来。"

    bs "大家都觉得我每天都很开心，对吧？"

    mc "嗯，你看起来总是很快乐。"

    show bs sad at char_center

    bs "其实……我也有很多不开心的时候。"
    bs "但我告诉自己，笑一笑，什么都会过去的。"
    bs "直到遇见你……我才觉得，原来不开心的时候，也可以跟人说。"

    menu:
        "以后不开心的时候，可以跟我说":
            $ change_mouse_affection(8, "承诺陪伴")
            jump ch6_mouse_promise

        "你不用总是那么坚强":
            $ change_mouse_affection(5, "理解拨鼠")
            jump ch6_mouse_understand

label ch6_mouse_promise:

    mc "以后不开心的时候，可以跟我说。"

    show bs shy at char_center

    "拨鼠的眼眶红了。她赶紧擦了擦眼睛。"

    bs "你说的哦！不许反悔！"

    "她轻轻打了我手臂一下，但笑容是我见过最真诚的。"

    jump ch6_mouse_end

label ch6_mouse_understand:

    mc "你不用总是那么坚强。"

    show bs shy at char_center

    "拨鼠安静了一会儿。"

    bs "……谢谢你。"

    "她说得很轻，没有平时的活力。但这样反而更有分量。"

    jump ch6_mouse_end

label ch6_mouse_end:

    scene bg school_road with dissolve

    "回家的路上，我看到了GG的背影。"
    "她一个人走在前面，看起来很孤单。"

    show gg school normal at char_center with dissolve

    mc "GG？"

    show gg school sad at char_center

    ww "……你不用管我。"
    ww "你去陪拨鼠就好了。"

    hide gg with dissolve

    "她快步走远了。"

    mc "（GG……）"

    scene bg black with fade
    pause 1.0

    "拨鼠的温暖，让我无法抗拒。"
    "但GG的背影，也让我无法释怀。"
    "明天，就是最后一天了。"

    $ chapter = 6
    jump chapter7

## ==================== 中立路线 ====================

label chapter6_neutral:

    scene bg school_road with dissolve
    pause 0.5

    "校庆后的第二天，我一个人走在放学的路上。"

    show zm normal at char_center with dissolve

    zm "兄弟，你还没做出选择吗？"

    mc "……没有。"

    zm "两个都喜欢，等于两个都不喜欢。"
    zm "你必须选一个。"

    show jc normal at char_left with dissolve

    jc "优柔寡断的人，谁都配不上。"

    hide jc with dissolve
    hide zm with dissolve

    menu:
        "我想选GG":
            $ change_gg_affection(5, "选择GG")
            $ route = "gg"
            jump ch6_neutral_pick_gg

        "我想选拨鼠":
            $ change_mouse_affection(5, "选择拨鼠")
            $ route = "mouse"
            jump ch6_neutral_pick_mouse

        "我……不知道":
            $ change_gg_affection(-3, "犹豫不决")
            $ change_mouse_affection(-3, "犹豫不决")
            jump ch6_neutral_undecided

label ch6_neutral_pick_gg:

    scene bg quiet_corner with dissolve

    "我去找GG。"
    "她正靠在墙上，看着天空发呆。"

    show gg school think at char_center

    ww "……你怎么来了。"

    mc "我有话想跟你说。"

    $ chapter = 6
    jump chapter7

label ch6_neutral_pick_mouse:

    scene bg flying_tree with dissolve

    "我去找拨鼠。"
    "但树下空无一人。"
    "红色的纸条在风中沙沙作响。"

    mc "（她已经走了。）"

    $ chapter = 6
    jump chapter7

label ch6_neutral_undecided:

    scene bg school_road with dissolve

    "我一个人走在回家的路上。"
    "脑子里很乱。"

    mc "（我到底喜欢谁？）"
    mc "（GG……拨鼠……）"
    mc "（我不知道。）"

    $ chapter = 6
    jump chapter7
