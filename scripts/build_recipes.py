"""Build readable recipe pages and a navigation index from reviewed records."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json,re,collections

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data';PAGES=ROOT/'recipes'
SOURCE={v['bv_id']:v for v in json.loads((DATA/'source_catalogue.json').read_text())}
TRANSLATIONS={}
for translation_file in sorted(DATA.glob('recipe_batch_*.en.json')):
    translated=json.loads(translation_file.read_text())
    assert not (TRANSLATIONS.keys() & translated.keys()), 'Duplicate video translation'
    TRANSLATIONS.update(translated)
CATEGORIES={'鸡鸭禽肉':'Poultry','猪肉':'Pork','牛羊肉':'Beef and lamb','鱼虾海鲜':'Fish and seafood','蛋豆蔬菜':'Eggs tofu and vegetables','米饭面点':'Rice noodles and bread','汤羹粥':'Soups and congee','甜品饮品':'Desserts and drinks','调味与备餐':'Preparation methods'}
NOTES_EN={
 'BV1pGxY6eEi5':['At 03:08–03:38 another white string-like ingredient is stewed with milk. It resembles bird nest but the ingredient and cooking time are not explicitly identified, so it is not included as a usable recipe.'],
 'BV1y3no69Eyg':['After 02:15 the creator prepares chicken and cucumber for the next morning. This is not counted again as a finished dish. The chicken rice meal is recorded under BV1bqxM6gERy.'],
 'BV1J9HV6FEjG':['Quinoa rice is shown only as a finished accompaniment, so no separate preparation recipe is claimed.'],
 'BV1fZHP6vEJn':['Layer cake is only cut and plated, and guava is only sliced; neither is counted as a recipe made in this video.'],
}

def main():
    batches=[]
    for p in sorted(DATA.glob('recipe_batch_*.json')):
        if p.name.endswith('.en.json'):continue
        batches.extend(json.loads(p.read_text()))
    assert len({v['bvid'] for v in batches})==len(batches)
    registry=[]
    for v in batches:
        bid=v['bvid'];original=SOURCE[bid];url=f'https://www.bilibili.com/video/{bid}/'
        date=datetime.fromtimestamp(original['pubtime'],ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d')
        tr=TRANSLATIONS[bid];assert len(tr)==len(v['recipes'])
        for lang in ['zh','en']:
            en=lang=='en';suffix='.en' if en else ''
            other=f'{bid}{"" if en else ".en"}.md'
            text=f'[{"中文" if en else "English"}]({other})\n\n'
            text+=f'# {"Recipes from this video" if en else "本期菜谱"}\n\n'
            text+=f'[{original["title"]}]({url})\n\n'
            review_method=v.get('review_method_en' if en else 'review_method')
            if review_method:
                assert v.get('review_method') and v.get('review_method_en'), 'Review method needs both languages'
                text+=(f'Published {date}. {review_method}\n\n' if en else f'发布于 {date}。{review_method}\n\n')
            else:
                text+=(f'Published {date}. Subtitles, visual overviews and key details were reviewed. Missing source parameters remain explicit.\n\n' if en else f'发布于 {date}。已核对字幕、全片画面概览及关键细节；原片未明确的参数保留缺项。\n\n')
            text+=f'[{"Recipe directory" if en else "返回菜谱目录"}](INDEX{suffix}.md)\n\n'
            for n,r in enumerate(v['recipes'],1):
                t=tr[n-1] if en else r
                title=r['name_en'] if en else r['name']
                tag=(' (preparation method)' if en else '（基础备餐方法）') if r['kind']=='preparation' else ''
                text+=f'<a id="r{n:02}"></a>\n\n## {n} {title}{tag}\n\n'
                text+=f'{"Time reference" if en else "回看时间"}: {r["time_ranges"]}\n\n'
                text+=f'**{"Ingredients" if en else "食材"}**: {t["ingredients"]}\n\n'
                text+=f'**{"Confirmed amounts and times" if en else "原片明确的用量和时间"}**: {t["quantities"]}\n\n'
                for i,s in enumerate(t['steps'],1):text+=f'{i}. {s}\n'
                text+=f'\n**{"Missing details" if en else "未明确的信息"}**: {t["missing"]}\n\n'
            notes=v.get('pending_segments_en',NOTES_EN.get(bid,[])) if en else v.get('pending_segments',[])
            assert bool(notes)==bool(v.get('pending_segments',[]))
            if notes:
                text+=f'## {"Segment notes" if en else "片段说明"}\n\n'
                text+='\n'.join('- '+s for s in notes)+'\n'
            (PAGES/f'{bid}{suffix}.md').write_text(text)
        for n,r in enumerate(v['recipes'],1):
            registry.append({'recipe_id':f'{bid}-{n:02}','bvid':bid,'name':r['name'],'name_en':r['name_en'],'category':r['category'],'kind':r['kind'],'time_ranges':r['time_ranges'],'published_date':date,'reviewed_on':v['reviewed_on'],'source_url':url,'page':f'recipes/{bid}.md#r{n:02}','page_en':f'recipes/{bid}.en.md#r{n:02}'})
    sample=json.loads((DATA/'sample_recipes.json').read_text())
    categories=['鱼虾海鲜','鸡鸭禽肉','鱼虾海鲜','蛋豆蔬菜','蛋豆蔬菜']
    names_en=['Baked mackerel with salmon on the same tray','Ginger scallion chicken with salt baked seasoning','Scallion shrimp','Greens with garlic oil and seasoning','Cabbage with garlic and dried chili']
    for n,r in enumerate(sample['recipes'],1):
        registry.append({'recipe_id':f'BV12D4FzaEDY-{n:02}','bvid':'BV12D4FzaEDY','name':r['name'],'name_en':names_en[n-1],'category':categories[n-1],'kind':'dish','time_ranges':r['time'],'published_date':'2025-10-11','reviewed_on':'2026-10-31','source_url':sample['video_url'],'page':f'recipes/BV12D4FzaEDY.md#r{n:02}','page_en':f'recipes/BV12D4FzaEDY.en.md#r{n:02}'})
    # Preserve the accepted sample's prose, adding only stable navigation anchors.
    for suffix in ['', '.en']:
        p=PAGES/f'BV12D4FzaEDY{suffix}.md';s=p.read_text();s=re.sub(r'<a id="r\d+"></a>\n\n','',s)
        counter=[0]
        def anchor(m):
            counter[0]+=1;return f'<a id="r{counter[0]:02}"></a>\n\n'+m.group(0)
        s=re.sub(r'^## .+$',anchor,s,flags=re.M);assert counter[0]==5;p.write_text(s)
    assert len({r['recipe_id'] for r in registry})==len(registry)
    (DATA/'recipe_registry.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    dishes=sum(r['kind']=='dish' for r in registry);prep=sum(r['kind']=='preparation' for r in registry);videos=len({r['bvid'] for r in registry})
    for lang in ['zh','en']:
        en=lang=='en';suffix='.en' if en else ''
        s=f'[{"中文" if en else "English"}](INDEX{"" if en else ".en"}.md)\n\n'
        s+=f'# {"Recipe directory and index" if en else "菜谱目录与菜名索引"}\n\n'
        s+=(f'This directory contains **{dishes} recipe entries and {prep} preparation methods from {videos} reviewed videos**. Different versions of a dish remain separate. This is an incomplete collection; missing quantities and heat settings are stated in each entry.\n\n' if en else f'目前收录 **{videos} 条已核视频中的 {dishes} 条菜谱和 {prep} 条基础备餐方法**。同名菜的不同版本分别保留；全量整理尚未完成，原片缺少的用量与火候在各条中说明。\n\n')
        s+=('[All video titles and pending clues](../docs/VIDEO_LIST.en.md) · [Progress](../README.en.md)\n\n' if en else '[全部视频与待核线索](../docs/VIDEO_LIST.md) · [当前进度](../README.md)\n\n')
        for category,category_en in CATEGORIES.items():
            rs=sorted([r for r in registry if r['category']==category],key=lambda r:(r['name'],r['published_date']))
            if not rs:continue
            s+=f'## {category_en if en else category}\n\n'
            s+=('| Recipe | Video date | Time reference |\n|---|---|---|\n' if en else '| 菜名 | 视频日期 | 回看时间 |\n|---|---|---|\n')
            for r in rs:
                label=r['name_en'] if en else r['name'];target=(r['page_en'] if en else r['page']).removeprefix('recipes/')
                s+=f'| [{label}]({target}) | {r["published_date"]} | {r["time_ranges"]} |\n'
            s+='\n'
        s+=f'## {"Browse by video" if en else "按视频查找"}\n\n'
        ids=list(dict.fromkeys(r['bvid'] for r in registry))
        for bid in ids:
            rs=[r for r in registry if r['bvid']==bid];title=SOURCE[bid]['title']
            s+=f'- [{title}]({bid}{suffix}.md)'+(f' — {len(rs)} entries\n' if en else f'：{len(rs)} 条记录\n')
        (PAGES/f'INDEX{suffix}.md').write_text(s)
    print(json.dumps({'reviewed_videos':videos,'recipes':dishes,'preparations':prep,'entries':len(registry)},ensure_ascii=False))

if __name__=='__main__':main()
