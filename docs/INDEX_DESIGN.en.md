[中文](INDEX_DESIGN.md)

# Recommended menu index

## Recommended structure

Use **dish names as the primary index, ingredient categories as a secondary index, and original videos as evidence**. Find a dish first, then open its source. Create separate references for the dishes contained in one video.

| Layer | Contents | Example |
|---|---|---|
| Primary index | Canonical dish name | Ginger-scallion chicken, meat-sauce pasta, mango sago |
| Secondary index | Main ingredient or finished-food category | Poultry, seafood, rice and noodles, soups and congee |
| Context tags | Context confirmed in the video | Breakfast, meals for one, meal preparation, low-smoke cooking |
| Source location | Original URL and time ranges | BV12D4FzaEDY, 01:08–01:18 and 01:39–02:08 |
| Recipe record | Ingredients, amounts, steps, heat and missing details | Mark an unstated weight as unspecified |

## Current implementation

The provisional title index has nine categories: poultry; pork; beef and lamb; fish and seafood; eggs, tofu and vegetables; rice, noodles and bread; soups and congee; desserts and drinks; sauces and meal preparation.

The current 470 index terms mainly reflect dish and preparation words mentioned in titles. They are not complete recipes verified from every video. A title may mention a dish for comparison, so index hits still need content review. Only the completed sample has timestamps cross-checked against subtitles and visual content.

## Inclusion and exclusion rules

1. Retain videos showing cooking, food preparation, seasoning or actual meal preparation.
2. Retain mixed lifestyle videos containing usable cooking segments and record their time ranges.
3. Exclude reviewed videos limited to travel, shopping, dining out or hotels without cooking; preserve the reason and original link.
4. Keep vague titles such as generic new-upload announcements pending review.
5. A cooking clue in a title is preliminary screening and must not automatically become verified cooking.

## Names and variations

Retain multiple video versions of a dish. Common spelling variants can share a search term, but this does not authorize combining ingredients from separate videos. Different seasoning styles, appliances and heat settings should remain separate variations.

## Fields to add

Suggested recipe fields are `recipe_id`, `dish_name`, `variant`, `video_bvid`, `start_seconds`, `end_seconds`, `ingredients`, `amounts`, `steps`, `heat`, `duration`, `missing_details`, and `review_status`. Join recipes to videos by BV ID instead of title or spreadsheet row number so incremental updates and corrections remain stable.

## Next batch priorities

Review the 68 inconclusive titles first, followed by videos not yet covered by the dish index. Then expand recipes by the user's preferred dishes or frequently appearing dishes. Retain verified, pending and excluded statuses on every update so intermediate results stay usable.
