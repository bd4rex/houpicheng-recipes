"""Build public title/link records and an explicitly provisional dish index."""
import argparse, csv, json, re
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
GROUPS={
 '鸡鸭禽肉':'白切鸡 豉油鸡 盐焗鸡 电饭锅盐焗鸡 电饭锅焗鸡 隔水蒸鸡 桑拿鸡 沙姜鸡 沙姜焗鸡 沙姜炒鸡 姜葱炒鸡 冬菇蒸鸡 冬菇滑鸡 虫草花蒸鸡 荷叶蒸鸡 五指毛桃盐焗鸡 五指毛桃焗鸡 板栗焖鸡 啫啫鸡 滑鸡啫啫煲 鲍鱼焖鸡 鲍鱼鸡煲 鸡煲 鸡腿扒 煎鸡扒 照烧鸡腿 咖喱鸡 咖喱鸡扒 咖喱鸡腿 奶油蘑菇鸡腿扒 盐焗鸡翅 蒜香鸡翅 烤鸡翅 奥尔良烤翅 可乐鸡翅 沙茶酱鸡翅 蜜汁叉烧鸡翅 脆皮鸡翅 蒜香鸡腿肉 鸡胸肉炒豆角 鸡胸肉杂蔬丁 姜母鸭 陈皮鸭 胡椒鸭 焖鹅掌翼 鹅掌煲 手撕鸡 红葱头淋鸡 炸鸡柳',
 '猪肉':'红烧肉 可乐红烧肉 蒸排骨 豉汁蒸排骨 豉汁排骨焗南瓜 南瓜焖排骨 生炒排骨 椒盐排骨 盐焗排骨 水煎排骨 烤排骨 糖醋排骨 话梅菠萝排骨 白切猪肉 白切肉 水煎五花肉 水煎肉 香煎贵妃肉 洋葱猪扒 黑椒猪扒 苹果肉桂猪扒 脆皮猪扒 吉列猪扒 煎猪扒 盐焗猪扒 盐焗猪手 猪脚姜 猪肉饼 肉饼 蒸肉饼 马蹄蒸肉饼 榨菜蒸肉饼 淮山蒸肉饼 台式卤肉 叉烧',
 '牛羊肉':'广式牛腩 咖喱牛腩 番茄牛腩 萝卜牛腩 清汤腩 清炖牛肋条 卤牛肉 白切牛肉 凉拌牛肉 凉拌牛肋条 啫啫牛肉 番茄牛肉煲 黑椒牛肉 黑椒牛肉粒 黑椒牛柳 黑椒牛仔骨 黑椒牛排 孜然牛肉 紫苏雪花牛肉 菠萝牛肉 芒果牛肉 草菇炒牛肉 番茄炒牛肉 苦瓜炒牛肉 芥蓝牛肉 炒牛肉 香煎牛小排 煎牛排 煎牛肋条 牛肉饼 牛肉丸 瑞典肉丸 泉水牛肉 沙茶酱牛肉 牛肉火锅',
 '鱼虾海鲜':'烤青花鱼 烤三文鱼 烤三文鱼头 柠汁黄油三文鱼 黄油蒜香三文鱼 奶油三文鱼 椒盐三文鱼骨 盐水浸鱼 盐水煮鱼 盐焗鱼 豉汁蒸鱼 陈皮蒸鱼 清蒸鲷鱼 黄豆酱焖鱼 香煎龙利鱼 香煎巴浪鱼 香煎秋刀鱼 烤秋刀鱼 肉饼蒸鱼 豆豉鲮鱼 盐焗虾 盐水焗虾 白灼虾 芝士焗虾 蒜香黄油焗虾 蒜香黄油虾 蒜香虾仁 芥末虾球 葱香虾球 芝士虾球 柠檬虾 酸辣柠檬虾 百香果柠檬虾 咖喱虾 醉虾 虾仁炒丝瓜 芦笋虾仁 虾仁豆腐煲 蒜蓉虾滑煲 羊肚菌酿虾滑 紫菜虾滑煎饼 虾饼 紫菜虾滑 紫菜卷 咖喱鱼蛋 蒲烧鳗鱼 爆炒鱿鱼 炒鱿鱼 豉汁炒鱿鱼 豉油炒鲜鱿 芥末鱿鱼 白灼鱿鱼 清蒸生蚝 蒸鲍鱼 焖鲍鱼 盐焗海鲜 无水焗海鲜 花甲粉丝煲 扇贝粉丝煲 花腩鱿鱼啫啫煲 泰式海鲜沙拉',
 '蛋豆蔬菜':'蒸水蛋 滑蛋 溏心蛋 水波蛋 水煎蛋 炖蛋 芝士焗蛋 茄汁煎蛋 五柳炸蛋 北非蛋 蟹柳滑蛋 虾仁滑蛋 滑蛋牛肉 紫菜煎蛋 叉烧炒蛋 肉末蒸水蛋 肉末蒸蛋 白贝蒸水蛋 醪糟鸡蛋 茄汁黄豆 红烧豆腐 肉末豆腐 蒸嫩豆腐 蟹黄豆腐 金针菇豆腐煲 蒜蓉蒸丝瓜 蒜蓉炒丝瓜 蒜蓉粉丝娃娃菜 蚝油生菜 盐水菜心 上汤苋菜 椒丝腐乳空心菜 瑶柱冬菇焖节瓜 凉拌莴笋 凉拌毛豆 凉拌莲藕 凉拌包菜 酸辣包菜 手撕包菜 蒜香干辣椒炒包菜 蒜蓉淋汁青菜 肉末包菜 肉末土豆炒包菜 干煸菜花 干锅花菜 烤土豆 烤南瓜 烤玉米 烤杏鲍菇 黄油杏鲍菇 黄油炒杂蔬 黄油煎菌菇 焗西兰花 黑椒西兰花 酿辣椒 酿蘑菇 土豆泥沙拉 土豆鸡蛋沙拉 藜麦沙拉 油浸小番茄',
 '米饭面点':'煲仔饭 腊味煲仔饭 排骨煲仔饭 腊味饭 糙米饭 杂粮饭 藜麦饭 糯米饭 菌菇焖饭 三文鱼焖饭 鸡油饭 台式卤肉饭 洋葱肥牛饭 猪扒饭 鸡腿扒饭 咖喱鸡腿扒饭 咖喱牛腩饭 鳗鱼饭 杂扒饭 波奇饭 牛肉饭 牛肉饼饭 黑椒牛肉饭 黑椒牛扒饭 黑椒鸡腿饭 叉烧滑蛋饭 手撕鸡饭 鲍汁捞饭 黯然销魂饭 吞拿鱼拌饭 三文鱼拌饭 牛肉拌饭 肉末饭 藜麦拌饭 儿童拌饭 蔬菜拌饭 鸡腿扒拌饭 鸡蛋拌饭 紫菜包饭 寿司饭团 海苔拌饭 金包银炒饭 虾仁炒饭 咖喱炒饭 菠萝炒饭 牛肉菠萝炒饭 叉烧炒饭 三文鱼炒饭 蛋包饭 包菜炒饭 蟹黄炒饭 菜心牛肉炒饭 芝士焗饭 白汁焗饭 芝士牛肉焗饭 肉酱意面 奶油意面 白汁意面 白汁虾仁意面 虾仁意面 芝士三文鱼意面 芝士牛肉烤意面 蘑菇虾仁面 广式云吞面 云吞面 竹升面 车仔面 乌冬面 炒乌冬 餐蛋面 猪油捞面 虾籽捞面 沙茶牛肉面 牛肉河粉 牛腩面 牛腩粉 牛腩米粉 牛腩猪肠粉 牛腩啫啫肠粉 猪杂汤粉 潮汕牛肉粿条 炒牛河 炒米粉 炒河粉 煎饺 冰花煎饺 蒸饺 鱼皮饺 鱼肉烧卖 西多士 奶油猪 汉堡 猪柳蛋麦满分 牛肉汉堡 牛油果三明治 吞拿鱼三明治 金枪鱼三明治 牛肉三文治 牛角包三明治 虾滑三明治 菠萝牛肉三明治 花生酱三明治 芝士火腿蛋三明治 蟹柳滑蛋三明治 滑蛋贝果 牛肉芝士贝果 芝士牛肉吐司 烤芝士三明治 芝士牛肉卷 肠仔包 蔬菜饼 鸡蛋韭菜小饼 香蕉芝士春饼 爆浆芝士饼 麦片鸡蛋 微波炉麦片鸡蛋 鸡蛋煎粽 煎汤圆',
 '汤羹粥':'胡椒牛肉汤 牛肉汤 牛肉豆芽汤 牛肉汤羹 猪杂汤 猪红汤 咸蛋瘦肉汤 枸杞叶瘦肉猪肝汤 菜心瘦肉汤 滑肉汤 瘦肉水 苹果瘦肉水 羊肚菌瘦肉汤 苹果雪梨汤 无花果苹果瘦肉汤 橄榄瘦肉汤 橄榄石斛汤 太子参麦冬无花果瘦肉汤 无花果南北杏瘦肉汤 无花果川贝瘦肉汤 猪肚鸡 胡椒猪肚鸡 胡椒鸡 花胶鸡 花胶猪肚鸡 花旗参乌鸡汤 虫草花鸡汤 药膳鸡汤 土鸡汤 椰子鸡 排骨玉米香菇汤 香菇排骨汤 萝卜排骨汤 冬瓜薏米排骨汤 绿豆海带炖排骨 粉葛猪骨汤 五指毛桃猪骨汤 冬瓜薏米老鸭汤 花生眉豆鸡脚汤 粉葛鲮鱼汤 鱼骨豆腐汤 杂鱼汤 生蚝滚汤 鲮鱼滑西洋菜汤 西洋菜汤 裙带菜豆腐汤 裙带菜汤 花甲裙带菜汤 味噌汤 冬瓜海带汤 淮山肉饼鸡蛋汤 山药肉饼汤 哈佛蔬菜汤 罗宋汤 奶油蘑菇海鲜汤 白汁蘑菇汤 冬阴功汤 蟹黄豆腐羹 章鱼莲藕汤 沙虫炖汤 羊肚菌汤 皮蛋瘦肉粥 窝蛋牛肉粥 牛肉生菜粥 牛肉粥 猪杂粥 猪杂猪红粥 猪红粥 咸骨粥 烧骨粥 海鲜砂锅粥 海参粥 生滚粥 小米南瓜粥 麦片粥',
 '甜品饮品':'酸奶碗 抹茶酸奶碗 杨枝甘露 芒果西米露 椰汁西米露 西米露 陈皮红豆沙 红糖糯米莲藕 牛奶炖蛋 花胶炖牛奶 姜撞奶 蓝莓奶昔 牛油果奶昔 芒果奶昔 香蕉奶昔 火龙果香蕉奶昔 无糖莓果奶昔 冷冻莓果奶昔 奇亚籽牛奶 冷泡茶 手打百香果柠檬茶 玉米须茶 红豆薏仁水 赤小豆薏仁茶 罗汉果桂圆茶 抹茶拿铁 海盐苏打水',
 '调味与备餐':'蓝莓酱 苹果酱 肉桂苹果酱 番茄肉酱 姜葱酱 蒜蓉酱 蒜香酱 汉堡酱 广式牛腩酱料 凉拌汁 油浸番茄 虾滑'
}
ALIASES={
 '溏心蛋':['糖心蛋'], '虾仁滑蛋':['滑蛋虾仁'], '金包银炒饭':['金包银蛋炒饭'],
 '煲仔饭':['广式煲仔饭','广东煲仔饭','砂锅煲仔饭'], '广式牛腩':['港式牛腩'],
 '清汤腩':['港式清汤腩','粤式清汤腩'], '哈佛蔬菜汤':['哈弗蔬菜汤'],
 '吞拿鱼拌饭':['金枪鱼拌饭'], '牛肉三文治':['牛肉三明治'],
 '苹果肉桂猪扒':['肉桂苹果猪扒','苹果猪扒'], '蒜香鸡翅':['蒜香鸡翼'],
 '蒜蓉蒸丝瓜':['蒜茸蒸丝瓜'], '椒丝腐乳空心菜':['椒丝腐乳炒通菜'],
 '白切猪肉':['白切肉'], '紫菜虾滑煎饼':['紫菜虾滑饼','紫菜虾饼'],
 '肉末饭':['肉沫饭','肉沫拌饭'], '油浸小番茄':['油浸番茄'],
 '麦片鸡蛋':['鸡蛋麦片'], '赤小豆薏仁茶':['赤小豆薏米茶'],
 '姜撞奶':['自制姜撞奶'], '手打百香果柠檬茶':['手打柠檬茶'],
 '蒜蓉酱':['蒜蓉酱熬制'], '蓝莓酱':['自制蓝莓酱'],
}
REMOVED_CANON={'白切肉','油浸番茄'}
EXCLUDED={
 'BV1AAksB2Ep4':('自媒体拍摄工具、剪辑和账号收益经验分享；全片内嵌字幕及12秒间隔画面抽查未见做菜过程。','Discussion of filming tools, editing and creator-account income; on-screen captions across the video and visual sampling every 12 seconds show no cooking process.'),
 'BV14iXoBzEY1':('锅底去污及厨房清洁经验介绍；4秒间隔全时段画面和画面内字幕抽查未见食材制作过程。','Pan-bottom stain removal and kitchen-cleaning discussion; four-second visual sampling across the video and on-screen captions show no food preparation.'),
 'BV1SYA3zgEtk':('香港观光巴士与旅行路线，全时段画面抽查未见做菜。','Hong Kong sightseeing bus and travel route; no cooking found in sampled scenes across the full duration.'),
 'BV1KMZjBNEVp':('香港外出用餐和购物记录，全时段画面抽查未见做菜。','Hong Kong dining and shopping diary; no cooking found in sampled scenes across the full duration.'),
 'BV1LHtpzyEBD':('香港澳门交通、住宿、购物与外出用餐，全时段画面抽查未见做菜。','Hong Kong and Macao transport, hotels, shopping and dining; no cooking found in sampled scenes across the full duration.'),
 'BV1Votjz4EEw':('酒店与旅行提醒，展示吃杯面而无菜谱制作过程。','Hotel and travel tips; eating instant noodles, with no recipe preparation shown.'),
 'BV1QMHx6EEZB':('直播聊天讲述账号名字与买橙经历，完整字幕及全时段画面抽查未见做菜。','Livestream conversation about the account name and an orange purchase; no cooking found in the complete subtitles or sampled scenes across the full duration.'),
 'BV1XPad6fEZn':('锅底去油垢清洁示范，全时段画面抽查未见食材或做菜过程。','Demonstration of removing grease from pan bottoms; no ingredients or cooking found in sampled scenes across the full duration.'),
 'BV1yZjo6mEko':('餐具、厨具和砧板的尺寸、价格及使用感受介绍；4秒间隔全时段画面及画面内字幕抽查未见做菜过程。','Kitchenware, tableware and chopping-board sizes, prices and usage impressions; four-second visual sampling across the full duration and on-screen captions show no cooking process.'),
}
EXCLUDED_REVIEW_METHOD={
 'BV1AAksB2Ep4':'全片内嵌字幕文字核对及12秒间隔全时段画面抽查，共26帧',
 'BV14iXoBzEY1':'原标题、4秒间隔全时段画面及画面内字幕抽查',
 'BV1QMHx6EEZB':'完整中文字幕与4秒间隔全时段画面抽查',
 'BV1XPad6fEZn':'原标题与4秒间隔全时段画面抽查',
 'BV1yZjo6mEko':'4秒间隔全时段画面与画面内字幕抽查；错配的独立字幕已弃用',
}
EXCLUDED_REVIEW_DATE={'BV1yZjo6mEko':'2026-11-01','BV14iXoBzEY1':'2026-11-01','BV1AAksB2Ep4':'2026-11-02'}
SAMPLE='BV12D4FzaEDY'
TITLE_COMPARISON_EXCLUSIONS={'BV1yaxe6zEkP':{'猪肚鸡'}}
SAMPLE_DISHES={'烤青花鱼':'00:04–00:26；02:08–02:18','姜葱炒鸡':'01:08–01:18；01:39–02:08','葱香虾球':'01:19–01:38','蒜蓉淋汁青菜':'00:26–00:42','蒜香干辣椒炒包菜':'00:43–01:07'}
REGISTRY_PATH=ROOT/'data/recipe_registry.json'
REGISTRY=json.loads(REGISTRY_PATH.read_text()) if REGISTRY_PATH.exists() else []
REVIEWED={}
for record in REGISTRY:
    REVIEWED.setdefault(record['bvid'],[]).append(record)

