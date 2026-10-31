"""Render Chinese-default paired documentation from the public snapshot."""
from pathlib import Path
import json
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'data/progress.json').read_text())
V=json.loads((ROOT/'data/videos.json').read_text())
I=json.loads((ROOT/'data/dish_index.json').read_text())
E=json.loads((ROOT/'data/excluded.json').read_text())
S=json.loads((ROOT/'data/sample_recipes.json').read_text())
EN_CATEGORIES={'鸡鸭禽肉':'Poultry','猪肉':'Pork','牛羊肉':'Beef and lamb','鱼虾海鲜':'Fish and seafood','蛋豆蔬菜':'Eggs, tofu and vegetables','米饭面点':'Rice, noodles and bread','汤羹粥':'Soups and congee','甜品饮品':'Desserts and drinks','调味与备餐':'Sauces and meal preparation'}
ZH_STATUS={'verified_cooking':'已核做菜','title_cooking_lead':'标题有做菜线索','needs_content_review':'待核内容'}
EN_STATUS={'verified_cooking':'Cooking verified','title_cooking_lead':'Cooking clue in title','needs_content_review':'Content review needed'}

def write(p,text):
    (ROOT/p).write_text(text.strip()+'\n')
def cell(s):return str(s).replace('|','\\|').replace('\n',' ')

write('README.md',f'''[English](README.en.md)

# 是厚皮橙菜谱系列

整理 B 站 UP 主[是厚皮橙](https://space.bilibili.com/544087714)的视频标题、原链接与菜名索引，逐步补充可回看的菜谱。当前先完成清单和标题初筛，完整菜谱仍在整理中。

## 当前进度

截至 {M['as_of']}，已穷尽当前可访问的视频目录分页，按 BV 号去重得到 **{M['catalogue_unique_count']:,} 条**，与主页投稿数一致。接口总数曾返回 1,227，实际取得 1,226 个不同 BV 号。

| 项目 | 数量 | 含义 |
|---|---:|---|
| 主清单 | {M['main_list_count']:,} | 已剔除本轮核对的非做菜视频，其他内容仍待逐条核验 |
| 已剔除 | {M['excluded_count']} | 旅行、酒店、购物或外出用餐记录 |
| 菜名与备餐索引词 | {M['indexed_dish_count']} | 主要来自原标题，不是已完成菜谱数量 |
| 菜名与视频对应关系 | {M['dish_video_links']:,} | 一条视频可以对应多道菜 |
| 已核菜谱视频 | {M['reviewed_recipe_videos']} | 字幕和画面已交叉核对 |
| 已整理菜谱 | {M['reviewed_recipes']} | 位于单条视频样本中 |
| 标题有做菜线索 | {M['status_counts']['title_cooking_lead']:,} | 仍未逐条核对视频内容 |
| 标题不足以判断 | {M['status_counts']['needs_content_review']} | 优先待核队列 |

主清单覆盖 {M['first_publish_date']} 至 {M['last_publish_date']}。除样本外，**{M['unreviewed_content_count']:,} 条视频尚未完成逐条内容核验**；这份清单不能视为全部做菜视频已确认。

## 直接查看

- [视频标题与链接清单](docs/VIDEO_LIST.md)
- [按菜名查原视频](docs/DISH_INDEX.md)
- [索引结构建议](docs/INDEX_DESIGN.md)
- [剔除记录](docs/EXCLUDED.md)
- [一条视频的五道菜样本](recipes/BV12D4FzaEDY.md)
- [Excel 清单与菜名索引](downloads/是厚皮橙_视频清单与菜名索引.xlsx)
- [Word 菜谱样本](downloads/是厚皮橙_单条视频菜谱样本.docx)

## 使用方式

先在菜名索引中按分类或菜名查找，再打开原视频。视频清单保留原标题、发布时间、链接和核对状态。标题含糊的视频保留在清单中并标记待核，避免误删。

菜单索引采用“菜名为主、食材类别为辅”。同一道菜的多个视频全部保留；同一条视频可以出现在多个菜名下。视频没有明确给出的用量、温度、火候和调味品种，不补写成作者原配方。

## 数据与复现

- `data/source_catalogue.json`：公开目录的必要字段快照，共 {M['catalogue_unique_count']:,} 条。
- `data/videos.csv`、`data/videos.json`：剔除后的主清单。
- `data/dish_index.csv`、`data/dish_dictionary.json`：初步菜名对应关系和归一化词表。
- `data/review_queue.csv`：{M['status_counts']['needs_content_review']} 条标题含糊的优先待核视频。
- `data/excluded.csv`：剔除原因和原链接。
- `data/progress.json`：明确区分目录完成与菜谱未完成的进度快照。

以下命令只重建这份快照的派生清单和 Markdown，不会抓取新视频，也不会自动把待核改为已核：

```bash
python3 scripts/build_catalogue.py data/source_catalogue.json
python3 scripts/build_docs.py
```

Excel 是本次保存的可筛选下载版，更新数据后需同步刷新下载文件。

## 后续工作

1. 优先核对标题含糊的视频，确认包含做菜后补入具体菜名；无做菜则从主清单剔除并记录理由。
2. 按菜名分批核对字幕与画面，补充食材、做法和时间点。
3. 同名菜保留不同版本，逐项比较调味和火候，避免合并成不存在的配方。
4. 每次更新同步清单、索引、下载文件、进度和中英文文档。

## 来源与维护

原视频与创作归原作者。仓库保存原标题、来源链接、整理结果和进度，不分发原视频或完整字幕。

[更新时间记录](TIMESTAMP_LOG.md) · [English update log](TIMESTAMP_LOG.en.md)
''')

