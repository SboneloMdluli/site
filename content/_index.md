---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    content:
      username: admin

  - block: experience
    content:
      title: Industry Experience
      subtitle: Building robust models and data systems in finance
      date_format: Jan 2006
      items:
        - title: Data Scientist - Specialist Machine Learning
          company: ABSA Group
          company_url: ""
          location: South Africa
          date_start: "2025-06-01"
          date_end: ""
          description: ""
        - title: Consulting Software Engineer/Data Scientist
          company: Blue Bean Software
          company_url: ""
          location: South Africa
          date_start: "2022-09-01"
          date_end: "2025-05-31"
          description: |
            * Developed and deployed machine learning and statistical models, including model selection, validation, and ONNX quantisation for performance and efficiency
            * Built and optimised data pipelines for machine learning workloads using Kedro, including custom parsers and efficient workflow design
            * Used Apache Camel for asynchronous service communication, enhancing straight-through processing for High Value Payment Systems (HVPS)
            * Conducted business validation and data transformation of ISO 20022 messages between RTGS systems (central bank) and participant banks, leveraging XML Schema Definitions
            * Implemented MLOps practices (MLFlow, DVC, Evidently) for experiment tracking, model versioning, and monitoring
            * Delivered production-ready solutions on AWS (S3, EC2, SageMaker) and contributed to chatbot development for customer engagement
        - title: Graduate Trainee
          company: Iress
          company_url: ""
          location: South Africa
          date_start: "2021-01-01"
          date_end: "2022-08-31"
          description: |
            * Develop and test trading solutions, including algorithmic trading models using FIX protocol
            * Work with financial instruments such as (SSF, T/VWAP, Dark Pools, etc) and troubleshoot business requirements
            * Design trading setups, risk management and assisted in corporate action settlements
            * Worked on derivatives, funds, and equities
    design:
      columns: "2"

  - block: collection
    content:
      title: Articles
      subtitle: Theory, implementation, and real-world trade-offs
      count: 6
      filters:
        folders:
          - post
      archive:
        enable: true
        text: Explore all posts
    design:
      view: card
      columns: "2"
---
