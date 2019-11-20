# Google Cloud Build Notifications
It's a simple cloud function that is triggered everytime a build in Google Cloud Build gets queued, starts or fails. It posts a notificaiton in Slack accordingly. 

[Link to the blog post that started this.](https://alexredwood.com/blog/Creating-a-Slack-Notification-for-Google-Cloud-Build-in-Python_d08808c4-40af-466a-8492-e4133edc7f8a)

## Deployment

Deployment is fairly simple, but you'll need to ensure that you've have at least 1 build in Google Cloud Build (failed or successful).

There are 2 options:
 - You can either copy the code in main.py into a function, making sure to set the `SLACK_LINK` environment variable.
 - Link a clone of the repo into Google Cloud Build, then set the `SLACK_LINK` environment variable.
 
Once thats done, it should report directly to Slack - the initial notification is farily boring, it's worth spending some time into making it look good.
I'll be doing that and I'll keep the blog post, and the repo up to date with this work. 

