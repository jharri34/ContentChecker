.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/ContentChecker.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/ContentChecker
    .. image:: https://readthedocs.org/projects/ContentChecker/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://ContentChecker.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/ContentChecker/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/ContentChecker
    .. image:: https://img.shields.io/pypi/v/ContentChecker.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/ContentChecker/
    .. image:: https://img.shields.io/conda/vn/conda-forge/ContentChecker.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/ContentChecker
    .. image:: https://pepy.tech/badge/ContentChecker/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/ContentChecker
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/ContentChecker

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

==============
ContentChecker
==============


    ContentChecker is a tool that scans your images using the Yahoo Open-NSFW model to detect if they’re likely to be flagged as adult content. It helps sex workers and erotic content creators adjust posts before publishing to avoid unfair censorship, shadowbans, and visibility loss


# ContentChecker

  

ContentChecker is a tool designed to help content creators—especially those working in adult and erotic spaces—navigate the challenges of unfair censorship and content moderation. Leveraging the Yahoo Open-NSFW model, ContentChecker scans and scores your images to determine if they are likely to be flagged as "Not Safe for Work" (NSFW). This early detection allows creators to adjust their content proactively before posting, reducing the risk of account restrictions, blacklisting, or content suppression.

  

## How It Works

The model evaluates an image and returns a probability score between 0.0 and 1.0:

  

< 0.2: Likely safe for work.

  

> 0.8: Highly probable to be NSFW.

  

Scores in between can be interpreted with nuance or binned into custom moderation tiers.

  

The focus is solely on pornographic content; other NSFW types (e.g., violence, text-based, sketches) are not included.

  

Human moderation is recommended for edge cases to enhance overall accuracy.

  

## Why This Matters

In the current digital ecosystem, moderation systems often disproportionately target Black bodies, fat bodies, and those expressing sexuality outside the mainstream. Professional sex workers and erotic artists are frequently penalized or erased by automated moderation tools, even when following platform guidelines. Being locked out of features like livestreams, comments, or DMs—even briefly—can result in serious financial harm.

  

 A Tool for Survival and Strategy

ContentChecker shifts power back into the hands of the creator. It allows you to:

  

Scan and evaluate images before uploading to public platforms.

  

Adjust or "tune" images to remain under NSFW detection thresholds.

  

Protect visibility, reach, and income by reducing risk of shadowbans or takedowns.

  

This tool is not about silencing adult content—it's about preserving access. The oldest profession deserves modern tools to stay visible, safe, and profitable in a digital world that too often tries to erase it.

  
  

Useful links

https://github.com/bhky/opennsfw2?tab=readme-ov-file

https://github.com/yahoo/open_nsfw?tab=readme-ov-file

https://yahooeng.tumblr.com/post/151148689421/open-sourcing-a-deep-learning-solution-for


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
