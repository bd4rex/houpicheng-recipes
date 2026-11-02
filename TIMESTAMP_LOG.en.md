[中文](TIMESTAMP_LOG.md)

# Update log

## 2026 October 31 Initial catalogue

- Repository: `https://github.com/bd4rex/houpicheng-recipes`.
- Branch: `main`.
- Exhausted accessible catalogue pagination and obtained 1,226 distinct BV IDs, matching the profile count.
- Removed four travel, hotel and other non-cooking records from the main list, leaving 1,222 items. Exclusion evidence and links are retained separately.
- The provisional index contains 470 dish and preparation keywords and 1,680 video references, mainly based on original titles.
- Completed five recipes from one video; the other 1,221 videos have not been individually reviewed at the content level.
- This stage delivers the catalogue, index recommendations, exclusions, review queue, Excel and Word downloads, and synchronized Chinese and English documentation.
- 2026-10-31 14:17 (Asia/Shanghai): created the private repository and pushed initial commit `b2bcbcb66a14aad4bcbe24c57f565dab144a3b37`. Remote `main` matched the local commit, and Git object hashes matched for all 31 files.
- This record was appended after initial publication; the follow-up log commit is available in Git history.

## 2026 October 31 15:56 Recipe content expansion

- Continued from `b1f7211285f2671e9e60658c6b8587e3e8f19f7f`, reviewing subtitles, visual overviews across the duration, and key details for 12 more videos.
- Added 34 recipe entries and two preparation methods; totals are 13 reviewed videos, 39 recipes and two preparation methods.
- Added `recipes/INDEX.md` and its English counterpart, linking directly to recipe content and source time references.
- Synchronized reviewed statuses and the full clue index. The main list still contains 1,222 videos, of which 1,209 remain individually unreviewed.
- Retained unresolved ingredients, quantities, heat settings and segment gaps; corrected automatic subtitle errors for short minute ranges.
- Recipe content now takes priority. Historical Excel and Word exports remain old snapshots; final output formats are deferred until content is complete.
- Both language versions, navigation, progress and source relations were checked together. Content commit `8787b72edc43def803f629f3856922710b3f8cea` was pushed to remote `main`; Git object hashes matched the local version for all 62 files.

## 2026-10-31 19:32 Review of 20 more videos

- Baseline: `060e599106b022b18dd6ce741dff9ec1f5d0c5c7`; local and remote `main` matched before this update.
- Reviewed Chinese subtitles, four-second visual overviews across the full duration, and key on-screen details for 20 more videos, adding 65 recipes and 4 preparation methods.
- Totals: 33 reviewed videos, 104 recipes and 6 preparation methods; the main list still contains 1,222 videos, of which 1,189 await individual content review.
- Added fish steamed over pork, fish-bone tofu soup, rice-cooker beef shank, sweet-sour ribs, shiso beef, squid and lotus root with XO sauce, seasoned steamed chicken and other dishes; differences between titles and actual ingredients remain explicit.
- Plated prepared foods, shopping presentations and spoken alternatives are not counted as dishes made on camera. Missing quantities, temperatures and timings remain visible.
- Updated paired recipe pages and directories. The broader clue index has 566 dish or preparation terms and 1,746 video links; historical downloads remain snapshots.
- Checked 20 source BVID/CID pairs and subtitle digests, 110 recipe or preparation anchors, and the links and bilingual structure of 80 Markdown files; no broken links were found.
- Content commit `dd088a86953b01a9edc5136d2a7eb50f0b69087f` was pushed to remote `main`; the remote commit matched and all 112 file blob hashes matched the local checkout.

## 2026-11-01 01:06 Review of 24 more videos