def write_csv(path, rows, fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('source',type=Path);args=ap.parse_args()
    raw=json.loads(args.source.read_text())
    assert len({v['bv_id'] for v in raw})==len(raw)
    dictionary=[]
    for category, names in GROUPS.items():
        for name in names.split():
            if name in REMOVED_CANON:continue
            dictionary.append({'dish':name,'category':category,'aliases':[name]+ALIASES.get(name,[])})
    for r in REGISTRY:
        if not any(d['dish']==r['name'] for d in dictionary):
            dictionary.append({'dish':r['name'],'category':r['category'],'aliases':[r['name']]})
    rows=[];excluded=[];links=[]
    for n,v in enumerate(raw,1):
        assert v['upper']['mid']==544087714
        bvid=v['bv_id'];title=v['title'];date=datetime.fromtimestamp(v['pubtime'],ZoneInfo('Asia/Shanghai'))
        base={'catalogue_id':n,'bvid':bvid,'title':title,'url':f'https://www.bilibili.com/video/{bvid}/','published_date':date.strftime('%Y-%m-%d'),'published_at':date.isoformat(),'duration_seconds':v['duration']}
        if bvid in EXCLUDED:
            excluded.append({**base,'reason':EXCLUDED[bvid][0],'reason_en':EXCLUDED[bvid][1],'review_method':EXCLUDED_REVIEW_METHOD.get(bvid,'标题与5秒间隔全时段场景抽查'),'reviewed_on':EXCLUDED_REVIEW_DATE.get(bvid,'2026-10-31')})
            continue
        matches=[]
        for d in dictionary:
            hits=[a for a in d['aliases'] if a in title]
            if hits:matches.append((d,max(hits,key=len)))
        # Avoid indexing a generic dish a second time when it occurs only inside a more specific name.
        selected=[]
        for d,hit in matches:
            residual=title
            for d2,hit2 in matches:
                if len(hit2)>len(hit) and hit in hit2:residual=residual.replace(hit2,'')
            if hit in residual:selected.append((d,hit))
        selected=[pair for pair in selected if pair[0]['dish'] not in TITLE_COMPARISON_EXCLUSIONS.get(bvid,set())]
        if bvid in REVIEWED:
            selected=[(next(d for d in dictionary if d['dish']==r['name']),r['name']) for r in REVIEWED[bvid]]
        elif bvid==SAMPLE:
            selected=[(next(d for d in dictionary if d['dish']==name),name) for name in SAMPLE_DISHES]
        if bvid in REVIEWED or bvid==SAMPLE:status='verified_cooking'
        elif re.match(r'【是厚皮橙】',title):status='needs_content_review'
        elif selected or re.search(r'做法|做菜|炒|煎|蒸|焖|炖|煲|烤|卤|拌|备餐|早餐|午餐|晚餐|一人食|简餐|汤|米饭|意面|饺|包子|腌|煮|炸|三餐',title):status='title_cooking_lead'
        else:status='needs_content_review'
        row={**base,'status':status,'dishes':'；'.join(d['dish'] for d,_ in selected),'categories':'；'.join(dict.fromkeys(d['category'] for d,_ in selected)),'source_basis':'视频字幕与画面已核对' if status=='verified_cooking' else '原标题线索，尚未逐条核对视频内容'}
        rows.append(row)
        for d,hit in selected:
            record=next((r for r in REVIEWED.get(bvid,[]) if r['name']==d['dish']),None)
            time_range=record['time_ranges'] if record else SAMPLE_DISHES.get(d['dish'],'') if bvid==SAMPLE else ''
            links.append({'category':d['category'],'dish':d['dish'],'bvid':bvid,'title':title,'url':base['url'],'published_date':base['published_date'],'basis':'verified_video' if status=='verified_cooking' else 'title_match','matched_text':hit,'time_range':time_range})
    links.sort(key=lambda r:(list(GROUPS).index(r['category']),r['dish'],-int(r['published_date'].replace('-',''))))
    used={r['dish'] for r in links}; dictionary=[d for d in dictionary if d['dish'] in used]
    counts=Counter(r['status'] for r in rows)
    reviewed_videos=len(REVIEWED) if REGISTRY else 1
    reviewed_recipes=sum(r['kind']=='dish' for r in REGISTRY) if REGISTRY else 5
    preparations=sum(r['kind']=='preparation' for r in REGISTRY)
    metadata={'as_of':max(['2026-10-31']+[r['reviewed_on'] for r in REGISTRY]),'catalogue_as_of':'2026-10-31','author':'是厚皮橙','uid':544087714,'source_url':'https://space.bilibili.com/544087714','catalogue_unique_count':len(raw),'profile_display_count':1226,'api_reported_count':1227,'api_pagination_exhausted':True,'main_list_count':len(rows),'excluded_count':len(excluded),'reviewed_recipe_videos':reviewed_videos,'reviewed_recipes':reviewed_recipes,'reviewed_preparations':preparations,'unreviewed_content_count':len(rows)-reviewed_videos,'status_counts':dict(counts),'indexed_dish_count':len(used),'dish_video_links':len(links),'videos_with_dish_index':len({r['bvid'] for r in links}),'first_publish_date':min(r['published_date'] for r in rows),'last_publish_date':max(r['published_date'] for r in rows),'stage':'Catalogue complete; detailed recipe extraction is in progress. See recipes/INDEX.md for reviewed content.'}
    data=ROOT/'data';data.mkdir(exist_ok=True)
    for filename,value in [('videos.json',rows),('dish_index.json',links),('dish_dictionary.json',dictionary),('excluded.json',excluded),('progress.json',metadata)]:
        (data/filename).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    write_csv(data/'videos.csv',rows,list(rows[0]))
    write_csv(data/'dish_index.csv',links,list(links[0]))
    write_csv(data/'excluded.csv',excluded,list(excluded[0]))
    write_csv(data/'review_queue.csv',[r for r in rows if r['status']=='needs_content_review'],list(rows[0]))
    print(json.dumps(metadata,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
