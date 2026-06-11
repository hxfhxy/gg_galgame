## 第二章：日常交错

label chapter2_start:

    scene bg classroom with dissolve
    pause 0.5

    "转眼间，来到二中已经一周了。"

    show gg school normal at char_center with dissolve

    "早自习，GG难得主动开口了。"

    ww "昨天的数学作业，你做了吗？"

    mc "嗯，做了。"

    show gg school think at char_center

    ww "最后一道大题，你的答案是多少？"

    mc "我算出来是根号三。"

    show gg school tsundere at char_center

    ww "……跟我一样。"

    "她小声嘀咕了一句，继续低头看书。"

    mc "（所以她是在确认自己的答案？）"

    show bs normal at char_left with dissolve

    bs "[player_name]！你看窗外！"

    "拨鼠突然跑过来，拉着我往窗外看。"

    bs "你看那只猫！它在树上下不来了！哈哈哈哈哈！"

    mc "……确实挺好笑的。"

    show gg school angry at char_center

    "我感觉到背后有一道冰冷的目光。"

    show jj normal at char_right with dissolve

    jj "GG~你是不是吃醋了？"

    show gg school tsundere at char_center

    ww "才没有！"

    hide jj with dissolve
    hide bs with dissolve

    scene bg basketball_court with dissolve
    show bs normal at char_center with dissolve

    "体育课，拨鼠拉着我去看篮球赛。"

    bs "快快快！今天有我们班的比赛！"

    show jc normal at char_left with dissolve

    "球场上，jc正在运球，动作很帅气。"
    "他看到拨鼠和我站在一起，微微皱了皱眉。"

    show zm normal at char_right with dissolve

    zm "（小声）jc那家伙对GG有意思，不过他好像也在意拨鼠。"
    zm "（小声）兄弟，你情敌不少啊。"

    mc "我没有在追谁……"

    zm "（小声）是吗？那你跟两个女生都走这么近？"

    hide jc with dissolve
    hide zm with dissolve
    hide bs with dissolve

    scene bg quiet_corner with dissolve
    show gg school normal at char_center with dissolve

    "课间，我在安静角落找到了GG。"
    "她正靠在墙上看书，周围很安静。"

    mc "这里倒是挺隐蔽的。"

    show gg school tsundere at char_center

    ww "你怎么找到这里的？"

    mc "随便逛逛就到了。"

    ww "……这是我的秘密基地。"

    mc "那我走？"

    show gg school think at char_center

    ww "……算了。来都来了。"

    "我在她旁边坐下。两人沉默了一会儿。"

    ww "……你跟拨鼠，走得很近啊。"

    menu:
        "拨鼠人很好，很开朗":
            $ change_mouse_affection(3, "夸拨鼠")
            $ change_gg_affection(-2, "在GG面前夸拨鼠")
            jump ch2_jealousy_a

        "只是普通朋友":
            $ change_gg_affection(3, "解释关系")
            $ change_mouse_affection(-1, "撇清关系")
            jump ch2_jealousy_b

        "你在意吗？":
            $ change_gg_affection(5, "反问GG")
            jump ch2_jealousy_c

label ch2_jealousy_a:

    show gg school sad at char_center

    ww "哼，她确实……很会跟人打交道。"

    "她低下头继续看书，但书页好久没有翻动。"

    mc "（我是不是说错话了？）"

    jump ch2_afternoon

label ch2_jealousy_b:

    show gg school tsundere at char_center

    ww "……我又没问你们是什么关系。"

    "但她似乎松了一口气。"

    jump ch2_afternoon

label ch2_jealousy_c:

    show gg school shy at char_center

    ww "谁、谁在意了！我只是随便问问！"

    "她站起来，耳朵红红的。"

    ww "我走了！"

    "她快步离开，走了几步又回头看了一眼。"

    jump ch2_afternoon

label ch2_afternoon:

    scene bg playground with dissolve
    show bs normal at char_center with dissolve

    "下午放学后，拨鼠找到了我。"

    bs "[player_name]！走嘛走嘛，我带你去看飞天树！"

    mc "飞天树？"

    bs "就是杨利伟亲手种的那棵树啊！上面挂满了红色的愿望纸条！"
    bs "很漂亮的！你一定要去看看！"

    menu:
        "好啊，一起去":
            $ change_mouse_affection(5, "去看飞天树")
            jump ch2_tree_yes

        "今天有点累了，下次吧":
            $ change_mouse_affection(-1, "拒绝邀请")
            $ change_gg_affection(2, "保留精力")
            jump ch2_tree_no

label ch2_tree_yes:

    hide bs with dissolve
    scene bg flying_tree with dissolve
    show bs normal at char_center with dissolve

    "拨鼠带我来到学校后面的小广场。"
    "一棵巨大的树立在中央，枝条上挂满了红色的纸条。"
    "夕阳的光照在上面，像一片片燃烧的火焰。"

    bs "漂亮吧！"

    mc "真的很漂亮。"

    show bs shy at char_center

    bs "我小时候就在这棵树下许过愿。"
    bs "希望每天都能这么开心！"

    "她从口袋里掏出一张红纸条，认真地写了起来。"

    bs "你的愿望是什么？"

    mc "秘密。"

    bs "切——秘密的愿望最灵了！"

    "她站在我旁边，风把她的头发吹到了我肩上。"
    "我能闻到她洗发水的香味。"

    mc "（跟她在一起，真的很轻松。）"

    jump ch2_end

label ch2_tree_no:

    hide bs with dissolve
    scene bg classroom with dissolve
    show gg school normal at char_center with dissolve

    "我留在教室。"
    "GG还在，假装在看书。"

    ww "……你没跟拨鼠出去？"

    mc "嗯，今天想休息。"

    show gg school tsundere at char_center

    ww "……哼，随便你。"

    "但她似乎心情不错。"

    jump ch2_end

label ch2_end:

    scene bg school_gate with dissolve
    show zm normal at char_center with dissolve

    "放学路上，肥仔追了上来。"

    zm "兄弟，你今天同时跟两个女生互动了啊。"
    zm "GG和拨鼠……你到底喜欢哪个？"

    mc "我……还没想好。"

    zm "小心啊，这种事拖久了，两个都会受伤的。"

    show jc normal at char_left with dissolve

    "jc从旁边走过，故意撞了一下我的肩膀。"

    jc "……新来的，别太得意。"

    hide jc with dissolve

    zm "别理他。jc那家伙对GG有意思，看你跟GG走得近，心里不爽。"

    hide zm with dissolve

    scene bg black with fade
    pause 1.0

    "GG……她好像在等我记起什么。"
    "拨鼠……她的笑容，总能让人放松下来。"
    "但是，我不能同时对两个人……"

    $ chapter = 2
    jump chapter3
