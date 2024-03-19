---
title: Sample Markdown File
author: John Doe
date: 2024-03-19
description: This is a sample Markdown file with metadata.
slug: sample-markdown-file
tags: markdown, metadata, flask
---

# Test File

This is a test file for a markdown to HTML converter in Flask


### Run this to install dependencies

```bash
pip3 install -r requirements.txt
python3 main.py
```

## TABLE

| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |



## T2

| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |




### Test to check how python code renders

```pythom
def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        html_content = markdown.markdown(content, output_format='html', extensions=extensions, extension_configs=extensions_configs)
    return html_content
```



**Lorem ipsum** dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

1. list item 1
2. list item 2
3. list item 3

Names with dash --- --- Test

- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:


## Changelog
## 2024-03-18
### Fixes
### Added
- [X] Google Material Icons

## 2024-03-11
### Fixes
- [X] KEYSTONE: rich text does not display in card view
- [X] Application Settings - Breadcrumb Filters
- [X] Add a redirect_url so it comes back to the view after edit
- [X] When documentai validation is on in inspector view, the validity column is not visible
- [X] Disable draft for fields table
- [X] Make inspector shortcut tool tip hover.
- [X] When edit_fields is on, inspector view save does not work
- [X] Record dropdown does not work for expression builder modal
- [X] Remove document file path from file datatype properties
### Added


## 2024-02-26
### Fixes
- [X] [Squished thumbnails in KB comments](https://app.asana.com/0/1202347716179870/1206635511190614/f)
### Added
- [X] [WI DOR - Add classification model handler to doc ai code](https://app.asana.com/0/1202347716179870/1206353145802398/f)
- [X] [App ID based on URL](https://app.asana.com/0/1202347716179870/1203197754933480/f)
- [X] Detail View Icons, List View Image updates, Settings page UI updates


## 2024-02-12
### Fixes
- [X] [WCAG / ADA Updates](https://app.asana.com/0/1202347716179870/1206525353207151/f)
- [X] [Renamed display_style to card_type in views](https://app.asana.com/0/1202347716179870/1206497325791310)
- [X] [Import Doc AI is not successful](https://app.asana.com/0/1202347716179870/1206177241224502/f)
- [X] [Post Feedback](https://app.asana.com/0/1202347716179870/1206434362042842/f)
### Added
- [X] Menus (Left Nav) - Added ability to add custom html to the left nav.
- [X] [page slug does not work with id](https://app.asana.com/0/1202347716179870/1206530368504139/f)
- [X] [KEYSTONE - Higher Contrast Breadcrumbs](https://app.asana.com/0/1202347716179870/1206479090989594/f)
- [X] [knowledgebases tweaks](https://app.asana.com/0/1202347716179870/1206538764060609/f)
- [X] Add robots.txt


## 2024-02-05
### Fixes
- [X] [Create index for fields with search enabled](https://app.asana.com/0/1202347716179870/1206413290152567)
- [X] Global Settings ordering and renaming changes
- [X] [Modal backdrop updates and option to hide sidebar in page builder](https://app.asana.com/0/1202347716179870/1206467668232808)
- [X] [Pagination fixes](https://app.asana.com/0/1202347716179870/1206399043448618/f)
- [X] [Default App on Session Login](https://app.asana.com/0/1202347716179870/1206479094131547/f)
- [X] Left nav no element padding fix
- [X] [Can't add or Delete fields](https://app.asana.com/0/1202347716179870/1206507004540049/f)
- [X] Aria Label fix for Search Bar
- [X] [KB - Images not working on kb PageBuilder](https://app.asana.com/0/1202347716179870/1206510698679807/f)

### Added
- [X] Ability to toggle the SnapApp CLI API
- [X] [Where Used functionality to verify impact before deleting records](https://app.asana.com/0/1202347716179870/1204030969401144)
- [X] Ability to set timeout and time limits for login and session
- [X] reCAPTCHA for user registration and login page
- [X] [Export data as XML](https://app.asana.com/0/1202347716179870/1206446518809214)
- [X] [Rollback transactions in case of failure for /update](https://app.asana.com/0/1202347716179870/1206477606600773)
- [X] [Count key Metrics in-app](https://app.asana.com/0/1202347716179870/1205710509192074/f)
- [X] [Map Clusters](https://app.asana.com/0/1202347716179870/1206399043448618/f)
- [X] Ability to set custom site name, title and description for Open Graph
- [X] Duplicate attachments when uploading CSS or JS files in pages
- [X] [Added Application Selector to view and page builder and added clone option to page builder](https://app.asana.com/0/1202347716179870/1206475180881952)
