---
title: Contentchecker
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: ContentChecker is a privacy-first AI tool that helps adult a
license: mit
---
# ContentChecker

 ContentChecker is a privacy-first AI tool that empowers creators—especially those in adult and erotic spaces—to navigate unfair censorship and moderation on mainstream platforms. Using the Yahoo Open-NSFW model, it scans and scores your images to detect how likely they are to be flagged as "Not Safe for Work" (NSFW). By providing early detection, ContentChecker helps you proactively adjust posts before publishing—protecting your visibility, income, and voice from shadowbans, blacklisting, and algorithmic erasure.

## What Is ContentChecker?
ContentChecker scans images using the Yahoo Open-NSFW model to detect whether they’re likely to be flagged as adult content by automated moderation systems. It helps sex workers, erotic artists, and marginalized creators stay ahead of censorship by enabling them to:

- Reduce the risk of account restrictions and shadowbans

- Adjust content proactively before posting

- Protect visibility, safety, and income in digital spaces
## How It Works
ContentChecker analyzes each image and returns a score between 0.0 and 1.0:

< 0.2 → Likely Safe for Work

> 0.8 → Highly Likely to Be NSFW

0.2 – 0.8 → Use custom thresholds or human review

The model focuses specifically on pornographic content—it does not detect violence, drawings, or other NSFW types.
All analysis happens locally on your device: no uploads, tracking, or logging—your images stay private.

## Why Use ContentChecker? 
Proactive Protection, Not Censorship
ContentChecker gives creators early warnings about potentially risky content, so you can make adjustments before posting—protecting your visibility, reach, and income.

Mitigate Account Risk
Avoid penalties such as:

- Account restrictions

- Content suppression

- Shadowbans and blacklisting

Equity in Moderation
Automated moderation systems frequently misclassify and disproportionately target:

- Black bodies

- Fat bodies

- Queer and erotic expression

- Sex workers and marginalized creators

Even when following platform guidelines, these communities often face erasure, blocked features, or financial loss. ContentChecker helps reclaim your voice and agency in biased digital systems.

Empowering Creators
With ContentChecker, you can:

- Scan and evaluate images before uploading

- Adjust images to stay below NSFW detection thresholds

- Maintain safety, income, and visibility on hostile platforms

This tool is not about silencing adult content—it’s about helping creators survive and thrive under unfair systems.

visit to learn more: https://github.com/bhky/opennsfw2
https://github.com/yahoo/open_nsfw
https://yahooeng.tumblr.com/post/151148689421/open-sourcing-a-deep-learning-solution-for

## View the Demo

You can try out ContentChecker directly in your browser without installing anything by visiting the Hugging Face Spaces demo:

[View the Demo on Hugging Face](https://huggingface.co/spaces/jharri34/contentchecker)

This demo allows you to upload images and see how ContentChecker evaluates them for NSFW content.

## Installation and Running the Application

Follow these steps to install and run ContentChecker on your local machine:

### Prerequisites
Make sure you have the following installed:
- Python >=3.12 
- pip (Python package manager)
- Docker (optional, if you want to use the Docker setup)

### Installation
Clone the repository:
   ```bash
   git clone https://github.com/jharri34/ContentChecker.git
   cd ContentChecker
   ```
Create a virtual environment (optional but recommended):
```
python3 -m venv venv
source venv/bin/activate
```
Install the required dependencies:
```bash
   pip install -r requirements.txt
```
Running the Application
Start the application:

```bash
streamlit run src/contentchecker/app.py
```

Open your browser and navigate to:
http://localhost:8501

Running with Docker (Optional)
If you prefer to use Docker:

Build the Docker image:

```bash
docker build -t contentchecker .
```
Run the Docker container:

```bash
docker run -p 8501:8501 contentchecker
```
Open your browser and navigate to:
> http://localhost:8501

Notes
All processing happens locally on your device to ensure privacy.
Ensure your images are in supported formats (e.g., PNG, JPG, JPEG, GIF, BMP, TIFF).

## Next Steps
### Fine-Tuning the Model

While the default model offers strong baseline performance, results can be improved by fine-tuning the model for your dataset, use case, or personal definition of NSFW.

I envision a future where users can contribute to crowd-sourced model refinement:

Report misclassifications to help us gather edge cases.

Enable local reinforcement learning so your model learns from its mistakes.

Opt-in to share anonymized calibration data that can help improve future updates.

This empowers users—especially from marginalized communities often misrepresented in datasets—to know what gets flagged and why(kinda).

## Understanding the Landscape
Major platforms like Instagram, TikTok, and Facebook rely heavily on AI-powered moderation systems—especially deep learning models like CNNs—to flag NSFW content. These models are trained on massive datasets to detect patterns linked to nudity or sexual expression.

While human moderators may handle appeals, algorithmic moderation is the default—and it’s far from neutral.

Algorithmic Bias is Real
These systems:

- Reflect the biases of their training data and developers

- Disproportionately mislabel and suppress content from Black creators, fat bodies, queer expression, and sex workers

- Reinforce racial, cultural, and political prejudices baked into "objective" tech

This creates a form of technological redlining—where algorithms quietly gatekeep access to visibility, income, and expression.

***When your content is suppressed, your voice is erased.***

These opaque, black-boxed systems have become gatekeepers of labor, identity, and art—deciding whose bodies are "appropriate" and whose aren’t

**Classification is Never Neutral**

Information systems shape the world we live in.
From what’s visible to what’s banned, these tools are never “just code”—they’re expressions of power.

ContentChecker exists to push back.
By giving creators insight into these systems, it helps restore agency over how you’re seen, shared, and supported online.

------------------------------
Useful links
-------------------------------

https://github.com/bhky/opennsfw2?tab=readme-ov-file

https://github.com/yahoo/open_nsfw?tab=readme-ov-file

https://yahooeng.tumblr.com/post/151148689421/open-sourcing-a-deep-learning-solution-for



