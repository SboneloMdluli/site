---
title: "{{ replace .Name "-" " " | title }}"
event: Event Name
event_url: https://example.org
location: Location

summary: Talk summary
abstract: "Detailed abstract here"

date: {{ .Date }}
date_end: {{ .Date }}
all_day: true

authors: []
tags: []

featured: false

links:
- name: Slides
  url: ""
- name: Video
  url: ""
- name: Code
  url: ""

image:
  caption: ''
  focal_point: Right
---