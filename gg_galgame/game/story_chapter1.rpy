## 第一章：初遇与双面

label chapter1_start:

    scene bg classroom with dissolve
    pause 0.5

    "班主任把我带到了三楼的教室。"
    "推开门，几十双眼睛齐刷刷地看了过来。"

    "老师" "同学们，这是新转来的同学[player_name]，大家欢迎。"

    "稀稀拉拉的掌声。"

    "老师" "你坐那边，靠窗的位置，GG旁边。"

    show gg school normal at char_center with dissolve

    "我走向靠窗的座位。"
    "旁边的女生侧着头看窗外，马尾辫在阳光下微微发亮。"
    "她似乎完全没注意到我的存在。"

    mc "你好，我是[player_name]。"

    show gg school tsundere at char_center

    ww "……嗯。"

    "她头也没回，只是轻轻哼了一声。"

    mc "（好冷淡……）"

    "就在这时候——"

    show bs normal at char_left with dissolve

    bs "嘿！你就是新来的？"

    "一个女生从旁边的座位蹦了过来，笑容灿烂得像小太阳。"

    bs "我叫拨鼠！跟你同班！有什么不懂的尽管问我！"

    mc "你、你好……"

    bs "走走走，我带你去逛逛学校！教室里太闷了！"

    "她完全不给我拒绝的机会，拉着我的手臂就往外走。"
    "我回头看了一眼GG，她依然看着窗外，仿佛什么都没发生。"

    hide gg with dissolve
    hide bs with dissolve

    scene bg school_road with dissolve
    show bs normal at char_center with dissolve

    "拨鼠一边走一边介绍，语速快得像机关枪。"

    bs "那边是操场，那边是食堂，那边是小卖部——"
    bs "小卖部的烤肠特别好吃，下课要跑快一点才能买到！"

    mc "你……一直都这么热情吗？"

    show bs shy at char_center

    bs "有吗？大家都这么说啦！"

    mc "（跟她说话完全不需要动脑子，很轻松。）"

    scene bg basketball_court with dissolve
    show bs normal at char_center with dissolve

    "我们经过篮球场，几个男生在打球。"

    bs "我喜欢看篮球！虽然自己打得很烂就是了。"
    bs "你打篮球吗？"

    mc "偶尔。"

    show bs surprised at char_center

    bs "真的？那下次一起打！"

    "这时候一个胖胖的男生跑了过来。"

    show zm normal at char_right with dissolve

    zm "嘿，新来的！我叫肥仔，坐你后面。"

    mc "你好。"

    zm "（小声）兄弟，你运气不错啊。"
    zm "（小声）GG和拨鼠，一个是冰山，一个是小太阳。"
    zm "（小声）你第一天就被两个女生包围了。"

    mc "（我什么都没做啊……）"

    hide zm with dissolve
    hide bs with dissolve

    scene bg cafeteria_entrance with dissolve

    "不知不觉到了午饭时间。"

    show bs normal at char_left with dissolve

    bs "[player_name]！一起去食堂吃饭吧！"

    "拨鼠热情地邀请我。"
    "但我又想起教室里那个安静的背影。"

    menu:
        "和拨鼠一起去食堂吃饭":
            $ change_mouse_affection(5, "一起吃饭")
            jump ch1_lunch_mouse

        "回教室，想多了解GG一点":
            $ change_gg_affection(5, "主动接近GG")
            jump ch1_lunch_gg

        "跟肥仔一起去小卖部":
            $ change_gg_affection(1, "中立")
            $ change_mouse_affection(1, "中立")
            jump ch1_lunch_neutral

label ch1_lunch_mouse:

    hide bs with dissolve
    scene bg cafeteria_inside with dissolve
    show bs normal at char_center with dissolve

    "我和拨鼠在食堂找了位置坐下。"

    bs "你以前的学校怎么样？"

    mc "还行吧，没什么特别的。"

    bs "那你觉得二中怎么样？"

    mc "才来第一天，说不上来。"

    show bs shy at char_center

    bs "那你觉得我怎么样？"

    mc "……你这问题也太直接了吧。"

    bs "哈哈！开玩笑的！"

    "她笑起来的时候眼睛弯弯的，像月牙。"
    "跟她在一起，完全不会觉得尴尬。"

    bs "对了，GG那个人啊，别看她冷冷的，其实人很好的！"
    bs "她就是不太会表达，你别介意。"

    mc "你跟她很熟？"

    bs "还行吧！我们从初中就是同学了。"

    jump ch1_end

