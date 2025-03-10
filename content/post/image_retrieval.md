---
title: "Image Retrieval"
date: 2025-03-10
summary: "A comprehensive guide to building a modular image retrieval system with CLIP embeddings and Faiss. This article details the complete architecture including data pipelines with Kedro and Dask, feature storage with Feast..."
tags: ["Machine Learning"]
categories: [Machine Learning]
math: true
---

# Image Retrieval System Design

## System Overview

The Image Retrieval System is designed with a modular, separates concerns for optimal performance and maintainability. The system consists of four main components:

1. **Data Pipeline**
2. **Feature Store**
3. **Backend/Inference**
4. **Frontend**

{{< figure src="/site/images/system_diag.jpg" alt="System Architecture" >}}

The system is composed of two main platforms: one dedicated to handling data and the other focused on inference and user interaction. This design offers a modular and flexible architecture, ensuring seamless integration between components. A scheduler is used to initiate the pipeline and perform batch training processes.

## Data Pipeline

The data pipeline manages feature engineering and data science tasks using Kedro, which applies software engineering principles to data science projects. This approach eliminates disorganised notebooks and ensures maintainability and production-grade quality.

{{< figure src="/site/images/kedro.png" alt="Kedro Pipeline" >}}

Dask enables distributed processing across a cluster, making the pipeline efficient for handling large multidimensional image arrays and parallel I/O operations.

{{< figure src="/site/images/dask.png" alt="Dask Workers" >}}

## Model Architecture

The system uses the Contrastive Language-Image Pre-training (CLIP) model for embedding, which maps both images and text into a shared embedding space. CLIP is trained on image-text pairs and supports zero-shot prediction.

For efficient similarity searches, the system employs Faiss, which offers:

- Fast retrieval by storing indices in memory
- Minimal memory footprint to keep operational costs low
- GPU acceleration and parallel processing capabilities
- Balance between speed and accuracy

The current implementation uses a flat index suitable for small-scale searches (1,000-10,000 entries), but can easily transition to larger-scale index types if needed.

## Feature Store

The feature store houses images, embeddings, and image byte data, enabling data science teams to reuse this information without repeating EDA, feature engineering, or modeling tasks. This promotes efficiency and cost savings. Feast is used for the feature store, which provides:

The feature store houses images, embeddings, and image byte data using Feast, which provides:

- An offline store (Parquet files) designed for efficient data storage and quick data access
- An online store (SQLite) optimised for fast inference
- Reusability of data without repeating EDA, feature engineering, or modeling tasks

{{< figure src="/site/images/feast.png" alt="Feast Project" >}}

## Model Registry

The system uses a local file system as storage for models, mimicking a typical model registry. Models can be tested and approved for production readiness, with the potential to configure Kedro using MLflow for model management. We use DVC foe data and model tracking.

## Backend

The backend features an API for inference built with FastAPI, including:

- Basic schema validation for incoming requests
- In-memory model loading for quick response times
- Multi-model serving capabilities
- Resource optimization by loading/unloading models between RAM and disk

{{< figure src="/site/images/api.png" alt="Project Backend" >}}

## Frontend

The frontend is designed to minimize redundant backend calls by storing search results in the browser's local storage. If a user searches for fewer than k results for the same query, the system retrieves them from memory instead of making additional backend requests.

{{< figure src="/site/images/frontend.png" alt="System Frontend" >}}

The entire system can be easily deployed and containerised using existing Docker files.

## Extended System for Accessibility

The design can be adapted to assist visually impaired users by:

- Integrating speech-to-text directly in the browser using TensorFlow.js or ONNX Runtime Web
- Providing text descriptions of images instead of visual results
- Using text-to-speech engines running in the browser
- Leveraging geolocation to select appropriate voice accents

User feedback can be collected through simple thumbs up/down emoticons.

[View project →](https://github.com/SboneloMdluli/Multi-Modal-Image-Retrieval)