- Baseline: `85f32582071bf1d38e99ed80137e7fb25de1e2dc`. This batch continued from the evening of 2026-10-31 into 2026-11-01.
- Reviewed 24 videos: 22 contain cooking, adding 69 recipes and 4 preparation methods. Two videos about the account name and pan cleaning were removed from the main list and dish index.
- Totals: 55 reviewed cooking videos, 173 recipes and 10 preparation methods. The main list has 1,220 videos, with 6 exclusions and 1,165 awaiting content review; 66 titles remain inconclusive.
- Added Cantonese brisket, steamed fish and eggs, shrimp-stuffed morels, Thai shrimp salad, poached chicken, radish with beef offal, shrimp sandwiches, razor-clam and squid rice toppings and other methods, preserving unknown quantities, heat settings and ingredient identities.
- Updated paired recipe pages, directories, exclusion evidence and progress. The broader index has 637 dish or preparation terms and 1,802 video references.
- Distinguished the 2026-10-31 catalogue snapshot from the 2026-11-01 recipe update, so the later writing date does not imply a fresh catalogue crawl.
- Checked BVID, CID, subtitle digests and time ranges for all 22 new cooking sources, 183 recipe or preparation anchors and the links and bilingual structure of 124 Markdown files; no broken links were found.
- Content commit `1c991f80482a36ca2b4e76e2bd04b5b07db85016` was pushed to remote `main`; the remote commit matched and all 168 file blob hashes matched locally.

## 2026-11-01 16:19 Review five videos from the priority queue

- Local baseline: `cf7a188`. Continued with the first five entries in the previous priority queue, under batch `20261101_02`.
- Four cooking videos added 15 recipes; one kitchenware presentation was excluded with its reason retained. `BV1beuZ6BEgP` has a rights-dispute title but actually contains cooking, so it was retained and documented.
- Totals: 59 reviewed cooking videos, 188 recipes and 10 preparation methods. The main list has 1,219 videos, with seven exclusions, 1,160 videos still awaiting content review and 61 in the priority queue.
- Reviewed visual overviews sampled every four seconds across this batch and key frames. Three cooking videos were checked through on-screen captions; the fourth also had usable standalone Chinese subtitles. Mismatched subtitle files returned for three videos were rejected. The automatic subtitle naming almonds was corrected to Job’s tears using the source screen text.
- Already-plated salad and layered cake were not counted as new recipes. A three-minute clay-pot timer was not treated as a complete universal cooking duration. Unconfirmed ingredients, liquids, ratios and heat remain unknown.
- Synchronized Chinese and English recipes, indexes, exclusions and progress. The index now contains 652 dish/preparation terms and 1,817 video references. Evidence summaries and the continuation ID are saved in `data/review_batch_20261101_02.json`; the next priority video is `BV1VwVB6YEeW`.
- Validated 198 recipe/preparation registry entries, local links in 132 Markdown files, and time ranges and paired step counts for all 15 new recipes, with no broken links. Raw subtitles and videos remain only in the sibling source-material directory.
- Saved locally only; no Git commit or remote push was performed for this batch.

## 2026-11-01 18:52 Save individual review of BV1VwVB6YEeW

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261101_03` is 1/5 complete.
- Added 2 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 60 reviewed cooking videos, 190 recipes, 10 preparation methods and 1159 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-01 19:29 Save individual review of BV1EB5x6VEah

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261101_03` is 2/5 complete.
- Added 4 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 61 reviewed cooking videos, 194 recipes, 10 preparation methods and 1158 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-01 19:42 Exclude individually reviewed video BV14iXoBzEY1

- Checked this video alone using four-second visual sampling across its duration and on-screen captions. It covers pan and kitchen cleaning without food preparation; the exclusion reason and evidence hash are saved.
- Batch `20261101_03` is 3/5 complete. Totals: eight exclusions, 1,218 main-list videos, 61 reviewed cooking videos, 194 recipes, 10 preparation methods and 1,157 videos pending review.
- Synchronized both languages, exclusions, catalogue and progress. Removed this entry from the main and priority lists. Saved locally without pushing.

## 2026-11-01 20:34 Save individual review of BV1DsPmzLEhQ

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261101_03` is 4/5 complete.
- Added 2 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 62 reviewed cooking videos, 196 recipes, 10 preparation methods and 1156 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-01 22:25 Save individual review of BV1qpZxB2E9h

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261101_03` is 5/5 complete.
- Added 2 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 63 reviewed cooking videos, 198 recipes, 10 preparation methods and 1155 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