label ch1_lunch_gg:

    hide bs with dissolve
    scene bg classroom with dissolve
    show gg school normal at char_center with dissolve

    "我回到教室，发现GG一个人坐在位置上吃饭。"
    "她的便当盒很小，菜色很简单。"

    show gg school tsundere at char_center

    ww "你怎么回来了？"

    mc "想在这吃。"

    ww "……随便你。"

    "我在旁边坐下，两人之间隔着一段距离。"
    "谁也没说话。"
    "但我注意到，她偷偷瞄了我好几眼。"

    mc "（她在观察我？）"

    show gg school shy at char_center

    ww "……你看什么？"

    mc "没什么。"

    show gg school tsundere at char_center

    ww "哼。"

    "虽然很安静，但这种沉默并不让人难受。"

    jump ch1_end

label ch1_lunch_neutral:

    hide bs with dissolve
    scene bg school_road with dissolve
    show zm normal at char_center with dissolve

    "我跟肥仔去了小卖部。"

    zm "兄弟，我给你科普一下咱们班的情况。"
    zm "GG，班长，年级第一，脾气也是年级第一。"
    zm "拨鼠，人缘最好，全年级没有她不认识的人。"
    zm "这两个人啊，一个是冰山，一个是小太阳。"

    mc "她们关系怎么样？"

    zm "表面上还行，但你懂的……"
    zm "两个这么耀眼的女生在一个班，多少有点暗暗较劲。"

    hide zm with dissolve

    jump ch1_end

label ch1_end:

    scene bg school_gate with dissolve

    "放学了。"
    "我收拾好书包，走出教室。"

    show bs normal at char_left with dissolve

    bs "[player_name]！明天见！"

    "拨鼠朝我挥手，笑容灿烂。"

    show gg school normal at char_right with dissolve

    "GG背着书包，一个人默默地走在前面。"
    "她的背影看起来有点孤单。"

    menu:
        "追上拨鼠，跟她一起走":
            $ change_mouse_affection(3, "一起放学")
            $ change_gg_affection(-1, "忽略GG")
            jump ch1_end_mouse

        "快走几步追上GG":
            $ change_gg_affection(3, "一起放学")
            $ change_mouse_affection(-1, "忽略拨鼠")
            jump ch1_end_gg

        "自己走自己的":
            $ change_gg_affection(1, "中立")
            $ change_mouse_affection(1, "中立")
            jump ch1_end_final

label ch1_end_mouse:

    hide gg with dissolve
    show bs normal at char_center with dissolve

    mc "拨鼠，等等！"

    bs "嗯？怎么了？"

    mc "一起走吧。"

    show bs shy at char_center

    bs "好啊！"

    "我们并肩走在放学的路上。"
    "拨鼠叽叽喳喳地说个不停，我只需要偶尔应一声。"

    bs "对了，你知道飞天树吗？就是杨利伟亲手种的那棵！"
    bs "下次我带你去看！上面挂满了红色的愿望纸条！"

    mc "好啊。"

    bs "说定了哦！"

    jump ch1_end_final

label ch1_end_gg:

    hide bs with dissolve
    show gg school normal at char_center with dissolve

    mc "GG！"

    show gg school tsundere at char_center

    ww "……干什么？"

    mc "一起走吧。"

    ww "……随便你。"

    "她加快了脚步，但并没有甩开我。"
    "两个人沉默地走在放学路上。"
    "夕阳把我们的影子拉得很长。"

    mc "（她好像没有看起来那么难接近。）"

    jump ch1_end_final

label ch1_end_final:

    hide gg with dissolve
    hide bs with dissolve

    scene bg black with fade
    pause 1.0

    "第一天就这么结束了。"
    "GG……总觉得在哪里见过她。"
    "拨鼠……她真的很开朗，跟她在一起很轻松。"
    "明天开始，就是真正的校园生活了。"

    $ chapter = 1
    jump chapter2
