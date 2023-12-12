# AOC Team Bot

## Overview
Simple bot to notify our group of any solved puzzles that can be triggered by our library.

Built using AWS technologies.

## Disclaimer
This script/repo/tool does follow the automation guidelines on the /r/adventofcode community wiki (and link to this article that you're currently reading right now [https://www.reddit.com/r/adventofcode/wiki/faqs/automation] somewhere). Specifically:

Automated outbound calls are throttled to happen every 30 minutes (using Cloudwatch timer).

Triggers by our library are limited to once per minute in case of error, but do only happen when someone solves a puzzle.

The User-Agent header in userAgentHeaderFunction() is set to me since I maintain this tool.

In case of any issues with throttling, do not hesitate to contact me.

## How to setup
Built during a train ride using AWS tools.

Namely:
- CloudWatch to trigger every 30 minutes
- Lambda to poll API and compare with version stored locally in DynamoDB
- SNS to send notification via email to the group
- Teams webhook to send cards to teams (yay!)

If you want to reuse it, just replace the URL with your board and configure the environment variables (SNS_TOPIC, AOC_SESSION and USER_AGENT).

Alternatively use the deploy pipeline to deploy it to your AWS account (just set the secrets properly).

However, it is not really drag and drop, it is mostly made for us, so best use it to take inspiration and make your own, more awesome bot! You can do it!
