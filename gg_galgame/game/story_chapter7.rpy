## 第七章：结局

## ==================== GG 路线结局 ====================

label chapter7_gg_start:

    scene bg quiet_corner with dissolve
    pause 0.5

    "最后一天，我在安静角落找到了GG。"
    "她正靠在墙上，看着天空发呆。"

    show gg school normal at char_center with dissolve

    mc "GG。"

    show gg school think at char_center

    ww "……你怎么又来了。"

    mc "我有话想跟你说。"

    ww "如果是昨天的事，我已经忘了。"

    mc "不是昨天的事。"
    mc "是关于我们俩的事。"

    show gg school shy at char_center

    "她的身体明显僵了一下。"

    mc "GG，我想起来了。"
    mc "小时候，我们是邻居。你总是跟在我后面，叫我'小哥哥'。"
    mc "有一次你被别的小孩欺负，我帮你赶走了他们。"
    mc "我答应过你，会一直保护你。"

    show gg school sad at char_center

    ww "但是你后来搬家了。"
    ww "你连再见都没跟我说。"

    mc "对不起。那时候太小了，我不知道该怎么告别。"
    mc "而且我爸妈说走就走，我根本没有选择。"

    ww "……"

    mc "但是，GG，我现在记起来了。"
    mc "而且这一次，我不会再失约了。"

    show gg school think at char_center

    ww "你知道你在说什么吗？"

    mc "我知道。"

    ww "你才来这个学校一个月，你了解我吗？"
    ww "你知道我脾气不好，很容易生气吗？"
    ww "你知道我嘴硬心软，说话总是很难听吗？"

    mc "我都知道。"

    show gg school sad at char_center

    ww "那你为什么还……"

    mc "因为你是GG啊。"

    "她沉默了很久。"

    show gg school shy at char_center

    ww "……你真的很烦。"
    ww "明明才认识一个月，就说这种话。"

    mc "嗯。"

    ww "……笨蛋。"

    "她的声音越来越小，脸越来越红。"

    if gg_affection >= 20:
        jump ch7_gg_high
    elif gg_affection >= 10:
        jump ch7_gg_mid
    else:
        jump ch7_gg_low

label ch7_gg_high:

    mc "GG，我喜欢你。不是因为小时候的承诺，是因为你是你。"

    show gg school shy at char_center

    ww "你真的很烦……明明才一个月，就让我哭了。"

    mc "你哭了？"

    ww "才没有！是风沙迷了眼睛！"

    mc "（我笑了）嗯，是风沙。"

    ww "……笨蛋。"

    "她靠在我的肩膀上。"

    scene bg sunset with dissolve
    show gg school shy at char_center with dissolve

    "我们站在学校的走廊上，夕阳从窗户照进来，把一切都染成了金色。"

    ww "[player_name]。"

    mc "嗯？"

    ww "以后……我们还会一起走这条走廊吗？"

    mc "当然。以后的每一天，我都陪你走。"

    ww "……说话算话。"

    mc "说话算话。"

    jump gg_true_ending

label ch7_gg_mid:

    mc "GG，我想给你一个机会。也给我自己一个机会。"

    show gg school think at char_center

    ww "我……我需要时间。"
    ww "不是不喜欢你。只是……我还没完全放下小时候的事。"

    "她伸出手，又缩了回去。"

    ww "给我一点时间，好吗？"

    mc "好。我等你。"

    show gg school shy at char_center

    ww "谢谢你转学来这里。虽然你很烦，但有你在，日子确实没那么无聊了。"

    mc "（我笑了）你这是在夸我吗？"

    ww "才不是！你想多了！"

    jump gg_normal_ending

label ch7_gg_low:

    show gg school sad at char_center

    ww "太晚了。"
    ww "我等了你十年，你没有回来。"
    ww "我已经学会了不再期待。"
    ww "学会了把自己保护起来。"

    mc "GG……"

    ww "不是你的错。只是……我们错过了太多。"

    "她转身离开了。"

    jump bad_ending

## ==================== 拨鼠 路线结局 ====================

label chapter7_mouse_start:

    scene bg flying_tree with dissolve
    pause 0.5

    "最后一天放学后，拨鼠约我在飞天树下见面。"
    "夕阳把红色的纸条染成了金色。"

    show bs normal at char_center with dissolve

    bs "你来了。"

    mc "嗯。"

    show bs think at char_center

    bs "[player_name]，上次我说下次一定说……"
    bs "所以，我来了。"

    "她深吸一口气。"

    bs "我喜欢你。从你转学来的第一天就喜欢你了。"
    bs "你笑起来的样子，你认真听课的样子，你帮GG搬桌子时的样子……"
    bs "我都看到了，我都记住了。"

    show bs shy at char_center

    bs "我知道你心里可能还有别人。"
    bs "但是……我还是想让你知道。"

    if mouse_affection >= 20:
        jump ch7_mouse_high
    elif mouse_affection >= 10:
        jump ch7_mouse_mid
    else:
        jump ch7_mouse_low

label ch7_mouse_high:

    mc "拨鼠，我也喜欢你。"

    show bs shy at char_center

    "拨鼠的眼睛一下子亮了起来。"

    bs "真的吗？你不是在开玩笑？"

    mc "真的。"

    "她的眼泪掉了下来，但笑得比任何时候都灿烂。"

    bs "那你不许反悔！"

    "她抓住我的手。"

    bs "我们在这棵树上挂一个愿望吧！"

    "她掏出一张红纸条，认真地写了起来。"

    bs "希望永远和[player_name]在一起。"

    "她把纸条系在树枝上，然后转向我。"

    bs "你的愿望呢？"

    mc "我的愿望已经实现了。"

    show bs shy at char_center

    "她又哭了。但这次，是笑着哭的。"

    jump mouse_true_ending

label ch7_mouse_mid:

    mc "拨鼠，谢谢你。"

    show bs think at char_center

    bs "……你的'谢谢'听起来像是'对不起'。"

    mc "我……"

    bs "没关系，我理解。"
    bs "你心里还有放不下的事吧？"

    show bs shy at char_center

    bs "我可以等。"

    mc "拨鼠……"

    bs "谢什么啦！我们还是好朋友啊！"

    jump mouse_normal_ending

label ch7_mouse_low:

    mc "……"

    "我无法回应她。"

    show bs sad at char_center

    bs "……我明白了。"

    "她转过身去。"

    bs "没关系啦，当我没说过！"

    "但我能听到她的声音在发抖。"

    jump bad_ending

## ==================== BAD END ====================

label bad_ending:

    scene bg school_road with dissolve
    pause 0.5

    "我一个人走在放学的路上。"
    "经过飞天树——红色的纸条在风中飘动，但树下没有人。"
    "经过安静角落——空荡荡的。"

    show zm normal at char_center with dissolve

    zm "兄弟，你怎么一个人？"

    mc "……我错过了。"

    zm "错过了什么？"

    mc "……不知道。也许，是青春吧。"

    hide zm with dissolve

    "夕阳把我的影子拉得很长。"
    "一个人的影子。"

    scene bg black with fade
    pause 2.0

    "—— BAD END ——"
    "「错过了，就是错过了。」"
    "「但也许，下一次，我们不会再错过。」"

    jump ending_gallery_show

label ending_gallery_show:
    call screen ending_gallery_screen
    return
