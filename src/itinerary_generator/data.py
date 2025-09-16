"""Static destination profiles used by the itinerary generator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass(frozen=True)
class Activity:
    """Represents an activity suggestion for a period of the day."""

    title: str
    description: str
    image_url: str


@dataclass(frozen=True)
class Highlight:
    """Represents a recommendation card (food, souvenir or experience)."""

    title: str
    description: str
    image_url: str


@dataclass(frozen=True)
class DestinationProfile:
    """Static data describing a travel destination."""

    key: str
    display_name: str
    country: str
    cover_image: str
    tagline: str
    ideal_daily_cost: int
    min_days: int
    max_days: int
    daily_themes: List[str]
    morning_options: List[Activity]
    afternoon_options: List[Activity]
    evening_options: List[Activity]
    accommodation_tips: List[str]
    transport_tips: List[str]
    foods: List[Highlight]
    souvenirs: List[Highlight]
    experiences: List[Highlight]
    extra_tips: List[str] = field(default_factory=list)
    aliases: List[str] = field(default_factory=list)

    def all_aliases(self) -> Iterable[str]:
        for value in self.aliases:
            yield value
        yield self.key
        yield self.display_name


DESTINATIONS: dict[str, DestinationProfile] = {
    "tokyo": DestinationProfile(
        key="tokyo",
        display_name="日本东京",
        country="日本",
        cover_image="https://images.unsplash.com/photo-1549692520-acc6669e2f0c?auto=format&fit=crop&w=1500&q=80",
        tagline="霓虹灯下的潮流都市，传统与现代交织的沉浸式体验",
        ideal_daily_cost=1200,
        min_days=4,
        max_days=7,
        daily_themes=[
            "抵达东京 · 漫游浅草与隅田川",
            "潮流圣地秋叶原与原宿",
            "箱根温泉与富士山远眺",
            "迪士尼奇幻冒险",
            "自由行购物与文化巡礼",
            "日式职人体验",
            "都市美食收官夜",
        ],
        morning_options=[
            Activity(
                title="浅草寺祈福",
                description="穿过雷门参拜浅草寺，感受东京最古老寺庙的静谧与香火。",
                image_url="https://images.unsplash.com/photo-1503891450247-ee5f8ec46dc3?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="筑地市场早餐",
                description="在筑地市场品尝刚捕捞的海鲜，体验东京最具人气的寿司早餐。",
                image_url="https://images.unsplash.com/photo-1543353071-10c8ba85a904?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="皇居外苑晨跑",
                description="围绕皇居外苑慢跑或漫步，感受都市绿洲的悠闲与庄严。",
                image_url="https://images.unsplash.com/photo-1478720568477-152d9b164e26?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="明治神宫参拜",
                description="走进茂密森林环绕的明治神宫，体验静谧庄严的日本神道文化。",
                image_url="https://images.unsplash.com/photo-1561966313-6e756b0f9a15?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="台场海滨漫步",
                description="在台场海滨公园欣赏东京湾与彩虹大桥，开启活力满满的一天。",
                image_url="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        afternoon_options=[
            Activity(
                title="秋叶原动漫科技之旅",
                description="探索秋叶原的动漫、游戏与电子产品，感受二次元文化。",
                image_url="https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="上野文化艺术巡礼",
                description="参观东京国立博物馆或上野动物园，漫步上野公园。",
                image_url="https://images.unsplash.com/photo-1554797589-7241bb691973?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="箱根温泉半日游",
                description="乘坐浪漫特快前往箱根，欣赏富士山并体验露天温泉。",
                image_url="https://images.unsplash.com/photo-1544552866-0d4bb1d063c1?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="迪士尼海洋奇幻体验",
                description="畅玩东京迪士尼海洋主题乐园，沉浸式感受梦幻世界。",
                image_url="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="涩谷与原宿潮流漫步",
                description="打卡涩谷十字路口，探访原宿表参道的潮流品牌与设计店。",
                image_url="https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        evening_options=[
            Activity(
                title="银座米其林晚宴",
                description="预订米其林餐厅享用正宗怀石料理，品味东京顶级美食。",
                image_url="https://images.unsplash.com/photo-1432139555190-58524dae6a55?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="六本木夜景酒廊",
                description="登上六本木之丘，俯瞰东京璀璨夜景，享用创意鸡尾酒。",
                image_url="https://images.unsplash.com/photo-1470290378698-263fa7ca9729?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="新宿歌舞伎町夜生活",
                description="体验新宿歌舞伎町的夜生活，感受热闹不夜城的魅力。",
                image_url="https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="温泉旅馆怀石晚宴",
                description="入住温泉旅馆，享用多道式怀石料理，沉浸日式待客之道。",
                image_url="https://images.unsplash.com/photo-1542456429-5b047d333609?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="隅田川夜游",
                description="搭乘游船沿隅田川巡航，欣赏东京塔与天空树夜景。",
                image_url="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        accommodation_tips=[
            "推荐入住新宿或银座四星级酒店，方便交通与购物。",
            "若前往箱根，可选择带露天风吕的温泉旅馆。",
            "亲子家庭建议入住迪士尼合作酒店，享受专属接驳服务。",
        ],
        transport_tips=[
            "提前购买Suica交通卡，可在地铁与便利店通用。",
            "东京市区推荐搭乘JR山手线与地铁，节省时间。",
            "前往近郊可使用JR Pass或浪漫特快，需提前预约。",
        ],
        foods=[
            Highlight(
                title="筑地寿司大",
                description="品尝人气寿司店，以新鲜肥美的海产闻名。",
                image_url="https://images.unsplash.com/photo-1543353071-873f17a7a088?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="一兰拉面",
                description="随心调配口味的个性化拉面体验，适合夜宵。",
                image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="表参道甜品之旅",
                description="探访人气甜品店，感受东京的精致甜点文化。",
                image_url="https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        souvenirs=[
            Highlight(
                title="东京Banana",
                description="经典伴手礼，香蕉口味蛋糕柔软香甜。",
                image_url="https://images.unsplash.com/photo-1506617420156-8e4536971650?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="清酒与手工酒器",
                description="选购小众酒藏清酒搭配手作酒器，赠礼体面。",
                image_url="https://images.unsplash.com/photo-1527169402691-feff5539e52c?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="和风生活杂货",
                description="青山与代官山设计店的器皿、香氛与文创礼品。",
                image_url="https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        experiences=[
            Highlight(
                title="和服摄影体验",
                description="换上华丽和服，在浅草或京都风格街巷拍摄写真。",
                image_url="https://images.unsplash.com/photo-1542038784456-1ea8e935640e?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="寿司职人课堂",
                description="跟随寿司大师学习制作手握寿司，收获独特纪念。",
                image_url="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="富士山一日游",
                description="包车前往河口湖，欣赏富士山倒影与传统村落。",
                image_url="https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        extra_tips=[
            "建议提前预约热门餐厅和体验项目，避免现场排队。",
            "出行季节为春秋最佳，可观赏樱花或红叶。",
        ],
        aliases=["东京", "日本东京", "tokyo", "tokyo japan", "東京"],
    ),
    "dali": DestinationProfile(
        key="dali",
        display_name="云南大理",
        country="中国",
        cover_image="https://images.unsplash.com/photo-1580121441575-41bcb5d984de?auto=format&fit=crop&w=1500&q=80",
        tagline="风花雪月下的洱海之畔，邂逅慢节奏的民族风情",
        ideal_daily_cost=600,
        min_days=3,
        max_days=6,
        daily_themes=[
            "抵达大理 · 古城初见",
            "洱海东岸骑行",
            "苍山徒步与民俗体验",
            "喜洲古镇与非遗课堂",
            "双廊日落与海景下午茶",
            "大理深度慢生活",
        ],
        morning_options=[
            Activity(
                title="大理古城晨光",
                description="漫步五华楼与城墙，体验古城清晨的宁静。",
                image_url="https://images.unsplash.com/photo-1570168007204-e9df21d7571f?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="洱海东岸骑行",
                description="沿环海东路骑行或乘坐敞篷车，感受海天一色。",
                image_url="https://images.unsplash.com/photo-1591160690555-5ef8864f6132?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="苍山索道观景",
                description="乘坐索道直达苍山，俯瞰洱海全景与云海。",
                image_url="https://images.unsplash.com/photo-1602491453631-548a1a031c39?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="喜洲粑粑课堂",
                description="拜访白族人家，学习制作地道喜洲粑粑。",
                image_url="https://images.unsplash.com/photo-1505935428862-770b6f24f629?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        afternoon_options=[
            Activity(
                title="南诏风情岛",
                description="乘船前往南诏风情岛，欣赏洱海碧波与白族歌舞。",
                image_url="https://images.unsplash.com/photo-1580121433060-d61794630783?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="罗荃半岛摄影",
                description="拍摄洱海最美光影，在观景平台享用下午茶。",
                image_url="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="白族扎染体验",
                description="跟随老师傅体验传统扎染与手工艺，亲手制作纪念。",
                image_url="https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="双廊艺术聚落",
                description="探访双廊艺术小店与海景民宿，品味慢时光。",
                image_url="https://images.unsplash.com/photo-1526481280695-3c4691d80534?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        evening_options=[
            Activity(
                title="海景火锅",
                description="在洱海边享用新鲜食材的暖心火锅，看星辰倒影。",
                image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="古城酒吧驻唱",
                description="聆听民谣驻唱，在古城夜色中小酌放松。",
                image_url="https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="星空露营",
                description="在洱海畔搭建轻奢帐篷，享受星空与篝火。",
                image_url="https://images.unsplash.com/photo-1508261305432-e2efc997b27a?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="白族三道茶表演",
                description="品味苦、甘、回味的三道茶，了解白族礼仪。",
                image_url="https://images.unsplash.com/photo-1571689936114-d1d914c76be0?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        accommodation_tips=[
            "推荐入住双廊或海东海景度假酒店，享受一线湖景。",
            "古城内精选精品客栈，体验白族庭院与木雕风格。",
            "想要安静，可选择海舌公园附近的隐世民宿。",
        ],
        transport_tips=[
            "大理市区与古城之间提供旅游巴士，也可预约私家车。",
            "洱海环湖建议租赁电动车或敞篷车，沿途方便拍照。",
            "如需前往丽江或香格里拉，可安排包车或高铁衔接。",
        ],
        foods=[
            Highlight(
                title="砂锅鱼",
                description="选用洱海鲜鱼炖煮，汤鲜味美，暖胃滋补。",
                image_url="https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="乳扇卷",
                description="大理特有的乳扇搭配玫瑰花酱，香甜软糯。",
                image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="喜洲粑粑",
                description="现烤饼皮夹玫瑰糖或火腿，外酥内软。",
                image_url="https://images.unsplash.com/photo-1473093226795-af9932fe5856?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        souvenirs=[
            Highlight(
                title="白族扎染",
                description="以天然植物染色的布艺，色彩独特且环保。",
                image_url="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="银饰手作",
                description="白族匠人打造的精美银饰，寓意吉祥。",
                image_url="https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="云南普洱茶",
                description="精选老树普洱，茶香悠长，可收藏增值。",
                image_url="https://images.unsplash.com/photo-1459755486867-b55449bb39ff?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        experiences=[
            Highlight(
                title="洱海游艇包船",
                description="私人包船环湖，拍摄网红大片，享受定制茶歇。",
                image_url="https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="白族婚礼体验",
                description="换上民族服饰，体验白族独特的迎亲仪式。",
                image_url="https://images.unsplash.com/photo-1530789253388-582c481c54b0?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="苍山秘境徒步",
                description="专业向导带领探访原始森林与溪谷瀑布。",
                image_url="https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        extra_tips=[
            "洱海沿线阳光强烈，务必准备防晒与保湿用品。",
            "建议行程安排在每年3-5月或9-11月，气候舒适宜人。",
        ],
        aliases=["大理", "云南大理", "dali", "dali china"],
    ),
    "paris": DestinationProfile(
        key="paris",
        display_name="法国巴黎",
        country="法国",
        cover_image="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1500&q=80",
        tagline="浪漫之都的艺术与时尚，沿着塞纳河漫步的法式度假",
        ideal_daily_cost=1500,
        min_days=4,
        max_days=7,
        daily_themes=[
            "初识巴黎 · 塞纳河与铁塔",
            "卢浮宫与左岸文艺",
            "凡尔赛宫廷一日",
            "香榭丽舍与时尚精品",
            "蒙马特高地艺术巡礼",
            "香槟区庄园体验",
            "巴黎味蕾终章",
        ],
        morning_options=[
            Activity(
                title="卢浮宫艺术晨游",
                description="避开人潮欣赏《蒙娜丽莎》《胜利女神》等经典藏品。",
                image_url="https://images.unsplash.com/photo-1529429617124-aee711a368b8?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="塞纳河畔晨间漫步",
                description="沿着塞纳河散步，邂逅巴黎圣母院与旧书摊。",
                image_url="https://images.unsplash.com/photo-1508057198894-247b23fe5ade?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="蒙马特艺术人文",
                description="登上圣心大教堂俯瞰巴黎，全景尽收眼底。",
                image_url="https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="凡尔赛花园晨光",
                description="清晨进入凡尔赛宫，穿梭镜厅与法式园林。",
                image_url="https://images.unsplash.com/photo-1529429617124-aee711a368b8?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        afternoon_options=[
            Activity(
                title="香榭丽舍大道购物",
                description="汇集奢侈品牌与法式精品，是巴黎购物的标志街区。",
                image_url="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="奥赛博物馆",
                description="欣赏印象派大师莫奈、梵高与雷诺阿的传世之作。",
                image_url="https://images.unsplash.com/photo-1491557345352-5929e343eb89?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="香槟区庄园品鉴",
                description="乘车前往兰斯或埃佩尔奈，探访香槟酒窖并品鉴。",
                image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="塞纳河游船",
                description="乘坐豪华游船，欣赏两岸经典建筑与桥梁。",
                image_url="https://images.unsplash.com/photo-1529429617124-aee711a368b8?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        evening_options=[
            Activity(
                title="埃菲尔铁塔星光夜宴",
                description="预约铁塔内Le Jules Verne餐厅，俯瞰巴黎夜景。",
                image_url="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="红磨坊歌舞秀",
                description="欣赏经典康康舞，体验百年歌舞厅的热情。",
                image_url="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="米其林星级法餐",
                description="在塞纳河左岸品尝主厨创意菜单，享受法式服务。",
                image_url="https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=800&q=80",
            ),
            Activity(
                title="塞纳河夜游",
                description="夜间游船搭配香槟，欣赏灯火辉煌的巴黎。",
                image_url="https://images.unsplash.com/photo-1499028344343-cd173ffc68a9?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        accommodation_tips=[
            "推荐入住凯旋门或塞纳河畔五星级酒店，方便游览主景点。",
            "浪漫情侣可选择左岸精品酒店，氛围静谧。",
            "亲子家庭建议预订迪士尼周边度假酒店，配套齐全。",
        ],
        transport_tips=[
            "巴黎地铁网络发达，建议购买周票Navigo更实惠。",
            "机场往返可安排专车接送或搭乘RER B线火车。",
            "城际游览如前往香槟区，可安排包车或TGV高铁。",
        ],
        foods=[
            Highlight(
                title="Ladurée 马卡龙",
                description="品尝拥有百年历史的马卡龙，香甜细腻。",
                image_url="https://images.unsplash.com/photo-1521305916504-4a1121188589?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="Le Relais de l'Entrecôte",
                description="连锁牛排馆的秘制酱汁与无限续薯条，排队也值得。",
                image_url="https://images.unsplash.com/photo-1514516430032-7e68d63732a0?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="花神咖啡馆",
                description="左岸知名咖啡馆，感受文艺气息与法式早餐。",
                image_url="https://images.unsplash.com/photo-1447933601403-0c6688de566e?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        souvenirs=[
            Highlight(
                title="香水定制",
                description="在调香工坊亲自配制专属香水，留下独特记忆。",
                image_url="https://images.unsplash.com/photo-1524594081293-190a2fe0baae?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="法式手工巧克力",
                description="甄选Le Chocolat Alain Ducasse等品牌的精品巧克力。",
                image_url="https://images.unsplash.com/photo-1519869325930-281384150729?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="巴黎时尚精品",
                description="挑选巴黎设计师品牌的围巾、皮具或饰品。",
                image_url="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        experiences=[
            Highlight(
                title="塞纳河私人游船",
                description="定制私人游船派对，配备香槟与专业摄影。",
                image_url="https://images.unsplash.com/photo-1543342386-6c281e1f93a0?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="巴黎烹饪课堂",
                description="跟随法餐主厨学习制作马卡龙或法式大餐。",
                image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
            ),
            Highlight(
                title="卢浮宫私人导览",
                description="专业中文讲解员带领，深度解析艺术史。",
                image_url="https://images.unsplash.com/photo-1529429617124-aee711a368b8?auto=format&fit=crop&w=800&q=80",
            ),
        ],
        extra_tips=[
            "热门景点如卢浮宫、铁塔需提前在线预约时段。",
            "春秋气候宜人，也是巴黎时装与艺术活动集中季节。",
        ],
        aliases=["巴黎", "法国巴黎", "paris", "paris france"],
    ),
}

GENERIC_PROFILE = DestinationProfile(
    key="generic",
    display_name="梦想之旅",
    country="",
    cover_image="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1500&q=80",
    tagline="量身定制的专属旅行，探索世界的每一处精彩",
    ideal_daily_cost=800,
    min_days=3,
    max_days=7,
    daily_themes=[
        "抵达与城市初体验",
        "经典地标与当地文化",
        "户外探索与特色活动",
        "美食与市集",
        "自由行程与休闲时光",
        "主题体验",
        "收官之夜",
    ],
    morning_options=[
        Activity(
            title="城市迎宾步行",
            description="在导游带领下认识城市的地标建筑与故事。",
            image_url="https://images.unsplash.com/photo-1431540015161-0bf868a2d407?auto=format&fit=crop&w=800&q=80",
        ),
        Activity(
            title="当地市场探访",
            description="走进传统市集，与摊主互动并品尝特色小吃。",
            image_url="https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=800&q=80",
        ),
        Activity(
            title="自然风光晨游",
            description="前往城市周边的公园或海滨，感受大自然。",
            image_url="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        ),
    ],
    afternoon_options=[
        Activity(
            title="文化体验工作坊",
            description="参与手工艺或烹饪课堂，深入了解当地文化。",
            image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
        ),
        Activity(
            title="主题博物馆参观",
            description="选择一座具有代表性的博物馆或艺术馆。",
            image_url="https://images.unsplash.com/photo-1529429617124-aee711a368b8?auto=format&fit=crop&w=800&q=80",
        ),
        Activity(
            title="周边风景小众游",
            description="安排半日近郊游，体验自然与人文的融合。",
            image_url="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80",
        ),
    ],
    evening_options=[
        Activity(
            title="地道餐厅品鉴",
            description="在特色餐厅体验当地代表菜肴，搭配当地饮品。",
            image_url="https://images.unsplash.com/photo-1473093226795-af9932fe5856?auto=format&fit=crop&w=800&q=80",
        ),
        Activity(
            title="夜景与灯光秀",
            description="登高或乘船欣赏城市夜景，捕捉璀璨瞬间。",
            image_url="https://images.unsplash.com/photo-1499028344343-cd173ffc68a9?auto=format&fit=crop&w=800&q=80",
        ),
        Activity(
            title="音乐与表演",
            description="欣赏当地剧院、爵士吧或特色演出。",
            image_url="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80",
        ),
    ],
    accommodation_tips=[
        "精选市中心四星级酒店，兼顾舒适与便利。",
        "若偏好度假氛围，可选择度假村或精品民宿。",
        "团队出游可安排公寓式酒店，提升社交体验。",
    ],
    transport_tips=[
        "提供机场接送服务，行程无缝衔接。",
        "推荐购买城市交通卡，公交地铁无限次使用。",
        "可按需升级为专车司机与当地向导服务。",
    ],
    foods=[
        Highlight(
            title="必吃地标餐厅",
            description="预约口碑餐厅，体验当地最具代表性的味道。",
            image_url="https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=800&q=80",
        ),
        Highlight(
            title="夜市与街头小吃",
            description="感受地道烟火气，品尝平价又美味的特色小吃。",
            image_url="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80",
        ),
        Highlight(
            title="星级甜品下午茶",
            description="在网红咖啡厅享受精致甜品和轻松氛围。",
            image_url="https://images.unsplash.com/photo-1521305916504-4a1121188589?auto=format&fit=crop&w=800&q=80",
        ),
    ],
    souvenirs=[
        Highlight(
            title="城市主题纪念品",
            description="挑选独特纪念物，记录旅行故事。",
            image_url="https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=800&q=80",
        ),
        Highlight(
            title="手工艺品",
            description="支持当地匠人的手作艺品，兼具美感与意义。",
            image_url="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80",
        ),
        Highlight(
            title="特色食材礼盒",
            description="把旅行中的美味带回家，与亲友共享。",
            image_url="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&w=800&q=80",
        ),
    ],
    experiences=[
        Highlight(
            title="私人向导深度游",
            description="由专业向导量身定制路线，深入当地生活。",
            image_url="https://images.unsplash.com/photo-1473625247510-8ceb1760943f?auto=format&fit=crop&w=800&q=80",
        ),
        Highlight(
            title="主题派对或庆典",
            description="根据团队需求安排生日、纪念日或团建活动。",
            image_url="https://images.unsplash.com/photo-1525182008055-f88b95ff7980?auto=format&fit=crop&w=800&q=80",
        ),
        Highlight(
            title="摄影师随行记录",
            description="专业摄影师捕捉行程精彩瞬间，输出成片。",
            image_url="https://images.unsplash.com/photo-1444065381814-865dc9da92c0?auto=format&fit=crop&w=800&q=80",
        ),
    ],
    extra_tips=[
        "可根据季节与特殊需求（亲子、蜜月、商务）进行再定制。",
        "若需提供签证与机票服务，可一站式协助。",
    ],
    aliases=["定制旅行", "旅行", "tour", "holiday"],
)