write('README.en.md',f'''[中文](README.md)

# Shi Houpicheng recipe series

A catalogue of videos, original links and dish-name references from [是厚皮橙 on Bilibili](https://space.bilibili.com/544087714), with recipes added gradually. The current stage completes the catalogue and initial title screening. Full recipe extraction remains unfinished.

## Current progress

As of {M['as_of']}, pagination of the accessible upload catalogue has been exhausted. Deduplication by BV ID yielded **{M['catalogue_unique_count']:,} videos**, matching the profile count. The API sometimes reported 1,227; only 1,226 distinct BV IDs were retrieved.

| Item | Count | Meaning |
|---|---:|---|
| Main list | {M['main_list_count']:,} | Reviewed non-cooking items removed; remaining content still needs individual review |
| Excluded | {M['excluded_count']} | Travel, hotels, shopping or dining out |
| Dish and preparation index terms | {M['indexed_dish_count']} | Mostly from original titles; this is not a count of completed recipes |
| Dish-to-video references | {M['dish_video_links']:,} | One video may contain several dishes |
| Recipe videos reviewed | {M['reviewed_recipe_videos']} | Subtitles cross-checked against visual content |
| Recipes documented | {M['reviewed_recipes']} | Included in the single-video sample |
| Cooking clues in title | {M['status_counts']['title_cooking_lead']:,} | Video content not individually verified yet |
| Inconclusive titles | {M['status_counts']['needs_content_review']} | Priority content-review queue |

The main list spans {M['first_publish_date']} through {M['last_publish_date']}. **{M['unreviewed_content_count']:,} videos remain unverified at the content level**. The list does not establish that every remaining item contains cooking.

## Browse

- [Video titles and links](docs/VIDEO_LIST.en.md)
- [Find original videos by dish](docs/DISH_INDEX.en.md)
- [Recommended index structure](docs/INDEX_DESIGN.en.md)
- [Exclusions](docs/EXCLUDED.en.md)
- [Five dishes from one video](recipes/BV12D4FzaEDY.en.md)
- [Excel catalogue and dish index](downloads/是厚皮橙_视频清单与菜名索引.xlsx)
- [Word recipe sample](downloads/是厚皮橙_单条视频菜谱样本.docx)

## How to use

Filter the dish index by category or dish, then open an original video. The catalogue retains the original title, publication date, link and review status. Inconclusive titles stay in the list with a pending status to avoid accidental exclusion.

Dish names are the primary index and ingredient categories are secondary. Retain all videos for a dish and allow a video to reference several dishes. Do not invent quantities, temperatures, heat settings or seasoning identities missing from the source. Original Chinese titles and dish identifiers are retained as source data.

## Data and reproduction

- `data/source_catalogue.json`: necessary public catalogue fields for {M['catalogue_unique_count']:,} videos.
- `data/videos.csv`, `data/videos.json`: main list after exclusions.
- `data/dish_index.csv`, `data/dish_dictionary.json`: provisional references and normalization dictionary.
- `data/review_queue.csv`: {M['status_counts']['needs_content_review']} inconclusive titles awaiting priority review.
- `data/excluded.csv`: exclusion reasons and original links.
- `data/progress.json`: progress snapshot distinguishing catalogue completion from unfinished recipe extraction.

These commands rebuild derived lists and Markdown from the saved snapshot. They do not fetch new videos or change pending items to verified automatically:

```bash
python3 scripts/build_catalogue.py data/source_catalogue.json
python3 scripts/build_docs.py
```

The Excel workbook is a saved filterable export. Refresh the download when the underlying data changes.

## Remaining work

1. Review inconclusive titles first. Add dish names when cooking is present; otherwise exclude the video and record the reason.
2. Review subtitles and visual content by dish, adding ingredients, steps and time references.
3. Preserve variations of the same dish and compare seasoning and heat separately; do not merge them into a recipe that never appeared.
4. Synchronize lists, indexes, downloads, progress and both documentation languages on each update.

## Sources and maintenance

Original videos and creative work belong to their creator. This repository retains original titles, source links, organized notes and progress. Original video files and full subtitles are not distributed.

[Update log](TIMESTAMP_LOG.en.md) · [中文更新记录](TIMESTAMP_LOG.md)
''')

