from unittest import TestCase

from ch_title_gen import ChineseTitleGenerator


class TestChineseTitleGenerator(TestCase):
    def test_get_suffixes(self):
        print(f"\nRunning {self._testMethodName}...")
        gen = ChineseTitleGenerator()
        gen.name = "Sample name"
        self.assertEqual(gen.get_suffixes(), "")

    def test_miscellaneous_strings_filter(self):
        print(f"\nRunning {self._testMethodName}...")
        gen = ChineseTitleGenerator()
        test_vals = {
            '1080P': '',
            '1080P 一世成仙 第57集 4K': ' 一世成仙 第57集 ',
            '1080p': '1080p',
            '4K': '',
            '4k': '4k',
            '一世成仙 1080P 第57集': '一世成仙  第57集',
            '真武巅峰1080': '真武巅峰1080'
        }
        for i, (name, result) in enumerate(test_vals.items()):
            with self.subTest(i=i):
                name = gen.miscellaneous_strings_filter(name)
                self.assertEqual(name, result)

    def test_chinese_num_filter(self):
        print(f"\nRunning {self._testMethodName}...")
        gen = ChineseTitleGenerator()
        test_vals = {
            "绝世 第七季 peerless 第四十八集": "绝世 第7季 peerless 第48集",
        }
        for i, (name, result) in enumerate(test_vals.items()):
            with self.subTest(i=i):
                name = gen.chinese_num_filter(name)
                self.assertEqual(name, result)

    def test_use_all_name_numbers(self):
        print(f"\nRunning {self._testMethodName}...")
        gen = ChineseTitleGenerator()
        gen.filtered_name = "绝世 第七季 peerless Season7 54第五十四集"
        gen.use_all_name_numbers()
        self.assertEqual(gen.season_no, "7")
        self.assertEqual(gen.episode_no, "54")

    def test_generate_title(self):
        print(f"\nRunning {self._testMethodName}...")
        test_vals = {
            'Multi Sub【逆天至尊】  Against The Sky Supreme   EP 356 再下一城': ' EP356',
            '《毒手巫医丨Poisonous Witch Doctcr》EP83': ' EP83',
            '《网游之天下无双丨Online Game— Unparalleled In The World》EP35': ' EP35',
            '【Eng Sub】《都市圣手：我即医武巅峰｜Urban Sage： The Apex Healer》第51集：娇俏人妻，': ' EP51',
            '【万古第一神】第82集：海上救援 ｜ First God of the Ages #热血 #玄幻 #冒险 #动态漫画 #七号动漫馆': ' EP82',
            '【剑仙武帝：开局玄武门之变】第105集：无视屏障 ｜ Sword Immortal Martial Emperor #热血': ' EP105',
            "【原来我是魔道老祖】第44集：新的龙皇 ｜ So I'm the Devil's Elder？ ": ' EP44',
            '【古武高手在都市 第四季】第56集：神土，那是何物？ ｜ Ancient Martial Arts Master in the City #热血 ': ' S4 EP56',
            '【命轮之主！当异变降临人间】第39集：缨子出车祸了？！｜Lord of the Wheel of Fortune! ': ' EP39',
            '【大佬下山：开局成为男秘】第31集 我自有办法 ｜ Became a male secretary at the beginning': ' EP31',
            '【天渊归来：我即是天灾】第56集！｜ Return of the Heavenly Abyss： I Am the Divine Deluge': ' EP56',
            '【开局十个大帝都是我徒弟 第四季】第14集：本座成全你 ｜ The Emperor are my Apprentices': ' S4 EP14',
            '【开局十个大帝都是我徒弟】第195集：进入丹神峰 ｜ The Emperor are my Apprentices #热血 ': ' EP195',
            '【开局有剑域，我能苟成剑神】第108集：师傅，你终于回来了 ｜ There is a Sword Field at the Beginning': ' EP108',
            '【开局签到至尊丹田】第151集：十八神子，力挽狂澜 ｜ Sign in to the Supreme Dantian at the Beginning #热血': ' EP151',
            '【弟子修炼，我躺平！】第75集：火灵之力 ｜ The Disciple Cultivates while I Chill #热血 #玄幻 #修仙': ' EP75',
            '【弟子修炼，我躺平！第二季】第16集：有死无生 ｜ The Disciple Cultivates while I Chill #热血 #玄幻': ' S2 EP16',
            "【我拿捏了气运之子】第60集：小心他的符箓 ｜ I've got the Son of Fortune #热血 #修仙 #玄幻 #系统": ' EP60',
            '【我是大仙尊】第259集：救世万民，永享极乐 ｜ I Am Great Immortal #热血 #玄幻 #修仙 #动态漫画 #七号动漫馆': ' EP259',
            '【我有百万倍攻速】第85集：灵气探测法宝 ｜ I Have a Million Times Attack Speed #热血': ' EP85',
            '【我的妻子是大乘期大佬】第71集：阴险的太上长老 ｜ My Wife is a Mahayana Master #热血 #玄幻 #冒险': ' EP71',
            '【我的弟子遍布诸天万界】第134集：万箭穿心，皆为炮灰 ｜ My Disciples are All Over the World': ' EP134',
            "【我神魔双修：制霸当世】第49集：第三考场，初始积分 ｜ I'm Divine and Demonic #热血 #奇幻 #冒险 #动态漫画": ' EP49',
            '【新番上线】《我夫人竟是皇朝女帝》第1~5集   顾澜穿越玄幻小说，加载了文抄读书系统！只要读书抄书，就能提取修为，': ' EP1-5',
            '【无敌圣子：我可以无限顿悟】第86集：你的事就是我的事！｜ I Can Realize Infinitely #热血 #修仙 #玄幻 #动态漫画': ' EP86',
            '【暴富系统：我有999个新马甲】第66集 ｜ Profitable System： I Have 999 New Characters': ' EP66',
            '【最强仙尊陈北玄 第四季】第115~116集：陈北玄打破血脉诅咒？！｜ The Strongest Immortal Chen #': ' S4 EP115-116',
            '【武道大帝】第62集：破阵 ｜ The Great Emperor of Martial Arts #热血 #修仙 #玄幻 #动态漫画': ' EP62',
            '【气运之子：我可以无限暴击】第60集：领域之力，地火炎柱 ｜ Everything can be Critically Attacked #热血 #玄幻': ' EP60',
            '【沉睡万古：出世横推诸天】第74集：仙王曾经是我养的狗！｜ Sleeping for ages #热血 #重生 #修仙': ' EP74',
            '【炼体十万层：都市篇】第163话：实力碾压 ｜ One Hundred Thousand Layers of Body Refining #热血 #修仙 #都市': ' EP163',
            '【炼气练了三千年 第四季】第117集：战力最强的帝级机傀   Practicing Qi for 3,000 Years #热血 #玄幻 #冒险': ' S4 EP117',
            '【百炼成神】第113集：罪恶十层，再见云落 ｜ All things become gods #热血 #玄幻 #修仙 #动态漫画 #七号动漫馆': ' EP113',
            '【绝世战魂】第338集：威胁仙灵，分别之际 ｜ Peerless Martial Spirit #热血 #玄幻 #修仙 #逆袭 #动态漫画': ' EP338',
            '【邪神降世，我有一座大凶狱】第15集：千年老王八竟当场卖萌！｜ Warden of the Gods #热血 #奇幻 #末日 #冒险': ' EP15',
            '【邪神降世，我有一座大凶狱】第24~25集：末日当前，“姐妹情深” ｜ Warden of the Gods #热血 #奇幻 #末日': ' EP24-25',
            '【都市圣手：我即医武巅峰】第57~58集：都是花架子 ｜ I am the Peak of Medical and Martial Arts #热血': ' EP57-58',
            '【都市至尊】第38集：见死不救 ｜ Lord of the Metropolis #热血 #修仙 #玄幻 #都市 #动态漫画': ' EP38',
            '【长生不死的我只修禁术】第44集：噬命之塔，毫无作用 ｜ #修仙 #动态漫画 #七号动漫馆': ' EP44',
            '一万年后我无敌了 第27集': ' EP27',
            '一世成仙 第57集': ' EP57',
            '一切从我成为炉鼎开始 第14集': ' EP14',
            '一力破诸天万界 动态漫画 第29集': ' EP29',
            '一力破诸天万界 动态漫画第一季 第28集': ' EP28',
            '一念逍遥 动态漫画第一季 第1集': ' EP1',
            '万古神帝 动态漫画 第28集': ' EP28',
            '万古神帝 第30集': ' EP30',
            '万古第一神 动态漫画 第83集': ' EP83',
            '万古第一神 动态漫画第一季 第84集': ' EP84',
            '万古第一神 第80集 #七号动漫馆': ' EP80',
            '万界主宰008': ' EP8',
            '万界主宰11': ' EP11',
            '九位师娘，叫我别怂 第20集': ' EP20',
            '仙为奴神为仆，大帝看门狗 第23集 兴师问罪日升国 #七号动漫馆': ' EP23',
            '仙帝归来 动态漫画第三季 第101集': ' S3 EP101',
            '仙帝归来第3季100：不凡之处': ' S3 EP100',
            '仙帝归来第3季102：招蜂引蝶 #七号动漫馆': ' S3 EP102',
            '仙帝归来第三季103：以卵击石 #七号动漫馆': ' S3 EP103',
            '仙帝狂婿 第40集': ' EP40',
            '仙帝狂婿 第一季 第41集': ' EP41',
            '修仙从长生开始 第100集': ' EP100',
            '修仙从长生开始 第96集': ' EP96',
            '修仙氪金王 动态漫画  第一季 第70集': ' EP70',
            '修真百万年：我的弟子遍布仙界 动态漫画 第12集': ' EP12',
            '修真百万年：我的弟子遍布仙界 第13集': ' EP13',
            '全民末日：我！病毒君王 动态漫画第一季 第1集': ' EP1',
            '全民神祗：我献祭亿万生灵成神 动态漫画 第32集': ' EP32',
            '全民神祗：我献祭亿万生灵成神 第30集 小镇？僵尸？植物？这里是……- #七号动漫馆': ' EP30',
            '全民神祗：我献祭亿万生灵成神 第31集': ' EP31',
            '全民转职：我的技能全是禁咒 第56集': ' EP56',
            '全民转职：驭龙师是最弱职业 动态漫画 第2集': ' EP2',
            '全民转职：驭龙师是最弱职业？ 动态漫画第一季 第1集': ' EP1',
            '全球惊悚：我开启外挂自选商城 第1集': ' EP1',
            '全球诡异时代  第二季 第89集': ' S2 EP89',
            '全球诡异时代第二季 第88集': ' S2 EP88',
            '再不死我就真无敌了 动态漫画  第一季 第28集': ' EP28',
            '再不死我就真无敌了 动态漫画第一季 第27集': ' EP27',
            '剑仙武帝  第二季·动态漫画 第43集': ' S2 EP43',
            '剑起风云 第44集': ' EP44',
            '剑道第一仙 第67集 蓝光 #神话动漫社': ' EP67',
            '卑微系统，跪请我无敌 第6集': ' EP6',
            '原来我是魔道老祖？·动态漫画 第46集': ' EP46',
            '古武高手在都市 动态漫画第四季 第54集': ' S4 EP54',
            '只有我能用召唤术 第20集': ' EP20',
            '地球人实在太凶猛了 动态漫画第一季 第82集': ' EP82',
            '地球人实在太凶猛了 第78集': ' EP78',
            '地球人实在太凶猛了·动态漫画 第80集': ' EP80',
            '大奉打更人 第54集': ' EP54',
            '大奉打更人·动态漫画 第56集': ' EP56',
            '大奉打更人第一季 第60集': ' EP60',
            '大道朝天7': ' EP7',
            '天渊归来：我即是天灾 动态漫画 第54集': ' EP54',
            '天渊归来：我即是天灾 动态漫画第一季 第53集': ' EP53',
            '完蛋，我被美女武神绑定了 动态漫画第一季 第40集': ' EP40',
            '完蛋，我被美女武神绑定了 第39集': ' EP39',
            '开局十个大帝都是我徒弟 动态漫画第四季 第13集': ' S4 EP13',
            '开局就无敌  第二季 第64集': ' S2 EP64',
            '开局就无敌第二季 第65集': ' S2 EP65',
            '开局有剑域，我能苟成剑神 第106集 #七号动漫馆': ' EP106',
            '开局签到至尊丹田 第150集 以掌对掌，班门弄斧': ' EP150',
            '开局签到至尊丹田 第152集 大世之争，拉开序幕 #七号动漫馆': ' EP152',
            '开局签到荒古圣体 动态漫画 第6集': ' EP6',
            '开局签到荒古圣体 动态漫画第一季 第8集': ' EP8',
            '开局签到荒古圣体 第7集': ' EP7',
            '弟子修炼，我躺平！ 动态漫画第二季 第15集': ' S2 EP15',
            '徒弟升级 我躺着就变强 第32集': ' EP32',
            '我不可能是剑神 第108集': ' EP108',
            '我不可能是剑神·动态漫 第110集': ' EP110',
            '我为邪帝 动态漫  第二季 第54集': ' S2 EP54',
            '我为邪帝 动态漫画第二季 第53集': ' S2 EP53',
            '我为邪帝第二季 第55集': ' S2 EP55',
            '我只想安静地打游戏 第85集': ' EP85',
            '我召唤出了诸天神魔 动态漫画第一季 第35集': ' EP35',
            '我可以修改万物时间线 动态漫画 第一季 第77集': ' EP77',
            '我可以修改万物时间线 第80集': ' EP80',
            '我在修仙世界朝九晚五第84-85集 #七号动漫馆': ' EP84-85',
            '我在末日玄幻世界无敌了 动态漫画 第28集': ' EP28',
            '我在末日玄幻世界无敌了 第29集': ' EP29',
            '我天命大反派第二季 第35集': ' S2 EP35',
            '我契约了我自己 动态漫画第一季 第33集': ' EP33',
            '我契约了我自己 第32集': ' EP32',
            '我家娘子竟然是女帝 9': ' EP9',
            '我家娘子竟然是女帝 第10集 #七号动漫馆': ' EP10',
            '我有999种异能 动态漫画第二季 第6集': ' S2 EP6',
            '我有百万倍攻速 第84集 #七号动漫馆': ' EP84',
            '我独自崛起  第四季 第23集': ' S4 EP23',
            '我独自崛起第四季 第26集': ' S4 EP26',
            '我独自氪金升级 动态漫画 第28集': ' EP28',
            '我独自氪金升级 第27集': ' EP27',
            '我的妻子是大乘期大佬 第70集 萧逸枫的修为被质疑': ' EP70',
            '我的妻子是大乘期大佬 第73集': ' EP73',
            '我的妻子是大乘期大佬72 #七号动漫馆': ' EP72',
            '我的师父不过是个大罗金仙 动态漫画 第32集': ' EP32',
            '我的师父不过是个大罗金仙 第29集': ' EP29',
            '我的弟子遍布诸天万界  第四季 第3集': ' S4 EP3',
            '我的弟子遍布诸天万界 第136集 天元宝鼎，半帝神器 #七号动漫馆': ' EP136',
            '我的弟子遍布诸天万界【Eng Sub】《My Discipes are All Over the World》第142集：四大金刚，随手压制': ' EP142',
            '我的弟子都超神 动态漫画第二季 第67集': ' S2 EP67',
            '我的徒弟都是大反派·动态漫  第二季 第20集': ' S2 EP20',
            '我的无敌反套路 第28集': ' EP28',
            '我神魔双修：制霸当世 第48集 #七号动漫馆': ' EP48',
            '我被困在同一天一千年 第44集': ' EP44',
            '我被困在同一天十万年  第四季 第52集': ' S4 EP52',
            '我被困在同一天十万年第四季 第53集': ' S4 EP53',
            '我说苟，系统说狗带 动态漫画第一季 第11集': ' EP11',
            '我说苟，系统说狗带 第10集': ' EP10',
            '我靠打赏徒弟升级 第80集': ' EP80',
            '我靠捡垃圾上王者 第14集': ' EP14',
            '我，剑道无敌 动态漫画 第70集': ' EP70',
            '我，剑道无敌 第67集': ' EP67',
            '我，最强BOSS 第26集': ' EP26',
            '战神联盟32': ' EP32',
            '拿来吧你！反派的我掠夺诸天万界 第12集': ' EP12',
            '掌门低调点 动态漫画  第三季 第12集': ' S3 EP12',
            '掌门低调点 动态漫画第三季 第9集': ' S3 EP9',
            '无上神帝 第432集 蓝光 #神话动漫社': ' EP432',
            '最强反套路系统 动态漫画  第二季 第38集': ' S2 EP38',
            '最强反套路系统 动态漫画第二季 第39集': ' S2 EP39',
            '最强反套路系统（第2季）第37集 从未见过如此愤怒的系统 #七号动漫馆': ' S2 EP37',
            '末世盗贼行 动态漫画 第29集': ' EP29',
            '末世神级升级系统 动态漫画  第一季 第37集': ' EP37',
            '末世神级升级系统 动态漫画第一季 第35集': ' EP35',
            '正义的我被系统逼成了大反派 第29集': ' EP29',
            '武灵剑尊 第14集': ' EP14',
            '武炼巅峰 动态漫画  第二季 第13集': ' S2 EP13',
            '武炼巅峰 动态漫画第二季 第16集': ' S2 EP16',
            '武神主宰 第493集 蓝光 #神话动漫社': ' EP493',
            '武道大帝 第65集 炼神境 #七号动漫馆': ' EP65',
            '毒手巫医 动态漫画 第85集': ' EP85',
            '氪丹修仙只苟长生 动态漫画第一季 第28集': ' EP28',
            '沉睡万古：出世横推诸天 第72集 做不凡之事！ #七号动漫馆': ' EP72',
            '深渊之种 动态漫画第一季 第31集': ' EP31',
            '深渊之种 第29集': ' EP29',
            '混沌天帝诀 动态漫画第一季 第59集': ' EP59',
            '灵剑尊 第540集 蓝光 #神话动漫社': ' EP540',
            '炼气练了三千年 第4季 第119集：你们这群破铜烂铁，吔拳啦！ #七号动漫馆': ' S4 EP119',
            '炼气练了三千年｜ I AM Legend S4E88-89一起创世吧！(Original)Anime动态漫': ' S4 EP88-89',
            '牧龙师 第3集': ' EP3',
            '独步万古112': ' EP112',
            '独步逍遥 第468集 蓝光 #神话动漫社': ' EP468',
            '疯狂升级系统 动态漫画第一季 第20集': ' EP20',
            '百炼成神 第112集 刺杀之族，袭杀罗征 #七号动漫馆': ' EP112',
            '盖世扫地僧：我可以无限融合 94': ' EP94',
            '真武巅峰190': ' EP190',
            '神印王座 [132]': ' EP132',
            '神天至尊 动态漫画第一季 第39集': ' EP39',
            '神武天尊 第241集': ' EP241',
            '稳住别浪 第122~123集 #七号动漫馆': ' EP122-123',
            '突然成仙了怎么办 动态漫画第一季 第91集': ' EP91',
            '突然成仙了怎么办 第93集': ' EP93',
            '绝世战魂 动态漫画 第335集 万字铜墙，天仙之衣 #七号动漫馆': ' EP335',
            '绝世战魂 第333集 仇敌夹击，团结迎战 #七号动漫馆': ' EP333',
            '绝世战魂动态漫 第332集': ' EP332',
            '绝世武神 第七季 peerless martial god Season7 54第五十四集 自求多福#第七季': ' S7 EP54',
            '绝世武神第七季 第53集': ' S7 EP53',
            '绝世武魂 第428集 蓝光 #神话动漫社': ' EP428',
            '绝战魂 第426集 蓝光 #神话动漫社': ' EP426',
            '网游之天下无双 第37集': ' EP37',
            '荒天至尊 动态漫画 第18集': ' EP18',
            '荒天至尊 第19集': ' EP19',
            '超凡进化 动态漫画 第29集': ' EP29',
            '超凡进化 第31集': ' EP31',
            '逆天至尊 第353集 蓝光 #神话动漫社': ' EP353',
            '遮天 [81]': ' EP81',
            '邪神降世，我有一座大凶狱  第26-27集 #七号动漫馆': ' EP26-27',
            '邪神降世，我有一座大凶狱 第22-23集 #七号动漫馆': ' EP22-23',
            '邪神降世，我有一座大凶狱 第28集': ' EP28',
            '都市仙帝：龙王殿 第26集': ' EP26',
            '都市仙帝：龙王殿 第27集 #七号动漫馆': ' EP27',
            '都市最强仙尊动态漫第二季 第12集': ' S2 EP12',
            '都市最强仙尊第二季 第35集': ' S2 EP35',
            '都市最强仙尊第二季第11集': ' S2 EP11',
            '都市极品医神 第3集': ' EP3',
            '都市至尊 动态漫画 第41集': ' EP41',
            '都市至尊 动态漫画第一季 第39集': ' EP39',
            '重生之神级败家子 动态漫画 第7集': ' EP7',
            '重生之神级败家子 动态漫画第一季 第9集': ' EP9',
            '重生之神级败家子 第8集': ' EP8',
            '重生八万年 动态漫画第二季 第50集': ' S2 EP50',
            '重生八万年第二季 第52集': ' S2 EP52',
            '镇国神婿第二季 第88集': ' S2 EP88',
            '顶级气运，悄悄修练千年 动态漫画第一季 第37集': ' EP37',
            '高武：登陆未来一万年 动态漫画 第24集': ' EP24',
            "都市至尊 动态漫画第一季": " EP1",
            "都市至尊 动态漫画": "都市至尊 动态漫画",
            "都市至尊 S3 EP2-4 EP30": " S3 EP2-4",
            "都市至尊 S3 EP30 EP2-4": " S3 EP2-4",
            " 第七季 peerless 第四十八集": " S7 EP48",
            # "": "",
        }
        for i, (name, result) in enumerate(test_vals.items()):
            with self.subTest(i=i):
                gen = ChineseTitleGenerator()
                name = gen.generate_title(name, "")
                self.assertEqual(name, result)