- 22:36 All five videos in this batch have been saved individually: four cooking videos, 10 recipes and one cleaning-video exclusion. Verified five source hashes/durations, 208 registry entries and local links in 140 Markdown files, with no broken links. Next priority video: `BV16ucMzGE1C`.

## 2026-11-02 00:22 Publish two reviewed batches to GitHub

- Published batches `20261101_02` and `20261101_03` to `main` in `https://github.com/bd4rex/houpicheng-recipes`.
- Content commit `2fca14045f7f9ab4b9e03206ae522b9c6f56f8eb` was pushed successfully. A live remote-head check matches the local commit, covering 190 tracked files.
- Added eight reviewed cooking videos and 25 recipes, with two non-cooking exclusions. Totals are 63 reviewed videos, 198 recipes, 10 preparation methods and 1,155 videos awaiting review.
- Original videos, complete subtitles and browser-session material remain in the local source directory. This publication confirmation was added after the content push succeeded.

## 2026-11-02 01:01 Save individual review of BV16ucMzGE1C

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261102_01` is 1/5 complete.
- Added 1 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 64 reviewed cooking videos, 199 recipes, 10 preparation methods and 1154 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-02 01:31 Save individual review of BV1ioFpzkEEP

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261102_01` is 2/5 complete.
- Added 2 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 65 reviewed cooking videos, 201 recipes, 10 preparation methods and 1153 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-02 02:03 Save individual review of BV1AkzSBLEmw

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261102_01` is 3/5 complete.
- Added 2 recipes and 1 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 66 reviewed cooking videos, 203 recipes, 11 preparation methods and 1152 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-02 02:24 Save individual review of BV1vQzpBWEpH

- Following the user's instruction, finish and save each video before moving to the next. Batch `20261102_01` is 4/5 complete.
- Added 2 recipes and 0 preparation methods; synchronized both languages, indexes and progress. Unstated source parameters remain unknown.
- Totals: 67 reviewed cooking videos, 205 recipes, 11 preparation methods and 1151 videos awaiting review.
- Checked this video's BV ID, CID, evidence hashes, time ranges, paired step counts and page anchors. Saved locally without a Git commit or push.

## 2026-11-02 02:40 Complete individual-video batch 20261102_01

- Reviewed and saved five videos one at a time. Added four cooking videos, seven recipes and one warm-water chia-soaking method. Excluded creator-filming/income discussion `BV1AAksB2Ep4` with its source and reason retained.
- Used text first and reduced visual previews as needed. The final non-cooking video was checked through on-screen captions and a 12-second visual overview; the sampling method is explicitly recorded.
- Retained explicit parameters including one egg, 100 ml milk and one minute for bagel reheating. Unconfirmed powder, white ingredients, cup contents and ratios remain unknown.
- Totals: 67 reviewed cooking videos, 205 recipes and 11 preparation methods; 1,217 main-list videos, nine exclusions and 1,150 videos pending review. Next priority video: `BV1okieBEEqT`.
- Synchronized both languages, recipes, indexes, exclusions and progress. This batch will be published after final validation.

- 02:46 Validated the five source CIDs, file hashes and actual durations, 216 recipe/preparation registry entries and local links in 148 Markdown files. New paired step counts and time ranges match, with no broken links.

- 2026-11-02 02:53 Batch content commit `98f3c3281cd375dd90d7b1621be7a09463078e3f` was pushed to `origin/main`. A live remote-head check matches the local commit, covering 201 tracked files. This confirmation was added after successful publication.

## 2026-11-02 17:35 Make the repository public

- As requested, changed the visibility of `https://github.com/bd4rex/houpicheng-recipes` from `private` to `public`.
- Both GitHub CLI and the connector confirm `visibility=public`. Unauthenticated requests to the repository page and raw README return HTTP 200.
- The prior `main` baseline was `2d1eb901e7d1acd3a837a633d7f825982a46c2ae`, matching the local and remote heads. This record was written after the visibility change and public-access verification succeeded.