for lang in ['zh','en']:
    en=lang=='en';suffix='.en' if en else '';other='VIDEO_LIST.md' if en else 'VIDEO_LIST.en.md'
    text=f"[{'中文' if en else 'English'}]({other})\n\n# {'Video titles and links' if en else '视频标题与链接清单'}\n\n"
    text+=('Original Chinese titles are preserved. Four reviewed non-cooking videos have been removed. All items except the sample still need individual content verification.\n\n' if en else '保留原标题。已剔除本轮核对的 4 条非做菜视频；除样本外，其余视频仍未逐条核验。\n\n')
    text+=('| ID | Published | Original title and link | Duration | Review status |\n|---:|---|---|---:|---|\n' if en else '| 编号 | 发布日期 | 原标题与链接 | 时长 | 核对状态 |\n|---:|---|---|---:|---|\n')
    for r in V:
        sec=r['duration_seconds'];label=(EN_STATUS if en else ZH_STATUS)[r['status']]
        text+=f"| {r['catalogue_id']} | {r['published_date']} | [{cell(r['title'])}]({r['url']}) | {sec//60}:{sec%60:02} | {label} |\n"
    write(f'docs/VIDEO_LIST{suffix}.md',text)

    group=defaultdict(lambda:defaultdict(list))
    for r in I:group[r['category']][r['dish']].append(r)
    text=f"[{'中文' if en else 'English'}](DISH_INDEX{'' if en else '.en'}.md)\n\n# {'Dish index' if en else '菜名索引'}\n\n"
    text+=(f"{M['indexed_dish_count']} original-language dish and preparation terms with {M['dish_video_links']} video references. Titles provide provisional clues; they do not establish complete recipes. Only links marked reviewed have been checked against video content.\n\n" if en else f"{M['indexed_dish_count']} 个菜名与备餐关键词，{M['dish_video_links']} 条视频对应关系。标题索引只是线索，不是完整菜谱。只有标注“已核”的链接已经核对视频内容。\n\n")
    for category,ds in group.items():
        text+=f"## {EN_CATEGORIES[category] if en else category}\n\n"
        text+=('| Original dish name | Videos | Original video links |\n|---|---:|---|\n' if en else '| 菜名或备餐关键词 | 视频数 | 原视频链接 |\n|---|---:|---|\n')
        for dish,rels in sorted(ds.items()):
            links=[]
            for r in rels:
                marker=(' reviewed' if en else ' 已核') if r['basis']=='verified_video' else ''
                links.append(f"[{r['published_date']} {r['bvid']}{marker}]({r['url']})")
            text+=f"| {dish} | {len(rels)} | {' · '.join(links)} |\n"
        text+='\n'
    write(f'docs/DISH_INDEX{suffix}.md',text)

    text=f"[{'中文' if en else 'English'}](EXCLUDED{'' if en else '.en'}.md)\n\n# {'Excluded videos' if en else '已剔除的视频'}\n\n"
    text+=('These videos are excluded from the main list and dish index. Review used original titles and scenes sampled every five seconds across the full duration; it was not frame-by-frame viewing. Links remain available for rechecking.\n\n' if en else '以下条目已从主清单和菜名索引剔除。核对方式为原标题加覆盖全时段的 5 秒间隔场景抽查，并非逐帧观看；保留链接与理由以便复查。\n\n')
    text+=('| Video | Reason |\n|---|---|\n' if en else '| 视频 | 剔除原因 |\n|---|---|\n')
    for r in E:text+=f"| [{cell(r['title'])}]({r['url']}) | {r['reason_en'] if en else r['reason']} |\n"
    write(f'docs/EXCLUDED{suffix}.md',text)

text='[English](BV12D4FzaEDY.en.md)\n\n# 单条视频菜谱样本\n\n'
text+=f"来源：[是厚皮橙原视频]({S['video_url']})，发布于 2025-10-11，时长 2分29秒。字幕与画面交叉核对。\n\n"
for n,r in enumerate(S['recipes'],1):
    text+=f"## {n} {r['name']}\n\n回看时间：{r['time']}。\n\n**食材**：{r['ingredients']}\n\n"
    for i,step in enumerate(r['steps'],1):text+=f'{i}. {step}\n'
    text+=f"\n**关键点**：{r['key']}\n\n**未明确的信息**：{r['missing']}\n\n"
write('recipes/BV12D4FzaEDY.md',text)
print('Wrote paired catalogue, dish index, exclusions, README and Chinese sample.')
