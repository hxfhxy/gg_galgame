## 角色定义与变量系统

## 男主名字（允许玩家自定义）
default player_name = "杨哥"

## 双女主好感度系统
default gg_affection = 0
default mouse_affection = 0
default route = ""  # "gg", "mouse", or ""

## 章节进度
default chapter = 0

## CG 解锁状态
default cg_unlocked = {
    "cg_cover": False,
    "cg_festival": False,
    "cg_mountain": False,
    "cg_confession": False,
    "cg_gg_true_end": False,
    "cg_gg_normal_end": False,
    "cg_mouse_true_end": False,
    "cg_mouse_normal_end": False,
    "cg_bad_end": False,
}

## 结局解锁状态
default ending_unlocked = {
    "gg_true_end": False,
    "gg_normal_end": False,
    "mouse_true_end": False,
    "mouse_normal_end": False,
    "bad_end": False,
}

## 角色定义
define narrator = Character(None, what_color="#ffffff")
define mc = DynamicCharacter("player_name", color="#4fc3f7", what_color="#ffffff")
define ww = Character("GG", color="#ff8a80", what_color="#ffffff")
define bs = Character("拨鼠", color="#ffb74d", what_color="#ffffff")
define jj = Character("进进", color="#81c784", what_color="#ffffff")
define zm = Character("肥仔", color="#90caf9", what_color="#ffffff")
define jc = Character("jc", color="#ce93d8", what_color="#ffffff")

## 角色图片定义 - 拨鼠
image bs normal = "images/char/boshu/normal.png"
image bs shy = "images/char/boshu/shy.png"
image bs angry = "images/char/boshu/angry.png"
image bs sad = "images/char/boshu/sad.png"
image bs surprised = "images/char/boshu/surprised.png"
image bs disappointed = "images/char/boshu/disappointed.png"
image bs think = "images/char/boshu/normal.png"

## 角色图片定义 - 肥仔
image zm normal = "images/char/feizai/normal.png"
image zm surprised = "images/char/feizai/surprised.png"
image zm angry = "images/char/feizai/angry.png"
image zm sad = "images/char/feizai/sad.png"
image zm disappointed = "images/char/feizai/disappointed.png"
image zm shy = "images/char/feizai/shy.png"

## 角色图片定义 - jc
image jc normal = "images/char/jc/normal.png"
image jc shy = "images/char/jc/shy.png"
image jc angry = "images/char/jc/angry.png"
image jc sad = "images/char/jc/sad.png"
image jc surprised = "images/char/jc/surprised.png"
image jc upset = "images/char/jc/upset.png"
image jc disappointed = "images/char/jc/sad.png"

## 角色图片定义 - 女主GG（校服）
image gg school normal = "images/char/gg/school_normal.png"
image gg school shy = "images/char/gg/school_shy.png"
image gg school tsundere = "images/char/gg/school_tsundere.png"
image gg school angry = "images/char/gg/school_angry.png"
image gg school sad = "images/char/gg/school_sad.png"
image gg school think = "images/char/gg/school_think.png"

## 角色图片定义 - 女主GG（日常）
image gg casual normal = "images/char/gg/casual_normal.png"
image gg casual shy = "images/char/gg/casual_shy.png"
image gg casual tsundere = "images/char/gg/casual_tsundere.png"
image gg casual angry = "images/char/gg/casual_angry.png"
image gg casual unhappy = "images/char/gg/casual_unhappy.png"
image gg casual think = "images/char/gg/casual_think.png"
image gg casual surprised = "images/char/gg/casual_shy.png"

## 角色图片定义 - 女配进进
image jj normal = "images/char/jinjin/normal.png"
image jj shy = "images/char/jinjin/shy.png"
image jj tsundere = "images/char/jinjin/tsundere.png"
image jj angry = "images/char/jinjin/angry.png"
image jj sad = "images/char/jinjin/sad.png"
image jj think = "images/char/jinjin/think.png"

## CG 图片定义
image cg cover = "images/cg/gg_cover.png"
image cg base = "images/cg/gg_base.jpg"

## 背景图片定义（自动缩放填满屏幕）
image bg school_gate = Transform("images/bg/school_gate.png", size=(1920, 1080), fit="cover")
image bg classroom = Transform("images/bg/classroom.jpg", size=(1920, 1080), fit="cover")
image bg playground = Transform("images/bg/playground.jpg", size=(1920, 1080), fit="cover")
image bg quiet_corner = Transform("images/bg/quiet_corner.jpg", size=(1920, 1080), fit="cover")
image bg dorm_area = Transform("images/bg/dorm_area.jpg", size=(1920, 1080), fit="cover")
image bg school_road = Transform("images/bg/school_road.jpg", size=(1920, 1080), fit="cover")
image bg hiking = Transform("images/bg/hiking.jpg", size=(1920, 1080), fit="cover")
image bg mountaintop = Transform("images/bg/mountaintop.jpg", size=(1920, 1080), fit="cover")
image bg corridor = Transform("images/bg/school_road.jpg", size=(1920, 1080), fit="cover")
image bg sunset = Transform("images/bg/sunset.jpg", size=(1920, 1080))
image bg festival_stage = Transform("images/bg/festival_stage.jpg", size=(1920, 1080), fit="cover")
image bg basketball_court = Transform("images/bg/basketball_court.jpg", size=(1920, 1080))
image bg flying_tree = Transform("images/bg/flying_tree.jpg", size=(1920, 1080))
image bg cafeteria_entrance = Transform("images/bg/cafeteria_entrance.jpg", size=(1920, 1080))
image bg cafeteria_inside = Transform("images/bg/cafeteria_inside.jpg", size=(1920, 1080))
image bg gym_entrance = Transform("images/bg/gym_entrance.jpg", size=(1920, 1080))
image bg gym_inside = Transform("images/bg/gym_inside.jpg", size=(1920, 1080))

## 白色占位背景
image bg white = "#ffffff"
image bg black = "#000000"

## 标题界面背景
image bg title = "gui/main_menu.png"

## 好感度变化函数
init python:
    def change_gg_affection(amount, reason=""):
        global gg_affection
        gg_affection += amount
        if gg_affection < 0:
            gg_affection = 0
        if gg_affection > 100:
            gg_affection = 100
        renpy.notify("GG好感度 " + ("+" if amount > 0 else "") + str(amount) + " (当前: " + str(gg_affection) + ")")

    def change_mouse_affection(amount, reason=""):
        global mouse_affection
        mouse_affection += amount
        if mouse_affection < 0:
            mouse_affection = 0
        if mouse_affection > 100:
            mouse_affection = 100
        renpy.notify("拨鼠好感度 " + ("+" if amount > 0 else "") + str(amount) + " (当前: " + str(mouse_affection) + ")")

    def unlock_cg(cg_name):
        global cg_unlocked
        if cg_name in cg_unlocked:
            cg_unlocked[cg_name] = True

    def unlock_ending(ending_name):
        global ending_unlocked
        if ending_name in ending_unlocked:
            ending_unlocked[ending_name] = True
