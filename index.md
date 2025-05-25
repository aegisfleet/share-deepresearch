---
layout: default
title: ポちのDeepResearch
---

# ポちのDeepResearch

このサイトは、Google Gemini を使用した DeepResearch の結果を個人的にまとめたものです。

## トピック一覧

{% assign sorted_topics = site.topics | sort: 'date' | reverse %}

<ul class="topic-list">
{% for topic in sorted_topics %}
<li data-type="{{ topic.type | default: 'default' }}">[{{ topic.title }}]({{ topic.url | relative_url }}) *{{ topic.date | date: "%Y年%m月%d日" }}*</li>
{% endfor %}
</ul>
