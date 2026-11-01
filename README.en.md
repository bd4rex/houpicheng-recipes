[中文](README.md)

# Shi Houpicheng recipe series

A catalogue of videos, original links and dish-name references from [是厚皮橙 on Bilibili](https://space.bilibili.com/544087714), with recipes added gradually. Reviewed recipe content is available in the recipe directory. Extraction proceeds video by video; final packaging is deferred until content is complete.

## Current progress

The catalogue snapshot was collected on 2026-10-31, when pagination of accessible uploads was exhausted. Deduplication by BV ID yielded **1,226 videos**, matching the profile count. The API sometimes reported 1,227; only 1,226 distinct BV IDs were retrieved. Recipe content review is updated through 2026-11-02.

| Item | Count | Meaning |
|---|---:|---|
| Main list | 1,217 | Reviewed non-cooking items removed; remaining content still needs individual review |
| Excluded | 9 | Travel, hotels, dining out, conversation, cleaning or kitchenware presentations without cooking |
| Dish and preparation index terms | 670 | Mostly from original titles; this is not a count of completed recipes |
| Dish-to-video references | 1,835 | One video may contain several dishes |
| Recipe videos reviewed | 67 | Subtitles cross-checked against visual content |
| Recipes documented | 205 | Reviewed recipe entries; variations are retained separately |
| Preparation methods | 11 | Soaking, marinating and other preparations, counted separately |
| Cooking clues in title | 1,099 | Video content not individually verified yet |
| Inconclusive titles | 51 | Priority content-review queue |

The main list spans 2025-02-04 through 2026-10-30. **1,150 videos remain unverified at the content level**. The list does not establish that every remaining item contains cooking.

## Browse

- [Reviewed recipe directory and index](recipes/INDEX.en.md)
- [Video titles and links](docs/VIDEO_LIST.en.md)
- [Find original videos by dish](docs/DISH_INDEX.en.md)
- [Recommended index structure](docs/INDEX_DESIGN.en.md)
- [Exclusions](docs/EXCLUDED.en.md)
- [Five dishes from one video](recipes/BV12D4FzaEDY.en.md)

## How to use

Browse the reviewed recipe directory by category or dish, then use its time references to revisit the source. The full title index supplies leads for remaining work. The catalogue retains the original title, publication date, link and review status. Inconclusive titles stay in the list with a pending status to avoid accidental exclusion.

Dish names are the primary index and ingredient categories are secondary. Retain all videos for a dish and allow a video to reference several dishes. Do not invent quantities, temperatures, heat settings or seasoning identities missing from the source. Original Chinese titles and dish identifiers are retained as source data.

## Data and reproduction

- `data/source_catalogue.json`: necessary public catalogue fields for 1,226 videos.
- `data/videos.csv`, `data/videos.json`: main list after exclusions.
- `data/dish_index.csv`, `data/dish_dictionary.json`: provisional references and normalization dictionary.
- `data/review_queue.csv`: 51 inconclusive titles awaiting priority review.
- `data/excluded.csv`: exclusion reasons and original links.
- `data/progress.json`: progress snapshot distinguishing catalogue completion from unfinished recipe extraction.
- `data/review_batch_*.json`: batch review records with selected videos, evidence summaries, exclusion reasons and the next priority video ID.

These commands rebuild derived lists and Markdown from the saved snapshot. They do not fetch new videos or change pending items to verified automatically:

```bash
python3 scripts/build_recipes.py
python3 scripts/build_catalogue.py data/source_catalogue.json
python3 scripts/build_docs.py
```

Historical downloads preserve the initial catalogue snapshot. Current recipes and progress are authoritative in the recipe directory and `data/progress.json`. Final exports are deferred until the content is complete.

## Remaining work

1. Review inconclusive titles first. Add dish names when cooking is present; otherwise exclude the video and record the reason.
2. Review subtitles and visual content by dish, adding ingredients, steps and time references.
3. Preserve variations of the same dish and compare seasoning and heat separately; do not merge them into a recipe that never appeared.
4. Synchronize recipes, indexes, review status, progress and both documentation languages on each update; prepare final exports once the content is complete.

## Sources and maintenance

Original videos and creative work belong to their creator. This repository retains original titles, source links, organized notes and progress. Original video files and full subtitles are not distributed.

[Update log](TIMESTAMP_LOG.en.md) · [中文更新记录](TIMESTAMP_LOG.md)
